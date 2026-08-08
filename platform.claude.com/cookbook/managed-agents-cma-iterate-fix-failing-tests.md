<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-iterate-fix-failing-tests -->

#  Iterate: do → observe → fix

This is the entry-point notebook. You'll learn the Managed Agents API surface by doing the most universal thing an agent does: try something, read what happened, try again. We upload a tiny package with two planted bugs, tell the agent to make the tests pass, and watch it work the loop, run the tests, read the traceback, edit the code, rerun, repeat until green.

Along the way you'll see every API shape the rest of the cookbook builds on: agent / environment / session, the file mount, the event stream, and the archive call. By the end of this notebook you'll have done everything you need to drive an agent end-to-end.

##  Concepts

Three resources to know about:

* **Agent**, a reusable config (model, system prompt, tools)
* **Environment**, a container template (packages, networking)
* **Session**, binds an agent and an environment, mounts any files the agent needs, and produces an event stream

You create an agent and an environment once and reuse them across many sessions. Each session is one self-contained run.



import os

from pathlib import Path

from anthropic import Anthropic

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-4-6")

client = Anthropic()

FIXTURE = Path("example\_data") / "iterate"

##  1. Create the agent

The system prompt is deliberately sparse. We want the agent to figure out the iterate loop for itself rather than follow a step-by-step script, the test output makes the task obvious enough without further hand-holding.

`agent_toolset_20260401` is the built-in toolset: bash, read, write, edit, glob, grep, web\_fetch, and web\_search. Setting `permission_policy` to `always_allow` lets the agent run them without round-tripping for confirmation.



agent = client.beta.agents.create(

name="cookbook-iterate",

model=MODEL,

system=(

"You are a debugging agent. Your job is to make failing tests pass. "

"Run the tests, read the failures, fix the code, repeat until green. "

"Stop when every assertion passes."

),

tools=[

{

"type": "agent\_toolset\_20260401",

"default\_config": {

"enabled": True,

"permission\_policy": {"type": "always\_allow"},

},

}

],

)

##  2. Create the environment

An environment is a container template. `type: cloud` runs in Anthropic's hosted sandbox. `networking: limited` blocks arbitrary outbound traffic, this notebook doesn't need network access at all, so we keep it locked down.



env = client.beta.environments.create(

name="cookbook-iterate-env",

config={"type": "cloud", "networking": {"type": "limited"}},

)

##  3. Upload the failing tests

Upload files through the Files API to get back IDs. We'll mount them on the session in step 4.

`calc.py` has two planted bugs and `test_calc.py` has three assertions that catch them. One of the failures (`test_mean`) is downstream of the other two, which quietly teaches the agent not to over-fix: `mean()` calls `add` and `divide` internally, so once those are fixed `test_mean` starts passing on its own without any direct edit to `mean()`.



calc\_file = client.beta.files.upload(

file=("calc.py", (FIXTURE / "calc.py").read\_bytes(), "text/x-python")

)

test\_file = client.beta.files.upload(

file=("test\_calc.py", (FIXTURE / "test\_calc.py").read\_bytes(), "text/x-python")

)

print(f"uploaded: {calc\_file.id}, {test\_file.id}")

##  4. Create the session

A session binds the agent and the environment, mounts any files the agent needs, and starts a fresh container. `resources=` is how you put data into the container before the agent starts — the orchestrate notebook shows how to use the same field to clone a GitHub repo instead of mounting individual files.

Files mount under `/mnt/session/uploads/<mount_path>`, which is read-only. The agent has to copy files into a writable directory like `/mnt/user` or `/tmp` before it can edit them, and anything you want to retrieve later goes in `/mnt/session/outputs/`.



session = client.beta.sessions.create(

environment\_id=env.id,

agent={"type": "agent", "id": agent.id, "version": agent.version},

resources=[

{"type": "file", "file\_id": calc\_file.id, "mount\_path": "calc.py"},

{"type": "file", "file\_id": test\_file.id, "mount\_path": "test\_calc.py"},

],

title="Get the tests green",

)

print(f"session: {session.id}")

##  5. Drive the agent and watch it work

Two steps: send a `user.message` event with the task, then read the event stream until the agent reaches `end_turn`.

The stream is a server-sent event connection. We use it (rather than polling, see the sidebar at the end) because the agent will spend ~30 seconds iterating and we want to see each round live.

Two patterns to internalize:

1. **Open the stream first, then send.** The `with` block opens the SSE connection; anything you `send` inside the block is guaranteed to be observable. Sending before opening risks losing events that fire in the race window.
2. **Exit on `session.status_idle` with `stop_reason.type == "end_turn"`.** The session goes idle any time it's waiting for input, both at end of turn AND when a custom tool call needs a response. `stop_reason.type` disambiguates; `end_turn` is our exit signal. The gate notebook shows the `requires_action` side of the same loop.



with client.beta.sessions.events.stream(session.id) as stream:

client.beta.sessions.events.send(

session\_id=session.id,

events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": (

"The tests in /mnt/session/uploads/test\_calc.py are "

"failing. Copy both files into /mnt/user, iterate "

"on calc.py until every test passes, then write the "

"final calc.py to /mnt/session/outputs/calc.py. "

"pytest isn't installed here, run the assertions "

"directly with `python3 -c ...` instead."

),

}

],

}

],

)

print("--- iterate loop ---")

for ev in stream:

match ev.type:

case "agent.message":

for b in ev.content:

if b.type == "text":

print(b.text, end="")

case "agent.tool\_use":

print(f"\n[{ev.name}]")

case "session.status\_idle" if ev.stop\_reason and ev.stop\_reason.type == "end\_turn":

break

case "session.status\_terminated":

break

That `match ev.type:` block is the canonical streaming pattern. Every other notebook in this cookbook imports it as `stream_until_end_turn` from `utilities.py` instead of repeating the loop. We use it for the verify step below.

`wait_for_idle_status` is the second helper from `utilities.py`. It absorbs the race described in the callout in step 7: even after a stream has yielded `session.status_idle`, the server-side `status` field on the session record can briefly still read `running`, and an immediate `archive()` call would 400. The helper just polls `sessions.retrieve` until the field settles. Code that streams and then archives in the next breath needs it.



from utilities import stream\_until\_end\_turn, wait\_for\_idle\_status

##  6. Verify

Don't take the agent's word for it. Re-run every assertion one more time independently and print the final `calc.py`. If the agent over-fixed or regressed something between the last in-loop run and the end of the turn, this catches it.



client.beta.sessions.events.send(

session\_id=session.id,

events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": (

"Re-run every assertion from "

"/mnt/session/uploads/test\_calc.py one more time "

"against your final calc.py with `python3 -c ...` "

"to confirm they all pass, then cat the final "

"/mnt/session/outputs/calc.py."

),

}

],

}

],

)

stream\_until\_end\_turn(client, session.id)

##  7. Cleanup

Archiving is how you mark a session, environment, or agent as finished. It tears down any live container, stops the resource from counting against your workspace quotas, and hides it from default list views, but it keeps the record, configuration, and event history around for audit and for anyone who wants to retrieve the resource later by ID. If you want to remove the record entirely, most resources also expose a separate `delete` endpoint (the operate notebook walks through resource lifecycle in detail), but `archive` is almost always what you want at the end of a run.



wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id)

client.beta.environments.archive(env.id)

client.beta.agents.archive(agent.id)

print("archived")

##  Sidebar: polling instead of streaming

The streaming pattern in step 5 is the right choice when you want live progress on something the agent will spend more than a few seconds on. For shorter tasks, or for production code where you don't want a long-lived HTTP connection, you can do the same thing with `events.list` polling instead:



client.beta.sessions.events.send(session\_id=..., events=[...])

while True:

time.sleep(2)

events = client.beta.sessions.events.list(session.id).data

last = events[-1] if events else None

if last and last.type == "session.status\_terminated":

break

if (

last

and last.type == "session.status\_idle"

and last.stop\_reason

and last.stop\_reason.type == "end\_turn"

):

break

# walk events to print agent.message text

Tradeoffs:

Streaming wins when you want to watch the agent work. Every tool call, every partial message, every state transition arrives as soon as the server emits it, which is exactly what you want while developing a new workflow. The cost is a long-lived SSE connection: your process has to stay alive for the duration of the turn, it can't pause and resume across gaps, and a network blip at the wrong moment can drop you mid-stream with no clean way to recover where you left off.

Polling wins in the opposite situation. It's stateless, survives process restarts, and composes cleanly with webhook handlers and queue workers that don't want to hold connections open. The cost is latency and hidden progress: you don't see anything until you poll again, so feedback is bounded by your poll interval, and a long turn looks like silence until it's done.

In production setups where the agent might run for minutes and your handler can't hold a connection open, the polling pattern (or its production cousin, the `session.status_idled` webhook shown in the gate notebook) is what you want.

##  Where to go next

The iterate loop is the simplest shape an agent loop takes. Four companion notebooks in this directory build on the same API shapes and show other workflows you can drive:

* [`CMA_orchestrate_issue_to_pr.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_orchestrate_issue_to_pr.ipynb) — multi-turn agent that carries state through a longer tool chain: read an issue, write a fix, open a PR, recover from a CI failure, address a review comment, and merge.
* [`CMA_explore_unfamiliar_codebase.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_explore_unfamiliar_codebase.ipynb) — the grounding pattern for an agent dropped into a repo it has never seen, with a planted stale-doc trap. Also shows `sessions.resources.add` for pushing more context into a running session.
* [`CMA_gate_human_in_the_loop.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb) — custom-tool `decide()` and `escalate()` round-trip for human-in-the-loop workflows. Covers the `requires_action` idle bounce and parallel-tool-call dedupe.
* [`CMA_operate_in_production.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_operate_in_production.ipynb) — production setup story: vault-backed MCP credentials, the `session.status_idled` webhook for HITL without long-lived connections, and the resource lifecycle CRUD verbs.
