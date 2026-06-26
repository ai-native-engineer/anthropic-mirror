<!-- source: https://platform.claude.com/docs/en/managed-agents/define-outcomes -->

# Define outcomes
Tell the agent what 'done' looks like, and let it iterate until it gets there.
The `outcome` elevates a session from _conversation_ to _work_. You define what the end result should look like and how to measure quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.
When you define an outcome, the harness automatically provisions a _grader_ to evaluate the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices.
The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric. That feedback is handed back to the agent for the next iteration.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a rubric
A rubric is a markdown document describing per-criterion scoring. The rubric is required.
### Tips for writing effective rubrics
Example rubric:

# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
- Growth rate assumptions are explicitly stated and reasonable

## Cost Structure
- COGS and operating expenses are modeled separately
- Margins are consistent with historical trends or deviations are justified

## Discount Rate
- WACC is calculated with stated assumptions for cost of equity and cost of debt
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Terminal Value
- Uses either perpetuity growth or exit multiple method (stated which)
- Terminal growth rate does not exceed long-term GDP growth

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
- Key assumptions are on a separate "Assumptions" sheet
- Sensitivity analysis on WACC and terminal growth rate is included

Pass the rubric as inline text on `user.define_outcome` (see the next section), or upload it through the Files API for reuse across sessions.
Uploading through the Files API requires both the `managed-agents-2026-04-01` and `files-api-2025-04-14` beta headers.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

rubric = client.beta.files.upload(file=Path("/tmp/rubric.md"))
print(f"Uploaded rubric: {rubric.id}")

Create a session with an outcome
After creating a session, send a `user.define_outcome` event. The agent begins work immediately; no additional user message event is required.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a session
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Financial analysis on Costco",
)

# Define the outcome — agent starts working on receipt
client.beta.sessions.events.send(
    session_id=session.id,
    events=[
            "type": "user.define_outcome",
            "description": "Build a DCF model for Costco in .xlsx",
            "rubric": {"type": "text", "content": RUBRIC},
            # or: "rubric": {"type": "file", "file_id": rubric.id},
            "max_iterations": 5,  # optional; default 3, max 20
    ],
)

Outcome events
Progress on an outcome-oriented session is surfaced on the events [stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming).
  * `agent.*` events (such as messages and tool use) show progress toward the outcome.
  * `span.outcome_evaluation_*` events are only emitted for outcome-oriented sessions and show the number of iteration loops and the grader's feedback process.
  * You can also send `user.message` [events](https://platform.claude.com/docs/en/managed-agents/reference#event-types) to an outcome-oriented session to direct the agent's work as it progresses, but it isn't required: the agent works toward the outcome on its own, iterating until it succeeds or runs out of iterations.
  * A `user.interrupt` event pauses work on the current outcome and marks the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.
  * After the final outcome evaluation, the session can be continued as a conversational session, or a new outcome can be kicked off. The session retains history of the prior outcome.

### 
Define outcome user event
Only one outcome is supported at a time, but you may chain outcomes in sequence. To do this, send a new `user.define_outcome` event after the terminal event of the previous outcome.
This is the event you send to initiate an outcome. It is echoed back on receipt, including a `processed_at` timestamp and `outcome_id`.

  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": { "type": "file", "file_id": "file_01..." },
  "max_iterations": 5

### 
Outcome evaluation start
Emitted once the grader starts an evaluation over one iteration loop. The `iteration` field is a 0-indexed revision counter: `0` is the first evaluation, `1` is the re-evaluation after the first revision, and so on.

  "type": "span.outcome_evaluation_start",
  "id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:01:45Z"

### 
Outcome evaluation ongoing
Heartbeat emitted while the grader runs. The grader's internal reasoning is opaque: you see that it's working, not what it's thinking.

  "type": "span.outcome_evaluation_ongoing",
  "id": "sevt_01ghi...",
  "outcome_id": "outc_01a...",
  "processed_at": "2026-03-25T14:02:10Z"

### 
Outcome evaluation end
Emitted after the grader finishes evaluating one iteration. The `result` field indicates what happens next.  
| Result  | Next  |  
| --- | --- |  
| `satisfied`  | Session transitions to `idle`.  |  
| `needs_revision`  | Agent starts a new iteration cycle.  |  
| `max_iterations_reached`  | No further evaluation cycles. The agent may run one final revision before the session transitions to `idle`.  |  
| `failed`  | Session transitions to `idle`. Returned when the rubric fundamentally does not match the task, for example if the description and rubric contradict each other.  |  
| `interrupted`  | Only emitted if `outcome_evaluation_start` already fired before the interrupt.  |  

  "type": "span.outcome_evaluation_end",
  "id": "sevt_01jkl...",
  "outcome_evaluation_start_id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated, sensitivity table is included...",
  "iteration": 0,
  "usage": {
    "input_tokens": 2400,
    "output_tokens": 350,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 1800
  "processed_at": "2026-03-25T14:03:00Z"

Checking on outcome status
You can either listen on the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for `span.outcome_evaluation_end`, or poll `GET /v1/sessions/:id` and read `outcome_evaluations[].result`:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.retrieve(session.id)

for outcome in session.outcome_evaluations:
    print(f"{outcome.outcome_id}: {outcome.result}")
    # outc_01a...: satisfied

Retrieving deliverables
The agent writes output files to `/mnt/session/outputs/` inside the sandbox. Once the session is idle, fetch them through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) scoped to the session:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List files produced by this session
files = client.beta.files.list(scope_id=session.id)
for f in files:
    print(f.id, f.filename)

# Download a file
if files.data:
    content = client.beta.files.download(files.data[0].id)
    content.write_to_file("/tmp/output.txt")

  * [Create a rubric](https://platform.claude.com/docs/en/managed-agents/define-outcomes#create-a-rubric)
  * [Create a session with an outcome](https://platform.claude.com/docs/en/managed-agents/define-outcomes#create-a-session-with-an-outcome)
  * [Outcome events](https://platform.claude.com/docs/en/managed-agents/define-outcomes#outcome-events)
  * [Define outcome user event](https://platform.claude.com/docs/en/managed-agents/define-outcomes#define-outcome-user-event)
  * [Outcome evaluation start](https://platform.claude.com/docs/en/managed-agents/define-outcomes#outcome-evaluation-start)
  * [Outcome evaluation ongoing](https://platform.claude.com/docs/en/managed-agents/define-outcomes#outcome-evaluation-ongoing)
  * [Outcome evaluation end](https://platform.claude.com/docs/en/managed-agents/define-outcomes#outcome-evaluation-end)
  * [Checking on outcome status](https://platform.claude.com/docs/en/managed-agents/define-outcomes#checking-on-outcome-status)
  * [Retrieving deliverables](https://platform.claude.com/docs/en/managed-agents/define-outcomes#retrieving-deliverables)

Managed Agents/Delegate work to your agent
# Define outcomes
Tell the agent what 'done' looks like, and let it iterate until it gets there.
The `outcome` elevates a session from _conversation_ to _work_. You define what the end result should look like and how to measure quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.
When you define an outcome, the harness automatically provisions a _grader_ to evaluate the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices.
The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric. That feedback is handed back to the agent for the next iteration.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a rubric
A rubric is a markdown document describing per-criterion scoring. The rubric is required.
### Tips for writing effective rubrics
Example rubric:

# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
- Growth rate assumptions are explicitly stated and reasonable

## Cost Structure
- COGS and operating expenses are modeled separately
- Margins are consistent with historical trends or deviations are justified

## Discount Rate
- WACC is calculated with stated assumptions for cost of equity and cost of debt
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Terminal Value
- Uses either perpetuity growth or exit multiple method (stated which)
- Terminal growth rate does not exceed long-term GDP growth

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
- Key assumptions are on a separate "Assumptions" sheet
- Sensitivity analysis on WACC and terminal growth rate is included

Pass the rubric as inline text on `user.define_outcome` (see the next section), or upload it through the Files API for reuse across sessions.
Uploading through the Files API requires both the `managed-agents-2026-04-01` and `files-api-2025-04-14` beta headers.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

rubric = client.beta.files.upload(file=Path("/tmp/rubric.md"))
print(f"Uploaded rubric: {rubric.id}")

Create a session with an outcome
After creating a session, send a `user.define_outcome` event. The agent begins work immediately; no additional user message event is required.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a session
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Financial analysis on Costco",
)

# Define the outcome — agent starts working on receipt
client.beta.sessions.events.send(
    session_id=session.id,
    events=[
            "type": "user.define_outcome",
            "description": "Build a DCF model for Costco in .xlsx",
            "rubric": {"type": "text", "content": RUBRIC},
            # or: "rubric": {"type": "file", "file_id": rubric.id},
            "max_iterations": 5,  # optional; default 3, max 20
    ],
)

Outcome events
Progress on an outcome-oriented session is surfaced on the events [stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming).
  * `agent.*` events (such as messages and tool use) show progress toward the outcome.
  * `span.outcome_evaluation_*` events are only emitted for outcome-oriented sessions and show the number of iteration loops and the grader's feedback process.
  * You can also send `user.message` [events](https://platform.claude.com/docs/en/managed-agents/reference#event-types) to an outcome-oriented session to direct the agent's work as it progresses, but it isn't required: the agent works toward the outcome on its own, iterating until it succeeds or runs out of iterations.
  * A `user.interrupt` event pauses work on the current outcome and marks the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.
  * After the final outcome evaluation, the session can be continued as a conversational session, or a new outcome can be kicked off. The session retains history of the prior outcome.

### 
Define outcome user event
Only one outcome is supported at a time, but you may chain outcomes in sequence. To do this, send a new `user.define_outcome` event after the terminal event of the previous outcome.
This is the event you send to initiate an outcome. It is echoed back on receipt, including a `processed_at` timestamp and `outcome_id`.

  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": { "type": "file", "file_id": "file_01..." },
  "max_iterations": 5

### 
Outcome evaluation start
Emitted once the grader starts an evaluation over one iteration loop. The `iteration` field is a 0-indexed revision counter: `0` is the first evaluation, `1` is the re-evaluation after the first revision, and so on.

  "type": "span.outcome_evaluation_start",
  "id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:01:45Z"

### 
Outcome evaluation ongoing
Heartbeat emitted while the grader runs. The grader's internal reasoning is opaque: you see that it's working, not what it's thinking.

  "type": "span.outcome_evaluation_ongoing",
  "id": "sevt_01ghi...",
  "outcome_id": "outc_01a...",
  "processed_at": "2026-03-25T14:02:10Z"

### 
Outcome evaluation end
Emitted after the grader finishes evaluating one iteration. The `result` field indicates what happens next.  
| Result  | Next  |  
| --- | --- |  
| `satisfied`  | Session transitions to `idle`.  |  
| `needs_revision`  | Agent starts a new iteration cycle.  |  
| `max_iterations_reached`  | No further evaluation cycles. The agent may run one final revision before the session transitions to `idle`.  |  
| `failed`  | Session transitions to `idle`. Returned when the rubric fundamentally does not match the task, for example if the description and rubric contradict each other.  |  
| `interrupted`  | Only emitted if `outcome_evaluation_start` already fired before the interrupt.  |  

  "type": "span.outcome_evaluation_end",
  "id": "sevt_01jkl...",
  "outcome_evaluation_start_id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated, sensitivity table is included...",
  "iteration": 0,
  "usage": {
    "input_tokens": 2400,
    "output_tokens": 350,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 1800
  "processed_at": "2026-03-25T14:03:00Z"

Checking on outcome status
You can either listen on the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for `span.outcome_evaluation_end`, or poll `GET /v1/sessions/:id` and read `outcome_evaluations[].result`:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.retrieve(session.id)

for outcome in session.outcome_evaluations:
    print(f"{outcome.outcome_id}: {outcome.result}")
    # outc_01a...: satisfied

Retrieving deliverables
The agent writes output files to `/mnt/session/outputs/` inside the sandbox. Once the session is idle, fetch them through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) scoped to the session:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List files produced by this session
files = client.beta.files.list(scope_id=session.id)
for f in files:
    print(f.id, f.filename)

# Download a file
if files.data:
    content = client.beta.files.download(files.data[0].id)
    content.write_to_file("/tmp/output.txt")
