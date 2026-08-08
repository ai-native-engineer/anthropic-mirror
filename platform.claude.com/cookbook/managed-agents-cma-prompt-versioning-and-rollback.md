<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-prompt-versioning-and-rollback -->

#  Prompt Versioning and Rollback

Imagine you're a PM whose product support system uses an LLM to route incoming tickets to the right team. You want to tweak the routing prompt so that more API-related tickets go to the platform team. Previously, the prompt lived in your codebase. Changing it required a PR, a CI run, and deployment. Reverting required the same changes. Managed Agents keeps the prompt server-side instead. Every `agents.update` produces a new immutable version, and sessions choose which version to use by ID. You still review and approve prompt changes, but you're approving a version number in config rather than a code diff, and your running service picks up the change without a rebuild. If something goes wrong, pointing callers back at the old version is all it takes to roll back.

In this cookbook, we'll create a support-ticket triage agent, update the system prompt, and roll it back when the performance degrades.

By the end you'll have:

* created an agent and seen it come back as `version: 1`
* scored a specific version against a labelled test set
* shipped a v2 prompt and watched the version number move
* rolled a regressed agent back to v1 without a deploy

##  Prerequisites

**Required:**

* Python 3.11+
* `anthropic>=0.91.0`
* An Anthropic API key
* The `example_data/prompt_versioning_and_rollback/support_tickets.jsonl` fixture in this directory

##  Setup



%%capture

%pip install -q "anthropic>=0.91.0" python-dotenv



import json

import os

import time

from collections import defaultdict

from pathlib import Path

from anthropic import Anthropic

from dotenv import load\_dotenv

load\_dotenv()

if not os.getenv("ANTHROPIC\_API\_KEY"):

raise RuntimeError("Set ANTHROPIC\_API\_KEY in your environment or .env file")

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-4-6")

client = Anthropic()

##  Create the agent (version 1)

We'll start by creating an Environment (the container template the agent runs in) and the agent itself. The system prompt is short: classify each ticket into a team and priority, and respond with JSON only.



env = client.beta.environments.create(name="ticket-triage-env")

ENV\_ID = env.id

V1\_SYSTEM = """You are a support-ticket triage agent for a usage-billed API product.

Read the ticket and respond with ONLY a single line of raw JSON (no code fences, no prose):

{"team": "<billing|auth|api-platform|dashboard>", "priority": "<P1|P2|P3>"}

Route based on the customer's actual problem, not surface keywords."""

agent = client.beta.agents.create(name="ticket-triage", model=MODEL, system=V1\_SYSTEM)

AGENT\_ID = agent.id

print(f"env={ENV\_ID} agent={AGENT\_ID} v{agent.version}")



```
env=env_017FKqTdU6dFgEe6zbbVQvE5  agent=agent_011CZo6t9Cr6Eg5TeFFPWPpi v1
```

`agents.create` handed us back `version: 1` without us asking for it. Every update we make later will produce a new version with the same `id`, and that number is what we'll use to pin sessions and roll back.

##  Load the labelled test set

Below we have twenty tickets, five per team, with the correct routing already labelled. These are the ground truth we'll score against.



fixture = Path("example\_data/prompt\_versioning\_and\_rollback/support\_tickets.jsonl")

tickets = [json.loads(line) for line in fixture.read\_text().splitlines()]

teams = sorted({t["team"] for t in tickets})

print(f"{len(tickets)} tickets across {len(teams)} teams: {teams}")



```
20 tickets across 4 teams: ['api-platform', 'auth', 'billing', 'dashboard']
```

##  Score version 1

Let's run every ticket through v1 and see how it does. The `triage` helper below opens a session pinned to a specific version, sends one ticket, polls `events.list` until the session goes idle, and parses the JSON verdict out of the `agent.message` events.

The part that matters for this cookbook is the `agent=` argument on `sessions.create`. Passing a plain string (`agent=AGENT_ID`) gets you whatever the latest version is. Passing `{"type": "agent", "id": ..., "version": ...}` pins to an exact version, which is what we want for a controlled comparison.



def triage(version: int, ticket: dict) -> dict:

"""Run one ticket through a pinned agent version and return its verdict."""

session = client.beta.sessions.create(

agent={"type": "agent", "id": AGENT\_ID, "version": version},

environment\_id=ENV\_ID,

)

try:

prompt = "Subject: " + ticket["subject"] + "\n\n" + ticket["body"]

client.beta.sessions.events.send(

session.id,

events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],

)

deadline = time.time() + 60

while time.time() < deadline:

events = client.beta.sessions.events.list(session.id).data

if events and events[-1].type == "session.status\_idle":

break

time.sleep(1)

else:

raise TimeoutError(f"session {session.id} did not idle within 60s")

agent\_events = [e for e in events if e.type == "agent.message"]

reply = "".join(b.text for e in agent\_events for b in e.content)

return json.loads(reply)

finally:

try:

client.beta.sessions.archive(session.id)

except Exception: # noqa: S110

pass

def score(version: int) -> dict:

"""Evaluate all tickets against the given version and return per-team accuracy."""

hits = defaultdict(lambda: [0, 0])

for t in tickets:

pred = triage(version, t)

hits[t["team"]][1] += 1

if pred.get("team") == t["team"]:

hits[t["team"]][0] += 1

return dict(hits)

v1\_scores = score(version=1)

print("v1 results:")

for team, (correct, total) in sorted(v1\_scores.items()):

print(f" {team:14s} {correct}/{total}")



```
v1 results:
  api-platform   5/5
  auth           5/5
  billing        4/5
  dashboard      5/5
```

The model did well and got almost all routing correct.

##  Ship version 2

Now the PM ships her change: a routing rule telling the agent that anything about API usage or rate limits belongs to the platform team. `agents.update` updates the agent to the new system prompt.



V2\_SYSTEM = V1\_SYSTEM + (

"\n\nROUTING RULE: If the ticket text mentions API usage, rate limits, quotas, "

"or request volume, route to api-platform. Apply this rule before any other "

"consideration; do not second-guess it based on the rest of the ticket."

)

agent = client.beta.agents.update(AGENT\_ID, version=agent.version, system=V2\_SYSTEM)

print(f"agent {AGENT\_ID} now at v{agent.version}")



```
agent agent_011CZo6t9Cr6Eg5TeFFPWPpi now at v2
```

###  Where did code review go?

We just changed the agent with one API call. In this notebook that happened with no review at all, which is fine for a demo but not how you'd run production.

There's no built-in approval workflow on `agents.update`. Any key in the workspace can call it. If callers are passing the bare agent ID instead of a pinned version, they'll start using the new prompt on their very next session. That's the tradeoff for not needing a deploy, the same one you make with feature flags or any other config you manage through an API instead of through code.

The pattern that puts the review step back: production callers always pin to an explicit version, and *that pinned number* is the thing under change control. Anyone can create v2, v3, v10; those versions sit on the server with no traffic. Promotion means updating whatever config tells production callers which version to pass, and that update goes through your normal review process. This process makes creating versions cheap and keeps your SDLC intact. It's still a win, because instead of updating production code, you only need to update config values and the change gets picked up across all runners.

##  Score version 2

Same evaluation, pinned to v2. The new rule is broad, and on a usage-billed API product the billing tickets talk about API usage too.



v2\_scores = score(version=agent.version)

for team in sorted(v1\_scores):

c1, n1 = v1\_scores[team]

c2, n2 = v2\_scores[team]

flag = " <-- regressed" if c2 < c1 else ""

print(team)

print(f" v1: {c1}/{n1}")

print(f" v2: {c2}/{n2}{flag}")



```
api-platform
  v1: 5/5
  v2: 5/5
auth
  v1: 5/5
  v2: 5/5
billing
  v1: 4/5
  v2: 2/5  <-- regressed
dashboard
  v1: 5/5
  v2: 5/5
```

##  Roll back

Billing regressed. Version 1 is still sitting on the server. Rolling back isn't a deploy; callers just go back to passing `version: 1`.



billing = [t for t in tickets if t["team"] == "billing"]

rerun = [triage(version=1, ticket=t).get("team") for t in billing]

print(f"billing tickets via version=1: {rerun.count('billing')}/{len(billing)} correct")



```
billing tickets via version=1: 4/5 correct
```

Since versions live server-side, v2 is still there if the PM wants to keep iterating on it while production stays on v1, or route a small slice of traffic to it as a canary. When a fix is ready, she can create v3 and run through the same process to promote it.

##  Clean up



client.beta.agents.archive(AGENT\_ID)

client.beta.environments.archive(ENV\_ID)

print("archived")



```
archived
```

##  Recap

The mechanics here are small (create, update, pin, re-pin), but prompts becoming a versioned server-side resource allows you to evaluate and promote prompts independently of application code, either through `update` runs as shown above or through changing the version in config.

A few things worth carrying into your workflow:

* Have production callers pin to an explicit version, not the bare agent ID. New versions stay invisible until you promote one.
* Treat the pinned version number as the gate for changing prompts. Creating versions is exploratory; updating the production pin is what goes through review.
* For higher-stakes agents, route a fraction of traffic to a new version and compare (as this notebook does) before promoting fully. You can effectively use this versioning as a feature flag.

###  Next steps

* `client.beta.agents.versions.list(AGENT_ID)` returns every version of an agent.
* The other notebooks in `managed_agents/` cover sessions, custom tools, and end-to-end patterns.
