<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-pin-inference-geo -->

#  Data residency: pin an agent's inference geography

An agent that touches regulated data needs an answer to one question before it ships: where do its model requests run. Answering it in a proxy or a runbook leaves the guarantee outside the system that enforces it.

`model.inference_geo` puts the answer on the agent definition. It pins the geography that serves the agent's model requests, is validated against the workspace's residency policy, and is enforced on every turn, so the constraint travels with the agent and holds even if the policy changes after the agent shipped.

This notebook walks through:

* pinning an agent to `us` inference and confirming the pin on a session
* how the pin resolves against the workspace's `allowed_inference_geos` and `default_inference_geo`
* the update semantics that clear a pin
* overriding the geography for one session with `agent_with_overrides`

##  1. Set up the client

`inference_geo` rides the standard `managed-agents-2026-04-01` beta header and needs `anthropic>=0.121.0` for the typed field.

%%capture

%pip install -qU "anthropic>=0.121.0" python-dotenv

import os

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5")

client = anthropic.Anthropic()

##  2. Pin the agent to US inference

`inference_geo` sits inside the `model` config next to `effort` and `speed`. The accepted values are `"global"` and `"us"`. Leave it out and every model request resolves to your workspace's `default_inference_geo` at the moment that request is served, which means a later change to the workspace default reaches sessions that are already running. Set it and the pin is fixed on the agent.

The pin is validated three times: when the agent is saved, when a session is created from it, and on every turn that session serves. It is enforced strictly rather than grandfathered. If a workspace admin narrows `allowed_inference_geos` after the fact, new sessions from a now-disallowed agent are rejected, and a session already running refuses its next turn. That strictness is the point: workspaces rely on it for residency, so the pin holds even against a mid-session policy change.

researcher = client.beta.agents.create(

name="us\_records\_analyst",

description="Answers questions about internal records, pinned to US inference.",

model={"id": MODEL, "inference\_geo": "us"},

system="You answer questions about the records you are given, concisely.",

tools=[{"type": "agent\_toolset\_20260401"}],

betas=BETAS,

)

print(f"{researcher.name}: {researcher.id} v{researcher.version}")

print("inference\_geo:", researcher.model.inference\_geo)

##  3. Confirm the pin on a session

A session snapshots the agent's config at creation, so the pin is visible on `session.agent.model`. Reading it back there is the check that this session's turns are bound to `us`, independent of what the workspace default is today.

env = client.beta.environments.create(

name="residency-demo",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

betas=BETAS,

)

session = client.beta.sessions.create(

agent=researcher.id,

environment\_id=env.id,

title="Records question, US-pinned",

initial\_events=[

{

"type": "user.message",

"content": [

{"type": "text", "text": "In one sentence: what is a data residency policy?"}

],

}

],

betas=BETAS,

)

print("session pin:", session.agent.model.inference\_geo)

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

if ev.type == "agent.message":

print("".join(b.text for b in ev.content if b.type == "text"), end="")

elif ev.type == "session.status\_idle":

print(f"\n[idle] stop\_reason={ev.stop\_reason.type}")

break

##  4. The workspace decides what the pin can point at

The workspace's residency policy lives on the Admin API, in the workspace's `data_residency` block: `allowed_inference_geos` (a list of geos, or the literal `"unrestricted"`) and `default_inference_geo`. An agent's `inference_geo` must be a member of `allowed_inference_geos` unless that field is `"unrestricted"`. Anything else is a 400 at save. In a multiagent roster the pin must agree across the board: the coordinator and every roster member are either all set to the same geo or all unset.

One update subtlety worth pinning down. On `agents.update`, `model` is replaced as a whole rather than merged, so sending `model` without `inference_geo` clears the pin. To change the model id and keep the geography, restate it.

cleared = client.beta.agents.update(researcher.id, model={"id": MODEL}, betas=BETAS)

print("after model update without geo:", cleared.model.inference\_geo)

researcher = client.beta.agents.update(

researcher.id,

model={"id": MODEL, "inference\_geo": "us"}, # restate the pin

betas=BETAS,

)

print("restated:", researcher.model.inference\_geo)

##  5. Override the geography for one session

The agent's pin is the default for every session created from it. To run one session in a different geography without editing the shared agent, pass an `agent_with_overrides` object to `sessions.create` and override `model`. The override replaces the model config for that session only, and the agent resource is untouched. The same membership rule applies: the geo you override to must be allowed by the workspace, and a roster's members must still all agree.

override = client.beta.sessions.create(

agent={

"type": "agent\_with\_overrides",

"id": researcher.id,

"model": {"id": MODEL, "inference\_geo": "global"}, # this session only

},

environment\_id=env.id,

title="One-off, global geography",

betas=BETAS,

)

print("override session pin:", override.agent.model.inference\_geo)

print(

"agent still pinned to:",

client.beta.agents.retrieve(researcher.id, betas=BETAS).model.inference\_geo,

)

##  6. Clean up

from utilities import wait\_for\_idle\_status

wait\_for\_idle\_status(client, session.id)

for s in (session, override):

client.beta.sessions.archive(s.id, betas=BETAS)

client.beta.agents.archive(researcher.id, betas=BETAS)

client.beta.environments.archive(env.id, betas=BETAS)

print("archived")

##  Where the pin fits

`inference_geo` is a residency and compliance control. It says nothing about what the agent can read or where its data is stored, only where its tokens are processed. Storage geography is a separate, immutable workspace setting (`workspace_geo`); the two together answer the questions a compliance review asks.

Because it is enforced on every turn rather than only at creation, the pin is the right control when the guarantee has to survive changes made after the agent ships. For a fleet, set the workspace `default_inference_geo` so unpinned agents inherit the right geography, and reserve the per-agent pin for the agents whose residency must never depend on that default.
