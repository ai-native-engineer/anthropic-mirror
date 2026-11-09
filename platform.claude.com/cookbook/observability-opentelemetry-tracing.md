<!-- source: https://platform.claude.com/cookbook/observability-opentelemetry-tracing -->

#  Trace Claude API requests and Managed Agents sessions with OpenTelemetry

A slow or expensive Claude request doesn't tell you where the time and tokens went. OpenTelemetry (OTel) spans do, and they come from two places. The Claude SDK emits spans inside your process, one per request it sends. The Claude API emits spans on Anthropic's side for the work inside each request, and delivers them straight to your observability backend. The SDK tags every request with a `traceparent` header and the API attaches its spans under it, so both land in one trace next to your own handler and database spans.

This notebook prints the SDK spans live. The API's spans never pass through your process, so they appear here as reference trees. Both halves are in beta: span names and attributes can change between versions.

A *span* is one timed step with a name, a kind, a status, and key-value attributes. A *trace* is the tree of spans that share a trace ID.

|  | SDK spans | API spans |
| --- | --- | --- |
| Emitted by | The `anthropic` package, inside your process | The Claude API, inside Anthropic |
| Covers | Each request the SDK sends, and each tool its tool-runner helper executes (section 5) | What the API does inside a request: each model run, each server-side tool such as `web_search`, each context compaction, and each Managed Agents turn (section 6) |
| Span kind | `CLIENT` for requests, `INTERNAL` for tools | `SERVER` for requests, `INTERNAL` for the steps inside |
| How you receive them | Your own OTel exporter (section 7) | A *destination*: your backend's OTLP (OpenTelemetry Protocol) HTTPS endpoint and auth header, registered once in the Console (section 8) |
| Joined by | The `traceparent` header on each request | The API reads that header and parents its span under the SDK's |
| Available on | Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry | Claude API only |

Both halves use the [OpenTelemetry GenAI semantic conventions(opens in new tab)](https://github.com/open-telemetry/semantic-conventions-genai), so a backend that understands `gen_ai.*` attributes renders models, token counts, and messages without custom mapping. The span names and attributes are the same across the official SDKs.

By the end you'll be able to:

* read an SDK span attribute by attribute and know which attributes to alert on, group by, and sum
* nest SDK spans under your own for a request, a stream, a tool loop, and a Managed Agents session
* export to an OTLP backend and add the Console destination that puts the API's spans in the same trace

**Documentation**

* [OpenTelemetry for the Claude API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry): overview, content modes, example traces, token counting
* [Use OpenTelemetry with the Claude SDK(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk): setup for every language, every client option and environment variable
* [Use OpenTelemetry with the Claude API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api): destinations, delivery, sampling whole conversations
* [OpenTelemetry span reference(opens in new tab)](https://platform.claude.com/docs/en/api/opentelemetry/spans): every span, attribute, and parent relationship

##  1. Set up

**Prerequisites**

* Claude API credentials: either `ANTHROPIC_API_KEY` (in the environment or a `.env` file next to this notebook) or a profile from `ant auth login`. `anthropic.Anthropic()` finds both on its own
* Python 3.11+
* Familiarity with the [Messages API(opens in new tab)](https://platform.claude.com/docs/en/api/messages). Section 6 assumes [Managed Agents(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/overview) basics, needs Managed Agents beta access, and creates a cloud environment and one short session
* Optional, for section 7: an OTLP endpoint and its auth header
* Optional, for section 8: the admin role in your Anthropic organization

The `anthropic` package depends only on `opentelemetry-api`, the interface package, which records nothing by itself. Install `opentelemetry-sdk` and an exporter alongside it:

%%capture

%pip install -qU "anthropic>=1.14.0" opentelemetry-sdk opentelemetry-exporter-otlp-proto-http python-dotenv

A *tracer provider* creates spans and hands them to *span processors*, which pass them to *exporters*. This notebook registers two processors on one provider:

* an in-memory exporter, so each section can print the spans it produced
* an OTLP exporter, added only when `OTEL_EXPORTER_OTLP_ENDPOINT` is set, so the same spans also reach your backend (section 7)

`trace.set_tracer_provider()` makes the provider global. The SDK emits into the global provider, so `anthropic.Anthropic()` needs no tracing arguments. Register the provider before the first call you want traced.

import json

import os

from collections import defaultdict

import anthropic

from dotenv import load\_dotenv

from opentelemetry import trace

from opentelemetry.exporter.otlp.proto.http.trace\_exporter import OTLPSpanExporter

from opentelemetry.sdk.resources import Resource

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor

from opentelemetry.sdk.trace.export.in\_memory\_span\_exporter import InMemorySpanExporter

load\_dotenv()

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5-5")

BETAS = ["managed-agents-2026-04-01"] # beta header for the Managed Agents calls in section 6

# service.name is how your backend labels these spans. The API's spans arrive as "claude-platform".

provider = TracerProvider(resource=Resource.create({"service.name": "otel-cookbook"}))

memory\_exporter = InMemorySpanExporter()

provider.add\_span\_processor(SimpleSpanProcessor(memory\_exporter))

if os.environ.get("OTEL\_EXPORTER\_OTLP\_ENDPOINT"):

# Reads OTEL\_EXPORTER\_OTLP\_ENDPOINT and OTEL\_EXPORTER\_OTLP\_HEADERS from the environment.

provider.add\_span\_processor(BatchSpanProcessor(OTLPSpanExporter()))

trace.set\_tracer\_provider(provider)

tracer = trace.get\_tracer("otel-cookbook")

client = anthropic.Anthropic()

print("anthropic", anthropic.\_\_version\_\_)

client.open\_telemetry

```
anthropic 1.13.0

{'propagation': True,
 'traces': {'enabled': True,
  'content_mode': 'metadata_only',
  'max_content_bytes': 750000}}
```

`client.open_telemetry` shows the tracing settings after constructor arguments and the `ANTHROPIC_OPEN_TELEMETRY*` environment variables merge. The [SDK guide(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk) lists every option, including `open_telemetry=False` to turn spans off for one client. Tracing and `traceparent` propagation are on, and `content_mode` is `metadata_only`: spans carry identifiers, timing, token counts, and the names and descriptions of your tools and agents, but not prompts or responses.

The next cell defines `print_traces()`, which prints the collected spans as a tree with the attributes listed in `KEY_ATTRIBUTES`, then clears the buffer. Pass `show="all"` to print every attribute.

KEY\_ATTRIBUTES = [

"gen\_ai.operation.name",

"gen\_ai.request.model",

"gen\_ai.request.stream",

"gen\_ai.response.model",

"gen\_ai.conversation.id",

"gen\_ai.agent.id",

"gen\_ai.agent.name",

"anthropic.session.id",

"anthropic.session.environment.id",

"anthropic.environment.id",

"gen\_ai.tool.name",

"gen\_ai.tool.call.id",

"anthropic.message.stop\_reason",

"gen\_ai.usage.input\_tokens",

"gen\_ai.usage.cache\_read.input\_tokens",

"gen\_ai.usage.output\_tokens",

"gen\_ai.response.time\_to\_first\_chunk",

"anthropic.request.id",

"http.response.status\_code",

"error.type",

"gen\_ai.system\_instructions",

"gen\_ai.input.messages",

"gen\_ai.output.messages",

"gen\_ai.tool.call.arguments",

"anthropic.tool\_result.content",

"anthropic.content.truncated",

]

def print\_traces(show: str = "key") -> None:

spans = sorted(memory\_exporter.get\_finished\_spans(), key=lambda s: s.start\_time or 0)

memory\_exporter.clear()

span\_ids = {s.context.span\_id for s in spans}

children = defaultdict(list)

roots = []

for s in spans:

parent\_id = s.parent.span\_id if s.parent else None

(children[parent\_id] if parent\_id in span\_ids else roots).append(s)

def walk(span, depth):

pad = " " \* depth

seconds = (span.end\_time - span.start\_time) / 1e9

kind, status = span.kind.name, span.status.status\_code.name

print(f"{pad}{span.name} [{kind} {status} {seconds:.2f}s]")

if show == "all":

keys = list(span.attributes)

else:

keys = [k for k in KEY\_ATTRIBUTES if k in span.attributes]

for k in keys:

print(f"{pad} │ {k} = {span.attributes[k]}")

for child in children[span.context.span\_id]:

walk(child, depth + 1)

for root in roots:

print(f"── trace {root.context.trace\_id:032x}")

walk(root, 0)

print()

##  2. Trace a Messages API request

Send one request and print every attribute on its span. `with_raw_response` is here only to show the `traceparent` header the SDK attached. A plain `client.messages.create()` produces the same span.

raw = client.messages.with\_raw\_response.create(

model=MODEL,

max\_tokens=100,

messages=[{"role": "user", "content": "In one word, what is the capital of France?"}],

)

message = raw.parse()

print("Claude:", message.content[0].text)

print("traceparent sent:", raw.http\_response.request.headers["traceparent"])

print()

print\_traces(show="all")

```
Claude: Paris
traceparent sent: 00-1d5dcf464f37ba0cf3357bef68d5319e-a33e2f3d458804bc-03

── trace 1d5dcf464f37ba0cf3357bef68d5319e
anthropic.messages.create  [CLIENT  OK  0.69s]
  │ server.address = api.anthropic.com
  │ server.port = 443
  │ http.request.method = POST
  │ http.route = /v1/messages
  │ gen_ai.provider.name = anthropic
  │ gen_ai.operation.name = chat
  │ gen_ai.request.model = claude-sonnet-5-5
  │ gen_ai.request.max_tokens = 100
  │ url.scheme = https
  │ url.path = /v1/messages
  │ url.full = https://api.anthropic.com/v1/messages
  │ anthropic.request.id = req_011Cg1MqD5J9qv8hW8Nr9hJ6
  │ anthropic.organization.id = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  │ anthropic.workspace.id = wrkspc_xxxxxxxxxxxxxxxxxxxxxxxx
  │ gen_ai.response.id = msg_011Cg1MqDLRghkLPbApauf2r
  │ gen_ai.response.model = claude-sonnet-5-5
  │ anthropic.message.stop_reason = end_turn
  │ gen_ai.usage.input_tokens = 20
  │ gen_ai.usage.cache_write.input_tokens = 0
  │ gen_ai.usage.cache_read.input_tokens = 0
  │ anthropic.usage.cache_creation.ephemeral_5m_input_tokens = 0
  │ anthropic.usage.cache_creation.ephemeral_1h_input_tokens = 0
  │ anthropic.response.service_tier = standard
  │ gen_ai.usage.output_tokens = 5
  │ gen_ai.usage.reasoning.output_tokens = 0
  │ http.response.status_code = 200
```

###  How to read this span

**Name and kind.** The name is `anthropic.` plus the API method with dots, minus `beta`: `client.messages.create()` becomes `anthropic.messages.create`, and `client.beta.sessions.events.send()` becomes `anthropic.sessions.events.send`. The kind is `CLIENT` because this is the SDK's view of an outbound request. The API's span for the same request has the same name with kind `SERVER` and sits directly under this one once it reaches your backend (section 8).

**Status.** `OK` means the call returned. `ERROR` means it raised, and `error.type` says why: an API error type such as `rate_limit_error` or `overloaded_error`, an HTTP status such as `502`, or `connection_error` / `client_timeout_error` for transport failures. One span covers the whole call including retries, and `http.request.resend_count` appears when the SDK retried.

**The `traceparent` header** is how the API finds this span. Its format is `00-<trace id>-<span id>-<flags>`. The trace ID matches the one printed under it and the span ID is this span's, so the API parents its `SERVER` span here. In `flags`, bit 0 is the sampled flag and bit 1 marks the trace ID as random, so `03` means both. The SDK writes the header through your application's global *propagator* (the OTel component that serializes trace context into headers), so if the rest of your system is configured for a different format such as B3, add the W3C trace-context propagator as well or the API can't read it.

**Attributes, by group:**

| Group | Attributes | What they tell you |
| --- | --- | --- |
| Operation | `gen_ai.operation.name=chat`, `gen_ai.provider.name=anthropic` | GenAI-convention markers that backends use to recognize an LLM call |
| Request | `gen_ai.request.model`, `gen_ai.request.max_tokens`, and when you set them `gen_ai.request.temperature`, `gen_ai.request.top_p`, `gen_ai.request.top_k`, `gen_ai.request.stream`, `gen_ai.request.reasoning.level` (the `effort` setting), `anthropic.thinking.type`, `anthropic.beta` | What you asked for |
| Response | `gen_ai.response.id` (the `msg_` ID), `gen_ai.response.model`, `anthropic.message.stop_reason`, `anthropic.response.service_tier` | What came back. `response.model` differs from `request.model` when you passed an alias or a fallback model served the request. Alert on `stop_reason=max_tokens` to catch truncated answers |
| Usage | `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.usage.cache_read.input_tokens`, `gen_ai.usage.cache_write.input_tokens`, `anthropic.usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`, `gen_ai.usage.reasoning.output_tokens` | Token counts. `gen_ai.usage.input_tokens` is `usage.input_tokens + cache_read_input_tokens + cache_creation_input_tokens` from the `Message` object, so it already includes the cache attributes and you must not add them again. Reasoning (thinking) tokens are part of `output_tokens` |
| Correlation | `anthropic.request.id`, `anthropic.organization.id`, `anthropic.workspace.id` | `anthropic.request.id` is the `request-id` response header: quote it to support, and join on it to pair this span with the API's `SERVER` span. The organization and workspace IDs let you split traffic per workspace in a shared backend |
| HTTP | `http.request.method`, `http.route`, `http.response.status_code`, `url.full`, and the other `url.*` and `server.*` client attributes | Standard HTTP client semantics, so generic HTTP dashboards work too |

##  3. Nest SDK spans under your own, and record content

Compared with section 2:

1. The call runs inside `tracer.start_as_current_span("answer_question")`, so the SDK span becomes its child. In production the outer span is your request handler or background job.
2. A second client sets `traces.content_mode` to `content`. Its spans add `gen_ai.system_instructions`, `gen_ai.input.messages`, and `gen_ai.output.messages`. The environment variable `ANTHROPIC_OPEN_TELEMETRY_TRACES_CONTENT_MODE=content` does the same for every client.
3. `with_options()` tags the call with a `conversation_id`, which lands in `gen_ai.conversation.id`. Give every request in a multi-turn conversation the same ID so your backend can group them. The ID is exported even in `metadata_only` mode, so don't put user data in it. `with_options()` replaces the whole `open_telemetry` option rather than merging, so spread the client's current value into the new one, as the cell does with `content_client.open_telemetry`.

content\_client = anthropic.Anthropic(open\_telemetry={"traces": {"content\_mode": "content"}})

conversation = content\_client.with\_options(

open\_telemetry={\*\*content\_client.open\_telemetry, "conversation\_id": "conv\_sky\_0001"}

)

with tracer.start\_as\_current\_span("answer\_question"):

reply = conversation.messages.create(

model=MODEL,

max\_tokens=200,

system="Answer in one short sentence.",

messages=[{"role": "user", "content": "Why is the sky blue?"}],

)

print("Claude:", reply.content[0].text)

print()

print\_traces()

```
Claude: The sky looks blue because air molecules scatter short-wavelength blue light from the sun much more strongly than longer-wavelength red light, sending blue light to our eyes from every direction.

── trace 52022f8b623ba8736bbe49dd41134822
answer_question  [INTERNAL  UNSET  0.93s]
    anthropic.messages.create  [CLIENT  OK  0.93s]
      │ gen_ai.operation.name = chat
      │ gen_ai.request.model = claude-sonnet-5-5
      │ gen_ai.response.model = claude-sonnet-5-5
      │ gen_ai.conversation.id = conv_sky_0001
      │ anthropic.message.stop_reason = end_turn
      │ gen_ai.usage.input_tokens = 28
      │ gen_ai.usage.cache_read.input_tokens = 0
      │ gen_ai.usage.output_tokens = 61
      │ anthropic.request.id = req_011Cg1MqGVBR9wQkir7ZK9Qf
      │ http.response.status_code = 200
      │ gen_ai.system_instructions = [{"type":"text","content":"Answer in one short sentence."}]
      │ gen_ai.input.messages = [{"role":"user","parts":[{"type":"text","content":"Why is the sky blue?"}]}]
      │ gen_ai.output.messages = [{"role":"assistant","parts":[{"type":"text","content":"The sky looks blue because air molecules scatter short-wavelength blue light from the sun much more strongly than longer-wavelength red light, sending blue light to our eyes from every direction."}]}]
```

Your `answer_question` span has status `UNSET` because your code didn't set one. Backends treat `UNSET` as success, so that's harmless.

The three content attributes are JSON strings in the GenAI conventions' message format, not the Messages API format. Each message is `{"role", "parts": [...]}` and each part has a `type`:

| Messages API block | Part in the span |
| --- | --- |
| `text` | `{"type": "text", "content": "..."}` |
| `thinking` | `{"type": "reasoning", "content": "..."}` (the block's `signature` field is dropped) |
| `tool_use`, `server_tool_use`, `mcp_tool_use` | `{"type": "tool_call", "id", "name", "arguments"}` |
| `tool_result` and server tool results | `{"type": "tool_call_response", "id", "response": [...]}` |
| `image`, `document`, anything else | `{"type": "anthropic_image"}` and so on: the type only, never the data |

The SDK caps content at 750,000 bytes per span (`traces.max_content_bytes`). Over the cap it keeps the latest turns, which are the ones you debug: it removes the system prompt and the earliest messages first and sets `anthropic.content.truncated=true`. A backend with small field limits needs a lower cap, for example `{"traces": {"max_content_bytes": 50_000}}` for Honeycomb's 64 KB fields.

Prompts and responses often hold user data, and once exported they live under your backend's retention policy, not Anthropic's. Keep production on `metadata_only` unless your data-handling policy covers exporting prompts. `metadata_only` still exports tool names and descriptions, agent names, MCP (Model Context Protocol) server names, and your `conversation_id`.

##  4. Trace a stream

A streamed request uses the same span name with two extra attributes: `gen_ai.request.stream=true`, and `gen_ai.response.time_to_first_chunk`, the seconds from sending the request to the first `content_block_delta` event. Use the latter as your time-to-first-token metric. When extended thinking streams, that first delta is a thinking delta rather than visible text.

with tracer.start\_as\_current\_span("stream\_haiku"):

with content\_client.messages.stream(

model=MODEL,

max\_tokens=2000,

messages=[{"role": "user", "content": "Write a haiku about distributed tracing."}],

) as stream:

for text in stream.text\_stream:

print(text, end="", flush=True)

print("\n")

print\_traces()

```
A request departs,
spans bloom through a hundred hops,
one trace ID binds.

── trace 0876bf2b7afa9308edae081812829315
stream_haiku  [INTERNAL  UNSET  1.47s]
    anthropic.messages.create  [CLIENT  OK  1.47s]
      │ gen_ai.operation.name = chat
      │ gen_ai.request.model = claude-sonnet-5-5
      │ gen_ai.request.stream = True
      │ gen_ai.response.model = claude-sonnet-5-5
      │ anthropic.message.stop_reason = end_turn
      │ gen_ai.usage.input_tokens = 22
      │ gen_ai.usage.cache_read.input_tokens = 0
      │ gen_ai.usage.output_tokens = 167
      │ gen_ai.response.time_to_first_chunk = 0.459185962
      │ anthropic.request.id = req_011Cg1MqL8CWWD7WAudzj5UY
      │ http.response.status_code = 200
      │ gen_ai.input.messages = [{"role":"user","parts":[{"type":"text","content":"Write a haiku about distributed tracing."}]}]
      │ gen_ai.output.messages = [{"role":"assistant","parts":[{"type":"reasoning","content":"Haiku 5-7-5. Let me write.\n\n\"A request departs—\" count: A(1) re-quest(2) de-parts(2) =5. \n\"spans bloom through a hundred hops,\" spans(1) bloom(1) through(1) a(1) hun-dred(2) hops(1) =7.\n\"one trace ID binds.\" one(1) trace(1) I-D(2) binds(1)=5.\n\nGood."},{"type":"text","content":"A request departs,\nspans bloom through a hundred hops,\none trace ID binds."}]}]
```

If the model thought before answering, `gen_ai.output.messages` has a `reasoning` part ahead of the `text` part. That's the `thinking` block in span form (the table in section 3), and its tokens are inside `gen_ai.usage.output_tokens`, which is why a 17-syllable haiku can cost over a hundred output tokens.

Rules for stream spans:

* The span ends when the stream is read to the end or closed, not when headers arrive. Its duration is the wall-clock time of the whole response. If you stop reading early, close the stream (the `with` block does) or the span stays open. A stream closed early ends with status `UNSET` rather than `OK`.
* Only `messages.stream()` records `gen_ai.output.messages`, because it accumulates the final message. `messages.create(stream=True)` yields raw events, so its span has usage and stop reason but no output content.
* Spans you start inside the read loop are siblings of the SDK span, not children, because the SDK span isn't the current span while your loop body runs. To group per-chunk work with the request, wrap both the call and the loop in your own span, as `stream_haiku` does here.

##  5. Trace the tool runner

`client.beta.messages.tool_runner()` loops between Claude and your tools until Claude stops asking for one. With tracing on, the loop, each request, and each tool execution get their own spans. The tree shows how many round trips a question took and where the time went.

from anthropic import beta\_tool

@beta\_tool

def get\_weather(city: str) -> str:

"""Get the current weather for a city."""

# A real tool would call a weather API here. With HTTP client instrumentation

# installed, that call would get its own span under this tool's span.

return json.dumps({"city": city, "temp\_c": 18, "conditions": "fog"})

with tracer.start\_as\_current\_span("weather\_question"):

runner = content\_client.beta.messages.tool\_runner(

model=MODEL,

max\_tokens=500,

tools=[get\_weather],

messages=[{"role": "user", "content": "Weather in San Francisco? One sentence."}],

)

final = runner.until\_done()

print("Claude:", final.content[-1].text)

print()

print\_traces()

```
Claude: San Francisco is foggy right now, with a temperature of 18°C (about 64°F).

── trace de0633442f5078398a8c8dec46514cf4
weather_question  [INTERNAL  UNSET  1.94s]
    anthropic.messages.tool_runner  [INTERNAL  OK  1.94s]
      │ gen_ai.operation.name = invoke_agent
      │ gen_ai.request.model = claude-sonnet-5-5
        anthropic.messages.create  [CLIENT  OK  1.31s]
          │ gen_ai.operation.name = chat
          │ gen_ai.request.model = claude-sonnet-5-5
          │ gen_ai.response.model = claude-sonnet-5-5
          │ anthropic.message.stop_reason = tool_use
          │ gen_ai.usage.input_tokens = 397
          │ gen_ai.usage.cache_read.input_tokens = 0
          │ gen_ai.usage.output_tokens = 52
          │ anthropic.request.id = req_011Cg1MqSatuPgV7MCvqiegX
          │ http.response.status_code = 200
          │ gen_ai.input.messages = [{"role":"user","parts":[{"type":"text","content":"Weather in San Francisco? One sentence."}]}]
          │ gen_ai.output.messages = [{"role":"assistant","parts":[{"type":"tool_call","id":"toolu_01Fco8q4hEyZ4QFHvejscxZP","name":"get_weather","arguments":{"city":"San Francisco"}}]}]
        anthropic.custom_tool_use get_weather  [INTERNAL  OK  0.00s]
          │ gen_ai.operation.name = execute_tool
          │ gen_ai.tool.name = get_weather
          │ gen_ai.tool.call.id = toolu_01Fco8q4hEyZ4QFHvejscxZP
          │ gen_ai.tool.call.arguments = {"city":"San Francisco"}
          │ anthropic.tool_result.content = [{"type":"text","text":"{\"city\": \"San Francisco\", \"temp_c\": 18, \"conditions\": \"fog\"}"}]
        anthropic.messages.create  [CLIENT  OK  0.59s]
          │ gen_ai.operation.name = chat
          │ gen_ai.request.model = claude-sonnet-5-5
          │ gen_ai.response.model = claude-sonnet-5-5
          │ anthropic.message.stop_reason = end_turn
          │ gen_ai.usage.input_tokens = 484
          │ gen_ai.usage.cache_read.input_tokens = 0
          │ gen_ai.usage.output_tokens = 31
          │ anthropic.request.id = req_011Cg1MqYBVGjkuKxFDq79LQ
          │ http.response.status_code = 200
          │ gen_ai.input.messages = [{"role":"user","parts":[{"type":"text","content":"Weather in San Francisco? One sentence."}]},{"role":"assistant","parts":[{"type":"tool_call","id":"toolu_01Fco8q4hEyZ4QFHvejscxZP","name":"get_weather","arguments":{"city":"San Francisco"}}]},{"role":"user","parts":[{"type":"tool_call_response","id":"toolu_01Fco8q4hEyZ4QFHvejscxZP","response":[{"type":"text","text":"{\"city\": \"San Francisco\", \"temp_c\": 18, \"conditions\": \"fog\"}"}]}]}]
          │ gen_ai.output.messages = [{"role":"assistant","parts":[{"type":"text","content":"San Francisco is foggy right now, with a temperature of 18°C (about 64°F)."}]}]
```

* **`anthropic.messages.tool_runner`** (`INTERNAL`, `gen_ai.operation.name=invoke_agent`) covers the whole loop. Its duration is the end-to-end latency of the question. It has no usage attributes, so sum its children for cost. If you stop a runner you won't resume, call `runner.close()`, which also ends this span.
* **The first `anthropic.messages.create`** ends with `anthropic.message.stop_reason=tool_use`, and in content mode its `gen_ai.output.messages` holds one `tool_call` part with the arguments Claude chose.
* **`anthropic.custom_tool_use get_weather`** (`INTERNAL`, `gen_ai.operation.name=execute_tool`) is your function running. Tool span names are the tool kind, a space, then the tool name. `gen_ai.tool.call.id` is the join key across the three spans: the same `toolu_` ID is on the `tool_call` part in the previous request's output and on the `tool_call_response` part in the next request's input. In content mode, `gen_ai.tool.call.arguments` and `anthropic.tool_result.content` hold the input and output. If the function raises, this span gets status `ERROR` with `error.type=tool_error` and the loop continues with the error text as the tool result.
* **The second `anthropic.messages.create`** ends with `end_turn`. Its `gen_ai.usage.input_tokens` grew by the tool call and result, which is the visible cost of the round trip.

Tool spans come in three kinds:

* `anthropic.custom_tool_use <name>`: a tool you defined and an SDK tool runner ran. SDK spans only.
* `anthropic.mcp_tool_use <name>`: a tool from an MCP server, run by the SDK's MCP helpers or by the API's MCP connector.
* `anthropic.tool_use <name>`: a server tool such as `web_search`, or a tool from the Managed Agents prebuilt toolset such as `bash`, run by the API. API spans only, under the request's `SERVER` span on the Messages API and under the turn span in a Managed Agents session.

##  6. Trace a Managed Agents session

A Managed Agents session runs the agent loop on Anthropic's infrastructure, inside an *environment* (the container where the agent's tools execute), so the turn, model-request, and toolset-tool spans are API spans. The SDK contributes one span per Sessions API request, and its `traceparent` headers pull the API's turn spans into your trace. A custom tool you run locally gets the span you give it.

This example defines an agent with the prebuilt toolset (`agent_toolset_20260401`: bash, file read/write/edit, and search tools) plus one custom tool, then passes `initial_events` to `sessions.create` so the session and its first turn start in one request. The API parents a turn under the request that started it, so the first `anthropic.session.turn` span sits under `anthropic.sessions.create`. Without `initial_events`, it would sit under the first `sessions.events.send` instead.

agent = client.beta.agents.create(

name="release-notes-helper",

description="Looks up a package version and reports on it.",

model=MODEL,

system="You are concise. Use tools when they help. Reply in two sentences or fewer.",

tools=[

{"type": "agent\_toolset\_20260401"},

{

"type": "custom",

"name": "get\_latest\_version",

"description": "Return the latest released version of a package on the internal registry.",

"input\_schema": {

"type": "object",

"properties": {"package": {"type": "string"}},

"required": ["package"],

},

},

],

betas=BETAS,

)

environment = client.beta.environments.create(

name="otel-cookbook",

config={

"type": "anthropic\_cloud",

"networking": {"type": "limited"},

}, # no outbound network needed

betas=BETAS,

)

print(f"agent {agent.id} v{agent.version}, environment {environment.id}")

print\_traces()

```
agent agent_01Rn9W7qwgEHGV6cNc9Kmgpx v1, environment env_01KqmS21fqFhcjWuufz33532
── trace ff57054bb43bf540b4baeb9ace55354f
anthropic.agents.create  [CLIENT  OK  0.16s]
  │ gen_ai.agent.id = agent_01Rn9W7qwgEHGV6cNc9Kmgpx
  │ anthropic.request.id = req_011Cg1Mqad5pkAMgdir3L3mq
  │ http.response.status_code = 200

── trace f45b9758bf9bbe4925326bb443a9fb01
anthropic.environments.create  [CLIENT  OK  0.29s]
  │ anthropic.environment.id = env_01KqmS21fqFhcjWuufz33532
  │ anthropic.request.id = req_011Cg1MqbJ1hyVqRJiQNUVTE
  │ http.response.status_code = 200
```

Resource-creating calls put the new ID on their span (`gen_ai.agent.id`, `anthropic.environment.id`), so you can find the request that created any resource.

The following cell wraps the session in one `handle_ticket` span, the way a web handler or queue consumer would. Inside it:

1. `sessions.create` with `initial_events` creates the session already `running`.
2. The loop reads the event stream until `session.status_idle`. When the stop reason is `requires_action`, the agent is waiting on the custom tool, so the code runs it inside its own span and sends a `user.custom_tool_result`. That `events.send` request starts the second turn, and the loop reopens the stream to read it, which is why the output has two `events.stream` spans.
3. On any other stop reason (`end_turn`, `retries_exhausted`), the loop exits.

import datetime

def get\_latest\_version(package: str) -> str:

released = datetime.date.today() - datetime.timedelta(days=3)

return json.dumps({"package": package, "version": "4.2.0", "released": released.isoformat()})

with tracer.start\_as\_current\_span("handle\_ticket") as span:

session = client.beta.sessions.create(

agent=agent.id,

environment\_id=environment.id,

title="OTel cookbook demo",

initial\_events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "Find the latest version of the `acme-billing` package with your tool, "

f"then use bash to compute how many days ago it was released (today is {datetime.date.today()}).",

}

],

}

],

betas=BETAS,

)

span.set\_attribute("anthropic.session.id", session.id)

print(f"session {session.id} is {session.status}\n")

pending\_tool\_calls = {}

done = False

while not done:

with client.beta.sessions.events.stream(session.id, betas=BETAS) as events:

for event in events:

if event.type == "agent.custom\_tool\_use":

pending\_tool\_calls[event.id] = event

elif event.type == "agent.tool\_use":

print(f"[{event.name}] {json.dumps(event.input)[:80]}")

elif event.type == "agent.message":

print("".join(b.text for b in event.content if b.type == "text"))

elif event.type == "session.status\_idle":

if event.stop\_reason.type != "requires\_action":

done = True

break

results = []

for event\_id in event.stop\_reason.event\_ids:

call = pending\_tool\_calls.pop(event\_id)

with tracer.start\_as\_current\_span(

f"run\_tool {call.name}",

attributes={

"gen\_ai.operation.name": "execute\_tool",

"gen\_ai.tool.name": call.name,

"gen\_ai.tool.call.id": call.id,

"anthropic.session.id": session.id,

},

):

output = get\_latest\_version(\*\*call.input)

print(f"[{call.name}] {call.input} -> {output}")

results.append(

{

"type": "user.custom\_tool\_result",

"custom\_tool\_use\_id": call.id,

"content": [{"type": "text", "text": output}],

}

)

client.beta.sessions.events.send(session.id, events=results, betas=BETAS)

break # reopen the stream for the next turn

print()

print\_traces()

```
session sesn_01DDAMC6SZFVHAnsWqExd4kN is running

[get_latest_version] {'package': 'acme-billing'} -> {"package": "acme-billing", "version": "4.2.0", "released": "2026-10-11"}
[bash] {"command": "echo $(( ($(date -d 2026-10-14 +%s) - $(date -d 2026-10-11 +%s)) /
The latest `acme-billing` is version 4.2.0, released on 2026-10-11, which is 3 days before today (2026-10-14).

── trace 784c6c3872a0dffcd06983f6d5aa40a3
handle_ticket  [INTERNAL  UNSET  5.29s]
  │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
    anthropic.sessions.create  [CLIENT  OK  0.56s]
      │ gen_ai.request.model = claude-sonnet-5-5
      │ gen_ai.agent.id = agent_01Rn9W7qwgEHGV6cNc9Kmgpx
      │ gen_ai.agent.name = release-notes-helper
      │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
      │ anthropic.session.environment.id = env_01KqmS21fqFhcjWuufz33532
      │ anthropic.request.id = req_011Cg1MqcedDcVaVnDndVcnP
      │ http.response.status_code = 200
    anthropic.sessions.events.stream  [CLIENT  UNSET  1.24s]
      │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
      │ anthropic.request.id = req_011Cg1Mqf3VbYzhzc5cmAHzL
      │ http.response.status_code = 200
    run_tool get_latest_version  [INTERNAL  UNSET  0.00s]
      │ gen_ai.operation.name = execute_tool
      │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
      │ gen_ai.tool.name = get_latest_version
      │ gen_ai.tool.call.id = sevt_01Eif9fEB6vLWRZM7RtZiTon
    anthropic.sessions.events.send  [CLIENT  OK  0.28s]
      │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
      │ anthropic.request.id = req_011Cg1MqjNgj8NCyuWASXWpt
      │ http.response.status_code = 200
    anthropic.sessions.events.stream  [CLIENT  UNSET  3.48s]
      │ anthropic.session.id = sesn_01DDAMC6SZFVHAnsWqExd4kN
      │ anthropic.request.id = req_011Cg1MqkMitp9XvBeBvSf3t
      │ http.response.status_code = 200
```

###  How to read a session trace

The SDK spans under `handle_ticket`:

* **`anthropic.sessions.create`** carries `anthropic.session.id`, `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.request.model`, and `anthropic.session.environment.id`. Later spans for this session, SDK and API, carry the same `anthropic.session.id`. Group by it to see one session across requests and traces. Set it on your own spans too (the cell sets it on `handle_ticket`) so the same query finds them. The request returns as soon as the turn starts, so the API's turn span runs longer than the request span it hangs under.
* **`anthropic.sessions.events.stream`** has status `UNSET`, not `OK`. An event stream has no natural end, so closing it is a cancel rather than a success (the same rule as section 4). Expect `UNSET` on every `events.stream` span and alert only on `ERROR`.
* **`run_tool get_latest_version`** is your span. The SDK didn't run this tool, so naming and attributes are up to you. The cell copies the SDK's convention (`gen_ai.operation.name=execute_tool`, `gen_ai.tool.name`, `gen_ai.tool.call.id`, `anthropic.session.id`) so it lines up with tool-runner spans in dashboards. The `client.beta.sessions.events.tool_runner()` helper runs tools for you and emits `anthropic.custom_tool_use <name>` spans with these attributes.

What the API adds once you add a destination (section 8). A *thread* is one agent's conversation inside a session: a single-agent session has one, and a multi-agent session has one per subagent. These spans arrive with `service.name=claude-platform` and attach under the SDK spans by `traceparent`:

handle\_ticket INTERNAL (yours)

├── anthropic.sessions.create CLIENT (SDK)

│ └── anthropic.sessions.create SERVER (API)

│ └── anthropic.session.turn INTERNAL stop\_reason=requires\_action

│ └── anthropic.model\_request INTERNAL gen\_ai.usage.\* (asks for get\_latest\_version)

├── anthropic.sessions.events.stream CLIENT (SDK)

│ └── anthropic.sessions.events.stream SERVER (API)

├── run\_tool get\_latest\_version INTERNAL (yours)

├── anthropic.sessions.events.send CLIENT (SDK)

│ └── anthropic.sessions.events.send SERVER (API)

│ └── anthropic.session.turn INTERNAL stop\_reason=end\_turn

│ ├── anthropic.model\_request INTERNAL gen\_ai.usage.\*

│ ├── anthropic.tool\_use bash INTERNAL gen\_ai.tool.call.id

│ └── anthropic.model\_request INTERNAL gen\_ai.usage.\* (final answer)

└── anthropic.sessions.events.stream CLIENT (SDK)

└── anthropic.sessions.events.stream SERVER (API)

* **`anthropic.session.turn`** (`gen_ai.operation.name=invoke_agent`) is one agent turn on one thread, from `running` to idle. Its parent is the request that started it: `sessions.create` for `initial_events`, `sessions.events.send` for later messages and tool results. `anthropic.session.turn.stop_reason` is the same stop reason the loop read from the idle event (`end_turn`, `requires_action`, `retries_exhausted`). When the destination's content mode is Full content, the turn carries `gen_ai.input.messages` and `gen_ai.output.messages`, and a thread's first turn also carries `gen_ai.system_instructions`. The SDK client's `content_mode` has no effect on API spans.
* **`anthropic.model_request`** is one model call inside the turn, with the `gen_ai.usage.*` attributes. To total a session's tokens, sum its `anthropic.model_request` spans (plus `anthropic.session.outcome_evaluation` spans if you use outcomes). Turn spans carry no usage attributes, so a sum over the trace never double counts.
* **`anthropic.tool_use <name>`** is a prebuilt-toolset tool the API ran in the environment. `anthropic.mcp_tool_use <name>` is an MCP tool, with `anthropic.mcp.server.name`.
* **`gen_ai.conversation.id`** on the API's turn, model-request, and tool spans is the thread ID. Group by it and sort by start time to read one thread as a transcript. In a multi-agent session, a turn on another thread nests under the turn that called it, and a turn that starts because another thread replied has no parent request, so it begins a new trace that you find by `anthropic.session.id`. This thread ID is separate from the `conversation_id` you set in section 3, which tags SDK spans only.

##  7. Send spans to your backend

The SDK has no exporter settings of its own. It emits into whatever provider you registered, so shipping spans is standard OTel configuration. Set the OTLP environment variables before starting the kernel, and the setup cell's `BatchSpanProcessor(OTLPSpanExporter())` exports every span this notebook produced:

export OTEL\_EXPORTER\_OTLP\_ENDPOINT="http://localhost:4318" # base URL, the exporter appends /v1/traces

export OTEL\_EXPORTER\_OTLP\_HEADERS="authorization=Bearer <token>" # comma-separated key=value pairs, if your backend needs auth

export OTEL\_SERVICE\_NAME="ticket-service" # optional, overrides the Resource in code

`http://localhost:4318` is the default OTLP/HTTP port of a local OpenTelemetry Collector, the vendor-neutral proxy that batches, retries, redacts, and fans spans out to one or more backends. Every major backend also documents a direct OTLP/HTTP endpoint and auth header. In production, put a Collector between your services and the vendor so application code never holds vendor credentials, use `BatchSpanProcessor` rather than `SimpleSpanProcessor`, and call `provider.shutdown()` on exit so the last batch flushes.

if os.environ.get("OTEL\_EXPORTER\_OTLP\_ENDPOINT"):

provider.force\_flush()

print("Flushed SDK spans to", os.environ["OTEL\_EXPORTER\_OTLP\_ENDPOINT"])

else:

print("OTEL\_EXPORTER\_OTLP\_ENDPOINT is not set, spans stayed in memory.")

```
OTEL_EXPORTER_OTLP_ENDPOINT is not set, spans stayed in memory.
```

##  8. Add the API's spans to the same trace

SDK spans stop at the network boundary. Model runs, server tools, compactions, and Managed Agents turns happen inside the API. The API exports those as its own spans to a *destination*: an OTLP/HTTP endpoint plus headers that you register in your organization (up to 10, each scoped to all or some workspaces). A destination needs no code changes and covers every client in the organization, SDK or not.

To add one (organization admins only), go to [Settings > Telemetry destinations(opens in new tab)](https://platform.claude.com/settings/telemetry-destinations) in the Console, choose **Add destination**, pick your provider or **Custom**, and fill in:

| Field | Value |
| --- | --- |
| OTLP endpoint URL | The HTTPS base URL of your backend's OTLP/HTTP endpoint: port 443, a hostname rather than an IP, no redirects. The API delivers only to public HTTPS hosts so a destination can't point at internal infrastructure. Don't append `/v1/traces` |
| Request headers | Your backend's auth header. Values are write-only after save |
| Content mode | **Metadata only** or **Full content**. Independent of the SDK's `traces.content_mode`, so set each deliberately |
| Workspaces | All, selected, or all except |
| Maximum content size | Optional. Empty means up to 8 MiB per span. Lower it for backends with small field limits |

The API delivers OTLP/HTTP protobuf with gzip, at least once (dedupe on trace ID plus span ID), and marks the destination **Healthy** within about a minute of the first span. The API disables a destination that redirects, resolves to a private IP, or fails for 24 hours straight.

###  Pair API spans with SDK spans

Filter your backend on `service.name = claude-platform` to see only API spans. For a Messages API request the API emits a `SERVER` span with the same name as the SDK span, and under it one span per step it ran:

anthropic.messages.create SERVER parented under the SDK CLIENT span by traceparent

├── anthropic.model\_request INTERNAL one per model run, with gen\_ai.usage.\*

├── anthropic.tool\_use web\_search INTERNAL one per server-tool use (anthropic.mcp\_tool\_use <name> for the MCP connector)

├── anthropic.model\_request INTERNAL the run after the tool result

└── anthropic.compaction INTERNAL when context compaction ran, with its own usage

With a destination configured and `web_search` added to its tools, the tool-runner trace from section 5 becomes:

weather\_question INTERNAL (yours)

└── anthropic.messages.tool\_runner INTERNAL (SDK)

├── anthropic.messages.create CLIENT (SDK)

│ └── anthropic.messages.create SERVER (API)

│ ├── anthropic.model\_request INTERNAL

│ ├── anthropic.tool\_use web\_search INTERNAL

│ └── anthropic.model\_request INTERNAL asks for get\_weather

├── anthropic.custom\_tool\_use get\_weather INTERNAL (SDK)

└── anthropic.messages.create CLIENT (SDK)

└── anthropic.messages.create SERVER (API)

└── anthropic.model\_request INTERNAL final answer

Four rules keep queries correct when both sources are on:

* **Tell the pair apart by kind or service.** The SDK span is `CLIENT` from your `service.name`. The API span is `SERVER` from `claude-platform`. Both carry the same `anthropic.request.id`.
* **Count tokens from one source per request.** The `CLIENT` span, the `SERVER` span, and the `anthropic.model_request` spans under it all report the same usage. Sum the `SERVER` spans or their `anthropic.model_request` children, never both, and add `anthropic.compaction` spans if present. For Managed Agents, sum `anthropic.model_request` and `anthropic.session.outcome_evaluation`.
* **Your sampler controls API span volume.** If your sampler drops a trace, the sampled bit in `traceparent` is off and the API emits nothing for that request. A request with no `traceparent` gets API spans in a new trace.
* **Don't bill from spans.** Delivery is at least once, so duplicates happen, and a disabled destination or an unsampled trace drops spans. Use the [Usage and Cost API(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/observability/usage_cost_api.ipynb) for accounting.

##  9. Clean up

Archiving is permanent. Skip this cell to keep the agent and environment for reuse. `provider.shutdown()` ends tracing for this kernel, so restart the kernel before re-running earlier cells.

client.beta.sessions.archive(session.id, betas=BETAS)

client.beta.agents.archive(agent.id, betas=BETAS)

client.beta.environments.archive(environment.id, betas=BETAS)

memory\_exporter.clear()

provider.shutdown() # flushes the OTLP batch processor if one was added

print("archived and flushed")

```
archived and flushed
```

##  Taking this to production

* Wrap each unit of work (request handler, queue message, cron run) in one span of your own and call the SDK inside it, so SDK and API spans land under the operation that caused them.
* Export through an OpenTelemetry Collector with `BatchSpanProcessor`, keep `content_mode` on `metadata_only` until your data policy says otherwise, and register one Console destination per backend.
* Alert on `ERROR` status and on `anthropic.message.stop_reason=max_tokens`. Treat `UNSET` on stream and event-stream spans as normal.
* Build cost views from one source per request: `SERVER` spans or `anthropic.model_request`, never stacked on the `CLIENT` span. Reconcile against the Usage and Cost API.

##  Documentation

* [OpenTelemetry for the Claude API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry): overview, content modes, example traces, token counting
* [Use OpenTelemetry with the Claude SDK(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk): setup for every language, every client option and environment variable
* [Use OpenTelemetry with the Claude API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api): destinations, delivery, sampling whole conversations
* [OpenTelemetry span reference(opens in new tab)](https://platform.claude.com/docs/en/api/opentelemetry/spans): every span, attribute, and parent relationship
