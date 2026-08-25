<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-consult-an-advisor -->

#  Advisor: let a working agent consult a stronger model mid-turn

Running every turn on your most capable model is the safe choice and the expensive one. Running on a mid-tier model is cheap until the agent hits the one decision in the task that needed more judgment, and by then it has committed. The usual fix is to build your own escalation: detect the hard case, package the context, call a bigger model, splice the answer back in.

An advisor does that inside the session. You name a second, more capable model in the agent's `multiagent` roster as an `{"type": "advisor", "model": ...}` entry. The primary thread then has an `advisor` tool it can call mid-turn: the platform puts the conversation so far in front of the advisor model, returns its guidance to the working model, and sampling continues. Each consultation runs as a short-lived platform thread with its own token usage, so you can see when it happened and price exactly what it cost.

This notebook walks through:

* adding an advisor entry to an agent
* telling the working model when to consult
* reading a consultation off the event stream and its cost off the thread
* what changes when the advisor's output comes back redacted

##  1. Set up the client

The advisor entry lives in the `multiagent` block, under the standard `managed-agents-2026-04-01` beta header. The typed roster shape needs `anthropic>=0.121.0`.

%%capture

%pip install -qU "anthropic>=0.121.0" python-dotenv

import os

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

WORKER\_MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5")

ADVISOR\_MODEL = os.environ.get("COOKBOOK\_ADVISOR\_MODEL", "claude-opus-5")

client = anthropic.Anthropic()

##  2. Give a Sonnet agent an Opus advisor

You declare the advisor in the roster, not as a tool definition and not as an agent you create separately. The entry goes in `multiagent.agents` alongside any specialists, and a roster that holds nothing but the advisor entry is valid: the agent consults but spawns no subagents. A few rules the server enforces at save time:

* At most one advisor entry per roster.
* The `model` must be permitted as an advisor, and the pairing of the agent's own model with it must be one the platform allows. An ineligible pairing is a 400 on `agents.create`, not a runtime surprise.
* The entry occupies the name `anthropic.advisor` in the roster, so no specialist can use that name.

At runtime the platform surfaces the entry to the working model as an `advisor` tool. The tool takes no input, because the advisor reads the whole conversation up to the call rather than a query the working model writes. So the system prompt is where you set the consultation policy: what it controls is when the model reaches for the tool.

SYSTEM = """You are a backend engineer designing HTTP APIs.

You have an advisor: a more capable model that can review your conversation so far and

send back guidance. Consult it with the advisor tool before you commit to any decision

that would be expensive to reverse once clients depend on it: identifier and idempotency

schemes, pagination contracts, error semantics, versioning. Do routine drafting yourself.

When you consult, act on the guidance you get back and say what you changed.

Write your final design to /mnt/session/outputs/design.md."""

designer = client.beta.agents.create(

name="api\_designer",

description="Designs HTTP APIs, escalating irreversible decisions to an advisor.",

model={"id": WORKER\_MODEL},

system=SYSTEM,

tools=[{"type": "agent\_toolset\_20260401"}],

multiagent={

"type": "coordinator",

"agents": [

{"type": "advisor", "model": ADVISOR\_MODEL},

],

},

betas=BETAS,

)

print(f"{designer.name}: {designer.id} v{designer.version}")

print("roster:", [entry.to\_dict() for entry in designer.multiagent.agents])

```
api_designer: agent_staging_018FvRjvrM6ASGuXXcDTAvdH v1
roster: [{'model': 'claude-opus-5', 'type': 'advisor'}]
```

##  3. Hand it a task with a hard call inside

An idempotency scheme for a money-moving endpoint is the kind of decision the prompt told the agent to escalate: cheap to write, expensive to change after clients ship against it. The rest of the design is routine, so a well-calibrated agent consults on that and drafts the remainder itself.

Consultation spend is bounded only by the consulting turn: advisor tokens bill in addition to the working model's, and there is no per-consultation cap. The session carries a `budget` so an over-eager escalation habit pauses at a known ceiling instead of running up the bill (the mechanics are in [`CMA_cap_session_spend.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_cap_session_spend.ipynb)).

env = client.beta.environments.create(

name="advisor-demo",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

betas=BETAS,

)

session = client.beta.sessions.create(

agent=designer.id,

environment\_id=env.id,

title="Design: refunds API",

budget={"type": "limit", "max\_list\_cost": {"currency": "USD", "amount": "500"}},

initial\_events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "Design the REST surface for a refunds resource on a payments "

"API: create, retrieve, list. Refund creation is retried by mobile "

"clients on flaky networks, and a double refund costs real money. "

"Cover the request/response shapes, idempotency, pagination on list, "

"and error codes.",

}

],

}

],

betas=BETAS,

)

print(session.id, session.status)

```
sesn_staging_013TqQwzrbUZDX1KJW2b9KnC running
```

##  4. Watch a consultation on the primary stream

A consultation is not an `agent.tool_use` event. It surfaces as a thread lifecycle on the primary stream, with `agent_name` set to `anthropic.advisor`:

session.thread\_created agent\_name: anthropic.advisor

session.thread\_status\_running agent\_name: anthropic.advisor

agent.thread\_message\_received from\_agent\_name: anthropic.advisor, content: [{type: "text", ...}]

session.thread\_status\_idle agent\_name: anthropic.advisor

session.thread\_status\_terminated agent\_name: anthropic.advisor

The consulting thread stays `running` the whole time. The advice is delivered at the point of the call and sampling continues, so from the outside the primary thread pauses, an advisor thread appears and disappears, and the primary thread resumes with the guidance folded in. Each consultation is a fresh thread that terminates itself when it delivers.

def advice\_text(content):

"""Render an advisor delivery: joined text, or a marker for the redacted arm."""

if any(block.type == "redacted" for block in content):

return "[redacted advice: content withheld by the advisor model's policy]"

return "".join(block.text for block in content if block.type == "text")

consultations = 0

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

if ev.type == "session.thread\_created" and ev.agent\_name == "anthropic.advisor":

consultations += 1

print(f"\n--- consulting advisor #{consultations} ({ev.session\_thread\_id}) ---")

elif (

ev.type == "agent.thread\_message\_received" and ev.from\_agent\_name == "anthropic.advisor"

):

print(advice\_text(ev.content)[:800])

print("--- advice received, primary thread resumes ---\n")

elif ev.type == "agent.message":

print("".join(b.text for b in ev.content if b.type == "text"), end="")

elif ev.type == "session.status\_idle":

print(f"\n[idle] stop\_reason={ev.stop\_reason.type}")

break

print(f"\nconsultations this turn: {consultations}")

```
--- consulting advisor #1 (sthr_staging_01PnQEQPc1nLxUK4S2vcVbCL) ---

[redacted advice: content withheld by the advisor model's policy]
--- advice received, primary thread resumes ---

Incorporated the advisor's feedback directly into the design — the most consequential changes were:

- **Idempotency became a stored resource with a claim→execute→finalize lifecycle**, not a simple header check. This closes the "processor succeeded but our server died before recording it" window, which a naive check-then-execute design leaves open.
- **Added a second, independent safety layer**: a server-side invariant (`sum(active refunds) + new_amount <= captured_amount`) enforced under a row lock, so the system is safe even if a client reuses/loses its idempotency key.
- **Made refund creation explicitly asynchronous** (`201` + `status: pending`, terminal states `succeeded|failed|canceled`) instead of implying synchronous success.
- **Added a recovery path** (`GET /refunds?idempotency_key=...`) for clients that lose the response to a request that actually succeeded — critical for flaky mobile networks.
- **Switched list pagination to opaque cursor-based** instead of offset, since refunds are append-heavy and offset pagination skips/duplicates rows under concurrent inserts.
- **Made the retry policy part of the documented contract** (which codes are safe to retry, and that retries must reuse the same idempotency key), not just implicit.
- **Resolved the nesting question**: creation under `/payments/{id}/refunds` for natural scoping and clean 404s; retrieve/list stay top-level at `/refunds`.

Full design written below.
The design is written to `/mnt/session/outputs/design.md`.

**Summary of the approach:**

- **Endpoints:** `POST /v1/payments/{payment_id}/refunds` (create, scoped to parent), `GET /v1/refunds/{id}` (retrieve), `GET /v1/refunds` (list) — top-level for retrieve/list per advisor guidance.
- **Idempotency — the centerpiece:** `Idempotency-Key` header is required and persisted as its own resource with a **claim → execute → finalize** lifecycle (claim written in the same transaction as the pending refund), so a crash after the processor succeeds but before we record it can't produce a silent duplicate on retry. Replay rules are explicit: same key+body replays the original response, same key+different body is a `422`, same key still in-flight is a `409`.
- **Second safety net, independent of the header:** a server-enforced invariant (`sum(active refunds) + new_amount <= captured_amount`) under a row lock, protecting against buggy clients that regenerate keys or omit them.
- **Async-first status model:** `201` means "accepted," not "money moved" — `pending → succeeded|failed|canceled`.
- **Recovery path:** `GET /v1/refunds?idempotency_key=...` so a client that lost the response never needs to guess by retrying a write.
- **Pagination:** opaque cursor on `(created_at DESC, id DESC)`, not offset, since refunds are append-only and growing.
- **Errors:** one envelope (`type`, `code`, `message`, `param`, `request_id`), plus an explicit table of which codes are safe to retry with the same key — documented as part of the API contract, not left to client guesswork.

All of this reflects the advisor's review — the biggest change from my initial draft was moving idempotency from "check a header" to "a durably-claimed resource," and adding the amount-conservation invariant as a belt-and-suspenders check that holds even when the idempotency layer is bypassed.
[idle] stop_reason=end_turn

consultations this turn: 1
```

##  5. Price the consultations

Because every consultation is a real session thread, its cost is on the thread rather than folded invisibly into the primary thread's numbers. Pull each advisor thread by the id from its `session.thread_created` event and read its `usage`. The token counts are there, and so is `usage.list_cost`: the thread's tokens priced at the advisor model's public list price, as an integer string in minor units of USD (`"131"` is $1.31), so the cost comes off the API instead of a rate card you maintain. Those tokens are billed in addition to the primary thread's, and they are already counted in the session-level `usage` aggregate, which carries a `list_cost` of its own.

A completed consultation is a `terminated` thread. It stays retrievable, but its `agent` is not the usual snapshotted agent: no Agent resource backs a platform advisor, so the thread carries the roster entry itself, `{"type": "advisor", "model": ...}`. That `agent.type` of `"advisor"` is the reliable way to tell a platform advisor thread apart from an ordinary child, more so than the name.

from decimal import Decimal

def usd(money) -> str:

"""Render an integer minor-unit amount ("131" = $1.31) as dollars."""

return f"${Decimal(money.amount) / 100:.2f}"

advisor\_thread\_ids = [

ev.session\_thread\_id

for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS)

if ev.type == "session.thread\_created" and ev.agent\_name == "anthropic.advisor"

]

advisor\_in = advisor\_out = 0

advisor\_cents = Decimal("0")

for thread\_id in advisor\_thread\_ids:

thread = client.beta.sessions.threads.retrieve(thread\_id, session\_id=session.id, betas=BETAS)

usage = thread.usage

advisor\_in += usage.input\_tokens or 0

advisor\_out += usage.output\_tokens or 0

advisor\_cents += Decimal(usage.list\_cost.amount)

print(

f"{thread.id} agent.type={thread.agent.type} model={thread.agent.model} "

f"status={thread.status} "

f"in={usage.input\_tokens} out={usage.output\_tokens} {usd(usage.list\_cost)}"

)

total = client.beta.sessions.retrieve(session.id, betas=BETAS).usage

print(f"\nadvisor tokens: in={advisor\_in} out={advisor\_out} cost=${advisor\_cents / 100:.2f}")

print(

f"session total: in={total.input\_tokens} out={total.output\_tokens} "

f"cost={usd(total.list\_cost)} (advisor included)"

)

```
sthr_staging_01PnQEQPc1nLxUK4S2vcVbCL  agent.type=advisor  model=claude-opus-5  status=terminated  in=603 out=2468  $0.07

advisor tokens: in=603 out=2468  cost=$0.07
session total:  in=15553 out=8491  cost=$0.21  (advisor included)
```

##  6. Read the design

The agent wrote the final document with the `write` tool. Pull it from the event log and look at the idempotency section, which is where the consultation landed.

design = ""

for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS):

if (

ev.type == "agent.tool\_use"

and ev.name == "write"

and ev.input.get("file\_path", "").endswith("design.md")

):

design = ev.input["content"] # keep the last write, in case of revisions

for line in design.splitlines():

if line.startswith("#"):

print(line)

print()

print(design[:1200])

```
# Refunds API Design
## 1. Resources & endpoints
## 2. Idempotency (the core problem: safe retries on flaky mobile networks)
### 2.1 Header contract
### 2.2 Server-side lifecycle (claim → execute → finalize)
### 2.3 Replay semantics (what a retry actually gets back)
### 2.4 Second, independent safety layer: a business invariant
### 2.5 Recovery path for lost responses
## 3. Request / response shapes
### 3.1 Create
### 3.2 Retrieve
### 3.3 List
## 4. Error model

# Refunds API Design

## 1. Resources & endpoints

| Action | Method & path |
|---|---|
| Create a refund | `POST /v1/payments/{payment_id}/refunds` |
| Retrieve a refund | `GET /v1/refunds/{refund_id}` |
| List refunds | `GET /v1/refunds` |
| Look up by idempotency key (recovery) | `GET /v1/refunds?idempotency_key={key}` |

**Why creation is nested but retrieve/list are top-level:** creation under the parent
gives a natural scope for the amount-conservation invariant ("refunds of this payment")
and a clean `404` when `payment_id` doesn't exist or isn't owned by the caller. Retrieve
and list don't need that scope, and clients generally want to fetch/list refunds without
knowing the parent — so they stay at a flat `/refunds` collection. Both resources are
versioned via the URL (`/v1/...`); breaking changes get a new version, not a new header.

Refund IDs: `re_<26-char base32 ulid>` — sortable by creation time, opaque, collision-safe,
visually distinct from payment IDs (`pi_...`). Never expose database auto-increment IDs.

## 2. Idempotency (the core problem: safe retries on flaky mobile networks)

### 2.1 Header contract

- `Idempotency-Key` is **required** on `POST .../refunds`. Cl
```

##  7. When the advice comes back redacted

Whether you get to read a consultation is a property of the advisor model, set by the same Anthropic policy that governs the Messages API advisor tool. For a model whose output the policy withholds, the delivery event carries `[{"type": "redacted"}]` placeholder blocks instead of text, and the advisor thread's own `agent.message` events are placeholders too.

Redaction changes what you observe, not what the agent uses. The working model reads the advice in full either way, so the design still improves. Everything structural stays visible: the thread, its status transitions, its timing, and its `usage`, which is why the `advice_text` helper in step 4 renders a marker rather than crashing. The advisor's own reasoning is never delivered under either policy, only its final text.

Since the policy can change without an API change, treat the `text` and `redacted` arms as equally normal in anything that consumes these events.

##  8. An advisor next to a specialist team

The advisor entry shares the `agents` array with ordinary roster members, so a coordinator can delegate to specialists and consult a stronger model in the same session. Only the primary thread consults. The specialists it spawns run without an advisor of their own, and advisor threads are exempt from the concurrency bound on child threads, so a coordinator already at its child limit can still consult.

client.beta.agents.create(

name="research\_coordinator",

model={"id": WORKER\_MODEL},

system="Delegate research to your specialists, then synthesize their reports.",

tools=[{"type": "agent\_toolset\_20260401"}],

multiagent={

"type": "coordinator",

"agents": [

"agent\_01Res...", # a specialist, by id

{"type": "agent", "id": "agent\_01Aud...", "version": 3},

{"type": "advisor", "model": ADVISOR\_MODEL}, # the advisor

],

},

betas=BETAS,

)

The coordinator pattern itself, per-role tool scoping and the delegation event types, is covered in [`CMA_coordinate_specialist_team.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb). The advisor is fixed for a session at creation: changing it on the agent affects sessions created afterward, not one already running.

##  9. Clean up

from utilities import wait\_for\_idle\_status

wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id, betas=BETAS)

client.beta.environments.archive(env.id, betas=BETAS)

print("archived")

```
archived
```
