<!-- source: https://platform.claude.com/cookbook/evals-agentic-search-reproduce-agentic-search-benchmarks -->

# Reproducing Claude's Agentic Search Benchmark Scores

Claude's [published agentic-search scores](https://www.anthropic.com/system-cards) (DeepSearchQA, BrowseComp) **are reproducible on the public Messages API**. The key is harness configuration: a handful of API parameters that don't matter for short conversations become load-bearing once an agent is running 30+ tool calls across hundreds of thousands of tokens.

A common reason third-party evaluations come in lower is harness configuration. This cookbook walks through each parameter and explains why it matters.

> **Cost & runtime**: the live cells in this notebook run **3 demo questions** (roughly 5–10 minutes, a few dollars in API spend). Reproducing a full 900-question benchmark takes a few hundred dollars and a couple of hours at moderate concurrency; this notebook does not re-execute the full run.

## By the end of this cookbook, you'll be able to:

* **Build** an agentic search loop using programmatic tool calling, server-side compaction, and task budgets that reproduces Claude's published agentic-search scores.
* **Understand** why each configuration choice matters for long-horizon agentic tasks.
* **Adapt** the same harness to BrowseComp, or your own deep-research benchmark, by swapping the dataset, a few config lines, and the grader.

## Prerequisites

**Required knowledge**

* Comfortable with the Messages API and basic tool use
* Familiar with the concept of an agentic loop (call model → handle tool use → call again)

**Required tools**

* Python 3.11+
* `anthropic >= 0.111.0`
* An Anthropic API key with access to the `web_search`, `web_fetch`, and `code_execution` server tools ([how to enable](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool))

**Recommended**

* The [Programmatic Tool Calling cookbook](https://platform.claude.com/cookbook/tool-use-programmatic-tool-calling-ptc), which introduces the pattern we use here
* The [Automatic Context Compaction cookbook](https://platform.claude.com/cookbook/tool-use-automatic-context-compaction), which we lean on heavily

## Setup

python

```
%%capture
%pip install -U "anthropic>=0.111.0" pandas python-dotenv
```

python

```
import time

import anthropic
import pandas as pd
from dotenv import load_dotenv
from utils.agentic_search import (
    SAMPLE_QUESTIONS,
    USER_PROMPT_TEMPLATE,
    extract_result_tag,
    grade_response,
    summarize_response,
)

load_dotenv()

MODEL = "claude-sonnet-5"
# Hold the grader model fixed so scores are comparable across the model under test.
GRADER_MODEL = "claude-opus-4-6"

# With server-side tools, a single streamed call can run for many minutes of
# in-sandbox tool execution before the first token arrives. We raise the read
# timeout to 60 minutes; with streaming this is a per-event ceiling, not a
# whole-response one, so it only matters for the gap before the first event.
client = anthropic.Anthropic(
    max_retries=20,
    timeout=anthropic.Timeout(5.0, read=3600.0, write=600.0, pool=600.0),
)
```

## The task

Here are three demo questions in the DeepSearchQA format. Each is answerable, but only after several rounds of searching, reading, and cross-referencing:

python

```
for q in SAMPLE_QUESTIONS:
    print(f"[{q['example_id']}] ({q['answer_type']})")
    print(f"  Q: {q['problem']}")
    print(f"  A: {q['answer']}\n")
```

```
[demo-0] (Single Answer)
  Q: Among the chief executives of the four largest US banks by total assets as of Q1 2024, which one had held their CEO position the longest?
  A: Jamie Dimon

[demo-1] (Set Answer)
  Q: Which three countries had the largest installed offshore wind capacity at the end of 2023?
  A: China, United Kingdom, Germany

[demo-2] (Set Answer)
  Q: List the films that won the Palme d'Or at the Cannes Film Festival in 2021, 2022, and 2023, and name the director of each.
  A: Titane (Julia Ducournau), Triangle of Sadness (Ruben Östlund), Anatomy of a Fall (Justine Triet)
```

We wrap each question in a short prompt that asks Claude to plan freely and put its final answer in `<result>` tags so the grader can extract it cleanly:

python

```
print(USER_PROMPT_TEMPLATE.format(question=SAMPLE_QUESTIONS[0]["problem"]))
```

```
I want you to answer the following question.

<question>Among the chief executives of the four largest US banks by total assets as of Q1 2024, which one had held their CEO position the longest?</question>

First plan out your response. This part can be as long as needed. You may need to run many searches, this is totally fine.

Then provide a short and concise answer in <result> tags. For questions expecting multiple answers, separate them with commas.
```

The model needs to plan, search the web, fetch and read pages, run calculations, and keep doing that until it's confident, then emit a clean final answer we can grade. Almost every part of that sentence is a place where a naive harness silently loses points. We'll build the loop piece by piece.

> The three questions above are written for this cookbook (not drawn from DeepSearchQA-900) to keep the live cells fast and cheap. For the real benchmarks, see *Datasets* below.

### Datasets

| Benchmark | Size | Where to get it |
| --- | --- | --- |
| **BrowseComp** | 1,266 questions | [Wei et al., 2025](https://arxiv.org/html/2504.12516v1) (OpenAI) |
| **DeepSearchQA** | 900 questions | [Kaggle Benchmarks](https://www.kaggle.com/benchmarks/google/dsqa) ([paper](https://arxiv.org/abs/2601.20975)) |

The harness expects each row to have `problem`, `answer`, and `answer_type` fields; map the source schema accordingly when you load it.

## 1. Tools: programmatic tool calling

The single biggest efficiency lever is **[programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)** (PTC): instead of Claude calling `web_search` and `web_fetch` directly and round-tripping each result through the API, Claude writes Python in a `code_execution` sandbox and calls search/fetch *from inside that code*. Only the code's printed summary returns to the conversation.

For deep research this is essential. A single question can issue 50+ fetches. Without PTC every one of those page bodies lands in context; with PTC the model reads them in-sandbox and surfaces only what it needs.

We enable it by listing `code_execution` as the only directly-callable tool, and marking `web_search`/`web_fetch` as callable *from* code execution with their results excluded from the response:

python

```
TOOLS = [
    {
        "type": "code_execution_20260521",
        "name": "code_execution",
    },
    {
        "type": "web_search_20260318",
        "name": "web_search",
        "max_uses": 10_000,
        "allowed_callers": ["code_execution_20260521"],
        "response_inclusion": "excluded",
    },
    {
        "type": "web_fetch_20260318",
        "name": "web_fetch",
        "max_uses": 10_000,
        "max_content_tokens": 1_000_000,
        "allowed_callers": ["code_execution_20260521"],
        "response_inclusion": "excluded",
    },
]

BETAS = [
    "compact-2026-01-12",
    "task-budgets-2026-03-13",
]
```

Two details worth calling out:

* **`code_execution_20260521`** uses a tool prompt that discloses the sandbox's per-cell wall-clock limit, so Claude breaks long-running searches into shorter cells instead of writing one big loop that times out.
* **`response_inclusion: "excluded"`** keeps `web_search` and `web_fetch` results inside the sandbox; everything else in the response (`thinking`, `text`, `server_tool_use`, code-execution results, `compaction`) round-trips with `model_dump()` in §3.

## 2. Thinking, effort, budget, and compaction

Four request-level parameters tell Claude *how hard to work* and *how to manage its own context*:

python

```
THINKING = {"type": "adaptive"}

OUTPUT_CONFIG = {
    "effort": "max",
    "task_budget": {"type": "tokens", "total": 3_000_000},
}

# Match the system-card configuration. To reproduce a different model's score,
# use the effort tier and compaction trigger from that model's model card.
COMPACTION_TRIGGER = 200_000

COMPACT_INSTRUCTIONS = (
    "Your summary MUST begin by restating the user's ORIGINAL QUESTION "
    "verbatim and in full, wrapped in <original_question> and "
    "</original_question> tags. Then summarize the research progress so "
    "far: key sources found, data extracted, partial answers, and what "
    "remains to be done. Do NOT call any tools. Your summary MUST also "
    "include this instruction verbatim: 'Provide your final answer "
    "wrapped in <result> and </result> tags.'"
)

CONTEXT_MANAGEMENT = {
    "edits": [
        {
            "type": "compact_20260112",
            "trigger": {"type": "input_tokens", "value": COMPACTION_TRIGGER},
            "instructions": COMPACT_INSTRUCTIONS,
        }
    ]
}
```

### Why `COMPACT_INSTRUCTIONS` matters so much

When the conversation reaches the trigger threshold, the API compacts it: a separate model call summarizes the history and the agent continues from the summary. The default summarization prompt is task-agnostic by design; it doesn't know that *for a benchmark*, the original question and the answer-format instruction are the two things that absolutely must survive. [Custom `instructions`](https://platform.claude.com/docs/en/build-with-claude/compaction#custom-summarization-instructions) are how you tell it.

Without them, the post-compaction agent has a summary of *what it found* but not *what it was asked*, and on long questions it frequently asks the user to restate the question, which scores zero.

The effect scales with how often compaction fires: it's largest at low triggers (where a single question may compact several times) and smaller at the 200K trigger used here, but it's the cheapest insurance in the harness either way.

> **Note**: the latest Claude model card reports DeepSearchQA *without* compaction (the model has a 1M-token context window, so a 1M-budget task fits in one window), while BrowseComp is reported *with* compaction at a 3M total budget. We use the 3M-budget BrowseComp configuration here so compaction is meaningful; on DeepSearchQA most questions still finish well under 1M and never trigger it.

The other three:

| Parameter | Why |
| --- | --- |
| `thinking: adaptive` | Lets Claude think between tool calls when the result is surprising, skip thinking when it isn't |
| `effort` | The model card numbers are reported at the model's highest effort tier |
| `task_budget.total` | Tells Claude its cumulative output budget across all turns and compactions, so it can pace itself instead of giving up early |

## 3. The round-trip loop

With server-side tools, each API call can run many tool iterations internally, then return with `stop_reason="pause_turn"` to checkpoint. Our job on the client is just: take the response content, append it as an assistant turn, and call again. We keep going until `stop_reason="end_turn"`.

One helper keeps the request body tidy across turns:

python

```
def truncate_to_last_compaction(messages: list[dict]) -> list[dict]:
    """Drop history that precedes the most recent compaction block.

    The server already discarded that history when it compacted; resending it is
    pure overhead and on long runs can exceed the 32 MB request-body limit.
    `messages[0]` (the original user prompt) is always kept so the request still
    starts with a user turn.
    """
    for mi in range(len(messages) - 1, 0, -1):
        content = messages[mi].get("content")
        if not isinstance(content, list):
            continue
        for bi in range(len(content) - 1, -1, -1):
            blk = content[bi]
            if isinstance(blk, dict) and blk.get("type") == "compaction":
                trimmed = {**messages[mi], "content": content[bi:]}
                return [messages[0], trimmed, *messages[mi + 1 :]]
    return messages
```

Now the loop itself. It's a single function, long but with every line doing something a real benchmark run needs:

python

```
def sample(question: str, *, max_turns: int = 100) -> dict:
    """Run one question to completion through the agentic search loop."""
    # cache_control on the user message turns on prompt caching for the whole
    # request, so the server-side tool loop caches between iterations.
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": USER_PROMPT_TEMPLATE.format(question=question),
                    "cache_control": {"type": "ephemeral"},
                }
            ],
        }
    ]
    request = {
        "model": MODEL,
        "max_tokens": 64_000,
        "tools": TOOLS,
        "betas": BETAS,
        "thinking": THINKING,
        "output_config": OUTPUT_CONFIG,
        "context_management": CONTEXT_MANAGEMENT,
        "messages": messages,
    }

    usage = {"input_tokens": 0, "output_tokens": 0, "cache_read_input_tokens": 0}
    transcript: list[str] = []
    tool_calls = 0
    start = time.time()

    for turn in range(max_turns):
        # Stream so the per-event read-timeout applies, not a per-response one.
        with client.beta.messages.stream(**request) as stream:
            response = stream.get_final_message()

        usage["input_tokens"] += response.usage.input_tokens
        usage["output_tokens"] += response.usage.output_tokens
        usage["cache_read_input_tokens"] += (
            getattr(response.usage, "cache_read_input_tokens", 0) or 0
        )
        tool_calls += sum(
            1 for b in response.content if getattr(b, "type", "") == "server_tool_use"
        )
        transcript.append(f"--- turn {turn} ---\n" + summarize_response(response))

        # Persist the code-execution container so state survives across turns.
        if getattr(response, "container", None) is not None:
            request["container"] = response.container.id

        # Round-trip: append assistant content, drop pre-compaction history.
        messages.append(
            {
                "role": "assistant",
                "content": [b.model_dump(exclude_none=True) for b in response.content],
            }
        )
        messages[:] = truncate_to_last_compaction(messages)

        if response.stop_reason == "end_turn":
            final_text = "".join(
                b.text for b in response.content if getattr(b, "type", "") == "text"
            )
            return {
                "text": final_text,
                "result": extract_result_tag(final_text),
                "turns": turn + 1,
                "tool_calls": tool_calls,
                "elapsed_s": time.time() - start,
                "usage": usage,
                "transcript": transcript,
            }
        if response.stop_reason not in ("pause_turn", "max_tokens"):
            raise RuntimeError(f"unexpected stop_reason={response.stop_reason}")

    raise RuntimeError(f"did not finish within {max_turns} turns")
```

### Retries

The SDK [retries automatically](https://platform.claude.com/docs/en/api/sdks/python#retries) on connection errors, `408`, `409`, `429`, and `≥500` responses with exponential backoff, and honors the `Retry-After` header the API sends on rate-limit responses. The default is 2 retries; for a full benchmark run we set `max_retries=20` on the client (in *Setup* above) so a brief overload mid-run doesn't score a question as zero.

> **Spotting silent tool throttling**: server-tool rate limits are separate from model token limits. Exhausting them does not raise an API error; the `too_many_requests` shows up as a tool-result error inside the response, and Claude usually retries in-sandbox. If a full-benchmark run scores unexpectedly low with no exceptions, check `result["transcript"]` for code-execution cells that print `rate_limit_error` or `too_many_requests`. The client-side fix is lower concurrency (or contact Anthropic support for higher tool rate limits); client retries won't help because the API call returned 200.
>
> Similarly, wrap each per-question `sample()` call in a `try/except` so a single `stop_reason="refusal"` or unrecoverable error scores that question as zero instead of aborting the whole run.

## 4. Run one question end-to-end

Let's run the first question. Expect this cell to take a minute or two: behind that single `stream()` call, Claude is writing and executing search code several times.

python

```
result = sample(SAMPLE_QUESTIONS[0]["problem"])

print(f"tool_calls={result['tool_calls']}  elapsed={result['elapsed_s']:.0f}s")
print(
    f"tokens: in={result['usage']['input_tokens']:,}  out={result['usage']['output_tokens']:,}  "
    f"cache_read={result['usage']['cache_read_input_tokens']:,}"
)
print()
print("Final <result>:", result["result"])
```

```
tool_calls=4  elapsed=56s
tokens: in=130  out=3,842  cache_read=39,703

Final <result>: **Jamie Dimon**, CEO of **JPMorgan Chase**, had held his CEO position the longest among the chief executives of the four largest US banks by total assets (JPMorgan Chase, Bank of America, Citigroup, and Wells Fargo) as of Q1 2024. Dimon became JPMorgan Chase's CEO on January 1, 2006 — roughly 18 years by Q1 2024 — compared to Brian Moynihan (Bank of America CEO since January 2010), Charles Scharf (Wells Fargo CEO since October 2019), and Jane Fraser (Citigroup CEO since March 2021).
```

The transcript shows the shape of the work. Each turn is a `pause_turn` checkpoint after a batch of in-sandbox tool calls:

python

```
for line in result["transcript"]:
    print(line + "\n")
```

```
--- turn 0 ---
  [thinking]  963 chars
  [text]      I'll research this step by step: first identifying the four largest US banks by total assets as of Q
  [tool_use]  code_execution
  [code_execution_tool_result]
  [thinking]  82 chars
  [tool_use]  code_execution
  [code_execution_tool_result]
  [thinking]  511 chars
  [tool_use]  code_execution
  [code_execution_tool_result]
  [thinking]  1365 chars
  [tool_use]  code_execution
  [code_execution_tool_result]
  [thinking]  700 chars
  [text]      Based on my research, I now have sufficient information to answer this question.  **Summary of findi
  [text]      "JPMorgan Chase & Co., the largest US bank by total assets, reported a sequential increase of $215.3
  [text]       were the other top banks, a ranking that held consistently across 2024.  Their respective CEOs and
  [text]      Dimon became CEO on January 1, 2006 and one year later also became Chairman of the Board.
  [text]        2. **Bank of America – Brian Moynihan**:
  [text]      Moynihan took office on January 1, 2010, and also is a member of the Bank of America board of direct
  [text]        3. **Wells Fargo – Charles Scharf**:
  [text]      The current CEO and President is Charles W. Scharf, appointed in September 2019
  [text]      , with his effective start date being October 21, 2019 according to Wells Fargo's official announcem
  [text]      Jane Fraser is a British-American banking executive who has been chief executive officer (CEO) of Ci
  [text]      , becoming the first woman to lead a major U.S. bank.  Comparing the start dates — 2006 for Dimon, 2
  usage: in=130 out=3,842 cache_read=39,703 stop=end_turn
```

## 5. Grading

Benchmark scoring uses a model-as-judge F1 grader. The grader sees the question, the gold answer, and the extracted `<result>` text, then reports which gold items were found and which extra items appeared that aren't in the gold set. From that we compute precision, recall, and F1.

Two things to get right:

* **Grade the `<result>` tag, not the whole response.** The full response includes planning prose and search summaries; feeding that to the grader inflates both false positives and false negatives. `extract_result_tag()` pulls out just the final answer.
* **Hold the grader model fixed.** We use `GRADER_MODEL = "claude-opus-4-6"` regardless of `MODEL`. Grading with the model under test makes scores incomparable across models.

The grader prompt is straightforward:

```
Your task is to evaluate whether a given response arrived at the correct answer.

Question: <question>\{question}</question>
Correct answer (type: \{answer_type}): <correct_answer>\{answer}</correct_answer>
Response to evaluate: <response>\{response}</response>

For each expected answer item, indicate whether it appears in the response.
Then list any answers in the response that are NOT in the correct-answer list.
Wording does not need to match exactly.

Reply in this exact XML format:
<evaluation>
  <explanation>one sentence</explanation>
  <correctness_details>
    <item answer="expected_item_1" correct="true|false"/>
  </correctness_details>
  <excessive_answers>
    <item>extra_item_if_any</item>
  </excessive_answers>
</evaluation>
```

Parsing and the precision/recall/F1 arithmetic live in [`utils/agentic_search.py`](https://github.com/anthropics/claude-cookbooks/blob/main/evals/agentic_search/utils/agentic_search.py); here we just call it:

python

```
grade = grade_response(client, GRADER_MODEL, SAMPLE_QUESTIONS[0], result["text"])
print(f"answer    : {grade['extracted_answer']}")
print(f"precision : {grade['precision']:.2f}")
print(f"recall    : {grade['recall']:.2f}")
print(f"F1        : {grade['f1']:.2f}")
```

```
answer    : **Jamie Dimon**, CEO of **JPMorgan Chase**, had held his CEO position the longest among the chief executives of the four largest US banks by total assets (JPMorgan Chase, Bank of America, Citigroup, and Wells Fargo) as of Q1 2024. Dimon became JPMorgan Chase's CEO on January 1, 2006 — roughly 18 years by Q1 2024 — compared to Brian Moynihan (Bank of America CEO since January 2010), Charles Scharf (Wells Fargo CEO since October 2019), and Jane Fraser (Citigroup CEO since March 2021).
precision : 1.00
recall    : 1.00
F1        : 1.00
```

## 6. Run the demo set

Now all three questions, with usage and F1 in a comparison table. (To run the full 900-question benchmark, replace `SAMPLE_QUESTIONS` with the full dataset and add concurrency; see *Next steps*.)

python

```
rows = []
for q in SAMPLE_QUESTIONS:
    r = sample(q["problem"])
    g = grade_response(client, GRADER_MODEL, q, r["text"])
    rows.append(
        {
            "id": q["example_id"],
            "tool_calls": r["tool_calls"],
            "in_tokens": r["usage"]["input_tokens"],
            "out_tokens": r["usage"]["output_tokens"],
            "f1": g["f1"],
            "answer": g["extracted_answer"][:60],
        }
    )

df = pd.DataFrame(rows)
print(df.to_string(index=False))
print(f"\nMean F1: {df['f1'].mean():.2f}")
# in_tokens is the uncached billed input; with caching on, most of the actual
# context is cache reads (tracked separately in usage.cache_read_input_tokens).
print(f"Total tokens: {df['in_tokens'].sum():,} in / {df['out_tokens'].sum():,} out")
```

```
id  tool_calls  in_tokens  out_tokens  f1                                                        answer
demo-0          11        312       10503 1.0  **Jamie Dimon**, CEO of **JPMorgan Chase** (the largest US b
demo-1           7        208        9768 1.0  The three countries with the largest installed offshore wind
demo-2           3        104        1592 1.0 - **2021**: *Titane* — directed by Julia Ducournau\n- **2022*

Mean F1: 1.00
Total tokens: 624 in / 21,863 out
```

## 7. Scaling to the full benchmark

Running this notebook's configuration over the full DeepSearchQA-900 and BrowseComp-1266 sets reproduces the published model-card scores. For published agentic-search scores across models, see the per-model [Claude model cards](https://www.anthropic.com/system-cards).

## 8. Adapting to BrowseComp

BrowseComp questions are single-answer ("Which 1995 film…") rather than set-valued, so the only harness change is the grader:

python

```
from utils.agentic_search import grade_browsecomp

# Grading: a single-letter judge (A=correct, B=incorrect, C=abstain).
# accuracy = fraction of "A" verdicts.
bc_grade = grade_browsecomp(client, GRADER_MODEL, SAMPLE_QUESTIONS[0], result["text"])
print(bc_grade)
```

```
{'example_id': 'demo-0', 'extracted_answer': "**Jamie Dimon**, CEO of **JPMorgan Chase**, had held his CEO position the longest among the chief executives of the four largest US banks by total assets (JPMorgan Chase, Bank of America, Citigroup, and Wells Fargo) as of Q1 2024. Dimon became JPMorgan Chase's CEO on January 1, 2006 — roughly 18 years by Q1 2024 — compared to Brian Moynihan (Bank of America CEO since January 2010), Charles Scharf (Wells Fargo CEO since October 2019), and Jane Fraser (Citigroup CEO since March 2021).", 'grader_letter': 'A', 'accuracy': 1.0}
```

Tools, betas, and the `sample()` loop are unchanged. Check the model card for the exact effort tier and compaction trigger BrowseComp was reported at if you want a strict reproduction; the §2 values are a good default.

That's the point: once the loop is right, swapping benchmarks is a dataset, a few config lines, and a grader.

## Recap

You built an agentic search loop that:

* Calls `web_search` and `web_fetch` **programmatically from code execution**, so 50+ page fetches don't flood the context (§1).
* Tells Claude **how hard to work** (`effort`, `task_budget`) and **how to think** (`adaptive`) (§2).
* Survives compaction by **restating the question in the compaction prompt**, the single biggest lever at high compaction frequency (§2).
* Round-trips `pause_turn` responses correctly, persisting the code container and trimming pre-compaction history (§3).
* Grades with a model-as-judge F1 grader and reproduces the published DeepSearchQA score (§5–7).

## Next steps

* **Scale to the full benchmark**: wrap `sample()` in a `concurrent.futures.ThreadPoolExecutor` (the client is thread-safe); the SDK's built-in retry already covers 429/529. At concurrency 50, DeepSearchQA-900 finishes in roughly 2 hours.
* **Try the multi-agent variant**: the [Async Multi-Agent Orchestration cookbook](https://platform.claude.com/cookbook/patterns-agents-async-multi-agent-orchestration) shows how an N-agent team can exceed this single-agent loop's accuracy at lower latency.
* **Port to your own benchmark**: the contract is `[{problem, answer, answer_type}]` rows, a few config lines, and a grader function. The loop doesn't change.
* **Read the model cards**: the per-model [Claude model cards](https://www.anthropic.com/system-cards) document the configuration each published benchmark number was produced with.
