<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-with-mongodb-atlas -->

#  Fraud Review Agent with MongoDB Atlas and Claude Managed Agents

This cookbook shows how to bring **MongoDB Atlas** to an agent running on
[Claude Managed Agents(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/README.md) (CMA) — as its retrieval engine, its graph store, and its
system of record — using only the standard CMA patterns (custom tools and MCP toolsets), with
**no platform-level MongoDB integration required**. The runnable helpers live beside this
notebook in [`mongodb_on_cma/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/). Each section links the full file so the
narrative stays focused on *where MongoDB plugs in* and *where the agent adds value*.

**Where MongoDB Plugs In:** Most agent stacks bolt together three or four systems: a vector
database for semantic search, a separate engine for keywords, a graph store for relationships,
and an operational database for the records themselves. Every seam is another integration,
another credential, another place the agent's view of the world can drift. MongoDB collapses
that into one engine: the same documents are searchable by **vector** (`$vectorSearch`), by
**full-text** (`$search`), as a **hybrid** of the two fused with reciprocal rank fusion, or RRF
(`$rankFusion`), and traversable as a **graph** (`$graphLookup`) — and they are the same
documents the agent reads, writes, and persists its decisions to. One query language, one
cluster, one connection (`pymongo`).

**Where the Agent Adds Value:** CMA runs the agent loop and sandbox on Anthropic's side. Your
application owns the **data path** to MongoDB. The agent reasons over what MongoDB retrieves,
pauses for a human on risky calls through CMA's native `requires_action` gate, and writes its
verdict back — all without the database credential ever entering the agent context or its
sandbox.

> MongoDB here is your **operational data store and retrieval engine** — your system of record,
> controlled by your application. That's distinct from the memory features CMA manages natively
> on the platform. The two are complementary.

**By the end you will be able to:**

* Connect a credential-safe MongoDB Atlas data path into a Claude Managed Agent in three ways.
* Lift vector, full-text, hybrid, and graph retrieval into an agent's custom tools.
* Gate risky agent decisions behind CMA's native human-in-the-loop pause.
* Make one MongoDB Atlas cluster the agent's system of record and audit backbone.

The worked example is a **human-in-the-loop fraud-review agent**, but the patterns are
vertical-agnostic: swap the collection and the tools, and the same shape serves a support,
research, or operations agent.

##  What this guide covers

1. [Connect MongoDB to a managed agent](#1-connect-mongodb-to-a-managed-agent)
2. [Retrieve: four patterns, one engine](#2-retrieve-four-patterns-one-engine)
3. [The end-to-end agent: human-in-the-loop fraud review](#3-the-end-to-end-agent-human-in-the-loop-fraud-review)
4. [MongoDB Atlas as the system of record and audit backbone](#4-mongodb-atlas-as-the-system-of-record-and-audit-backbone)
5. [Recap](#5-recap)



%%capture

# Third-party dependencies: the Anthropic SDK (drives Claude Managed Agents via client.beta.\*),

# pymongo (the host-side data path), python-dotenv, and cryptography + pyjwt (sign/verify the

# AP2 mandates). This installs the PyPI packages only — the notebook also imports the adjacent

# `mongodb\_on\_cma/` package and `utilities.py`, so run it from a clone of this repo (see Setup).

%pip install -q "anthropic>=0.109.0" pymongo python-dotenv cryptography pyjwt

##  Prerequisites

**Required knowledge:** Python and `pymongo` basics, plus passing familiarity with the Claude
API. New to MongoDB + Claude? The
[library-RAG notebook(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/../third_party/MongoDB/rag_using_mongodb.ipynb) covers `$vectorSearch`
first. New to the custom-tool gate?
[`CMA_gate_human_in_the_loop.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb) teaches the round-trip.

**Required tools:** Python 3.11+, an [Anthropic API key(opens in new tab)](https://console.anthropic.com), and a
MongoDB Atlas cluster.

##  Setup

**Required:** `MONGO_URI` (an Atlas SRV connection string) plus Anthropic API access. A **free
M0 cluster runs everything in this cookbook** — vector, full-text, hybrid `$rankFusion`, and
graph traversal — so there is no paid-tier requirement. Hybrid search uses the native
`$rankFusion` stage, which needs MongoDB 8.0+; every current Atlas cluster (M0 included) is on
8.0 or later, so this holds by default.



uv sync --all-extras # from the repo root

cp .env.example .env # then add MONGO\_URI (and Anthropic auth, if not already configured)

**Optional embeddings/rerank provider:** The seed fixture ships precomputed embeddings, so the
cookbook runs without one. To enable the live-embedding and reranker paths, set **one** of
`MDB_ATLAS_API_KEY` (the MongoDB Atlas AI endpoint, serving both `/v1/embeddings` and
`/v1/rerank`) or `VOYAGE_API_KEY` (the `voyageai` SDK). `ENABLE_RERANK=1` adds the reranker
second stage. `AUTO_APPROVE=1` resolves the human gate deterministically for CI. `COOKBOOK_MODEL`
overrides the agent model (default `claude-haiku-4-5`).

**No Atlas cluster yet?** The partner notebook [`rag_using_mongodb.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/../third_party/MongoDB/rag_using_mongodb.ipynb) walks through creating a free cluster and getting your `MONGO_URI`; the [Atlas Search index docs(opens in new tab)](https://www.mongodb.com/docs/atlas/atlas-search/create-index/) cover index setup.

The teaching code lives **inline in this notebook**: the four retrieval pipeline builders
(Section 2) and the custom-tool handlers plus the `requires_action` gate loop (Section 3). The
[`mongodb_on_cma/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/) package next to the notebook holds only setup boilerplate
you import rather than read: [`config.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/config.py) (index names + tunables),
[`embeddings.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/embeddings.py) (the Atlas/Voyage client),
[`tools.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/tools.py) (Atlas seed/index setup + shared decision/audit doc
shapers), [`ap2_mandates.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/ap2_mandates.py) (AP2 signing/verification — a
crypto black box you call through `verify_mandates`), and
[`seed.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/seed.py) (the example-data loader). Import them, connect the clients,
and resolve the run configuration.



import hashlib

import json

import logging

import os

from datetime import UTC, datetime

from typing import Any

import dotenv

from anthropic import Anthropic

from mongodb\_on\_cma import (

EMBED\_DIM,

build\_audit\_event,

build\_decision\_doc,

ensure\_indexes,

has\_anthropic\_auth,

load\_seed,

make\_embedding\_client,

missing\_required\_env,

preflight,

prepare\_seed,

rerank,

resolve\_model,

seed\_collection,

server\_version,

supports\_rank\_fusion,

)

from mongodb\_on\_cma.ap2\_mandates import (

attach\_mandates,

store\_mandate\_receipt,

tool\_verify\_mandates,

)

from pymongo import MongoClient

from utilities import wait\_for\_idle\_status

dotenv.load\_dotenv()

missing = missing\_required\_env()

assert not missing, f"Set these in your environment / .env: {missing}"

# Anthropic auth is a soft check: an API key, an auth token, or a profile (e.g. the `ant`

# CLI's workload-identity federation) all work, so warn rather than block if none is set.

if not has\_anthropic\_auth():

print(

"warning: no ANTHROPIC\_API\_KEY / ANTHROPIC\_AUTH\_TOKEN / ANTHROPIC\_PROFILE found; "

"relying on the SDK / `ant` CLI to resolve credentials."

)

MODEL = resolve\_model()

ENABLE\_RERANK = os.getenv("ENABLE\_RERANK", "").lower() in ("1", "true")

AUTO\_APPROVE = os.getenv("AUTO\_APPROVE", "").lower() in ("1", "true")

# Quiet the SDK's one-shot notice that ANTHROPIC\_API\_KEY shadows profile/federation

# auto-discovery — expected when an API key is set; harmless under `ant` / WIF auth.

logging.getLogger("anthropic.lib.credentials.\_auth").setLevel(logging.ERROR)

client = Anthropic()

mongo = MongoClient(os.environ["MONGO\_URI"])

db = mongo["fraud\_review\_demo"]

coll = db["transactions"]

ai\_client = make\_embedding\_client() # Atlas / Voyage / None (seed ships precomputed vectors)

print(

f"model={MODEL} rerank={'on' if ENABLE\_RERANK else 'off'} provider={'yes' if ai\_client else 'none'}"

)



```
warning: no ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN / ANTHROPIC_PROFILE found; relying on the SDK / `ant` CLI to resolve credentials.
model=claude-haiku-4-5  rerank=on  provider=yes
```

##  1. Connect MongoDB to a managed agent

The agent loop and its sandbox are **Anthropic-hosted** — that is what "Managed" means. The
only thing you host is the **data path** to MongoDB. On every path, the MongoDB credential
lives on *your* side of the boundary: it never enters the agent context, a cloud sandbox's
environment, or a file the agent can read.

> **Why this cookbook talks to CMA through `client.beta.*` and not the Claude Agent SDK.**
> Managed Agents (CMA) is a [hosted REST API(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/overview):
> Anthropic runs the agent loop and the sandbox, and you drive it by creating agents/sessions
> and streaming events through the standard Anthropic SDK's beta surface
> (`client.beta.agents`, `client.beta.sessions`, `client.beta.sessions.events`). There is no
> separate "CMA SDK" — this *is* how you use CMA. The
> [Claude Agent SDK(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/overview)
> (`claude-agent-sdk`, showcased in the repo's
> [`claude_agent_sdk/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/../claude_agent_sdk/) cookbooks) is a different product: a library that
> runs the agent loop **inside your own process**, on your own infrastructure. The two are
> complementary — you'd prototype locally with the Agent SDK and run in production on CMA — but
> a CMA integration like this one is built on the beta sessions/events API. That choice is also
> what makes the credential boundary below work: because *your* process handles each custom-tool
> call, the MongoDB secret stays host-side (see Path A).

There are three ways to wire the data path. **This cookbook uses Path A throughout** — it is
the recommended, lightest pattern and the one that keeps the credential fully host-side. Paths
B and C are summarized after it for completeness.

###  Path A: host-side custom tool (recommended)

Your application defines a `custom` tool. When the agent calls it, the session pauses with
`requires_action`, **your** process runs the query with `pymongo`, and you post back a
`user.custom_tool_result`. The secret never enters the sandbox, MongoDB can sit in a private
VPC, and the agent is constrained to a fixed, audited set of queries. It is the lightest path —
no standing server — and Anthropic's recommended pattern for any secret-bearing data source.

To see the wiring unobscured, here is the whole round-trip with one tiny `find_notes` tool over
a throwaway `notes` collection. **This is the core integration: a few lines of `pymongo`, run
host-side, behind a custom tool.** Section 3 scales this exact shape to five tools and a real
workload.



notes = mongo["cookbook\_mongodb\_on\_cma"]["notes"]

notes.delete\_many({})

notes.insert\_many(

[

{"note\_id": "n1", "tag": "todo", "text": "Renew the SSL certificate before it expires."},

{"note\_id": "n2", "tag": "idea", "text": "Add a dark-mode toggle to the dashboard."},

{"note\_id": "n3", "tag": "todo", "text": "Email the quarterly report to the finance team."},

]

)

notes\_agent = client.beta.agents.create(

name="cookbook-mongodb-notes",

model=MODEL,

system=(

"You answer questions about the user's notes. Use the find\_notes tool to fetch notes "

"(optionally filtered by `tag`) before answering, then give a concise final answer."

),

tools=[

{

"type": "agent\_toolset\_20260401",

"default\_config": {"enabled": True, "permission\_policy": {"type": "always\_allow"}},

},

{

"type": "custom",

"name": "find\_notes",

"description": "Return stored notes, optionally filtered by tag (e.g. 'todo', 'idea').",

"input\_schema": {

"type": "object",

"properties": {"tag": {"type": "string", "description": "optional tag filter"}},

"required": [],

},

},

],

)

notes\_env = client.beta.environments.create(

name="cookbook-mongodb-notes-env", config={"type": "cloud", "networking": {"type": "limited"}}

)

notes\_session = client.beta.sessions.create(

environment\_id=notes\_env.id,

agent={"type": "agent", "id": notes\_agent.id, "version": notes\_agent.version},

title="MongoDB notes (host-side custom tool)",

)

print(f"seeded {notes.count\_documents({})} notes; session: {notes\_session.id}")



```
seeded 3 notes; session: sesn_016ufm58BVJ8aZeWjUt39bsq
```

Open the event stream, ask a question, and drive the round-trip: on each
`agent.custom_tool_use`, run the query **host-side** with `pymongo` and post back a
`user.custom_tool_result`. Results are projected with `{"_id": 0}` because a raw MongoDB
`ObjectId` is not JSON-serializable.



def run\_find\_notes(args: dict) -> dict:

"""Host-side handler: pymongo runs here; \_id (ObjectId) is projected out so the result is JSON-able."""

flt = {"tag": args["tag"]} if args.get("tag") else {}

return {"notes": list(notes.find(flt, {"\_id": 0}))}

tool\_use\_events, responded, round\_trips = {}, set(), []

question = "Using find\_notes, list every note tagged 'todo', then tell me how many there are."

with client.beta.sessions.events.stream(notes\_session.id) as stream:

client.beta.sessions.events.send(

session\_id=notes\_session.id,

events=[{"type": "user.message", "content": [{"type": "text", "text": question}]}],

)

for ev in stream:

if ev.type == "agent.custom\_tool\_use":

tool\_use\_events[ev.id] = ev

elif ev.type == "session.status\_idle" and ev.stop\_reason:

if ev.stop\_reason.type == "requires\_action":

for event\_id in ev.stop\_reason.event\_ids:

if event\_id in responded:

continue

tev = tool\_use\_events[event\_id]

result = (

run\_find\_notes(tev.input)

if tev.name == "find\_notes"

else {"error": "unknown"}

)

if tev.name == "find\_notes":

round\_trips.append(

{"tool\_input": tev.input, "returned": len(result["notes"])}

)

client.beta.sessions.events.send(

session\_id=notes\_session.id,

events=[

{

"type": "user.custom\_tool\_result",

"custom\_tool\_use\_id": event\_id,

"content": [{"type": "text", "text": json.dumps(result)}],

}

],

)

responded.add(event\_id)

elif ev.stop\_reason.type == "end\_turn":

break

elif ev.type == "session.status\_terminated":

break

wait\_for\_idle\_status(client, notes\_session.id)

print("host-side find\_notes round-trips:")

for rt in round\_trips:

print(f" find\_notes({rt['tool\_input']}) -> {rt['returned']} notes")

client.beta.sessions.archive(notes\_session.id)

client.beta.environments.archive(notes\_env.id)

client.beta.agents.archive(notes\_agent.id)

notes.drop()

print("archived the demo agent / environment / session; dropped the notes collection")



```
host-side find_notes round-trips:
  find_notes({'tag': 'todo'}) -> 2 notes
archived the demo agent / environment / session; dropped the notes collection
```

###  Other options (brief)

Path A is the default and the rest of this cookbook uses it. Two alternatives exist for cases
it doesn't fit — you don't need them to follow along:

* **Path B — in-sandbox `pymongo` (self-hosted sandbox).** If you run the sandbox on your own
  infrastructure, the MongoDB client can live *inside* it and the agent queries MongoDB straight
  from its `bash` tool, with `MONGO_URI` as an ordinary container env var. Pick this only for
  self-hosted sandboxes (on a cloud sandbox the connection string would land in session history).
  Runnable image: [`self_hosted_sandboxes/docker/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/self_hosted_sandboxes/docker/).
* **Path C — self-hosted MongoDB MCP server.** Host the official MongoDB MCP server behind HTTPS
  and register it as an `mcp_toolset` so the agent can query the full surface (`find`,
  `aggregate`, `$vectorSearch`) rather than a fixed query set. Standard CMA MCP + vault wiring.

The trade-off in one line: **Path A** keeps the query set fixed and the secret in your backend
(the safest default); **Path B** hands the sandbox direct access; **Path C** gives the agent the
broadest query surface at the cost of running a server. When in doubt, stay on Path A.

##  2. Retrieve: four patterns, one engine

An agent is only as well-grounded as its retrieval. These are the four MongoDB retrieval
patterns shown **in isolation** — here's the builder, here's what it returns — so you can lift a
single pattern into your own agent's tools. Each is a plain aggregation-pipeline builder; the
Section 3 agent calls these same functions through its tools.

| Pattern | Builder | MongoDB stage |
| --- | --- | --- |
| Vector search | `build_vector_pipeline` | `$vectorSearch` |
| Full-text search | `build_lexical_pipeline` | `$search` |
| Hybrid (reciprocal rank fusion) | `build_rank_fusion_pipeline` | `$rankFusion` (8.0+) |
| Graph traversal | `build_graph_pipeline` | `$graphLookup` |

The builders are defined inline in the next cell — each returns a list of aggregation stages you
can lift into your own collection. Index names and the projected fields come from
[`config.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/config.py); `EMBED_DIM` and the index constants are imported in the
setup cell above.

First, load the seed fixture from
[`example_data/mongodb_on_cma/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/example_data/mongodb_on_cma/seed_transactions.jsonl) and build
the indexes. The fixture ships precomputed embeddings, so this runs with no provider key.



# The four retrieval builders — each returns a plain aggregation pipeline you can lift into your

# own collection. These are the functions Section 3's agent calls through its custom tools.

from mongodb\_on\_cma.config import (

DECIDED\_STATUSES,

LEXICAL\_PATHS,

PROJECT\_FIELDS,

SEARCH\_INDEX\_NAME,

VECTOR\_INDEX\_NAME,

)

def \_project\_stage(with\_score: bool = False) -> dict:

proj: dict[str, Any] = {f: 1 for f in PROJECT\_FIELDS}

proj["\_id"] = 0

if with\_score:

proj["score"] = {"$meta": "score"}

return {"$project": proj}

def build\_vector\_pipeline(

qvec, \*, limit, candidates=None, vector\_index=VECTOR\_INDEX\_NAME, status\_in=DECIDED\_STATUSES

) -> list[dict]:

return [

{

"$vectorSearch": {

"index": vector\_index,

"path": "embedding",

"queryVector": qvec,

"numCandidates": candidates or max(50, limit \* 10),

"limit": limit,

"filter": {"status": {"$in": list(status\_in)}},

}

},

\_project\_stage(),

]

def build\_lexical\_pipeline(query, \*, limit, search\_index=SEARCH\_INDEX\_NAME) -> list[dict]:

return [

{"$search": {"index": search\_index, "text": {"query": query, "path": LEXICAL\_PATHS}}},

{"$limit": limit},

\_project\_stage(),

]

def build\_rank\_fusion\_pipeline(

qvec,

query,

\*,

k,

vector\_index=VECTOR\_INDEX\_NAME,

search\_index=SEARCH\_INDEX\_NAME,

status\_in=DECIDED\_STATUSES,

) -> list[dict]:

# $rankFusion (MongoDB 8.0+) runs both input pipelines and fuses them by reciprocal rank —

# one aggregation, server-side. Each input pipeline gets weight 1 (uniform). To bias toward

# semantic vs. lexical, add "combination": {"weights": {"vector": w, "lexical": w}}.

candidates = max(50, k \* 10)

per\_branch = max(k \* 4, 20)

return [

{

"$rankFusion": {

"input": {

"pipelines": {

"vector": [

{

"$vectorSearch": {

"index": vector\_index,

"path": "embedding",

"queryVector": qvec,

"numCandidates": candidates,

"limit": per\_branch,

"filter": {"status": {"$in": list(status\_in)}},

}

}

],

"lexical": [

{

"$search": {

"index": search\_index,

"text": {"query": query, "path": LEXICAL\_PATHS},

}

},

{"$limit": per\_branch},

],

}

},

}

},

{"$limit": k},

\_project\_stage(with\_score=True),

]

def build\_graph\_pipeline(

account\_id: str, \*, max\_depth: int = 4, collection: str = "transactions"

) -> list[dict]:

return [

{"$match": {"sender.account\_number": account\_id}},

{

"$graphLookup": {

"from": collection,

"startWith": "$recipient.account\_number",

"connectFromField": "recipient.account\_number",

"connectToField": "sender.account\_number",

"as": "chain",

"maxDepth": max\_depth,

"depthField": "depth",

}

},

]

def summarize\_ring(graph\_doc: dict, \*, seed\_account: str) -> dict:

# Turn a $graphLookup chain into fraud-ring signals: circular flow back to the seed account,

# layering (many small transfers), and overall network size.

chain: list[dict] = list(graph\_doc.get("chain", []))

accounts: set[str] = set()

small\_transfers = 0

circular\_flow = False

for edge in chain:

sender = (edge.get("sender") or {}).get("account\_number")

recipient = (edge.get("recipient") or {}).get("account\_number")

accounts.update(a for a in (sender, recipient) if a)

if recipient == seed\_account:

circular\_flow = True

if float(edge.get("amount", 0) or 0) < 1000:

small\_transfers += 1

network\_size = len(chain)

layering = small\_transfers >= 5

return {

"network\_size": network\_size,

"unique\_accounts": len(accounts),

"circular\_flow": circular\_flow,

"layering": layering,

"suspicious\_patterns": circular\_flow or layering or network\_size >= 3,

}



docs = prepare\_seed(load\_seed(), now=datetime.now(UTC))

count = seed\_collection(coll, docs)

print(f"seeded {count} transactions")

# Create the vector + Atlas Search indexes if absent, then block until both are queryable AND

# actually reflect the freshly-seeded docs (Atlas Search is eventually consistent).

ensure\_indexes(coll, dim=EMBED\_DIM)

check = preflight(coll)

for issue in check["issues"]:

print("PREFLIGHT:", issue)

assert check["ok"], "Fix the preflight issues above before continuing."

# This cookbook uses the native `$rankFusion` stage for hybrid search, which needs MongoDB 8.0+.

# Every current Atlas cluster — including the free M0 tier — runs 8.0 or later, so this holds by

# default; the check just fails loudly if you point MONGO\_URI at an older self-hosted server.

version = server\_version(coll)

assert supports\_rank\_fusion(version), (

f"MongoDB {version} predates $rankFusion (needs 8.0+). Use an Atlas cluster (any tier) or a "

f"self-hosted MongoDB 8.0+."

)

print(f"server={version} hybrid search=$rankFusion (native)")



```
seeded 20 transactions
server=8.0.27  hybrid search=$rankFusion (native)
```

###  Pattern 1: Vector search (`$vectorSearch`)

Semantic recall: find documents whose `embedding` is nearest the query vector. This example
reuses an existing document's embedding as the query (a pending case looking for decided
precedent), so no embedding API call is needed. The builder filters to decided cases via the `status` field.



query\_doc = coll.find\_one({"transaction\_id": "txn-review-struct"}) # a pending case

hits = list(coll.aggregate(build\_vector\_pipeline(query\_doc["embedding"], limit=3)))

print("nearest decided precedents:")

for h in hits:

print(f" {h['transaction\_id']}: {h['text'][:72]}")



```
nearest decided precedents:
  txn-struct-01: Cash deposit of 4950 USD, just under the 5000 reporting threshold. Third
  txn-struct-02: Cash deposit of 4900 USD just below the 5000 CTR threshold, same account
  txn-struct-03: Transfer of 4999 USD deliberately under 5000 to avoid reporting. Pattern
```

###  Pattern 2: Full-text search (`$search`, BM25)

Keyword and phrase matching over text fields — this is what catches the exact names, IDs, and
codes that embeddings blur.



hits = list(

coll.aggregate(

build\_lexical\_pipeline("cash deposit just under the reporting threshold", limit=3)

)

)

print("full-text matches:")

for h in hits:

print(f" {h['transaction\_id']}: {h['text'][:72]}")



```
full-text matches:
  txn-struct-01: Cash deposit of 4950 USD, just under the 5000 reporting threshold. Third
  txn-review-struct: Cash deposit of 4950 USD, just under the 5000 reporting threshold, follo
  txn-struct-02: Cash deposit of 4900 USD just below the 5000 CTR threshold, same account
```

###  Pattern 3: Hybrid (reciprocal rank fusion)

Fuse the vector and full-text rankings into one result set. `$rankFusion` (MongoDB 8.0+) runs
both input pipelines server-side and combines them by reciprocal rank — no client-side merging,
no second round-trip.



qvec, query = query\_doc["embedding"], "structuring: cash deposit just under the threshold"

hits = list(coll.aggregate(build\_rank\_fusion\_pipeline(qvec, query, k=3)))

print("hybrid via $rankFusion (server-side):")

for h in hits:

print(f" {h['transaction\_id']}: {h['text'][:72]}")



```
hybrid via $rankFusion (server-side):
  txn-struct-01: Cash deposit of 4950 USD, just under the 5000 reporting threshold. Third
  txn-struct-02: Cash deposit of 4900 USD just below the 5000 CTR threshold, same account
  txn-struct-03: Transfer of 4999 USD deliberately under 5000 to avoid reporting. Pattern
```

###  Pattern 4: Graph traversal (`$graphLookup`)

Follow `sender.account_number -> recipient.account_number` links to surface a network (here, a
circular money-flow ring). This is a *relationship* signal, deliberately separate from the
similarity ranking above.



graph\_doc = next(

iter(coll.aggregate(build\_graph\_pipeline("ACC-RING-A", collection=coll.name))), {"chain": []}

)

ring = summarize\_ring(graph\_doc, seed\_account="ACC-RING-A")

print(

f"graph traversal from ACC-RING-A: network\_size={ring['network\_size']} "

f"circular\_flow={ring['circular\_flow']} suspicious={ring['suspicious\_patterns']}"

)



```
graph traversal from ACC-RING-A: network_size=4 circular_flow=True suspicious=True
```

**Adapt these for your domain.** Each builder is a generic shape: embed your text with any
model and point `build_vector_pipeline` at your field; set the searchable paths for full-text;
tune the `$rankFusion` input weights to bias semantic vs. lexical; change the graph
`connectFromField`/`connectToField` to your relationship (citations, org charts, supply chains).
All four are defined in the cell above — lift them straight into your own project.

##  3. The end-to-end agent: human-in-the-loop fraud review

Now everything works together. A Managed Agent reviews flagged transactions, grounding each
recommendation in the MongoDB signals from Section 2 (exposed as **custom tools** over the
Path A round-trip), and pauses for a human on the risky cases. Decisions and an append-only
audit trail are written back to the same cluster.

![The agent loop runs on Anthropic; the data path runs in your notebook. MongoDB Atlas serves the retrieval signals and stores the decision and audit trail.](https://platform.claude.com/images/cma_with_mongodb_atlas.jpg)

The **agent loop runs on Anthropic**; the **data path runs in your notebook**. As a result,
`MONGO_URI` and the embedding key never enter the agent or its sandbox. The human wait is durable — the
session sits idle server-side via `requires_action` until you respond — while the simple
streaming loop below is for development (drive it from a durable backend with the webhook
pattern in production).

###  AP2 mandates: verify, then reason

This agent reviews *agent-initiated* payments, so before any behavioral analysis it verifies an
**AP2 (Agent Payments Protocol)** mandate — the cryptographically signed credential that proves a
user authorized the payment. AP2 is an [open protocol(opens in new tab)](https://github.com/google-agentic-commerce/AP2)
for agent-driven commerce. Its mandates (a **Checkout Mandate** and a **Payment Mandate**) are
tamper-evident, signed digital objects forming an auditable chain. You do not need to learn the
protocol to follow this cookbook: **call the `verify_mandates` tool and act on its verdict**
(valid, constraints-satisfied, and double-spend). The signing and verification details — ES256 JWTs —
stay encapsulated in [`ap2_mandates.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/ap2_mandates.py), and the signed mandates and
receipts are stored in MongoDB alongside the transactions.

The cell below plays the "Trusted Surface" (generates a keypair, attaches signed mandates to the
pending cases). The private key stays in local Python state — never the agent, a tool result, or
the database.



from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives.asymmetric import ec

ts\_private\_key = ec.generate\_private\_key(ec.SECP256R1()) # Trusted Surface key, fresh each run

AGENT\_PK = (

ts\_private\_key.public\_key()

.public\_bytes(serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint)

.hex()

)

ts\_public\_key = ts\_private\_key.public\_key()

PENDING = [

"txn-review-clean",

"txn-review-fraud",

"txn-review-struct", # seeded human-override case under AUTO\_APPROVE

"txn-review-high",

"txn-review-ring",

]

mandates = attach\_mandates(coll, PENDING, agent\_pk=AGENT\_PK, ts\_private\_key=ts\_private\_key)

print(f"attached AP2 mandates to {len(mandates)} transactions agent\_pk={AGENT\_PK[:16]}…")



```
attached AP2 mandates to 5 transactions  agent_pk=04e1e32b7414d6f7…
```

###  The custom tools and host-side handlers

Each tool is a `type: "custom"` tool. When the agent calls one, the session pauses, **this
notebook** runs the handler with `pymongo`, and sends the JSON result back — the agent never
touches the database or the connection string. The handler implementations are defined in the
next cell: they wrap the Section 2 builders plus the AP2 verification (`verify_mandates`).
`HANDLERS` maps only the five data tools; `escalate` is deliberately absent because the gate
loop routes it to the human resolver instead of a handler (see the next section).



# The host-side tool implementations — the pymongo work behind each custom tool. These run in

# THIS process (never the sandbox), reusing the Section 2 builders. The dispatch wiring + the

# AP2/record-decision wrappers are in the next cell; build\_decision\_doc / build\_audit\_event

# (imported above) shape the persisted documents and are shared with the AP2 module.

def \_jsonable(value):

"""Recursively coerce Mongo/BSON values (ObjectId, datetime, ...) into JSON-safe types."""

if isinstance(value, dict):

return {k: \_jsonable(v) for k, v in value.items()}

if isinstance(value, (list, tuple)):

return [\_jsonable(v) for v in value]

if isinstance(value, datetime):

return value.isoformat()

if isinstance(value, (str, int, float, bool)) or value is None:

return value

return str(value)

def \_pick\_fields(candidate):

keep = ("transaction\_id", "text", "amount", "sender", "recipient", "decision", "score")

return \_jsonable({k: candidate[k] for k in keep if k in candidate})

def rerank\_pool\_size(k: int, fanout: int, \*, enable\_rerank: bool) -> int:

return k \* fanout if enable\_rerank else k

def merge\_rerank(candidates, rerank\_results, \*, top\_k) -> list[dict]:

def \_score(r):

s = getattr(r, "relevance\_score", None)

return (

(s if s is not None else r.get("relevance\_score", float("-inf")))

if isinstance(r, dict)

else (s if s is not None else float("-inf"))

)

seen: set[str] = set()

out: list[dict] = []

for result in sorted(rerank\_results, key=\_score, reverse=True):

index = getattr(result, "index", None)

if index is None and isinstance(result, dict):

index = result.get("index")

score = getattr(result, "relevance\_score", None)

if score is None and isinstance(result, dict):

score = result.get("relevance\_score")

if index is None or index < 0 or index >= len(candidates):

continue

candidate = candidates[index]

cid = str(candidate.get("transaction\_id", index))

if cid in seen:

continue

seen.add(cid)

out.append({\*\*candidate, "score": score})

if len(out) >= top\_k:

break

return out

def tool\_get\_transaction(coll, transaction\_id) -> dict:

doc = coll.find\_one({"transaction\_id": transaction\_id})

if not doc:

return {"error": "not\_found", "transaction\_id": transaction\_id}

return \_jsonable({k: v for k, v in doc.items() if k not in ("embedding", "\_id")})

def tool\_hybrid\_search\_similar\_frauds(

coll,

transaction\_id,

k,

\*,

enable\_rerank=False,

fanout=5,

reranker=None,

vector\_index=VECTOR\_INDEX\_NAME,

search\_index=SEARCH\_INDEX\_NAME,

status\_in=DECIDED\_STATUSES,

) -> dict:

txn = coll.find\_one({"transaction\_id": transaction\_id})

if not txn:

return {"error": "not\_found", "transaction\_id": transaction\_id, "similar": []}

qvec = txn["embedding"]

query = txn.get("text", "")

pool\_k = rerank\_pool\_size(k, fanout, enable\_rerank=enable\_rerank)

candidates = list(

coll.aggregate(

build\_rank\_fusion\_pipeline(

qvec,

query,

k=pool\_k,

vector\_index=vector\_index,

search\_index=search\_index,

status\_in=status\_in,

)

)

)

candidates = [c for c in candidates if str(c.get("transaction\_id")) != str(transaction\_id)]

if enable\_rerank and reranker is not None and candidates:

results = reranker(query, [c.get("text", "") for c in candidates], top\_k=k)

candidates = merge\_rerank(candidates, results, top\_k=k)

else:

candidates = candidates[:k]

return {"similar": [\_pick\_fields(c) for c in candidates]}

def tool\_detect\_fraud\_ring(coll, account\_id, \*, max\_depth=4) -> dict:

pipeline = build\_graph\_pipeline(account\_id, max\_depth=max\_depth, collection=coll.name)

docs = list(coll.aggregate(pipeline))

return \_jsonable(summarize\_ring(docs[0] if docs else {"chain": []}, seed\_account=account\_id))

def tool\_record\_decision(

db,

transaction\_id,

decision,

\*,

confidence,

risk\_factors,

reasoning,

reviewed\_by,

escalated=False,

recommended\_decision=None,

) -> dict:

decision\_doc = build\_decision\_doc(

transaction\_id,

decision,

confidence=confidence,

risk\_factors=risk\_factors,

reasoning=reasoning,

reviewed\_by=reviewed\_by,

)

db["transaction\_decisions"].insert\_one(decision\_doc)

if escalated:

audit = build\_audit\_event(

"escalated\_to\_human",

transaction\_id,

decision\_id=decision\_doc["decision\_id"],

severity="warning",

event\_data={"human\_decision": decision, "recommended\_decision": recommended\_decision},

)

else:

audit = build\_audit\_event(

"decision\_stored", transaction\_id, decision\_id=decision\_doc["decision\_id"]

)

db["audit\_events"].insert\_one(audit)

# Advance the lifecycle status to past tense (approve -> approved) so a decided case matches

# the seed's vocabulary and DECIDED\_STATUSES, making it eligible as precedent in later reviews.

status = {"approve": "approved", "reject": "rejected"}.get(decision, decision)

db["transactions"].update\_one({"transaction\_id": transaction\_id}, {"$set": {"status": status}})

return {"recorded": True, "decision\_id": decision\_doc["decision\_id"]}



TOOLS = [

{

"type": "custom",

"name": "verify\_mandates",

"description": "Validate the AP2 Checkout and Payment Mandate JWTs (signature, constraints, "

"double-spend). Run this FIRST. If valid=false, constraints\_satisfied=false, or "

"double\_spend\_detected=true, reject immediately.",

"input\_schema": {

"type": "object",

"properties": {"transaction\_id": {"type": "string"}},

"required": ["transaction\_id"],

},

},

{

"type": "custom",

"name": "get\_transaction",

"description": "Fetch the full transaction record under review.",

"input\_schema": {

"type": "object",

"properties": {"transaction\_id": {"type": "string"}},

"required": ["transaction\_id"],

},

},

{

"type": "custom",

"name": "hybrid\_search\_similar\_frauds",

"description": "Retrieve the most similar prior (already-decided) cases as precedent, using "

"hybrid vector + full-text search.",

"input\_schema": {

"type": "object",

"properties": {

"transaction\_id": {"type": "string"},

"k": {"type": "integer", "description": "how many precedents (default 5)"},

},

"required": ["transaction\_id"],

},

},

{

"type": "custom",

"name": "detect\_fraud\_ring",

"description": "Trace the account's sender->recipient chain for circular-flow / mule / layering patterns.",

"input\_schema": {

"type": "object",

"properties": {"account\_id": {"type": "string"}},

"required": ["account\_id"],

},

},

{

"type": "custom",

"name": "record\_decision",

"description": "Persist the final approve/reject decision with reasoning and an audit event.",

"input\_schema": {

"type": "object",

"properties": {

"transaction\_id": {"type": "string"},

"decision": {"type": "string", "enum": ["approve", "reject"]},

"confidence": {"type": "number"},

"risk\_factors": {"type": "array", "items": {"type": "string"}},

"reasoning": {"type": "string"},

"escalated": {"type": "boolean"},

"recommended\_decision": {"type": "string", "enum": ["approve", "reject"]},

},

"required": ["transaction\_id", "decision", "reasoning"],

},

},

{

"type": "custom",

"name": "escalate",

"description": "Send a risky case to a human reviewer for the final decision. Use for "

"medium-confidence, high-value, structuring, or fraud-ring cases.",

"input\_schema": {

"type": "object",

"properties": {

"transaction\_id": {"type": "string"},

"recommended\_decision": {"type": "string", "enum": ["approve", "reject"]},

"confidence": {"type": "number"},

"reason": {"type": "string"},

},

"required": ["transaction\_id", "recommended\_decision", "reason"],

},

},

]



# Host-side handlers — map each data tool to its handler function.

reranker = (

(lambda q, ds, top\_k: rerank(q, ds, client=ai\_client, top\_k=top\_k))

if (ENABLE\_RERANK and ai\_client)

else None

)

def \_verify\_mandates(inp):

result = tool\_verify\_mandates(db, inp["transaction\_id"], ts\_public\_key)

ok = result["valid"] and result["constraints\_satisfied"] and not result["double\_spend\_detected"]

print(f"\n [verify\_mandates] {inp['transaction\_id']}: {'pass' if ok else 'FAIL'}")

return result

def \_hybrid(inp):

return tool\_hybrid\_search\_similar\_frauds(

coll,

inp["transaction\_id"],

inp.get("k", 5),

enable\_rerank=ENABLE\_RERANK,

reranker=reranker,

)

def \_record(inp):

result = tool\_record\_decision(

db,

inp["transaction\_id"],

inp["decision"],

confidence=inp.get("confidence", 0),

risk\_factors=inp.get("risk\_factors", []),

reasoning=inp.get("reasoning", ""),

reviewed\_by="human" if inp.get("escalated") else "agent",

escalated=inp.get("escalated", False),

recommended\_decision=inp.get("recommended\_decision"),

)

if (

inp["decision"] == "approve"

): # store the AP2 receipt that later powers double-spend detection

txn\_doc = coll.find\_one(

{"transaction\_id": inp["transaction\_id"]},

{"checkout\_mandate\_jwt": 1, "mandate\_id": 1, "agent\_pk": 1},

)

if txn\_doc and txn\_doc.get("mandate\_id"):

checkout\_hash = hashlib.sha256(txn\_doc["checkout\_mandate\_jwt"].encode()).hexdigest()

store\_mandate\_receipt(

db, txn\_doc["mandate\_id"], txn\_doc["agent\_pk"], checkout\_hash, "approve"

)

return result

HANDLERS = {

"verify\_mandates": \_verify\_mandates,

"get\_transaction": lambda inp: tool\_get\_transaction(coll, inp["transaction\_id"]),

"hybrid\_search\_similar\_frauds": \_hybrid,

"detect\_fraud\_ring": lambda inp: tool\_detect\_fraud\_ring(coll, inp["account\_id"]),

"record\_decision": \_record,

}

###  Create the agent, environment, and session

`model`, `system`, and `tools` live on the **agent**. The session references it and provisions
the sandbox. Networking is `limited`: the agent reaches MongoDB only through the host-side round-trip.



SYSTEM = """You are a financial fraud reviewer. You will be given transaction IDs to review.

For EACH transaction, in order:

1. Call get\_transaction to read it.

2. Call verify\_mandates to validate the AP2 mandate chain (signature, constraints, double-spend).

HARD GATE: if verify\_mandates returns valid=false, constraints\_satisfied=false, OR

double\_spend\_detected=true, call record\_decision immediately with decision="reject" and

skip the remaining steps for that transaction.

3. Call hybrid\_search\_similar\_frauds to retrieve similar decided precedents.

4. Call detect\_fraud\_ring on the sender's account\_number to check for ring/mule patterns.

5. Weigh the precedents, the ring signal, the amount, and your confidence. Then make EXACTLY

ONE terminal call for that transaction:

- You MUST call escalate (do NOT call record\_decision yourself) whenever ANY of these holds:

\* a structuring amount ($4,900-$4,999),

\* a high-value amount (>= $50,000) that you would otherwise approve,

\* detect\_fraud\_ring reports suspicious\_patterns, or

\* your confidence is medium (~75-85).

Give your recommended\_decision and a short reason.

- Otherwise (a clear-cut case matching none of the above), call record\_decision (approve/reject).

When you escalate, you will receive the human's decision. Then call record\_decision with that

decision, escalated=true, and recommended\_decision set to what you had recommended.

Be concise. Move to the next transaction after recording a decision."""

agent = client.beta.agents.create(

name="MongoDB Atlas fraud reviewer", model=MODEL, system=SYSTEM, tools=TOOLS

)

environment = client.beta.environments.create(

name="fraud-review-env", config={"type": "cloud", "networking": {"type": "limited"}}

)

session = client.beta.sessions.create(

agent={"type": "agent", "id": agent.id, "version": agent.version},

environment\_id=environment.id,

title="Fraud review",

)

print("session:", session.id)

print(f"Watch in Console: https://platform.claude.com/workspaces/default/sessions/{session.id}")



```
session: sesn_01LbAUC1V36CQS3Sk26eixTc
Watch in Console: https://platform.claude.com/workspaces/default/sessions/sesn_01LbAUC1V36CQS3Sk26eixTc
```

###  Run the review with the human gate

Open the event stream, send the queue of pending transactions, and drive the gate loop with
`run_gate_loop`: data-tool calls are serviced automatically from `HANDLERS`, and an `escalate`
call pauses for a human. With `AUTO_APPROVE` set (for example, in CI), the gate resolves
deterministically and **overrides the agent on the seeded structuring case** so a differing
human verdict is visible. Otherwise, you are prompted inline.



OVERRIDE\_IDS = {"txn-review-struct"}

def resolve\_human\_decision(recommendation, \*, auto\_approve, override\_ids, txn\_id) -> str:

"""Stand in for a human reviewer. In CI (auto\_approve) it concurs with the agent, except on

the seeded override\_ids where it flips the verdict so a differing human decision is visible."""

opposite = "reject" if recommendation == "approve" else "approve"

if auto\_approve and txn\_id in set(override\_ids):

return opposite

return recommendation

def resolver(tool\_input):

txn\_id = tool\_input.get("transaction\_id", "")

recommended = tool\_input.get("recommended\_decision", "reject")

if AUTO\_APPROVE:

decision = resolve\_human\_decision(

recommended, auto\_approve=True, override\_ids=OVERRIDE\_IDS, txn\_id=txn\_id

)

flag = " <-- HUMAN OVERRIDE" if decision != recommended else ""

print(f" [human/auto] {txn\_id}: agent recommended {recommended} -> human {decision}{flag}")

return decision

print(

f"\n ESCALATED {txn\_id} (agent recommends {recommended}): {tool\_input.get('reason', '')}"

)

return (

"approve"

if input(" Your decision [approve/reject]: ").strip().lower().startswith("a")

else "reject"

)

def send\_result(custom\_tool\_use\_id, result):

client.beta.sessions.events.send(

session\_id=session.id,

events=[

{

"type": "user.custom\_tool\_result",

"custom\_tool\_use\_id": custom\_tool\_use\_id,

"content": [{"type": "text", "text": json.dumps(result)}],

}

],

)

def run\_gate\_loop(stream, send, \*, handlers, resolver) -> dict:

"""Drive the session to completion, servicing custom-tool calls as they arrive.

This is the whole Path A round-trip for a real workload. Each `agent.custom\_tool\_use`

event names a tool and its input; the session then goes idle with

`stop\_reason == "requires\_action"` until we answer. We look up the tool in `handlers`

(which run `pymongo` host-side — the credential never leaves this process), and route the

special `escalate` tool to the human `resolver` instead. We post each result back with

`send`, and the session resumes. Break on a terminal idle (`end\_turn`) or termination.

"""

pending: dict[str, Any] = {}

responded: set[str] = set()

serviced: list[tuple[str, dict]] = []

for ev in stream:

if ev.type == "agent.custom\_tool\_use":

pending[ev.id] = ev

elif ev.type == "session.status\_idle":

stop = getattr(ev, "stop\_reason", None)

if stop is None:

continue

if stop.type != "requires\_action":

break # end\_turn / retries\_exhausted — the run is done

for event\_id in stop.event\_ids or []:

if event\_id in responded:

continue

call = pending.get(event\_id)

if call is None:

continue

if call.name == "escalate":

result = {"human\_decision": resolver(call.input)}

else:

handler = handlers.get(call.name)

result = (

handler(call.input) if handler else {"error": f"unknown tool {call.name}"}

)

responded.add(event\_id)

send(event\_id, result)

serviced.append((call.name, result))

elif ev.type == "session.status\_terminated":

break

return {"serviced": serviced, "responded": sorted(responded)}

kickoff = {

"type": "user.message",

"content": [

{"type": "text", "text": "Review these flagged transactions: " + ", ".join(PENDING)}

],

}

run\_start = datetime.now(UTC)

with client.beta.sessions.events.stream(session\_id=session.id) as stream:

client.beta.sessions.events.send(session\_id=session.id, events=[kickoff])

gate\_result = run\_gate\_loop(stream, send\_result, handlers=HANDLERS, resolver=resolver)

wait\_for\_idle\_status(client, session.id)

print(f"\nserviced {len(gate\_result['serviced'])} tool calls")



```
[verify_mandates] txn-review-clean: pass

  [verify_mandates] txn-review-fraud: pass

  [verify_mandates] txn-review-struct: pass

  [verify_mandates] txn-review-high: pass

  [verify_mandates] txn-review-ring: pass

  ESCALATED txn-review-struct (agent recommends reject): Structuring indicator: cash deposit of $4,950 just under $5,000 CTR threshold, matching precedent (txn-struct-01, txn-struct-02) showing pattern of deliberate sub-threshold deposits from same account. Amount in structuring range per policy. Requires human review.

  Your decision [approve/reject]:  reject

  ESCALATED txn-review-high (agent recommends approve): High-value wire of $75,000 from Northwind Foods to Pacific Logistics for bulk shipment. Legitimate business transaction matching precedent txn-high-01 ($120,000 supplier wire, approved). Mandate valid, no fraud signals. Escalation required per policy for high-value transactions ≥ $50,000.

  Your decision [approve/reject]:  approve

  ESCALATED txn-review-ring (agent recommends reject): Money-mule ring detected. Sender ACC-RING-A (Quartz Trading) is part of a 4-account network with circular flows. Precedent txn-ring-01 (same sender/recipient, $920, rejected) shows identical pattern. Fraud ring analysis confirms suspicious_patterns, circular_flow. Requires human review for definitive ring-case determination.

  Your decision [approve/reject]:  reject

serviced 28 tool calls
```

###  Review the decisions and audit trail

Read the decisions and audit trail back from MongoDB. The decision and audit collections are
**append-only**, so the read-back is scoped to this run. The closing asserts make this a
**self-check**: a re-run that doesn't reproduce the expected lane mix fails loudly.

The human-override count reflects how the gate was resolved: with `AUTO_APPROVE` it is 1 (the
seeded override on `txn-review-struct` is shown), while in an interactive run it is 0 whenever
you concur with the agent's recommendation on every escalation — both are expected.



from collections import Counter

decisions = list(db["transaction\_decisions"].find({"created\_at": {"$gte": run\_start}}, {"\_id": 0}))

audits = list(db["audit\_events"].find({"timestamp": {"$gte": run\_start}}, {"\_id": 0}))

print("Decisions by lane:")

lanes = Counter()

for d in decisions:

txn = coll.find\_one({"transaction\_id": d["transaction\_id"]})

lanes[f"{(txn['lane'] if txn else '?')} -> {d['decision']}"] += 1

for k, v in sorted(lanes.items()):

print(f" {k}: {v}")

overrides = [

a

for a in audits

if a["event\_type"] == "escalated\_to\_human"

and a["event\_data"].get("human\_decision") != a["event\_data"].get("recommended\_decision")

]

print(

f"\nescalated\_to\_human events: {sum(1 for a in audits if a['event\_type'] == 'escalated\_to\_human')}"

)

print(f"human overrides (verdict != agent recommendation): {len(overrides)}")

for a in overrides:

ed = a["event\_data"]

print(

f" {a['transaction\_id']}: agent {ed['recommended\_decision']} -> human {ed['human\_decision']}"

)

# Self-check — fail loudly if this run didn't produce the expected result.

decided\_lanes = {coll.find\_one({"transaction\_id": d["transaction\_id"]})["lane"] for d in decisions}

assert decided\_lanes == {"clean\_approve", "clear\_reject", "high\_value", "ring", "structuring"}, (

f"expected all 5 lanes decided, saw {sorted(decided\_lanes)}"

)

assert len(decisions) == len(PENDING), f"expected {len(PENDING)} decisions, got {len(decisions)}"

assert sum(1 for a in audits if a["event\_type"] == "escalated\_to\_human") >= 1, (

"expected >=1 escalation"

)

if AUTO\_APPROVE:

assert overrides, "AUTO\_APPROVE run should show the seeded override on txn-review-struct"

print("\nself-check OK")



```
Decisions by lane:
  clean_approve -> approve: 1
  clear_reject -> reject: 1
  high_value -> approve: 1
  ring -> reject: 1
  structuring -> reject: 1

escalated_to_human events: 3
human overrides (verdict != agent recommendation): 0

self-check OK
```

##  4. MongoDB Atlas as the system of record and audit backbone

Step back and look at where the run's state lives: everything the agent did is durable in the
same cluster it retrieved from. That is the single-engine payoff on the write side —
`transactions` is the operational record (each case advances `pending` → `approved` or
`rejected`), `transaction_decisions` holds immutable verdicts, `audit_events` is an append-only
trail, and `mandate_receipts` powers double-spend detection. One case, end to end:



case = "txn-review-struct"

txn = coll.find\_one({"transaction\_id": case}, {"\_id": 0, "embedding": 0})

print(f"operational record: {case} lane={txn['lane']} status={txn['status']}")

decision = db["transaction\_decisions"].find\_one(

{"transaction\_id": case, "created\_at": {"$gte": run\_start}}, {"\_id": 0}

)

print(

f"decision record: {decision['decision']} reviewed\_by={decision['reviewed\_by']} confidence={decision['confidence\_score']}"

)

print("audit trail (append-only):")

for a in (

db["audit\_events"]

.find({"transaction\_id": case, "timestamp": {"$gte": run\_start}}, {"\_id": 0})

.sort("timestamp", 1)

):

extra = ""

if a["event\_type"] == "escalated\_to\_human":

ed = a["event\_data"]

extra = f" (agent recommended {ed['recommended\_decision']}, human decided {ed['human\_decision']})"

print(f" {a['timestamp']:%H:%M:%S} {a['event\_type']} severity={a['severity']}{extra}")

txn\_mandate = coll.find\_one({"transaction\_id": case}, {"mandate\_id": 1, "agent\_pk": 1})

if txn\_mandate and txn\_mandate.get("mandate\_id"):

receipt = db["mandate\_receipts"].find\_one({"mandate\_id": txn\_mandate["mandate\_id"]}, {"\_id": 0})

if receipt:

print(

f"mandate receipt: mandate\_id={receipt['mandate\_id'][:12]}… decision={receipt['decision']}"

)



```
operational record: txn-review-struct  lane=structuring  status=rejected
decision record:    reject  reviewed_by=human  confidence=0.9
audit trail (append-only):
  13:49:22  escalated_to_human  severity=warning  (agent recommended reject, human decided reject)
```

**Webhooks for production (pointer, not run here):** The streaming loop above is great for
development but does not survive a restart. For production, register a webhook for
`session.status_idled`: your handler queues the case for a reviewer and later POSTs the
`user.custom_tool_result`. The **data-tool handlers are identical**; only the trigger changes.
See [`CMA_operate_in_production.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_operate_in_production.ipynb).



client.beta.sessions.archive(session.id)

client.beta.environments.archive(environment.id)

# Agents are reusable across runs; archiving is optional and permanent.

mongo.close()

print("archived session + environment; closed MongoDB connection")



```
archived session + environment; closed MongoDB connection
```

##  5. Recap

You connected MongoDB Atlas to a Claude Managed Agent and took it from connection to system of
record in one build:

* **Connect** — three credential-safe data paths (host-side custom tool, self-hosted sandbox,
  self-hosted MCP), the MongoDB secret always on your side of the boundary.
* **Retrieve** — vector, full-text, hybrid RRF, and graph traversal as liftable pipeline
  builders, defined inline in Section 2.
* **Gate** — risky decisions behind CMA's native `requires_action` human pause.
* **Persist** — decisions, an append-only audit trail, and AP2 receipts in the same cluster the
  agent retrieves from.

The integration surface was small: a few lines of `pymongo` behind a custom tool. Swap the
collection and the tools, and the same shape grounds any agent in MongoDB. The retrieval
builders, tool handlers, and gate loop are all right here in the notebook; the
[`mongodb_on_cma/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/mongodb_on_cma/) package holds only the setup boilerplate.
