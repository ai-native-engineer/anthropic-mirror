<!-- https://anthropic-partners.skilljar.com/partner-basecamp/464535 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/17vf5yos0i2y3/module-03-models-capabilities.html -->

# Models and Capabilities

Module 3 of 6

# Models & *Capabilities*

How each Claude model behaves, and why that knowledge matters more than any spec table.

Partner Basecamp
~28 min
SET A - DAY 1 PREP
1 knowledge check

The question that opens this session

"Our Opus deployment is producing *worse* results than Sonnet. We're paying 5× more for demonstrably worse output."

Enterprise Healthcare CTO, escalation thread

How is this possible?

### The resolution and this module's thesis

The team had spent weeks optimizing a system prompt for Sonnet: few-shot examples, formatting instructions, tone calibration, all tuned to Sonnet's behavioral style. Then someone swapped the model ID to Opus expecting an improvement. The few-shot examples that guided Sonnet's responses were **actively confusing Opus**, which interprets the same prompts differently. The fix was 30 minutes of prompt adjustment.

Model expertise is not knowing which model is "best." It is architectural and behavioral knowledge: the kind that lets you build systems that work and debug them when they don't.

Part 1: Model Families

## Three models. Three behavioral signatures.

The spec table tells you what each model can do. The behavioral signature tells you how it thinks. Both matter, but the signature shapes your architecture.

Opus 4.7

Precision Interpreter

Takes instructions literally and executes precisely on what you specify. Where earlier Opus versions hedged on ambiguity, 4.7 resolves it through action. Maintains coherence across very long outputs and sustains performance on complex multi-step tasks.

High-stakes analysis
Long-form reasoning
Edge cases

Sonnet 4.6 · NEW

Disciplined & Honest

Near-Opus reasoning at Sonnet speed. Significantly improved honesty: flags uncertainty rather than producing overconfident output. Reduced laziness on long tasks. The new default recommendation.

New deployments
Agentic coding
Honesty-critical

Haiku 4.5

Formulaic Executor

Follows instructions closely and consistently. Near-frontier intelligence for well-specified tasks at 4–5× Sonnet's speed. Best when you need predictable, high-throughput behavior, and the task is clearly defined.

Classification
Structured extraction
Routing layers

These labels are not marketing copy. They are behavioral patterns that show up in outputs, and that you need to design around.

🔮

## Opus 4.7

Most intelligent · Precision Interpreter

|  |  |
| --- | --- |
| API ID | `claude-opus-4-7` |
| Pricing | $5 / $25 per MTok |
| Context | 200K tokens (1M beta) |
| Max output | 128K tokens |
| Latency | Moderate |
| Adaptive thinking | ✓ All effort levels |
| Knowledge cutoff | May 2025 (reliable) |

### Precision Interpreter: in practice

Opus 4.7 takes instructions more literally than its predecessor. Where 4.6 hedged on ambiguous prompts and surfaced competing constraints, 4.7 resolves ambiguity through execution. Prompts written for Sonnet's direct style generally transfer well, but watch edge cases where 4.6's cautious qualification was load-bearing.

Reach for Opus when maximum intelligence applied directly matters: high-resolution vision tasks (images up to 3.75MP), very long-form generation requiring sustained coherence, and long-running autonomous work where step count or parallel tool use exceeds what Sonnet handles well.

🔥

## Sonnet 4.6 New

Default recommendation · Disciplined & Honest

|  |  |
| --- | --- |
| API ID | `claude-sonnet-4-6` |
| Pricing | $3 / $15 per MTok |
| Context | 200K tokens (1M beta) |
| Max output | 64K tokens |
| Latency | Fast |
| Adaptive thinking | ✓ All effort levels |
| Launched | February 17, 2026 |

### Disciplined & Honest: in practice

Sonnet 4.6's honesty improvements mean it flags uncertainty rather than producing confident output. In agentic contexts, Sonnet 4.5 would sometimes claim a task was complete when it wasn't. 4.6 flags uncertainty instead. That is the model working correctly, not a regression.

When migrating from Sonnet 4.5: if your system relied on 4.5's confident-but-wrong behavior, you may see more hedged outputs in 4.6. Adjust prompt expectations. Don't roll back.

**Default for new deployments.** The question before recommending Opus: "What specific capability does this use case need that Sonnet 4.6 doesn't provide?" If you can't answer that, start here.

🚀

## Haiku 4.5

Fastest · Formulaic Executor

|  |  |
| --- | --- |
| API ID | `claude-haiku-4-5-20251001` |
| Pricing | $1 / $5 per MTok |
| Context | 200K (no 1M beta) |
| Max output | 64K tokens |
| Latency | Fastest |
| Adaptive thinking | Manual mode only |
| Knowledge cutoff | Feb 2025 (reliable) |

### Formulaic Executor: in practice

Haiku follows instructions closely. It doesn't improvise. That is a strength when the task is well-specified: classification steps, structured extraction pipelines, routing decisions, eval graders. Predictable, high-throughput, cost-effective.

Where it breaks down: open-ended reasoning, ambiguous or competing constraints, anything that benefits from the model's judgment. Those belong to Sonnet or Opus. Haiku is a precision instrument for well-defined tasks, not a cheaper do-everything model.

At $1/$5 per MTok (a fifth of Sonnet's price), every request processed on Opus that Haiku could handle is a cost decision, not a quality one.

The rule that prevents the most expensive mistakes

## Requests are not portable across models.

Switching models breaks things in two distinct ways. Both are recoverable, but only if you know to look for them.

#### Prompt differences

Few-shot examples and formatting instructions calibrated for one model actively degrade another's performance. Sonnet-to-Opus transfers require prompt re-tuning. Behavioral differences surface as unexpected output changes, not obvious failures.

#### Capability differences

Features vary by model and platform. Adaptive thinking exists only on Opus 4.7 and Sonnet 4.6. The 1M context beta is the same. Web search via the API isn't available on Bedrock. Design an architecture around a feature, then discover the target platform doesn't support it, and you've designed yourself into a corner.

### The migration checklist: run every time

01

#### Confirm the current model isn't sufficient

First question when a client wants to upgrade: "What's failing that you're hoping the new model fixes?" The answer usually reveals a prompt issue, a capability gap, or an expectation mismatch. All are cheaper to fix than a model upgrade.

02

#### Audit capability support on the target model and platform

Does your architecture use any features unavailable on the target model or platform? Adaptive thinking, 1M context, and web search all have gaps depending on where you're deploying.

03

#### Re-tune prompts and run your eval suite

A model migration without eval results is guesswork. Behavioral differences that matter most surface in edge cases, not standard test prompts.

Part 2: Sonnet 4.6 Spotlight

## Why the default recommendation changed

Sonnet 4.6 launched February 17, 2026. For most new deployments, it is the right starting point. Here's what changed from Sonnet 4.5.

### Improved honesty

Sonnet 4.5 would sometimes claim a task was complete when it wasn't. That was a serious reliability issue in agentic workflows. 4.6 flags uncertainty. If a client is running agentic pipelines on 4.5, this alone is a reason to migrate.

### Adaptive thinking: now available

Sonnet 4.6 now supports adaptive thinking with effort levels (max, high, medium, low). That was previously Opus-only. For most reasoning-heavy tasks that previously required Opus, Sonnet 4.6 with adaptive thinking provides sufficient reasoning capability, at Sonnet pricing.

### Stronger coding

Near-Opus coding quality, reduced laziness on long tasks, more complete outputs. For agentic coding (navigating large codebases, making multi-file changes), Sonnet 4.6 is the recommended model.

### Same $3 / $15 pricing

No cost increase. Same 200K context window (1M beta), same 64K max output. The improvements come with no pricing change from Sonnet 4.5.

#### Where Sonnet 4.6 is the answer

Iterative development, agentic coding, document creation, honesty-critical applications, anything previously requiring Opus for extended thinking.

#### Where Opus still wins

Very long multi-step tasks with 150+ sequential steps. Maximum parallel tool calls per response. High-resolution vision tasks (images up to 3.75MP). Long-running autonomous work where sustained coherence across the full task matters. If the use case doesn't clearly require one of these, start with Sonnet 4.6.

**Co-launched as GA with Sonnet 4.6:** code execution, web fetch, tool search, programmatic tool calling, tool use examples, and memory.

Part 3: Extended Thinking & Multi-Model

## Three thinking modes. One billing gotcha.

Adaptive thinking is now GA on Opus 4.7 and Sonnet 4.6. Instead of specifying a token budget and hoping you picked the right number, give the model an effort level and it decides how much to reason per query.

Adaptive

#### Default for Opus + Sonnet 4.6

Claude dynamically determines when and how much to reason. Simpler API, better than fixed budgets, automatic thinking between tool calls in agentic loops. Use this unless you have a specific reason for manual.

Manual

#### All models: explicit budget

Right for Sonnet 4.5 or Haiku customers who need reasoning, and for pipelines where precise token budget control matters for cost predictability. Uses the `budget_tokens` parameter.

Disabled

#### When reasoning adds no value

Classification, structured extraction, format conversion. The reasoning step adds latency without quality gain. Omit the thinking parameter entirely.

**Prompt**
"Review this vendor software contract. Identify the top risks and recommend changes before signing." (real Opus 4.7 outputs)

low
22s

thinking

Identifies one-sided liability and IP ownership grab. Recommends removing blanket customer data liability and retaining sole IP for custom work. Covers basics but misses financial and operational risks.

886 tokens  •  **$0.023**

medium
46s

thinking

**5 critical risks.** Flags the 8% cost escalator ($779K over 3 years), computes compounding cost if auto-renewal is missed. Adds financial modeling the low effort missed entirely.

1,863 tokens  •  **$0.048**

high (default)
64s

thinking

**7 high-severity + 4 moderate risks** with severity ratings. Year-by-year cost projection table. Catches data-governance and legal exposure medium missed. Full redline suggestions per clause.

2,960 tokens  •  **$0.075**

xhigh

thinking

Deeper reasoning passes than high. For complex tasks, adds cross-clause consistency checking and surfaces downstream exposure the high pass typically misses. Closer to max depth with meaningfully lower token spend.

max
72s

thinking

**7 high + 4 medium risks.** Same depth as high. Quotes exact contract language for each risk, calls the data liability clause "the most dangerous" provision, adds negotiation priority ordering.

3,418 tokens  •  **$0.087**

**Key insight:** `xhigh` is the sweet spot for high-stakes tasks, closing the gap with max while costing significantly less. `high` remains a strong default for most use cases. `low` misses the financial modeling entirely. `max` adds polish with diminishing returns.

#### The billing gotcha: read this carefully

Claude 4 models return **summarized thinking** in the API response. You see a short thinking block. You are billed for the full reasoning, which is encrypted in the signature field. A developer who measures cost by reading the visible response content will dramatically underestimate token spend. Always check `usage.output_tokens`, not the length of the thinking block you can read.

Part 4: Platform Capabilities

## The easiest cost win in almost any deployment

Prompt Caching · GA · All platforms

### Tag stable content once. Pay 90% less on every subsequent read.

Tag any stable content with `cache_control`: system instructions, reference documents, few-shot examples. The API caches it server-side. Every request that hits the cache pays 90% less for those tokens.

$4,515

Without caching / mo

→

$466

With caching / mo

=

90%

Cost reduction

Legal AI product. 150K-token stable system prompt. 10,000 requests per month on Sonnet 4.6, each with ~500 tokens of variable input. That is $48,000 in annual savings from one API parameter change.

Bedrock + Vertex: 5-minute TTL only. Claude API + Azure: 5-minute and 1-hour TTL both available.

### Context Editing Beta

Automatically clears old tool results and thinking blocks when context exceeds a threshold, keeping agentic pipelines running without hitting the 200K limit. Essential for any agent making more than 20–30 tool calls. SDK client-side compaction is also available without the beta flag.

### Why it matters

An agent runs for 30 minutes. Each tool call adds results to the conversation history. By call 40, you're at 100K tokens. By call 80, you're approaching 200K. The agent fails. Not because it ran out of intelligence. Because it ran out of context window.

Delivery & Processing

## Four capabilities every deployed integration needs

StreamingGA · All platforms

Add `stream: true` to any request. Tokens appear as generated, turning an 8-second wait into a product that feels alive. Default for any user-facing app. Three event types to handle: `message_start` (metadata), `content_block_delta` (text tokens), `message_stop` (done). Also prevents HTTP timeouts on outputs longer than ~2K tokens.

Batch ProcessingGA · All platforms

Submit up to 100,000 requests as an async job: 50% discount on all tokens, 24-hour SLA, no rate limits. Any offline or scheduled workload should be on batch. Three-step lifecycle: POST to create → poll for status → GET results, each mapped by your `custom_id`. Stacks with caching: cached batch reads get 90% off the already-discounted rate.

CitationsGA · All platforms

Claude attaches character-level source references to each claim, so users can verify exactly which sentence in which document produced an answer. Three citation types: `char_location` (plain text), `page_location` (PDF), `content_block_location` (custom). Cited text in the response is free, not billed as output tokens. Incompatible with structured output mode.

Structured OutputsGA · All platforms

Grammar-constrained JSON via `output_config.format` with a JSON schema. The model physically cannot produce tokens that violate your schema. Not "usually outputs valid JSON." Always. The first request using a new schema takes slightly longer while Claude compiles the grammar in the background before responding. After that, subsequent requests are fast. Note: structured output support on Haiku 4.5 is still in beta. Test thoroughly before recommending it for high-volume or production use.

Data & Integration

## Five capabilities that change how you handle documents, retrieval, and data

Files APIBeta · API + Azure

Upload a file once, reference it by `file_id` across multiple requests. If you're sending the same 150-page contract in every request, you're resending 2.4MB of payload every time. With the Files API, that drops to 200 bytes. Currently beta on Claude API and Azure, not available on Bedrock or Vertex, where clients manage file injection themselves.

Search ResultsGA · All platforms

When you have your own retrieval infrastructure, use the `search_results` content type instead of concatenating RAG chunks into raw text. It preserves source separation: Claude knows which content came from which document, enabling better citations and cleaner attribution. This is not the web search tool. The `search_results` type is a structured input format for your own retrieval outputs.

PDF + VisionGA · All platforms

Send PDFs directly: no OCR pipeline, no Textract, no chunking. Claude reads text, tables, charts, and images natively. Pair with citations for verifiable extraction (page\_location offsets work on PDFs). For vision: resize to the minimum resolution needed. Receipt OCR at 720p is indistinguishable from 4K in accuracy but costs 75% less, a significant saving for high-volume image workloads.

MultilingualGA · All platforms

All Claude models support major world languages including code-switching within a single conversation. The cost gotcha: CJK scripts (Chinese, Japanese, Korean) use 2–3× more tokens per word than Latin scripts. A cost estimate based on English token counts will be significantly wrong for Japanese or Korean at volume. Tip: an English prompt with a non-English system instruction reduces input tokens vs. a full non-English prompt.

Voyage EmbeddingsGA · API + Azure + Bedrock

Anthropic's Voyage embedding family is available through the same API: one key, one SDK, one billing relationship for both retrieval and generation. Domain-specific variants outperform general-purpose on specialized corpora: `voyage-code-3` for code repositories, `voyage-finance-2` for financial documents, `voyage-law-2` for legal texts. Not available on Vertex. Clients on Vertex need a separate embedding solution.

Platform Coverage

## Not every feature works everywhere

Platform coverage gaps are architectural constraints, not things you can work around with a different API call. Confirm the client's target platform at the first scoping conversation.

| Capability | Claude API | Azure | Bedrock | Vertex AI |
| --- | --- | --- | --- | --- |
| All GA features | ✓ Full | ✓ Full | Partial | Partial |
| Prompt Caching | ✓ 5min+1hr | ✓ 5min+1hr | ✓ 5min only | ✓ 5min only |
| Adaptive Thinking | ✓ | ✓ | ✓ | ✓ |
| Web Search | ✓ | ✓ | ✗ | ✓ |
| Code Execution | ✓ | ✓ | ✓ | ✗ |
| MCP Connectors | ✓ | ✓ | ✓ | ✗ |
| Files API | ✓ | ✓ | ✗ | ✗ |
| Agent Skills | ✓ | ✓ | ✓ | ✗ |
| Voyage Embeddings | ✓ | ✓ | ✓ | ✗ |

#### The failure mode this creates

A team builds a prototype on Claude API using MCP connectors or code execution. It works perfectly. Three months later, during deployment planning, they discover the client is on Vertex AI, and those capabilities don't exist there. Confirm the target platform during scoping. Not implementation. Not deployment. Scoping.

Knowledge Check

## Spot the mistake

Three scenarios. Each describes a real approach taken with Claude models. Decide whether each approach is sound or flawed, then see the explanation. Answer all three to continue.

Scenario A

### The model upgrade

A client's engineering team runs a contract analysis system on Sonnet 4.5. They want sharper reasoning on complex multi-party agreements. They swap the model ID to Opus 4.7 and run their existing test suite. All tests pass. They ship to production the same afternoon.

Sounds right
Flag it

Flag it

Passing a test suite isn't enough. Prompts calibrated for Sonnet's direct style may produce unexpected results with Opus 4.7, which interprets instructions more literally and applies stricter interpretation to edge cases the test suite doesn't cover. Correct approach: re-tune prompts for Opus 4.7's instruction-literal signature, run a broader eval suite designed to surface behavioral differences, then ship.

Scenario B

### The cost estimate

A developer is building a due diligence tool on Opus 4.7 with adaptive thinking set to high effort. They review an API response, see the thinking block contains about 400 words, and use this to estimate per-request token cost. They build a product pricing model from this estimate.

Sounds right
Flag it

Flag it

Claude 4 models return **summarized thinking** in the API response. The full reasoning is encrypted in the signature field: you can't read it, but you're billed for it. A 400-word visible thinking block may represent thousands of tokens of actual reasoning. A pricing model built on visible response length will significantly underestimate costs. Always use `usage.output_tokens` from the response object for accurate cost measurement.

Scenario C

### The model recommendation

A partner engineer is scoping a new agentic coding assistant for a client's internal developer platform. The client hasn't committed to a deployment platform yet. The engineer recommends Sonnet 4.6 as the primary model and notes they should only escalate to Opus if the specific workflow demonstrates a clear need for Opus's capabilities.

Sounds right
Flag it

Sounds right

This is the correct default posture. Sonnet 4.6 delivers near-Opus coding quality with improved honesty and adaptive thinking at Sonnet pricing. For an agentic coding assistant (iterative development, codebase navigation, multi-file changes), Sonnet 4.6 is the recommended model. The engineer should confirm whether the workflow involves 150+ sequential steps, requires maximum parallel tool calls, involves high-resolution vision tasks, or requires long-running autonomous work. If none apply, Sonnet 4.6 is the right starting point, and the approach of confirming before escalating to Opus is exactly right.

Answer all three scenarios to continue.

Module 3 of 6 Complete

## The spec table is the least useful *thing you learned here.*

What you can do now is more specific. You know how each model interprets instructions differently, and how to design around that. You know what breaks when you switch models. You know which platform constraints to surface at the start of a client engagement, **before architecture decisions get made**. That is the difference between a partner who knows the models and a partner who can build with them.

You're ready for Day 1

Bring everything you've learned from the modules in Set A. They will enable you to build, apply and deepen your understanding. Then you can dive into Pre-work for Day 2, starting with **Claude Enterprise**.

Mark all pre-work for Day 1 Complete

Begin
