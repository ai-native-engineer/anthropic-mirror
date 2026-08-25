<!-- source: https://platform.claude.com/cookbook/fable-5-fallback-billing-guide -->

#  Classifier Fallback & Billing

Claude Fable 5's advanced capabilities in areas like cybersecurity, biology, and chemistry create real risk of misuse: the same skills that make it useful could help bad actors build cyberattacks or dangerous weapons. For that reason, Claude Fable 5 ships with safeguards that limit its performance in these specific areas, and automated safety checks run on every request. These checks block requests in three areas:

* **Offensive cybersecurity techniques** — building exploits, malware, or attack tooling
* **Biology and life sciences** — lab methods or molecular mechanisms
* **Extraction of the model's [summarized thinking(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking)**

These safeguards are deliberately conservative. They are tuned first for robustness, which means benign technical work sometimes triggers them. We are releasing Fable 5 with fallback to Opus 4.8 on every topic related to biology and cybersecurity, as a way of bringing you Fable's Mythos-level capability faster in all other areas. We will continue to reduce false-positive rates for Fable 5 after launch.

**API customers should configure fallback from Claude Fable 5 to Opus 4.8** — either with the [built-in server-side fallback(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#server-side-fallback) feature (available on the native Claude API and Claude Platform on AWS) or with [client-side fallback(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#client-side-fallback) logic built on the Anthropic SDK helpers.

We've also made billing changes so that customers don't incur token costs in most cases of Fable 5 fallback. Action is needed to adopt these changes **when you are not using the server-side fallback feature** — see [below](#4-billing-changes).

##  What this guide covers

1. [What a classifier block looks like](#1-what-a-classifier-block-looks-like)
2. [Server-side fallback (recommended)](#2-server-side-fallback-recommended)
3. [Streaming](#3-streaming)
4. [Billing changes](#4-billing-changes)
5. [Client-side fallback with the SDK](#5-client-side-fallback-with-the-sdk)
6. [Common anti-patterns](#6-common-anti-patterns)

%%capture

%pip install -U "anthropic>=0.108.0"

import os

from dotenv import load\_dotenv

load\_dotenv()

PRIMARY\_MODEL = "claude-fable-5"

FALLBACK\_MODEL = "claude-opus-4-8"

SERVER\_SIDE\_FALLBACK\_BETA = "server-side-fallback-2026-06-01"

FALLBACK\_CREDIT\_BETA = "fallback-credit-2026-06-01"

# Anthropic() reads ANTHROPIC\_API\_KEY from the environment. Add it to a .env

# file (loaded above) or export it in your shell before running the live examples.

if not os.environ.get("ANTHROPIC\_API\_KEY"):

print(

"ANTHROPIC\_API\_KEY is not set - add it to .env or export it."

)

##  1. What a classifier block looks like

A *classifier block* is what the API returns when a request appears to violate our safeguards. The API returns `200` with `stop_reason: "refusal"` and a `stop_details` object describing the category:

{

"stop\_reason": "refusal",

"stop\_details": {

"type": "refusal",

"category": "cyber",

"explanation": "This request triggered restrictions on violative cyber content and was blocked under Anthropic's Usage Policy..."

},

"content": [...]

}

Branch your logic on **`stop_reason`, not on `content` or `stop_details`**. `stop_details` is informational and can be `null`, which you should treat as a generic refusal (unspecific to the categories below).

When present, `category` is one of `"cyber"`, `"bio"`, or `"reasoning_extraction"`. This can help you refine your fallback choice:

| category | fires on |
| --- | --- |
| `cyber` | offensive cybersecurity content (exploits, malware, attack tooling) |
| `bio` | biology / life-sciences content (lab methods, molecular mechanisms) |
| `reasoning_extraction` | requests that attempt to extract the model's [summarized thinking(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking) |

Classifier blocks are distinct from **model refusals** (the model itself declining for other policy reasons). Both surface as `stop_reason: "refusal"`, but `stop_details.category` tells you which classifier blocked you.

> **Note:** When you are **not** using the server-side fallback feature, `stop_details` also includes a `fallback_credit_token`, which you use to bill your fallback model request as a cache read — see [Billing changes](#4-billing-changes).

##  2. Server-side fallback (recommended)

The Messages API can run the fallback for you. Pass `fallbacks` with `[{"model": "claude-opus-4-8"}]` and the `server-side-fallback-2026-06-01` beta header. If Fable's classifiers block the turn, the API automatically retries it with Opus 4.8 — annotated so you can tell what happened.

The automatic fallback feature is currently supported on the **Claude API** and **Claude Platform on AWS**. Today it only supports falling back from Fable 5 to Opus 4.8; we expect to expand this.

curl https://api.anthropic.com/v1/messages \

-H "x-api-key: $ANTHROPIC\_API\_KEY" \

-H "anthropic-version: 2023-06-01" \

-H "anthropic-beta: server-side-fallback-2026-06-01" \

-H "content-type: application/json" \

-d '{

"model": "claude-fable-5",

"max\_tokens": 1024,

"fallbacks": [

{ "model": "claude-opus-4-8" }

],

"messages": [

{ "role": "user", "content": "Hello, world" }

]

}'

###  When the fallback can't run

When you've configured `fallbacks` but the API can't reach the fallback model — its rate limit is exhausted or it's overloaded — the turn still comes back as a refusal, and `stop_details.recommended_model` names the canonical model id to retry directly:

{

"stop\_reason": "refusal",

"stop\_details": {

"type": "refusal",

"category": "cyber",

"recommended\_model": "claude-opus-4-8"

}

}

`recommended_model` is populated **only** in this case (fallbacks configured *and* the fallback couldn't execute). On a plain block with no fallbacks configured, it isn't present — which is why it's absent from the basic example in [section 1](#1-what-a-classifier-block-looks-like).

# Fable applies extra safety filters. With a fallback chain configured, the API

# retries blocked turns on the next model server-side. A stop\_reason of "refusal"

# means the whole chain refused.

from anthropic import Anthropic

client = Anthropic()

def chat\_turn(messages, max\_tokens=1024):

"""One API call; the server handles the fallback."""

return client.beta.messages.create(

model=PRIMARY\_MODEL,

max\_tokens=max\_tokens,

messages=messages,

betas=[SERVER\_SIDE\_FALLBACK\_BETA],

fallbacks=[{"model": FALLBACK\_MODEL}],

)

###  Detecting fallback (non-streaming)

A fallback response carries a `{"type": "fallback"}` content block at each switch point, and `usage.iterations` records per-model usage. Note that a **sticky-served** turn — one routed directly to the fallback model because an earlier turn in the conversation fell back — carries *no* fallback block, because the request was routed directly and there is no boundary in `content` to mark. `usage.iterations` is the reliable way to tell whether a fallback model served the turn.

def fallback\_hops(response):

"""(from\_model, to\_model) for each hop that ran and blocked this turn."""

hops = []

for b in response.content:

if getattr(b, "type", None) == "fallback":

d = b.model\_dump() if hasattr(b, "model\_dump") else dict(b)

hops.append((d["from"]["model"], d["to"]["model"]))

return hops

def served\_by\_fallback(response):

"""True whenever a fallback model served the response, INCLUDING a

sticky-served turn (which carries no fallback block). usage.iterations is

the best way to check whether a turn was served by a fallback model."""

iters = getattr(response.usage, "iterations", None) or []

return any(

(i.get("type") if isinstance(i, dict) else getattr(i, "type", None))

== "fallback\_message"

for i in iters

)

response = chat\_turn([{"role": "user", "content": "Hello, world"}])

hops = fallback\_hops(response)

for from\_model, to\_model in hops:

print(f"[{from\_model} blocked \u2014 continued on {to\_model}]")

if not hops and served\_by\_fallback(response):

print(f"[sticky: served directly by {response.model}]")

###  Detecting fallback while streaming

Watch for a `content_block_start` event whose block is `{"type": "fallback"}` — that marks an in-stream switch point. But for the definitive per-turn answer, check `usage.iterations` on the **final** message, exactly as you would for a non-streaming response. That check is reliable in every case, including a stream that was served directly by the fallback model, so use it as your source of truth rather than depending on the in-stream events alone.

with client.beta.messages.stream(

model=PRIMARY\_MODEL,

max\_tokens=1024,

messages=[{"role": "user", "content": "Hello, world"}],

betas=[SERVER\_SIDE\_FALLBACK\_BETA],

fallbacks=[{"model": FALLBACK\_MODEL}],

) as stream:

for event in stream:

if (

getattr(event, "type", None) == "content\_block\_start"

and getattr(event.content\_block, "type", None) == "fallback"

):

fb = event.content\_block

fb = fb.model\_dump() if hasattr(fb, "model\_dump") else dict(fb)

print(f"[switching: {fb['from']['model']} -> {fb['to']['model']}]")

final = stream.get\_final\_message()

# Definitive per-turn check, same as non-streaming: usage.iterations also

# catches a stream served directly by the fallback model (no in-stream event).

if served\_by\_fallback(final):

print(f"[fallback model served this stream: {final.model}]")

###  The fallback response shape

A fallback response contains `message.model` (the model that eventually answered), a `{"type": "fallback"}` content block marking each switch point, and per-attempt usage in `usage.iterations`:

{

"id": "msg\_01Ab...",

"type": "message",

"role": "assistant",

"model": "claude-opus-4-8",

"content": [

{ "type": "fallback", "from": { "model": "claude-fable-5" }, "to": { "model": "claude-opus-4-8" } },

{ "type": "text", "text": "..." }

],

"stop\_reason": "end\_turn",

"stop\_details": null,

"usage": {

"input\_tokens": 412, "output\_tokens": 264,

"cache\_read\_input\_tokens": 0, "cache\_creation\_input\_tokens": 0,

"iterations": [

{ "type": "message", "model": "claude-fable-5", "input\_tokens": 408, "output\_tokens": 0,

"cache\_read\_input\_tokens": 0, "cache\_creation\_input\_tokens": 0 },

{ "type": "fallback\_message", "model": "claude-opus-4-8", "input\_tokens": 412, "output\_tokens": 264,

"cache\_read\_input\_tokens": 0, "cache\_creation\_input\_tokens": 0 }

]

}

}

**Per-attempt overrides.** Each fallback entry may override `max_tokens`, `thinking`, `output_config`, and `speed` for that attempt only (`output_config` and `speed` additionally require the same beta headers as the corresponding top-level fields). The request with an entry's overrides merged in must be a correctly formatted direct request to that entry's model.

{

"model": "claude-fable-5",

"max\_tokens": 1024,

"fallbacks": [

{ "model": "claude-opus-4-8", "max\_tokens": 8192, "thinking": {"type": "disabled"}, "speed": "fast" }

],

"messages": [

{ "role": "user", "content": "Hello, world" }

]

}

**Billing.** `usage.input_tokens` is counted once for the turn. `usage.output_tokens` reflects the answer. Use `usage.iterations` if you need exact per-model attribution.

##  3. Streaming

In streaming, fallback is designed to work automatically. If the classifier blocks **before any output reaches you**, the stream starts with the fallback model's response. This retry is invisible and no fallback SSE event is emitted.

If the classifier blocks **mid-stream**, the retry happens on the same stream too: the partial output is kept, a `{"type": "fallback"}` content block marks the boundary, and the fallback model continues from the partial. Nothing streamed is ever discarded.

def stream\_turn(messages, max\_tokens=1024):

with client.beta.messages.stream(

model=PRIMARY\_MODEL,

max\_tokens=max\_tokens,

messages=messages,

betas=[SERVER\_SIDE\_FALLBACK\_BETA],

fallbacks=[{"model": FALLBACK\_MODEL}],

) as stream:

# Nothing streamed is ever discarded: after a mid-stream block, the

# final message is partial + fallback block + continuation.

final = stream.get\_final\_message()

if final.stop\_reason == "refusal":

return final # the whole chain refused

text = "".join(b.text for b in final.content if b.type == "text")

print(f"{final.model}: {text}")

return final

##  4. Billing changes

We've made billing changes to minimize the cost impact of fallback. These apply automatically when you use fallback and the Anthropic SDK helpers. **Action is only needed to adopt the cache-miss billing change, and only when you are not using server-side fallback.**

**1. Input tokens are not billed on a direct classifier block** (i.e. when a request is blocked before any output tokens were returned). No action needed — this is already applied automatically to all production models, including Fable 5.

**2. Fable 5 → Opus 4.8 fallback input tokens are billed as a cache hit.** Normally, switching to another model is billed as a [cache *write*(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#how-prompt-caching-works), which is 1.25× (5-min TTL) or 2× (60-min TTL) higher than the base input-token cost. Instead, we bill these Opus tokens as if they had already been cached — i.e. as a cache *read*, which is 10% of the base input-token price.

* **Using the server-side fallback feature:** this billing change is applied automatically.
* **Not using the server-side fallback feature:** see the credit-token flow below.

###  Redeeming the fallback credit token (client-side fallback only)

Fable requests blocked by safety classifiers include a `fallback_credit_token` in `stop_details`. The token is present **only** when the blocked request had a billable cached prefix, and is `null` otherwise.

To redeem it:

1. Send your subsequent Opus 4.8 request with the `anthropic-beta: fallback-credit-2026-06-01` header.
2. Pass the token as a top-level `fallback_credit_token` parameter.
3. Keep the prompt-shaping fields **identical** to the blocked request — the exact same `system`, `messages`, and `tools`.

The prefix that was cached on the Fable request is then billed at the cache-read rate instead of cache-write. The switching cost is refunded, so the retry costs what it would have if the conversation had been on Opus all along.

**Validity:** the token is valid only on Opus 4.8 requests that occur **within 5 minutes** of the blocked Fable 5 request and originate from the **same org and workspace**.

**Mid-stream blocks.** If the Fable 5 request is blocked in the middle of streaming output tokens, `stop_details` also includes `fallback_has_prefill_claim: true` alongside the credit token. This means that in your subsequent Opus 4.8 request you can append that partial output as an assistant prefill and continue from where Fable stopped — something [normally not allowed(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency#prefill-claudes-response) in Opus 4.8 requests.

def redeem\_credit\_after\_block(blocked\_response, messages, max\_tokens=1024):

"""Retry a classifier-blocked Fable turn on Opus 4.8, redeeming the

fallback credit token so the cached prefix is billed at the cache-read

rate. Use this only when you are NOT using server-side fallback."""

details = blocked\_response.stop\_details

credit = getattr(details, "fallback\_credit\_token", None) if details else None

extra = {}

betas = []

if credit is not None: # present only when the blocked request had a cached prefix

betas.append(FALLBACK\_CREDIT\_BETA)

extra["fallback\_credit\_token"] = credit

# The system, messages, and tools must be IDENTICAL to the blocked request.

return client.beta.messages.create(

model=FALLBACK\_MODEL,

max\_tokens=max\_tokens,

messages=messages,

betas=betas or None,

extra\_body=extra or None,

)

##  5. Client-side fallback with the SDK

Server-side fallback is available on the native Claude API and Claude Platform on AWS, but not currently on Amazon Bedrock, Vertex AI, Microsoft Foundry, or the Message Batches API. For those, or any time you want the fallback logic in your client, the Anthropic SDKs (Python, TypeScript, Go, Java, C#) ship a **refusal-fallback middleware**.

Configure it once on a client with your fallback model list and a `BetaFallbackState`, then call `client.beta.messages` as usual. The middleware:

* retries a `stop_reason: "refusal"` turn on the next model in the list (continuing down the chain if a fallback also refuses; if every entry refuses it surfaces the original refusal rather than raising);
* **sends the `fallback-credit-2026-06-01` beta header automatically on every request**, so you get the cache-read billing change from [section 4](#4-billing-changes) without managing tokens yourself;
* manages the `fallback` content blocks in conversation history for you;
* records the accepting model in `BetaFallbackState` so follow-up turns stay pinned to it.

It is **mutually exclusive** with the server-side `fallbacks` parameter; use one or the other. (To send a server-side `fallbacks` request from an app that installs the middleware, use a separate client instance without it.)

from anthropic import Anthropic, BetaFallbackState, BetaRefusalFallbackMiddleware

# Install the middleware once, with your fallback chain. No per-request betas needed.

client = Anthropic(

middleware=[BetaRefusalFallbackMiddleware([{"model": FALLBACK\_MODEL}])],

)

state = BetaFallbackState() # reuse across turns to pin follow-ups to the accepting model

# Non-streaming: a refused Fable turn is retried on Opus 4.8 transparently.

with state:

message = client.beta.messages.create(

model=PRIMARY\_MODEL,

max\_tokens=1024,

messages=[{"role": "user", "content": "Hello, Claude"}],

)

print(f"served by: {message.model}")

# Streaming: on a refusal the middleware splices the fallback model's events

# onto the same open stream.

with (

state,

client.beta.messages.stream(

model=PRIMARY\_MODEL,

max\_tokens=1024,

messages=[{"role": "user", "content": "Hello, Claude"}],

) as stream,

):

for event in stream:

if event.type == "text":

print(event.text, end="", flush=True)

final = stream.get\_final\_message()

print(f"\nserved by: {final.model}")

##  6. Common anti-patterns

**Set the fallback on every request, not once per account.** There is no account-level or session-level switch that enables the Opus 4.8 fallback. Each API call must include the fallback configuration. A call that doesn't turn on fallbacks returns a refusal instead of silently retrying on the fallback model.

**Audit every code path that builds a request.** Features such as retry buttons, message regeneration, and tool-use continuations often construct their own requests, and each one can silently omit the fallback configuration. Set the fallback explicitly at every entry point. (See the [migration guide(opens in new tab)](https://platform.claude.com/docs/en/about-claude/models/migration-guide) and the [claude-api skill(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) to add fallbacks across a codebase quickly.)

**Include the fallback on subagent calls, and expect per-agent behavior.** If your application runs multiple agents in one session, every agent's calls need the fallback configuration. When a refusal occurs, only the agent that received it moves to the fallback model — the other agents stay on Fable. Do not assume one agent's fallback applies to the whole session. (The same is true of sub-agents in Claude Code: only the sub-agent that hits a refusal falls back to Opus; the rest of the session continues on Fable 5.)

**Resubmitting the same request after a refusal just re-refuses.** The refused content is still in the conversation history, so resubmitting to the same model re-triggers the block. On `stop_reason: "refusal"`, retry on the fallback model and set a separate indicator so your router knows to stay on the fallback model for the rest of the conversation.

**Build serving-model analytics from `usage.iterations`, not from the model you requested.** The response's `model` field is the model that actually answered, so a fallback-served turn reports Opus 4.8. Analytics recorded against the *requested* model will be wrong whenever a fallback is used. The reliable per-turn check is `usage.iterations` in the final usage record.

**Handle streaming truncation carefully.** When you hit a classifier block mid-stream, omit any `thinking`, `tool_use`, or other blocks that appear before the fallback. A truncated `tool_use` block is unparseable JSON, and another model's `thinking` blocks will break the next call. If you continue without server-side fallback, use the `fallback_has_prefill_claim` grant from `stop_details` rather than pasting the partial response into a completed assistant turn.
