<!-- source: https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example -->

# Build an orchestration mode
Build a session-level mode that grants standing consent for multi-agent fan-out, switched on and off with mid-conversation system messages.
An orchestration mode is a session-level switch: when it is on, the model puts maximum thoroughness behind every substantive request, scouting the task itself and then fanning work out to parallel subagents by default. When it is off, the same orchestration tool goes back to per-request opt-in.
The mode is not an API parameter. It is built entirely from documented pieces:
  1. **An effort level:** requests run at a documented [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) value such as `xhigh`. There is no hidden level above the ones on that page.
  2. **A mode reminder:** a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) tells the model the mode is active, with a one-line refresher every several turns and an exit notice when the mode is turned off. The top-level `system` field never changes, so the cached prefix stays intact.
  3. **Standing consent in the tool description:** the orchestration tool's description states that while the mode is on, the model should author and run a workflow for every substantive task without asking first.

This example uses mid-conversation system messages, which are currently available on Claude Opus 4.8 only. The fan-out itself multiplies token usage: a single request can spawn many subagent conversations, so reserve the mode for work that justifies the cost.
Set up the loop
The example is a single file. The constants control the effort level, the fan-out shape, and how often the mode refresher is re-sent. `MAX_CONCURRENT` caps how many subagents run at the same time (the PHP port is sequential and ignores it); `MAX_TOTAL_SUBTASKS` caps how many the model may queue in a single Workflow call. Splitting the two lets the model plan a large backlog without launching it all at once. The `DOC_TEST_MODE` check caps the loops to a single turn when that environment variable is set, so the automated docs harness can validate that the file compiles and finishes quickly without running the full orchestration; leave it unset when running the example yourself.
PythonTypeScriptC#GoJavaPHPRuby

import atexit
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading

import anthropic

client = anthropic.Anthropic()

MODEL = "claude-opus-4-8"
EFFORT = "xhigh"

SYSTEM_PROMPT = "You are a helpful general-purpose agent. Answer the user's request directly."

REQUEST_TIMEOUT_SECONDS = 600
BASH_TIMEOUT_SECONDS = 60
TOOL_RESULT_MAX_CHARS = 8000
MAX_CONCURRENT = 10
DOC_TEST_MODE = bool(os.environ.get("DOC_TEST_MODE"))
MAX_TOTAL_SUBTASKS = 2 if DOC_TEST_MODE else 200
MAX_SUBAGENT_TURNS = 1 if DOC_TEST_MODE else 15
MAX_MAIN_TURNS = 1 if DOC_TEST_MODE else 30
TURNS_BETWEEN_REFRESHERS = 10
JOURNAL_PATH = os.environ.get("ORCH_JOURNAL") or "orchestration_journal.json"

Define the mode reminders
The reminders are short on purpose. They flip the mode and point at the tool description, where the heavyweight instructions live. The full text is sent once when the mode turns on, the refresher is re-sent only after several user turns, and the exit notice is sent once when the mode turns off.
PythonTypeScriptC#GoJavaPHPRuby

MODE_ENTER = (
    "Orchestration mode is on: optimize for the most exhaustive, correct answer rather than "
    "the fastest one. Use the Workflow tool on every substantive task, sized to the problem's "
    "natural decomposition rather than the maximum the tool allows. See the Workflow tool's "
    "description for standing consent, granularity guidance, and quality patterns. Work solo "
    "only on conversational or trivial turns."
)
MODE_REFRESH = (
    "Orchestration mode is still on. Use the Workflow tool; see its standing consent section."
)
MODE_EXIT = (
    "Orchestration mode is off. The Workflow tool's standard opt-in rule applies again."
)

Grant standing consent in the tool description
The Workflow tool carries the real behavioral contract: the opt-in rule, the standing consent that applies while the mode is on, granularity guidance for sizing the fan-out, and the quality patterns the model can reach for (a verification wave, a completeness critic, multi-phase sequencing). Subagents also get a `report_findings` tool so their results come back as structured JSON instead of prose, and the bash tool is the Anthropic-defined `bash_20250124` tool run locally.
PythonTypeScriptC#GoJavaPHPRuby

WORKFLOW_TOOL = {
    "name": "Workflow",
    "description": (
        "Orchestrate a multi-agent workflow: split a large task into independent subtasks "
        "and run them as parallel agents, then collect their results.\n\n"
        "Opt-in: only use this tool when the user explicitly asks for a workflow, or when a "
        "system message confirms that orchestration mode is on.\n\n"
        "Quality patterns: adversarial verification (a second wave of agents checks the first "
        "wave's findings against the source), a completeness critic (one agent hunts for what "
        "the others missed), and multi-phase sequencing (understand, design, implement, and "
        "review as separate workflow calls, reading results between phases). A useful default "
        "is hybrid: scout inline first to discover the work-list, then fan out over it.\n\n"
        "Granularity: scope each subtask to a distinct concern, component, or question rather "
        "than per line or per file section. Scale the count to what the user asked for: a "
        "focused review of a module of a few hundred lines rarely needs more than about ten "
        "subtasks; a broad audit of a large codebase can justify more.\n\n"
        "Standing consent: while a system message confirms orchestration mode is on, that "
        "opt-in is standing. Author and run a workflow for every substantive task by default, "
        "and lean toward verifying findings adversarially. Work solo only on conversational "
        "turns or trivial mechanical edits. When a system message says the mode is off, "
        "revert to the opt-in rule above."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "subtasks": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Independent subtask prompts to run as parallel agents",
        "required": ["subtasks"],

BASH_TOOL = {"type": "bash_20250124", "name": "bash"}

REPORT_TOOL = {
    "name": "report_findings",
    "description": (
        "Report the final findings for your subtask. Call this exactly once, when you are "
        "done investigating; it ends your task."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "summary": {"type": "string", "description": "Two or three sentences of synthesis"},
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "claim": {"type": "string", "description": "The finding, one sentence"},
                        "evidence": {
                            "type": "string",
                            "description": "How it was verified (file, line, or command output)",
                        "severity": {"type": "string", "enum": ["high", "medium", "low", "info"]},
                    "required": ["claim", "evidence", "severity"],
        "required": ["summary", "findings"],

Run the bash tool locally
The bash handler runs the requested command with a timeout, captures combined stdout and stderr, and truncates the result so a runaway command can't flood the context window. Commands run in the directory you launch the example from, so pointing it at a project means starting it there; when `DOC_TEST_MODE` is set, the harness instead gives bash a small throwaway fixture directory that is removed on exit. There is no sandbox here: the command runs with the permissions of the process that launched the example. For clarity this example runs each call in a fresh subshell rather than maintaining the persistent session the `bash_20250124` contract describes; a production agent should back the tool with a long-lived shell so that working directory, environment, and the `restart` action behave as documented.
PythonTypeScriptC#GoJavaPHPRuby

# Run bash where the example was launched. In DOC_TEST_MODE the docs harness
# points it at a throwaway fixture directory instead, removed on exit.
if DOC_TEST_MODE:
    WORK_DIR = tempfile.mkdtemp(prefix="orchestration-")
    atexit.register(shutil.rmtree, WORK_DIR, ignore_errors=True)
    with open(os.path.join(WORK_DIR, "sample.py"), "w") as fixture:
        fixture.write(
            "def fib(n):\n"
            "    return n if n < 2 else fib(n - 1) + fib(n - 2)\n\n"
            "print(fib(10))\n"
        )
else:
    WORK_DIR = os.getcwd()

def run_bash(command: str) -> tuple[str, bool]:
    """Run a shell command and return (output, is_error). No sandbox: example code only."""
    print(f"[bash] {command}", file=sys.stderr)
    try:
        proc = subprocess.run(
            ["bash", "-c", command],
            cwd=WORK_DIR,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=BASH_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return f"command timed out after {BASH_TIMEOUT_SECONDS}s", True
    output = (proc.stdout + proc.stderr).strip() or "(no output)"
    if len(output) > TOOL_RESULT_MAX_CHARS:
        output = output[:TOOL_RESULT_MAX_CHARS] + f"\n(truncated at {TOOL_RESULT_MAX_CHARS} chars)"
    if proc.returncode != 0:
        output = f"(exit code {proc.returncode})\n{output}"
    return output, proc.returncode != 0

def handle_bash_block(block) -> tuple[str, bool]:
    if block.input.get("restart") is True:
        return "Shell restarted.", False
    command = block.input.get("command")
    if not isinstance(command, str) or not command:
        return "bash error: no command was provided.", True
    return run_bash(command)

Run one subagent
Each workflow subtask becomes its own small agent loop with the bash tool, running at the same effort as the main loop. A per-request timeout bounds each API call so a dropped connection degrades one subagent instead of stalling the whole run.
PythonTypeScriptC#GoJavaPHPRuby

def run_subagent(model: str, prompt: str) -> str:
    """One subagent: a small nested agent loop with the bash tool plus report_findings.
    Subagents inherit the main loop's effort level."""
    subagent_system = (
        "You are one agent in a larger parallel fan-out, assigned a single subtask. "
        "Investigate it directly, using bash to check facts rather than guessing, and finish "
        "by calling report_findings exactly once. Return findings, not narration."
    )
    messages = [{"role": "user", "content": prompt}]
    for _ in range(MAX_SUBAGENT_TURNS):
        with client.messages.stream(
            model=model,
            max_tokens=64000,
            system=subagent_system,
            thinking={"type": "adaptive"},
            output_config={"effort": EFFORT},
            tools=[BASH_TOOL, REPORT_TOOL],
            messages=messages,
            timeout=REQUEST_TIMEOUT_SECONDS,
        ) as stream:
            response = stream.get_final_message()
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "pause_turn":
            continue
        if response.stop_reason != "tool_use":
            text = "".join(block.text for block in response.content if block.type == "text")
            if response.stop_reason == "max_tokens":
                text += "\n\n(warning: subagent response was truncated at max_tokens)"
            return text
        tool_results = []
        report = None
        for block in response.content:
            if block.type != "tool_use":
                continue
            if block.name == "report_findings":
                report = json.dumps(block.input, indent=2)
                output, is_error = "Findings recorded.", False
            elif block.name == "bash":
                output, is_error = handle_bash_block(block)
            else:
                output, is_error = f"unknown tool: {block.name}", True
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                    "is_error": is_error,
            )
        if report is not None:
            return report
        messages.append({"role": "user", "content": tool_results})
    return "(subagent hit the turn limit before finishing)"

Journal results so reruns resume
A fan-out that spawns dozens of subagents is expensive to restart from scratch. A small content-addressed journal makes it idempotent: before dispatching a subagent, look up the SHA-256 of its prompt in a local JSON file, and return the recorded result if one exists. Interrupt the run, rerun it, and only the subtasks that never finished are recomputed. The journal deduplicates across runs, not within a single fan-out wave; delete the journal file to start fresh.
PythonTypeScriptC#GoJavaPHPRuby

_journal_lock = threading.Lock()

def _load_journal() -> dict:
    try:
        with open(JOURNAL_PATH) as file:
            return json.load(file) or {}
    except (OSError, json.JSONDecodeError):
        return {}

def journaled(prompt: str, compute) -> str:
    """Return a cached result for this exact prompt, or compute and persist it. This
    makes the fan-out resumable: interrupt the run, rerun it, and only the subtasks
    that never finished are recomputed. Delete the journal file to start fresh."""
    key = hashlib.sha256(prompt.encode()).hexdigest()
    cached = _load_journal().get(key)
    if cached is not None:
        print(f"[journal] cache hit for {key[:12]}", file=sys.stderr)
        return cached
    result = compute()
    try:
        with _journal_lock:  # fan-out writes from many threads
            journal = _load_journal()
            journal[key] = result
            temp = f"{JOURNAL_PATH}.tmp"
            with open(temp, "w") as file:
                json.dump(journal, file)
            os.replace(temp, JOURNAL_PATH)  # atomic on POSIX and Windows
    except OSError as error:  # the journal is best-effort; never discard a computed result
        print(f"[journal] write failed: {error}", file=sys.stderr)
    return result

Fan out, then verify
The fan-out accepts up to `MAX_TOTAL_SUBTASKS` prompts, runs them through the journal with at most `MAX_CONCURRENT` in flight (sequential in the PHP port), and isolates failures so one broken subagent degrades to an error string instead of ending the run. Once the first wave finishes, a second wave reuses the same subagent path to try to refute each result: every verifier re-derives the claims from the source, defaulting to refuted when uncertain. Both the original result and its verdict are returned to the orchestrator so it can weigh them together.
PythonTypeScriptC#GoJavaPHPRuby

def normalize_subtasks(raw) -> list[str]:
    """Accept the subtasks input in whatever shape the model emits: an array, the array
    JSON-encoded as a single string, or a newline-separated list."""
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError:
            raw = raw.splitlines() if "\n" in raw else [raw]
    if not isinstance(raw, list):
        return []
    return [task.strip() for task in raw if isinstance(task, str) and task.strip()]

def verify_prompt_for(subtask: str, result: str) -> str:
    return (
        "Adversarially verify the subagent result below: try to REFUTE it. Re-derive the "
        "claims yourself with bash rather than trusting the result, and look for evidence "
        "that contradicts them. Default to refuted if uncertain. Call report_findings with "
        "summary 'refuted: <why>' or 'confirmed: <why>', citing the file:line or command "
        "output that decided it.\n\n"
        f"Subtask: {subtask}\n\nResult to verify:\n{result}"
    )

def run_workflow(model: str, raw_subtasks) -> tuple[str, bool]:
    """Run subtasks as parallel subagents, then run a second verification wave over
    the results, and return both. MAX_TOTAL_SUBTASKS bounds how many the model can
    queue; MAX_CONCURRENT bounds how many run at once."""
    all_subtasks = normalize_subtasks(raw_subtasks)
    subtasks = all_subtasks[:MAX_TOTAL_SUBTASKS]
    dropped = len(all_subtasks) - len(subtasks)
    if not subtasks:
        return "Workflow error: no usable subtasks were provided.", True
    print(f"[workflow] fanning out {len(subtasks)} agents", file=sys.stderr)

    def run_one(prompt: str) -> str:
        try:
            return journaled(prompt, lambda: run_subagent(model, prompt))
        except Exception as error:  # isolation boundary: one bad subagent should not end the run
            return f"(subagent failed: {type(error).__name__}: {error})"

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as pool:
        results = list(pool.map(run_one, subtasks))
        print(f"[workflow] verifying {len(results)} results", file=sys.stderr)
        verify_prompts = [verify_prompt_for(task, result) for task, result in zip(subtasks, results)]
        verdicts = list(pool.map(run_one, verify_prompts))

    joined = "\n\n".join(
        f"[agent {index + 1}: {task}]\n{result}\n\n[verify {index + 1}]\n{verdict}"
        for index, (task, result, verdict) in enumerate(zip(subtasks, results, verdicts))
    )
    if dropped > 0:
        joined = (
            f"(note: {dropped} subtasks beyond MAX_TOTAL_SUBTASKS={MAX_TOTAL_SUBTASKS} were not "
            "run; rerun them in a follow-up Workflow call)\n\n" + joined
        )
    return joined, False

Toggle the mode with mid-conversation system messages
The agent appends the user's message first, then any system messages that are due: the exit notice, the full mode text on entry, or the periodic refresher. Placing the system message after the user turn keeps every cached byte ahead of it untouched, and satisfies the placement rule that a system message follows a user turn.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

class ModeAgent:
    """An agent loop whose orchestration mode is toggled with mid-conversation system messages."""

    def __init__(self, model: str, mode_on: bool = True):
        self.model = model
        self.mode_on = mode_on
        self.messages: list[dict] = []
        self._mode_announced = False
        self._exit_pending = False
        self._turns_since_reminder = 0

    def set_mode(self, mode_on: bool) -> None:
        """Turn the mode on or off. The notice is delivered with the next user turn."""
        if mode_on == self.mode_on:
            return
        if not mode_on:
            if self._mode_announced:
                self._exit_pending = True
        else:
            self._exit_pending = False
        self.mode_on = mode_on

    def _due_system_messages(self) -> list[dict]:
        """System messages owed on this turn: an exit notice, the full mode text on entry,
        or a one-line refresher every TURNS_BETWEEN_REFRESHERS user turns."""
        due = []
        if self._exit_pending:
            self._exit_pending = False
            self._mode_announced = False
            due.append({"role": "system", "content": MODE_EXIT})
        if self.mode_on:
            if not self._mode_announced:
                self._mode_announced = True
                self._turns_since_reminder = 0
                due.append({"role": "system", "content": MODE_ENTER})
            elif self._turns_since_reminder >= TURNS_BETWEEN_REFRESHERS:
                self._turns_since_reminder = 0
                due.append({"role": "system", "content": MODE_REFRESH})
        return due

    def turn(self, user_input: str) -> str:
        # Mid-conversation system messages follow the user turn they apply to, which keeps
        # the cached prefix ahead of them untouched.
        self.messages.append({"role": "user", "content": user_input})
        self.messages.extend(self._due_system_messages())
        self._turns_since_reminder += 1

        for _ in range(MAX_MAIN_TURNS):
            with client.messages.stream(
                model=self.model,
                max_tokens=64000,
                system=SYSTEM_PROMPT,  # static for the whole session
                thinking={"type": "adaptive"},
                output_config={"effort": EFFORT},
                tools=[WORKFLOW_TOOL, BASH_TOOL],
                messages=self.messages,
                timeout=REQUEST_TIMEOUT_SECONDS,
            ) as stream:
                response = stream.get_final_message()
            self.messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "pause_turn":
                continue
            if response.stop_reason != "tool_use":
                text = "".join(block.text for block in response.content if block.type == "text")
                if response.stop_reason == "max_tokens":
                    # Drop the truncated assistant message so later turns don't build on it.
                    self.messages.pop()
                    text += "\n\n(warning: response was truncated at max_tokens)"
                return text

            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                if block.name == "Workflow":
                    output, is_error = run_workflow(self.model, block.input.get("subtasks", []))
                elif block.name == "bash":
                    output, is_error = handle_bash_block(block)
                else:
                    output, is_error = f"unknown tool: {block.name}", True
                tool_results.append(
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": output,
                        "is_error": is_error,
                )
            self.messages.append({"role": "user", "content": tool_results})
        return "(hit the main loop turn limit before finishing)"

Run it

The bash tool in this example runs model-written commands directly on your machine with no sandbox, and the fan-out runs several of those agents in parallel. Run it in a directory and environment you are comfortable exposing, and add sandboxing before adapting it for anything beyond local experimentation.
PythonTypeScriptC#GoJavaPHPRuby

if __name__ == "__main__":
    task = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Explore the current directory, then give a thorough review: what it does, "
        "code-quality issues, and concrete improvements."
    )
    agent = ModeAgent(MODEL)
    print(agent.turn(task))
    agent.set_mode(False)
    print(agent.turn("Briefly summarize what you found above, no fan-out needed."))

Start the example from the directory you want the agents to work in, for example the root of a repository to review:

python orchestration_mode.py "Review this repository for flaky tests and propose fixes."

With the mode on, expect the model to scout with a few bash commands, dispatch the Workflow tool unprompted, and synthesize the subagent reports into a final answer. Trivial or conversational requests stay solo, as the reminder instructs.
Toward a production harness
This example is deliberately small. A harness meant for real workloads would typically add:
  * **Sandboxed orchestration scripts:** let the model emit a short orchestration program (branching, loops, and reduce steps) and run it inside an isolated interpreter, rather than accepting only a flat list of subtask strings.
  * **Durable journaling:** replace the local JSON file with a store that survives process restarts and is safe under concurrent writers across machines.
  * **Budget enforcement:** track total subagents launched across the whole session, not just per Workflow call, and refuse to exceed a hard cap so a runaway plan cannot exhaust your quota.

The patterns in this example (the mode reminders, standing consent in the tool description, journaling, and a verification wave) carry over unchanged; only the execution substrate around them gets more robust.
Related
[  Mid-conversation system messages The mechanism the mode reminders use, and how it interacts with prompt caching. ](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)[ Effort The effort levels the API accepts and how to choose one. ](https://platform.claude.com/docs/en/build-with-claude/effort)[  Tool use with Claude Defining tools, handling tool calls, and tool results. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Bash tool The Anthropic-defined bash tool this example executes locally. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)
  * [Set up the loop](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#set-up-the-loop)
  * [Define the mode reminders](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#define-the-mode-reminders)
  * [Grant standing consent in the tool description](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#grant-standing-consent-in-the-tool-description)
  * [Run the bash tool locally](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#run-the-bash-tool-locally)
  * [Run one subagent](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#run-one-subagent)
  * [Journal results so reruns resume](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#journal-results-so-reruns-resume)
  * [Fan out, then verify](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#fan-out-then-verify)
  * [Toggle the mode with mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#toggle-the-mode-with-mid-conversation-system-messages)
  * [Run it](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#run-it)
  * [Toward a production harness](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#toward-a-production-harness)
  * [Related](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example#related)

Messages/Context management
# Build an orchestration mode
Build a session-level mode that grants standing consent for multi-agent fan-out, switched on and off with mid-conversation system messages.
An orchestration mode is a session-level switch: when it is on, the model puts maximum thoroughness behind every substantive request, scouting the task itself and then fanning work out to parallel subagents by default. When it is off, the same orchestration tool goes back to per-request opt-in.
The mode is not an API parameter. It is built entirely from documented pieces:
  1. **An effort level:** requests run at a documented [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) value such as `xhigh`. There is no hidden level above the ones on that page.
  2. **A mode reminder:** a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) tells the model the mode is active, with a one-line refresher every several turns and an exit notice when the mode is turned off. The top-level `system` field never changes, so the cached prefix stays intact.
  3. **Standing consent in the tool description:** the orchestration tool's description states that while the mode is on, the model should author and run a workflow for every substantive task without asking first.

This example uses mid-conversation system messages, which are currently available on Claude Opus 4.8 only. The fan-out itself multiplies token usage: a single request can spawn many subagent conversations, so reserve the mode for work that justifies the cost.
Set up the loop
The example is a single file. The constants control the effort level, the fan-out shape, and how often the mode refresher is re-sent. `MAX_CONCURRENT` caps how many subagents run at the same time (the PHP port is sequential and ignores it); `MAX_TOTAL_SUBTASKS` caps how many the model may queue in a single Workflow call. Splitting the two lets the model plan a large backlog without launching it all at once. The `DOC_TEST_MODE` check caps the loops to a single turn when that environment variable is set, so the automated docs harness can validate that the file compiles and finishes quickly without running the full orchestration; leave it unset when running the example yourself.
PythonTypeScriptC#GoJavaPHPRuby

import atexit
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading

import anthropic

client = anthropic.Anthropic()

MODEL = "claude-opus-4-8"
EFFORT = "xhigh"

SYSTEM_PROMPT = "You are a helpful general-purpose agent. Answer the user's request directly."

REQUEST_TIMEOUT_SECONDS = 600
BASH_TIMEOUT_SECONDS = 60
TOOL_RESULT_MAX_CHARS = 8000
MAX_CONCURRENT = 10
DOC_TEST_MODE = bool(os.environ.get("DOC_TEST_MODE"))
MAX_TOTAL_SUBTASKS = 2 if DOC_TEST_MODE else 200
MAX_SUBAGENT_TURNS = 1 if DOC_TEST_MODE else 15
MAX_MAIN_TURNS = 1 if DOC_TEST_MODE else 30
TURNS_BETWEEN_REFRESHERS = 10
JOURNAL_PATH = os.environ.get("ORCH_JOURNAL") or "orchestration_journal.json"

Define the mode reminders
The reminders are short on purpose. They flip the mode and point at the tool description, where the heavyweight instructions live. The full text is sent once when the mode turns on, the refresher is re-sent only after several user turns, and the exit notice is sent once when the mode turns off.
PythonTypeScriptC#GoJavaPHPRuby

MODE_ENTER = (
    "Orchestration mode is on: optimize for the most exhaustive, correct answer rather than "
    "the fastest one. Use the Workflow tool on every substantive task, sized to the problem's "
    "natural decomposition rather than the maximum the tool allows. See the Workflow tool's "
    "description for standing consent, granularity guidance, and quality patterns. Work solo "
    "only on conversational or trivial turns."
)
MODE_REFRESH = (
    "Orchestration mode is still on. Use the Workflow tool; see its standing consent section."
)
MODE_EXIT = (
    "Orchestration mode is off. The Workflow tool's standard opt-in rule applies again."
)

Grant standing consent in the tool description
The Workflow tool carries the real behavioral contract: the opt-in rule, the standing consent that applies while the mode is on, granularity guidance for sizing the fan-out, and the quality patterns the model can reach for (a verification wave, a completeness critic, multi-phase sequencing). Subagents also get a `report_findings` tool so their results come back as structured JSON instead of prose, and the bash tool is the Anthropic-defined `bash_20250124` tool run locally.
PythonTypeScriptC#GoJavaPHPRuby

WORKFLOW_TOOL = {
    "name": "Workflow",
    "description": (
        "Orchestrate a multi-agent workflow: split a large task into independent subtasks "
        "and run them as parallel agents, then collect their results.\n\n"
        "Opt-in: only use this tool when the user explicitly asks for a workflow, or when a "
        "system message confirms that orchestration mode is on.\n\n"
        "Quality patterns: adversarial verification (a second wave of agents checks the first "
        "wave's findings against the source), a completeness critic (one agent hunts for what "
        "the others missed), and multi-phase sequencing (understand, design, implement, and "
        "review as separate workflow calls, reading results between phases). A useful default "
        "is hybrid: scout inline first to discover the work-list, then fan out over it.\n\n"
        "Granularity: scope each subtask to a distinct concern, component, or question rather "
        "than per line or per file section. Scale the count to what the user asked for: a "
        "focused review of a module of a few hundred lines rarely needs more than about ten "
        "subtasks; a broad audit of a large codebase can justify more.\n\n"
        "Standing consent: while a system message confirms orchestration mode is on, that "
        "opt-in is standing. Author and run a workflow for every substantive task by default, "
        "and lean toward verifying findings adversarially. Work solo only on conversational "
        "turns or trivial mechanical edits. When a system message says the mode is off, "
        "revert to the opt-in rule above."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "subtasks": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Independent subtask prompts to run as parallel agents",
        "required": ["subtasks"],

BASH_TOOL = {"type": "bash_20250124", "name": "bash"}

REPORT_TOOL = {
    "name": "report_findings",
    "description": (
        "Report the final findings for your subtask. Call this exactly once, when you are "
        "done investigating; it ends your task."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "summary": {"type": "string", "description": "Two or three sentences of synthesis"},
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "claim": {"type": "string", "description": "The finding, one sentence"},
                        "evidence": {
                            "type": "string",
                            "description": "How it was verified (file, line, or command output)",
                        "severity": {"type": "string", "enum": ["high", "medium", "low", "info"]},
                    "required": ["claim", "evidence", "severity"],
        "required": ["summary", "findings"],

Run the bash tool locally
The bash handler runs the requested command with a timeout, captures combined stdout and stderr, and truncates the result so a runaway command can't flood the context window. Commands run in the directory you launch the example from, so pointing it at a project means starting it there; when `DOC_TEST_MODE` is set, the harness instead gives bash a small throwaway fixture directory that is removed on exit. There is no sandbox here: the command runs with the permissions of the process that launched the example. For clarity this example runs each call in a fresh subshell rather than maintaining the persistent session the `bash_20250124` contract describes; a production agent should back the tool with a long-lived shell so that working directory, environment, and the `restart` action behave as documented.
PythonTypeScriptC#GoJavaPHPRuby

# Run bash where the example was launched. In DOC_TEST_MODE the docs harness
# points it at a throwaway fixture directory instead, removed on exit.
if DOC_TEST_MODE:
    WORK_DIR = tempfile.mkdtemp(prefix="orchestration-")
    atexit.register(shutil.rmtree, WORK_DIR, ignore_errors=True)
    with open(os.path.join(WORK_DIR, "sample.py"), "w") as fixture:
        fixture.write(
            "def fib(n):\n"
            "    return n if n < 2 else fib(n - 1) + fib(n - 2)\n\n"
            "print(fib(10))\n"
        )
else:
    WORK_DIR = os.getcwd()

def run_bash(command: str) -> tuple[str, bool]:
    """Run a shell command and return (output, is_error). No sandbox: example code only."""
    print(f"[bash] {command}", file=sys.stderr)
    try:
        proc = subprocess.run(
            ["bash", "-c", command],
            cwd=WORK_DIR,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=BASH_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return f"command timed out after {BASH_TIMEOUT_SECONDS}s", True
    output = (proc.stdout + proc.stderr).strip() or "(no output)"
    if len(output) > TOOL_RESULT_MAX_CHARS:
        output = output[:TOOL_RESULT_MAX_CHARS] + f"\n(truncated at {TOOL_RESULT_MAX_CHARS} chars)"
    if proc.returncode != 0:
        output = f"(exit code {proc.returncode})\n{output}"
    return output, proc.returncode != 0

def handle_bash_block(block) -> tuple[str, bool]:
    if block.input.get("restart") is True:
        return "Shell restarted.", False
    command = block.input.get("command")
    if not isinstance(command, str) or not command:
        return "bash error: no command was provided.", True
    return run_bash(command)

Run one subagent
Each workflow subtask becomes its own small agent loop with the bash tool, running at the same effort as the main loop. A per-request timeout bounds each API call so a dropped connection degrades one subagent instead of stalling the whole run.
PythonTypeScriptC#GoJavaPHPRuby

def run_subagent(model: str, prompt: str) -> str:
    """One subagent: a small nested agent loop with the bash tool plus report_findings.
    Subagents inherit the main loop's effort level."""
    subagent_system = (
        "You are one agent in a larger parallel fan-out, assigned a single subtask. "
        "Investigate it directly, using bash to check facts rather than guessing, and finish "
        "by calling report_findings exactly once. Return findings, not narration."
    )
    messages = [{"role": "user", "content": prompt}]
    for _ in range(MAX_SUBAGENT_TURNS):
        with client.messages.stream(
            model=model,
            max_tokens=64000,
            system=subagent_system,
            thinking={"type": "adaptive"},
            output_config={"effort": EFFORT},
            tools=[BASH_TOOL, REPORT_TOOL],
            messages=messages,
            timeout=REQUEST_TIMEOUT_SECONDS,
        ) as stream:
            response = stream.get_final_message()
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "pause_turn":
            continue
        if response.stop_reason != "tool_use":
            text = "".join(block.text for block in response.content if block.type == "text")
            if response.stop_reason == "max_tokens":
                text += "\n\n(warning: subagent response was truncated at max_tokens)"
            return text
        tool_results = []
        report = None
        for block in response.content:
            if block.type != "tool_use":
                continue
            if block.name == "report_findings":
                report = json.dumps(block.input, indent=2)
                output, is_error = "Findings recorded.", False
            elif block.name == "bash":
                output, is_error = handle_bash_block(block)
            else:
                output, is_error = f"unknown tool: {block.name}", True
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                    "is_error": is_error,
            )
        if report is not None:
            return report
        messages.append({"role": "user", "content": tool_results})
    return "(subagent hit the turn limit before finishing)"

Journal results so reruns resume
A fan-out that spawns dozens of subagents is expensive to restart from scratch. A small content-addressed journal makes it idempotent: before dispatching a subagent, look up the SHA-256 of its prompt in a local JSON file, and return the recorded result if one exists. Interrupt the run, rerun it, and only the subtasks that never finished are recomputed. The journal deduplicates across runs, not within a single fan-out wave; delete the journal file to start fresh.
PythonTypeScriptC#GoJavaPHPRuby

_journal_lock = threading.Lock()

def _load_journal() -> dict:
    try:
        with open(JOURNAL_PATH) as file:
            return json.load(file) or {}
    except (OSError, json.JSONDecodeError):
        return {}

def journaled(prompt: str, compute) -> str:
    """Return a cached result for this exact prompt, or compute and persist it. This
    makes the fan-out resumable: interrupt the run, rerun it, and only the subtasks
    that never finished are recomputed. Delete the journal file to start fresh."""
    key = hashlib.sha256(prompt.encode()).hexdigest()
    cached = _load_journal().get(key)
    if cached is not None:
        print(f"[journal] cache hit for {key[:12]}", file=sys.stderr)
        return cached
    result = compute()
    try:
        with _journal_lock:  # fan-out writes from many threads
            journal = _load_journal()
            journal[key] = result
            temp = f"{JOURNAL_PATH}.tmp"
            with open(temp, "w") as file:
                json.dump(journal, file)
            os.replace(temp, JOURNAL_PATH)  # atomic on POSIX and Windows
    except OSError as error:  # the journal is best-effort; never discard a computed result
        print(f"[journal] write failed: {error}", file=sys.stderr)
    return result

Fan out, then verify
The fan-out accepts up to `MAX_TOTAL_SUBTASKS` prompts, runs them through the journal with at most `MAX_CONCURRENT` in flight (sequential in the PHP port), and isolates failures so one broken subagent degrades to an error string instead of ending the run. Once the first wave finishes, a second wave reuses the same subagent path to try to refute each result: every verifier re-derives the claims from the source, defaulting to refuted when uncertain. Both the original result and its verdict are returned to the orchestrator so it can weigh them together.
PythonTypeScriptC#GoJavaPHPRuby

def normalize_subtasks(raw) -> list[str]:
    """Accept the subtasks input in whatever shape the model emits: an array, the array
    JSON-encoded as a single string, or a newline-separated list."""
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError:
            raw = raw.splitlines() if "\n" in raw else [raw]
    if not isinstance(raw, list):
        return []
    return [task.strip() for task in raw if isinstance(task, str) and task.strip()]

def verify_prompt_for(subtask: str, result: str) -> str:
    return (
        "Adversarially verify the subagent result below: try to REFUTE it. Re-derive the "
        "claims yourself with bash rather than trusting the result, and look for evidence "
        "that contradicts them. Default to refuted if uncertain. Call report_findings with "
        "summary 'refuted: <why>' or 'confirmed: <why>', citing the file:line or command "
        "output that decided it.\n\n"
        f"Subtask: {subtask}\n\nResult to verify:\n{result}"
    )

def run_workflow(model: str, raw_subtasks) -> tuple[str, bool]:
    """Run subtasks as parallel subagents, then run a second verification wave over
    the results, and return both. MAX_TOTAL_SUBTASKS bounds how many the model can
    queue; MAX_CONCURRENT bounds how many run at once."""
    all_subtasks = normalize_subtasks(raw_subtasks)
    subtasks = all_subtasks[:MAX_TOTAL_SUBTASKS]
    dropped = len(all_subtasks) - len(subtasks)
    if not subtasks:
        return "Workflow error: no usable subtasks were provided.", True
    print(f"[workflow] fanning out {len(subtasks)} agents", file=sys.stderr)

    def run_one(prompt: str) -> str:
        try:
            return journaled(prompt, lambda: run_subagent(model, prompt))
        except Exception as error:  # isolation boundary: one bad subagent should not end the run
            return f"(subagent failed: {type(error).__name__}: {error})"

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as pool:
        results = list(pool.map(run_one, subtasks))
        print(f"[workflow] verifying {len(results)} results", file=sys.stderr)
        verify_prompts = [verify_prompt_for(task, result) for task, result in zip(subtasks, results)]
        verdicts = list(pool.map(run_one, verify_prompts))

    joined = "\n\n".join(
        f"[agent {index + 1}: {task}]\n{result}\n\n[verify {index + 1}]\n{verdict}"
        for index, (task, result, verdict) in enumerate(zip(subtasks, results, verdicts))
    )
    if dropped > 0:
        joined = (
            f"(note: {dropped} subtasks beyond MAX_TOTAL_SUBTASKS={MAX_TOTAL_SUBTASKS} were not "
            "run; rerun them in a follow-up Workflow call)\n\n" + joined
        )
    return joined, False

Toggle the mode with mid-conversation system messages
The agent appends the user's message first, then any system messages that are due: the exit notice, the full mode text on entry, or the periodic refresher. Placing the system message after the user turn keeps every cached byte ahead of it untouched, and satisfies the placement rule that a system message follows a user turn.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

class ModeAgent:
    """An agent loop whose orchestration mode is toggled with mid-conversation system messages."""

    def __init__(self, model: str, mode_on: bool = True):
        self.model = model
        self.mode_on = mode_on
        self.messages: list[dict] = []
        self._mode_announced = False
        self._exit_pending = False
        self._turns_since_reminder = 0

    def set_mode(self, mode_on: bool) -> None:
        """Turn the mode on or off. The notice is delivered with the next user turn."""
        if mode_on == self.mode_on:
            return
        if not mode_on:
            if self._mode_announced:
                self._exit_pending = True
        else:
            self._exit_pending = False
        self.mode_on = mode_on

    def _due_system_messages(self) -> list[dict]:
        """System messages owed on this turn: an exit notice, the full mode text on entry,
        or a one-line refresher every TURNS_BETWEEN_REFRESHERS user turns."""
        due = []
        if self._exit_pending:
            self._exit_pending = False
            self._mode_announced = False
            due.append({"role": "system", "content": MODE_EXIT})
        if self.mode_on:
            if not self._mode_announced:
                self._mode_announced = True
                self._turns_since_reminder = 0
                due.append({"role": "system", "content": MODE_ENTER})
            elif self._turns_since_reminder >= TURNS_BETWEEN_REFRESHERS:
                self._turns_since_reminder = 0
                due.append({"role": "system", "content": MODE_REFRESH})
        return due

    def turn(self, user_input: str) -> str:
        # Mid-conversation system messages follow the user turn they apply to, which keeps
        # the cached prefix ahead of them untouched.
        self.messages.append({"role": "user", "content": user_input})
        self.messages.extend(self._due_system_messages())
        self._turns_since_reminder += 1

        for _ in range(MAX_MAIN_TURNS):
            with client.messages.stream(
                model=self.model,
                max_tokens=64000,
                system=SYSTEM_PROMPT,  # static for the whole session
                thinking={"type": "adaptive"},
                output_config={"effort": EFFORT},
                tools=[WORKFLOW_TOOL, BASH_TOOL],
                messages=self.messages,
                timeout=REQUEST_TIMEOUT_SECONDS,
            ) as stream:
                response = stream.get_final_message()
            self.messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "pause_turn":
                continue
            if response.stop_reason != "tool_use":
                text = "".join(block.text for block in response.content if block.type == "text")
                if response.stop_reason == "max_tokens":
                    # Drop the truncated assistant message so later turns don't build on it.
                    self.messages.pop()
                    text += "\n\n(warning: response was truncated at max_tokens)"
                return text

            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                if block.name == "Workflow":
                    output, is_error = run_workflow(self.model, block.input.get("subtasks", []))
                elif block.name == "bash":
                    output, is_error = handle_bash_block(block)
                else:
                    output, is_error = f"unknown tool: {block.name}", True
                tool_results.append(
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": output,
                        "is_error": is_error,
                )
            self.messages.append({"role": "user", "content": tool_results})
        return "(hit the main loop turn limit before finishing)"

Run it

The bash tool in this example runs model-written commands directly on your machine with no sandbox, and the fan-out runs several of those agents in parallel. Run it in a directory and environment you are comfortable exposing, and add sandboxing before adapting it for anything beyond local experimentation.
PythonTypeScriptC#GoJavaPHPRuby

if __name__ == "__main__":
    task = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Explore the current directory, then give a thorough review: what it does, "
        "code-quality issues, and concrete improvements."
    )
    agent = ModeAgent(MODEL)
    print(agent.turn(task))
    agent.set_mode(False)
    print(agent.turn("Briefly summarize what you found above, no fan-out needed."))

Start the example from the directory you want the agents to work in, for example the root of a repository to review:

python orchestration_mode.py "Review this repository for flaky tests and propose fixes."

With the mode on, expect the model to scout with a few bash commands, dispatch the Workflow tool unprompted, and synthesize the subagent reports into a final answer. Trivial or conversational requests stay solo, as the reminder instructs.
Toward a production harness
This example is deliberately small. A harness meant for real workloads would typically add:
  * **Sandboxed orchestration scripts:** let the model emit a short orchestration program (branching, loops, and reduce steps) and run it inside an isolated interpreter, rather than accepting only a flat list of subtask strings.
  * **Durable journaling:** replace the local JSON file with a store that survives process restarts and is safe under concurrent writers across machines.
  * **Budget enforcement:** track total subagents launched across the whole session, not just per Workflow call, and refuse to exceed a hard cap so a runaway plan cannot exhaust your quota.

The patterns in this example (the mode reminders, standing consent in the tool description, journaling, and a verification wave) carry over unchanged; only the execution substrate around them gets more robust.
Related
[  Mid-conversation system messages The mechanism the mode reminders use, and how it interacts with prompt caching. ](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)[ Effort The effort levels the API accepts and how to choose one. ](https://platform.claude.com/docs/en/build-with-claude/effort)[  Tool use with Claude Defining tools, handling tool calls, and tool results. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Bash tool The Anthropic-defined bash tool this example executes locally. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)
