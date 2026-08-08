<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-cap-session-spend -->

#  Budgets: cap what a session can spend

An unattended agent has no natural stopping point on cost. A research task with web search can drift into another hundred fetches. A coding loop can retry a flaky test until morning. Without a ceiling you find out from the invoice.

A session budget is an enforced spend cap on a single session. You set a maximum list cost when you create the session. The platform tracks the token cost of every thread in that session at public list prices, and when the running total reaches the cap the session goes idle with the stop reason `budget_reached`. Its files, tool state, and conversation stay intact. Raise the cap and the work continues from where it stopped.

This notebook walks through:

* setting a `budget` on `sessions.create`
* reading `usage.list_cost` and the `session.usage` snapshot the stream delivers as the turn ends
* the `budget_reached` stop and what a paused session keeps
* raising, lowering, and removing the cap with `sessions.update`

##  1. Set up the client

Budgets ride the standard `managed-agents-2026-04-01` beta header. The `budget` parameter and the cost fields on `session.usage` need `anthropic>=0.121.0`.



%%capture

%pip install -qU "anthropic>=0.121.0" python-dotenv



import os

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5")

client = anthropic.Anthropic()

##  2. Build an agent with room to overspend

The agent for this walkthrough writes a competitive landscape brief. It has web search and web fetch, and nothing in its prompt bounds how many sources it reads. That open-endedness is what a budget is for.



env = client.beta.environments.create(

name="budget-demo",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

betas=BETAS,

)

analyst = client.beta.agents.create(

name="market\_analyst",

description="Writes sourced competitive landscape briefs.",

model={"id": MODEL},

system="""You write competitive landscape briefs for product teams.

Given a market, use web search and web fetch to find the notable vendors, their

positioning, and recent moves. Read primary sources rather than aggregators.

Write the brief to /mnt/session/outputs/brief.md with a Sources section listing every

URL you relied on. Keep researching until you are confident the brief is complete.""",

tools=[

{

"type": "agent\_toolset\_20260401",

"configs": [{"name": "web\_search"}, {"name": "web\_fetch"}],

}

],

betas=BETAS,

)

print(f"{analyst.name}: {analyst.id} v{analyst.version}")



```
market_analyst: agent_staging_014U3BWzuiSNDwfzubN38hnz v1
```

##  3. Create the session with a budget

The `budget` field on `sessions.create` sets the cap:



{"type": "limit", "max\_list\_cost": {"currency": "USD", "amount": "10"}}

A few properties worth knowing before you pick a number:

* `amount` is an integer string in the currency's minor units: `"50"` is fifty cents, `"2500"` is $25.00. It stays a string, and fractional cents are rejected, so no float rounding is ever applied. `USD` is the only accepted currency, and every cost amount the API returns (`usage.list_cost` included) uses the same encoding.
* The cap counts model token cost at public list price, summed across every thread in the session, including subagent threads. List price applies regardless of any negotiated discount, so the cap fires at or before your actual charge, and you can reproduce the number from `session.usage` plus the public rate card.
* Every model the session can run needs a public list price. If one does not, create fails with `model_not_budgetable`.
* Omit `budget` and the session is uncapped. A budget can only be attached at creation: a session created without one can never gain one later, so decide up front.

The cap here is ten cents, deliberately low so the stop shows up in a couple of minutes. The `usd` helper renders minor-unit amounts as dollars for every printout below.



from decimal import Decimal

def usd(money) -> str:

"""Render an integer minor-unit amount ("50" = fifty cents) as dollars."""

return f"${Decimal(money.amount) / 100:.2f}"

session = client.beta.sessions.create(

agent=analyst.id,

environment\_id=env.id,

title="Landscape brief: observability platforms",

budget={

"type": "limit",

"max\_list\_cost": {"currency": "USD", "amount": "10"},

},

initial\_events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "Write a competitive landscape brief on the observability "

"platform market: the main vendors, how each positions itself, "

"and any notable moves in the last year.",

}

],

}

],

betas=BETAS,

)

print(session.id, session.status)

print("budget:", usd(session.budget.max\_list\_cost))



```
sesn_staging_01ELJgA2vqTR6EmjX8viwHZi running
budget: $0.10
```

##  4. Watch spend accumulate

Alongside the usual `agent.message` and `agent.tool_use` events, the stream delivers a `session.usage` snapshot each time the session settles into `idle`. It holds the cumulative token counts, the tracked `list_cost`, and the configured `budget`, so the moment the turn ends you know what it cost without a second call to `sessions.retrieve`.

The loop exits on `session.status_idle`. With a budget in play there are two stop reasons that end the turn: `end_turn` when the agent finishes and `budget_reached` when the cap fires first.



stop\_reason = None

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

if ev.type == "agent.tool\_use":

print(f"[{ev.name}] {str(ev.input)[:80]}")

elif ev.type == "session.usage":

print(f" usage: {usd(ev.usage.list\_cost)} of {usd(ev.budget.max\_list\_cost)}")

elif ev.type == "session.status\_idle":

stop\_reason = ev.stop\_reason.type

print(f"[idle] stop\_reason={stop\_reason}")

break

assert stop\_reason == "budget\_reached", (

f"expected budget\_reached, got {stop\_reason}: lower the cap in step 3 "

"or give the agent a bigger task"

)



```
[repl] {'script': '\nlet queries = [\n  "Datadog positioning observability platform 202
[web_search] {'query': 'Datadog positioning observability platform 2025'}
[web_search] {'query': 'New Relic observability platform positioning 2025'}
[web_search] {'query': 'Dynatrace observability platform AI 2025'}
[web_search] {'query': 'Splunk Cisco observability 2025'}
[web_search] {'query': 'Grafana Labs observability platform 2025 announcement'}
[web_search] {'query': 'Elastic observability 2025'}
[web_search] {'query': 'Honeycomb observability 2025'}
[web_search] {'query': 'Chronosphere observability 2025 acquisition'}
[web_search] {'query': 'Datadog acquisition 2024 2025'}
[web_search] {'query': 'Grafana Labs acquisition 2024 2025'}

  usage: $0.12 of $0.10
[idle] stop_reason=budget_reached
```

##  5. Inspect the paused session

`budget_reached` is a pause, not a failure. The session sits in `idle`, its `usage` reflects everything spent so far, and the container still holds whatever the agent wrote before the cap. Nothing needs to be rerun.

The cap is enforced between model requests, so the recorded `list_cost` can land slightly past `max_list_cost`: the request that crosses the line finishes, then the session pauses. Size your cap with that one-request margin in mind.



paused = client.beta.sessions.retrieve(session.id, betas=BETAS)

print("status: ", paused.status)

print("list cost: ", usd(paused.usage.list\_cost))

print("cap: ", usd(paused.budget.max\_list\_cost))

print("tokens: in", paused.usage.input\_tokens, "out", paused.usage.output\_tokens)

print("active secs: ", round(paused.usage.active\_seconds, 1))



```
status:       idle
list cost:    $0.12
cap:          $0.10
tokens:       in 471 out 606
active secs:  13.7
```

The event log shows how far the agent got: the tool calls it made and, if it had begun narrating, its last message. An agent deep in research may have written nothing yet when the cap fires, so treat the message as optional.



events = list(client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS))

tool\_calls = [ev for ev in events if ev.type == "agent.tool\_use"]

messages = [ev for ev in events if ev.type == "agent.message"]

print(f"tool calls before the cap: {len(tool\_calls)}")

if messages:

last = messages[-1]

print("".join(b.text for b in last.content if b.type == "text")[:600])

else:

print("(no agent.message yet: the agent was still gathering sources when the cap fired)")



```
tool calls before the cap: 11
(no agent.message yet: the agent was still gathering sources when the cap fired)
```

##  6. Raise the cap and let it finish

`sessions.update` accepts the same `budget` shape. Raising `max_list_cost` above the consumed cost lifts the pause and the session resumes the interrupted turn on its own, from the state it stopped in.

Lowering the cap to at or below what the session already spent is rejected with a 400: `max_list_cost` must stay above the consumed list cost, so an update can never wedge a session against its own history. The first call demonstrates the rejection, the second raises the cap for real. No follow-up message is needed after the raise; the session moves back to `running` and picks up the interrupted turn.



try:

client.beta.sessions.update(

session.id,

budget={"type": "limit", "max\_list\_cost": {"currency": "USD", "amount": "1"}},

betas=BETAS,

)

except anthropic.BadRequestError as e:

print("lower rejected:", e.message)

client.beta.sessions.update(

session.id,

budget={"type": "limit", "max\_list\_cost": {"currency": "USD", "amount": "500"}},

betas=BETAS,

)

print("cap raised to $5.00")



```
lower rejected: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': "`budget.max_list_cost` must be greater than the session's consumed list cost"}, 'request_id': 'req_staging_011CdiPi8iPJKWdiuurZuDkB'}

cap raised to $5.00
```



with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

if ev.type == "session.status\_running":

print("[resumed]")

elif ev.type == "agent.tool\_use":

print(f"[{ev.name}]")

elif ev.type == "session.status\_idle":

print(f"[idle] stop\_reason={ev.stop\_reason.type}")

break

done = client.beta.sessions.retrieve(session.id, betas=BETAS)

print("final list cost:", usd(done.usage.list\_cost), "of cap", usd(done.budget.max\_list\_cost))



```
[resumed]

[repl]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]
[web_search]

[repl]
[web_fetch]
[web_fetch]
[web_fetch]
[web_fetch]
[web_fetch]
[web_fetch]
[web_fetch]
[web_fetch]

[repl]
[web_fetch]

[web_fetch]
[web_fetch]

[web_fetch]

[web_fetch]
[web_fetch]

[web_fetch]
[web_fetch]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[bash]

[repl]
[web_search]

[repl]
[web_search]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[web_search]

[repl]
[web_fetch]

[web_fetch]

[web_fetch]

[web_fetch]

[repl]
[web_fetch]

[web_fetch]
[web_fetch]

[write]

[write]

[bash]

[idle] stop_reason=end_turn

final list cost: $1.83 of cap $5.00
```

##  7. Read the brief

The agent picked the task back up with its context intact and finished the write. Pull the file it produced from the event log.



brief = ""

for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS):

if (

ev.type == "agent.tool\_use"

and ev.name == "write"

and ev.input.get("file\_path", "").endswith("brief.md")

):

brief = ev.input["content"] # keep the last write, in case of revisions

print(brief[:1500] + ("\n..." if len(brief) > 1500 else ""))



```
# Competitive Landscape Brief: Observability Platform Market

*Scope: commercial platforms for metrics, logs, traces, and related telemetry (APM, infrastructure monitoring, log management, digital experience monitoring) used by engineering, IT operations, and SRE teams. Window for "recent moves": roughly the last twelve months of vendor activity found in primary sources (mid‑2025 through mid‑2026).*

## 1. Market shape

Observability has consolidated into a market with a handful of large, broad "full platform" vendors (Datadog, Splunk/Cisco, Dynatrace, New Relic, Elastic, Grafana Labs), a tier of cost‑ and scale‑focused challengers (Chronosphere, Coralogix, Honeycomb, SolarWinds, LogicMonitor, Sumo Logic), hyperscaler-native tooling bundled into the cloud platforms (AWS CloudWatch, Azure Monitor, Google Cloud Observability), and an open standard — OpenTelemetry — that now sits underneath almost every vendor's ingestion layer and was elevated to CNCF "graduated" status, cementing it as the de facto instrumentation standard (CNCF, announcement). Gartner's 2025 Magic Quadrant for Observability Platforms evaluated 20 vendors (AWS, Apica, BMC Helix, Chronosphere, Coralogix, Datadog, Dynatrace, Elastic, Grafana Labs, Honeycomb, IBM, ITRS, LogicMonitor, Microsoft, New Relic, Oracle, ScienceLogic, SolarWinds, Splunk, Sumo Logic), naming Datadog, Splunk, Dynatrace, New Relic, Elastic, Grafana Labs, Chronosphere, and IBM as Leaders (Gartner, 7 July 2025; corroborated by Datadog, Splunk
...
```

##  8. Remove the budget

Passing `budget=None` on update clears the cap, so the session is uncapped from that point on. Omitting `budget` entirely leaves the current cap in place. Those are two different requests: `None` is an explicit removal, absence is a preserve.

Removal is permanent for the same reason attachment is create-only: once a session has no budget, it can't gain one. Raise and lower the cap as often as you like, but treat removing it as a one-way door.



uncapped = client.beta.sessions.update(session.id, budget=None, betas=BETAS)

print("budget:", uncapped.budget)



```
budget: None
```

##  9. Clean up



from utilities import wait\_for\_idle\_status

wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id, betas=BETAS)

client.beta.environments.archive(env.id, betas=BETAS)

print("archived")



```
archived
```

##  Where budgets fit

A budget is a per-session control. It bounds one run, not an org, a workspace, or a day of traffic, so it composes with the spend limits you already set at those levels rather than replacing them. Reach for it whenever a session runs without a human watching: cron-driven deployments, webhook-triggered agents, long multiagent jobs where the coordinator's fan-out is data-dependent.

For fleets you are not streaming, subscribe to the `session.budget_reached` webhook instead of holding a connection open. It fires once when a session hits its cap, and the payload names the session so a supervisor process can decide whether to raise the cap or let the session stay paused. The webhook pattern is covered in [`CMA_operate_in_production.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_operate_in_production.ipynb).
