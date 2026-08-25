<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-plan-big-execute-small -->

#  Coordinator pattern: big models for planning, small models for execution

##  Introduction

Most agent workloads have two very different jobs inside them: a small amount of planning and judgment, and a large amount of mechanical reading and doing. Web research is the extreme case, and it's the example this notebook uses: verifying twenty facts against their authoritative sources means pulling hundreds of thousands of tokens of web pages through a model, and at frontier rates that reading bill dominates.

The coordinator pattern splits the two workloads. A frontier model plans the research and synthesizes the answer, but it never touches a raw web page — cheap workers do all the reading in their own parallel context windows and report back distilled findings. This notebook measures the split honestly: it runs the realistic alternative — one frontier agent with the same tools, held to the same verification standard — on the same question, and compares real bills and real wall-clock. On the authors' runs both arms read about the same amount, and the team came out roughly 2.5x cheaper and 3x faster, with 84-98% of its input tokens billed at the worker rate.

**By the end of this cookbook, you'll be able to:**

* Configure a two-model team with the `multiagent` coordinator field: a frontier coordinator and cheap search workers
* Follow a delegation live through the session event stream (`thread_created`, `thread_message_sent`, `thread_message_received`)
* Run a rigor-matched solo-frontier control and compare real bills
* Meter each thread with the typed per-thread cumulative `usage`

The same economics apply to any workload where a cheap model can do the token-heavy leg: document review, log analysis, codebase sweeps.

![Architecture of the coordinator pattern: the user's question goes to a frontier-model coordinator with no tools of its own; it sends one brief per park to parallel small-model search workers and gets distilled findings back; only the workers touch the open web, via web search and page fetch; the coordinator synthesizes the final answer.](https://platform.claude.com/cookbook/images/notebooks/managed-agents-cma-plan-big-execute-small/architecture_diagram.png)

##  Prerequisites

Before following this guide, ensure you have:

**Required Knowledge:**

* Python fundamentals
* Familiarity with the Managed Agents basics — agents, environments, sessions, and the streaming event loop ([`CMA_iterate_fix_failing_tests.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_iterate_fix_failing_tests.ipynb) introduces all of them)

**Required Tools:**

* Python 3.11 or higher
* Anthropic API key ([get one here(opens in new tab)](https://console.anthropic.com)) with access to the Managed Agents beta

If you haven't seen the `multiagent` field before, [`CMA_coordinate_specialist_team.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb) introduces it with a heterogeneous specialist team. This notebook uses the simplest possible team — one worker type — because the point here is the cost structure, not the team design.

##  Setup

%%capture

%pip install -qU "anthropic>=0.121.0" python-dotenv

import os

import time

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

# The frontier model plans and synthesizes; the cheap model reads the web.

COORDINATOR\_MODEL = os.environ.get("COOKBOOK\_COORDINATOR\_MODEL", "claude-fable-5")

WORKER\_MODEL = os.environ.get("COOKBOOK\_WORKER\_MODEL", "claude-sonnet-5")

client = anthropic.Anthropic()

##  1. The team: cheap readers, expensive thinker

Two agent definitions make the whole team.

The **worker** — in the docs' terms, a subagent the coordinator can spawn from its roster — is an ordinary agent: a model, a toolset scoped down to `web_search` + `web_fetch`, and a system prompt. Each worker instance researches one focused sub-question in its own session thread, so the giant web pages it reads never enter anyone else's context.

The **coordinator** has no tools of its own — only a `multiagent` roster naming the worker. That one field is what makes it a coordinator: the server automatically gives it `create_agent`, `send_to_agent`, `wait_for_agents`, and `list_agents`, and workers get `submit_result` and `send_to_parent` the same way. You never define any of those tools.

Two things to know about this relationship. First, the roster is snapshotted when the coordinator is created or updated — if you change the worker's definition, update or recreate the coordinator. Second, and less obvious: **the coordinator can't see anything about its roster agents** — not their prompts, not their names, not their descriptions. Its `create_agent` tool takes a bare agent name and task string. Everything the coordinator believes about its workers comes from its own system prompt, so keep that description and the workers' actual prompts in agreement — nothing on the server enforces it. (With a single-agent roster, any requested name resolves to the one worker; with several worker types, name them explicitly in the coordinator's prompt.)

worker = client.beta.agents.create(

name="search-worker",

model=WORKER\_MODEL,

# Everything off except the two web tools: the worker's job is

# reading, and scoping keeps the cheap model from wandering into

# bash or the filesystem. It's also the security boundary: workers

# read arbitrary (untrusted) web pages, so a worker that can only

# search, fetch, and report back is the blast radius you want for

# that input — and the coordinator reading the reports has no

# tools at all.

tools=[

{

"type": "agent\_toolset\_20260401",

"default\_config": {"enabled": False},

"configs": [

{"name": "web\_search", "enabled": True},

{"name": "web\_fetch", "enabled": True},

],

}

],

system=(

"You are a search worker researching one focused sub-question for "

"a coordinator. Use web\_search and web\_fetch to find the answer. "

"Be thorough: try multiple query phrasings, follow promising "

"links, and cross-check facts across sources. Report back with "

"the specific answer you found and the evidence (URLs, quotes) "

"that supports it. If you could not find a definitive answer, say "

"exactly what you did find and what remains uncertain. Always "

"finish by calling submit\_result."

),

betas=BETAS,

)

coordinator = client.beta.agents.create(

name="search-coordinator",

model=COORDINATOR\_MODEL,

multiagent={

"type": "coordinator",

"agents": [{"type": "agent", "id": worker.id}],

},

system=(

"You are coordinating a team of search workers to answer a hard "

"web-research question. Your workers have web\_search and "

"web\_fetch; you do not. Break the question into focused "

"sub-questions and delegate each to a worker via create\_agent. "

"Run several workers in parallel on independent sub-questions, "

"and ALWAYS call wait\_for\_agents after spawning before drawing "

"any conclusion. When a worker reports, decide whether its "

"findings answer the sub-question or whether to send a follow-up "

"with send\_to\_agent. If a worker returns an infrastructure error "

"(rate limit, timeout) instead of findings, re-assign the same "

"sub-question to a fresh worker. Once you have enough evidence, "

"synthesize the workers' findings into a single final answer to "

"the original question."

),

betas=BETAS,

)

print(f"worker {worker.id}")

print(f"coordinator {coordinator.id}")

##  2. Run a research question

Create an environment and a session for the coordinator, send the question as a `user.message`, and stream. The session-level stream is the coordinator's primary thread — a condensed view of the whole run. Worker threads show up in it as delegation traffic: `session.thread_created` when a worker is spawned, `agent.thread_message_sent` when the coordinator hands one a sub-question, and `agent.thread_message_received` when the findings come back.

The question is a coverage task — twenty facts (10 parks x 2 attributes), each of which must be verified against a specific authoritative source. Coverage questions are where the pattern shines, because the reading is mandatory: nobody gets to answer from memory, so the only question is what rate the reading bills at and whether it happens in parallel. (Discovery questions — find one answer hiding in a big search space, in the style of benchmarks like [BrowseComp(opens in new tab)](https://arxiv.org/abs/2504.12516) — reward a frontier model's search intuition more, and the gap narrows.)

Fan-out is data-dependent: the coordinator decides how many workers to spawn, so nothing in the prompt fixes its ceiling. The session below carries a `budget`, an enforced cap on the whole team's list cost across every thread. The $10 cap is generous enough that a normal run never touches it, but if a bad question ever sent the coordinator spawning workers without end, the session would pause at the cap instead of running up the bill. The pause mechanics, and raising the cap afterward, are in [`CMA_cap_session_spend.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_cap_session_spend.ipynb).

env = client.beta.environments.create(

name="research-fanout",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

)

session = client.beta.sessions.create(

agent=coordinator.id,

environment\_id=env.id,

# guardrail on data-dependent fan-out: cap the whole team's list cost

budget={"type": "limit", "max\_list\_cost": {"currency": "USD", "amount": "1000"}},

betas=BETAS,

)

QUESTION = (

"For each of the ten largest national parks in the contiguous United "

"States by area, find: the current standard private-vehicle entrance "

"fee, and whether the park currently requires a timed-entry or "

"day-use reservation for peak season. Each fact must be verified "

"against that park's official nps.gov pages (fees page and alerts/"

"reservations page) - not from third-party summaries. Give park, fee, "

"reservation requirement, and the nps.gov URLs you used."

)

t\_start = time.monotonic()

client.beta.sessions.events.send(

session.id,

betas=BETAS,

events=[{"type": "user.message", "content": [{"type": "text", "text": QUESTION}]}],

)

def text\_of(content):

return "".join(b.text for b in content or [] if b.type == "text")

def clip(s, n=160):

return s[:n] + ("..." if len(s) > n else "")

final\_answer = ""

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

match ev.type:

case "agent.message":

if text := text\_of(ev.content).strip():

final\_answer = text

print(f"[coordinator] {clip(text, 200)}")

case "session.thread\_created":

print(f"[spawn] {ev.agent\_name} ({ev.session\_thread\_id})")

case "agent.thread\_message\_sent":

print(f"[delegate -> {ev.to\_agent\_name}] {clip(text\_of(ev.content))}")

case "agent.thread\_message\_received":

print(f"[report <- {ev.from\_agent\_name}] {clip(text\_of(ev.content))}")

case "session.status\_idle":

break

print(f"\n[team finished in {time.monotonic() - t\_start:.0f}s]")

print("=" \* 70)

print(final\_answer)

The shape to notice: every `[delegate ->]` line is a small message, and every `[report <-]` line is a distilled summary. The megabytes of search results and fetched pages that produced those reports never crossed the coordinator's context. That separation is the entire cost story. To price it fairly, the next section runs the realistic alternative, then we meter both.

##  3. Run the control: one frontier agent, same verification standard

What would this cost without the pattern? The realistic alternative is a single frontier agent with the same two web tools. One subtlety makes this comparison fair or worthless: **the solo agent must be held to the same verification standard.** Left to its own judgment, a frontier model is economical — it reads a single source per fact and comes in cheap, but that's a lower-rigor product, not the same work at a different price. So the solo prompt below demands what the team already does: every fact verified from two independent fetches, conflicts re-checked and flagged.

Same question, quiet stream.

solo = client.beta.agents.create(

name="solo-researcher",

model=COORDINATOR\_MODEL,

tools=[

{

"type": "agent\_toolset\_20260401",

"default\_config": {"enabled": False},

"configs": [

{"name": "web\_search", "enabled": True},

{"name": "web\_fetch", "enabled": True},

],

}

],

system=(

"You research hard web questions with audit-grade rigor. Use "

"web\_search and web\_fetch. For EVERY fact you report, verify it "

"from at least two independent fetches (the authoritative page "

"plus one corroborating source), and re-fetch when two sources "

"disagree. Never carry a fact forward on one source or from "

"memory. In your answer, give each fact with both source URLs, "

"and explicitly flag any fact where sources conflicted. Before "

"finishing, audit your own answer: list each claim and check it "

"has two cited sources."

),

betas=BETAS,

)

t\_solo = time.monotonic()

solo\_session = client.beta.sessions.create(agent=solo.id, environment\_id=env.id, betas=BETAS)

client.beta.sessions.events.send(

solo\_session.id,

betas=BETAS,

events=[{"type": "user.message", "content": [{"type": "text", "text": QUESTION}]}],

)

solo\_answer = ""

with client.beta.sessions.events.stream(solo\_session.id, betas=BETAS) as stream:

for ev in stream:

match ev.type:

case "agent.message":

if text := text\_of(ev.content).strip():

solo\_answer = text

case "session.status\_idle":

break

print(f"[solo finished in {time.monotonic() - t\_solo:.0f}s]")

print(clip(solo\_answer, 300))

##  4. Meter and price both runs

Cost attribution is built into the API. Every session thread carries a cumulative `usage`, and both the session and each thread report `usage.list_cost`: the token cost at public list rates, computed server-side. List the threads, take the primary thread (`parent_thread_id is None`) as the coordinator, and the child threads are the workers — the solo session simply has no child threads. The session's own `list_cost` is the total, so there is no rate table to keep in sync for the headline numbers.

(If you ever need per-request detail instead, it's in each thread's own event feed — the session-level feed only carries the primary thread's `span.model_request_end` events.)

One number the API can't hand you is a counterfactual: what this exact team workload would have billed at all-frontier rates. That takes a rate table applied to the token counts, so the code keeps the input and output rates from the [pricing page(opens in new tab)](https://platform.claude.com/docs/en/about-claude/pricing) for that one what-if — 5-minute cache writes bill at 1.25x the input rate, 1-hour writes at 2x, cache reads at 0.1x — and uses `list_cost` for everything real.

# $ / MTok input and output from the pricing page, used only for the

# all-frontier counterfactual below; the real bills come from the API's

# server-side list\_cost. Sonnet 5 shows its introductory rate ($2/$10

# through Aug 31, 2026; standard $3/$15 after — update these then).

PRICES = {

"claude-fable-5": {"input": 10.0, "output": 50.0},

"claude-sonnet-5": {"input": 2.0, "output": 10.0},

}

def total\_input(u):

cache = u.cache\_creation # None on threads with no cache activity

return (

u.input\_tokens

+ u.cache\_read\_input\_tokens

+ (cache.ephemeral\_5m\_input\_tokens if cache else 0)

+ (cache.ephemeral\_1h\_input\_tokens if cache else 0)

)

def counterfactual\_cost(u, model):

"""Re-price a thread's tokens at another model's rates (the what-if)."""

p = PRICES[model]

cache = u.cache\_creation

return (

u.input\_tokens \* p["input"]

+ (cache.ephemeral\_5m\_input\_tokens if cache else 0) \* p["input"] \* 1.25

+ (cache.ephemeral\_1h\_input\_tokens if cache else 0) \* p["input"] \* 2.0

+ u.cache\_read\_input\_tokens \* p["input"] \* 0.1

+ u.output\_tokens \* p["output"]

) / 1e6

def dollars(list\_cost):

return float(list\_cost.amount) / 100 # amount is an integer string in cents

def report(session\_id):

session\_usage = client.beta.sessions.retrieve(session\_id, betas=BETAS).usage

threads = list(client.beta.sessions.threads.list(session\_id, betas=BETAS))

primary = next(t for t in threads if t.parent\_thread\_id is None)

workers = [t for t in threads if t.parent\_thread\_id is not None]

workers\_in = sum(total\_input(t.usage) for t in workers)

print(

f" primary thread ({primary.agent.model.id}): "

f"{total\_input(primary.usage):>9,} in / {primary.usage.output\_tokens:>6,} out"

f" -> ${dollars(primary.usage.list\_cost):.2f}"

)

if workers:

print(

f" {len(workers)} worker(s): {workers\_in:>9,} in / "

f"{sum(t.usage.output\_tokens for t in workers):>6,} out"

f" -> ${sum(dollars(t.usage.list\_cost) for t in workers):.2f}"

)

print(

f" workers' share of input: {workers\_in / (workers\_in + total\_input(primary.usage)):.0%}"

)

total = dollars(session\_usage.list\_cost)

print(f" total cost (session usage.list\_cost): ${total:.2f}")

return total, threads

print("split team (fable coordinator + sonnet workers):")

split\_cost, split\_threads = report(session.id)

print("\nsolo frontier agent:")

solo\_cost, \_ = report(solo\_session.id)

# The counterfactual that isolates the rate split: this run's team

# workload with every token billed at the frontier rate.

frontier\_team\_cost = sum(counterfactual\_cost(t.usage, COORDINATOR\_MODEL) for t in split\_threads)

print(f"\nsolo / split cost ratio on this pair of runs: {solo\_cost / split\_cost:.1f}x")

print(f"the split team's workload at all-frontier rates: ${frontier\_team\_cost:.2f}")

The two runs did nearly the same reading — that's the point of matching the verification standard. What differs is the rate the reading billed at and the shape of the work: the team's twenty lookups ran as parallel worker threads at the cheap rate, while the solo agent ground through them serially in one frontier-priced context. On the authors' runs that came out to the team being roughly 2.5x cheaper and 3x faster, with 84-98% of the team's input tokens billed at the worker rate. Token volumes vary run to run, so treat any single printed ratio as one sample; the structure is the stable part.

Four honest caveats, all observed while building this notebook:

* **Hold the comparison to matched rigor.** A solo frontier agent left to its own judgment reads far less (one source per fact) and comes in cheaper than the team — but that's a different, lower-rigor product. The split's cost win is real when the verification standard is fixed.
* **Delegation has a floor cost.** Each worker thread pays a fixed setup overhead. Splitting the same work into more, narrower briefs raised our bill instead of lowering it — brief granularity has an optimum.
* **The verification standard only covers what you put in it.** Both arms in the committed run verified all twenty facts against nps.gov — and both built their list of parks from model memory, which put Kings Canyon in the #10 slot that actually belongs to Great Smoky Mountains (Kings Canyon is #12 by area). The facts were audited; the question decomposition wasn't. If the premise matters, spend one more delegation making a worker verify it.
* **The coordinator only knows what you tell it.** Nothing on the server shows it the workers' prompts (see section 1), so the economics also depend on you describing the workers' behavior accurately in the coordinator's prompt.

When does the split *not* pay? On narrow questions there's too little reading to arbitrage. If the coordinator answers from its own knowledge (no delegation), you paid a frontier round-trip for nothing — watch for runs with no `[spawn]` lines. And if the task needs frontier judgment on the raw material itself (subtle document analysis rather than fact-finding), a cheap reader may summarize away exactly what mattered.

##  Recap

In this guide you built the cheapest useful shape of a multi-agent team and measured what it buys:

* **Configured a two-model team** — a frontier coordinator whose only capability is its `multiagent` roster, and a cheap worker scoped to the web tools
* **Followed the delegation live** through `thread_created` / `thread_message_sent` / `thread_message_received` on the session stream
* **Ran a rigor-matched solo-frontier control** and compared real bills and real wall-clock, not estimates
* **Metered each thread** with the typed cumulative `usage` every session thread carries (`session.usage` is the whole-team total)

To take this further:

1. Add specialist worker types with scoped toolsets — [`CMA_coordinate_specialist_team.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb) shows a three-role team and why per-role scoping matters
2. Put the per-thread metering into your production telemetry: the thread-level usage is how you attribute spend per delegation, not just per session
3. Try the same split on your own token-heavy workload — document review and log triage have the same read-heavy, coverage-shaped profile as web research

Reference: [multi-agent sessions documentation(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/multi-agent).
