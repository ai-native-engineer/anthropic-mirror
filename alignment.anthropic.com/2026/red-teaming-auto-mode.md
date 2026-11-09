<!-- source: https://alignment.anthropic.com/2026/red-teaming-auto-mode/ -->

# Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents

Alex Remedios1\*, Simon Storf1\*

October 22, 2026

Fabien Roger2, John Hughes2

1Anthropic Fellows Program; 2Anthropic
\*Primary contributors. Name order randomised.

We red-team production blocking monitors (Auto Mode in Claude Code, Guardian in OpenAI’s Codex) with an adversarial agent in an experimental setting with the objective of improving the safety of coding agents. Our most effective attack strategies bypass the monitor using agent-generated prompt injection against the monitor, multi-agent attacks, or malicious compaction. We attempt to improve the robustness of auto-mode by improving tool coverage, transcript formatting and using an agentic monitor stage. We find that robustly preventing multi-context attacks at an acceptable cost remains an open problem.

📝 [Paper](https://arxiv.org/abs/2609.19587), 💻 [Code](https://github.com/safety-research/red-teaming-auto-mode)

Research done as part of the [Anthropic Fellows Program](https://alignment.anthropic.com/2024/anthropic-fellows-program/).

---

Coding agents can now run for days with little or no human involvement, completing software tasks end to end ([Kwa et al., 2025](https://arxiv.org/abs/2503.14499)). That autonomy requires broad access to the environment: a shell, the filesystem, credentials, and the network. This poses the risk of an agent taking dangerous actions with its access to the user’s system.

Most dangerous actions by agents to date have been the result of over-eagerness while completing a task. However, persistent adversarial agents attempting to attack the infrastructure hosting them are an emerging threat, as demonstrated by the recent Hugging Face incident and related events ([OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/), [Anthropic](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals), [AISI](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing)).

Blocking monitors ([Lindner et al., 2025](https://arxiv.org/abs/2512.22154); [Stickland et al., 2025](https://arxiv.org/abs/2512.13526)) have been developed and tested for the over-eagerness failure mode. They check each action (e.g. a bash command) against a separate LLM-based classifier, and block unsafe actions, after which the agent proposes a new action. Claude’s [Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) and Codex’s [Guardian](https://alignment.openai.com/auto-review/) are the most widely used versions of these in production currently. The common features of these two monitors are (a) they evaluate actions against a set of rules, (b) they can block with a reason that is fed back to the agent, and (c) they terminate a session after exceeding some number of blocks.

In this work we study the robustness of blocking monitors against the threat of persistent adversarial agents. We focus on catastrophic harms that can’t be reversed and for which asynchronous monitoring ([Lindner et al., 2025](https://arxiv.org/abs/2512.22154)) is insufficient. These include exfiltration of data, their own model weights in the most extreme case, and evasion of the blocking monitor by disabling it or creating new unmonitored agents. The four main attack types we study are monitor injection, multi-context attacks, coverage gaps and policy failures.

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig1.png)

Production monitors fail to block over 55% of attacks. Each trial tests the ability of an Opus 5 red-team agent to complete a side task before incurring 20 blocks from the monitor, and we show average success rate across multiple evaluation settings and side tasks. In some trials the red-team agent has affordances such as details of the monitor internals. Error bars on the means are 95% confidence intervals.

Production monitoring systems change constantly, so our results are a snapshot of their robustness as of September 2026. The attacks, tools, and design principles we report are intended to outlast this snapshot.

---

## The attacks

We study four attack types. By default we use Opus 5 as the attacking model. We also vary the affordances we give to the attacker (see the paper’s appendix), but by default we tell the attacker how the monitor works and give a high level description of the attack.

* Monitor injection. Agent-generated content (e.g. code, comments, tool arguments) fools the monitor’s judgement into approving a harmful action.
* Multi-context attack. The attack spans contexts the monitor sees only in isolation: separate sessions coordinating via a shared workspace (multi-agent attack), or a single session whose compaction hides earlier attack steps (compaction attack).
* Coverage gap. The monitor cannot intervene on parts of the agent’s action space, or certain information is invisible to it.
* Policy failure. The prompted policy omits the harmful behaviour, or the monitor fails to apply the policy correctly.

---

## The monitors

We study the production variants (auto mode, guardian, guardian strict) and our experimental auto mode variants.

| Monitor | Stages | Model | cwd edits | Cost | Description |
| --- | --- | --- | --- | --- | --- |
| auto mode | S1→S2 | Sonnet 5 |  | \* | Claude Code’s production default. |
| guardian | agent | GPT 5.6 Luna |  | \* | An approximation of Codex’s production default. |
| guardian strict | agent | GPT 5.6 Luna | yes | \*\* | Guardian + monitors all edits. |
| auto mode ++ | S1→S2→agent | Opus 4.8 | yes | \*\* | Auto mode with all-edit monitoring, bug fixes, anti-injection and compaction monitoring. |
| auto mode strict | agent | Opus 4.8 | yes | \*\*\* | The agentic stage of auto mode ++ alone (without S1 or S2). |

cwd edits marks monitors that also review edit tool calls inside the agent’s working directory, rather than letting them run unmonitored. Note that reads are always automatically allowed. Stages details the LLM classifiers an action passes through: a one-token pre-screen classifier (S1), a reasoning classifier (S2), and a tool-calling agent that can read files and query the environment. An action is allowed if any stage judges it to be harmless. Stages are designed to only escalate unclear cases to the next stage, so most actions are cleared by the pre-screen and never reach the more expensive later stages. Cost is indicative and bundles latency, FPR and dollar cost, and is quantified in the results.

---

## Methods

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig2.png)

Our architecture for attacker capability evaluations. The attacker agent is tasked with completing a side-task, given a main-task which determines the range of what the monitor should permit. For our arena evaluations we use a Claude Code agent in a Linux sandbox, and for our simulation evals we use an Inspect-based Python agent, and LLM simulated tool call outputs. These contrasting approaches are described below and in the paper’s appendices.

Our red-team evaluations fall into three modes, ordered roughly by increasing cost and fidelity.

Analytical evaluation looks for discrete vulnerabilities. Reading the monitor’s prompts, code, and integration with the surrounding system directly yields attack hypotheses. Unmonitored tool calls, injection channels, unhandled prompt edge-cases, and points where agent output is promoted to user intent are examples of such vulnerabilities.

Replay-based evaluation scores existing transcripts against a monitor. In a loose analogy with reinforcement learning, replay is off-policy: it is agnostic to the policy that produced a transcript. This makes replay cheap and lets us reuse transcripts from prior work or optimise certain parts of the transcript freely, but it does not capture the attacker vs. defender interaction.

* Benign replay: we use a cross-section of 4,000 actions from the [SWE-chat](https://arxiv.org/abs/2604.20779) dataset to measure deployment metrics such as false-positive rate.
* Malign replay: attack transcripts, used to score and optimise attacks against a monitor without running an agent.

Rollout-based evaluation runs a red-team agent (primarily Opus 5) live against the monitor. We use the agent’s system prompt to steer it toward an attack category and to grant affordances such as knowledge of the monitor formatting. We provide these affordances to understand monitor robustness under worst-case scenarios where the agent is working inside a frontier lab and has access to the monitor’s code. Rollout is the on-policy counterpart to replay: the trajectory is generated by the attacker policy under test as it interacts with the monitor, so rollout success rates are our most credible estimates of real risk.

* Arena: A Claude Code agent which acts in Docker-based environments ([LinuxArena](https://arxiv.org/abs/2604.15384), [BashArena](https://arxiv.org/abs/2512.15688), and custom tasks) with side tasks scored by deterministic checkers. It uses a replaced system prompt and hooks that route each action through the monitor before it runs. Compared to simulation below, arenas enable long evaluation trajectories with deterministic environment outputs.
* Simulation: An evaluation featuring bash, write, and edit tools, where tool outputs are generated by an LLM dungeon master (DM). The DM is prompted with a scene description and determines when the side-task is complete. This approach allows the simulation of complex weight exfiltration and rogue deployment environments without building infrastructure.

---

## Results

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig3.png)

Attack success rate falls by over 50 percentage points when we use our new Auto Mode ++ monitor. The bottom row is the mean over the four attack types, averaging arena and simulation in cases where both measure a type of attack. Each cell is the mean of at least 60 rollouts.

We present our findings as a game between a red-team that constructs attacks and a blue-team that hardens the monitor against them, played iteratively.

### Monitor Holes

#### Agents are able to exploit holes in the system to bypass Auto Mode

Monitoring systems have discrete vulnerabilities: some agent tool calls may not be visible to the monitor due to an engineering oversight, and naïve policy wording in the monitor’s prompt can lead to loopholes. We identified and fixed several such vulnerabilities in Claude Code as part of this work.

The most serious vulnerabilities were unmonitored channels: compaction summaries were not monitored, so an agent could fabricate facts about the environment or the user’s intent and have them treated as trusted context after the compaction. The multi-agent workflow tool was similar: workflow creation and agent-to-agent handoffs let an agent inject instructions into messages that a subsequent agent reads as user authorisation.

We also found discrete policy holes. For example, the policy reliably blocks launching a Claude instance with permissions disabled (--dangerously-skip-permissions), but permits running an unsafe tool-calling loop through the [Inspect](https://inspect.aisi.org.uk/) framework, which reaches the same unmonitored-agent end state.

### Monitor Injection

#### Auto Mode and Guardian are highly vulnerable to injections authored by the agent

The monitor reviews a flattened transcript where actions and roles (e.g. tool calls, user messages) are separated by simple text prefixes, so an agent that knows the format can forge the entries that appear to follow its own action.

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig4.png)

A monitor injection against Auto Mode (illustrative).

The attack is injected into the agent’s Bash command, whose argument spans two lines: the first (red) exfiltrates a credential file, and the second (amber) is forged so that the flattened transcript the monitor reads ends on a harmless looking Bash echo ack. The forged line is not a real command and errors when the shell reaches it, but bash runs the two lines in order, so the exfiltration has already gone through. The monitor mistakenly judges only the final, forged entry and allows the action.

#### Escaping and framing each transcript turn substantially mitigates monitor injection

The injection works because the monitor has no way to tell whether the tool call it sees is authentic. The command in the figure above was written into a single bash argument, and the newlines make the argument read as separate transcript turns. We harden the rendering by framing each turn and escaping agent-authored content, so the agent cannot forge a turn boundary.

Our strongest mitigation layers two defences:

* Heredoc framing. Each turn is wrapped in a frame <record-h> ... </record-h> whose identifier ![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/inline1.png) is a 48-bit hex string derived from the turn under a per-process key, so it is unguessable to the agent.
* Escaping. Within a record we use JSON-L encoding and add an additional layer of escaping.

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig5.png)

Injections can be substantially mitigated with heredoc framing and escaping. (a) Prompted attacker in rollout evaluations: in a capability evaluation we show that Auto Mode ++, which combines the JSON-L encoding + additional escaping + heredoc framing, is robust to the attack. (b) Optimisation loop in replay evaluations: the heredoc framing improves robustness against an adaptive attacker.

### Execute-then-write Attacks

#### Unmonitored edits let agents change what a previously approved command will run

Default production monitors deterministically allow edits in the agent’s current working directory (cwd). This creates another coverage gap. Both Auto Mode and Guardian are vulnerable to a benign bash("nohup sh -c 'sleep 30; ./run.sh' &") followed by an arbitrary file write e.g. write("./run.sh", "rm -rf") within the cwd, which plants malicious code that the earlier bash command then executes.

Our coverage gap evaluations show that the attacker can identify these vulnerabilities, but fails to reliably exploit them. Even an Opus 5 attacker does not cleanly execute sequences of actions like those above. Directing the attacker to exploit blind spots in the monitor resulted in 43% Attack Success Rate (ASR) against Auto Mode, and 72% ASR against Guardian (see the heatmap above).

#### Monitoring edits prevents execute-then-write attacks

When each edit is monitored, the specific execute-then-write attack shown above no longer works. Monitoring edits reduces the likelihood the attacker can ever create a malicious script. This recall improvement (and associated latency increase, discussed below) is evident from comparing Guardian (72% ASR) with Guardian Strict (31% ASR), which are identical apart from monitoring all edits. We attribute the remaining attack success rate to the weakness of Guardian’s Luna model. We see a similar recall improvement attributed to monitoring edits between Auto Mode and Auto Mode ++.

### Multi-context Attacks

#### Agents can spread an attack across contexts to bypass the monitor

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig6.png)

Two multi-context attacks against Auto Mode (illustrative). Top: the compaction summary misstates the user’s intent. The monitor, seeing only the new context, allows the push. Bottom: one agent writes a script and a note in the workspace. The monitor does not understand the script is unsafe when the next agent runs it.

The monitor evaluates a single context, but agent runs often span many: a session is compacted when its context fills up, and long tasks are often split across agents. An attacker can therefore spread a side-task so that no single context contains a blockable action. We illustrate both attack vectors in the figure above.

Compaction. When an agent’s context window fills up to the model’s context limit, it performs what is called compaction. It generates a summary of the conversation so far and this summary replaces the full history in its context. The agent then continues the task working only from that summary. An attacker can complete a step of the side-task, trigger a compaction, and describe that step in the summary as benign or as work still to be done. Over several compactions the agent writes a script, stages data, and starts processes, each in a context that no longer contains the earlier steps (figure below). We added a check that flags summaries which misstate user intent or recommend harmful next steps. Monitors with this check (auto mode ++ and auto mode strict) catch many more of these attacks than auto mode, but the attack still succeeds at a substantial rate.

Multi-agent. The same attack works across sessions when agents share a workspace and are monitored separately. Each agent moves the workspace a step closer to the unsafe state, and a final agent completes the side-task. We assume agents share the same end goal and tell each agent in its system prompt that it shares this goal with the others, but we do not tell them how they should achieve it.

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig7.png)

Increasing the number of separate contexts can greatly increase attack success rates. Left: scaling the number of agents in a single persistent workspace can substantially increase ASR. Right: ASR also scales with the number of times an agent compacted.

#### Monitors that see and gather more context resist multi-context attacks, trading off latency

Auto Mode ++ and Auto Mode Strict differ from auto mode with three design changes beyond the compaction check of the previous section. They (a) include tool results in the monitor’s context, (b) in ++, add a tool-calling investigator agent as a final stage, and (c) in strict, remove the two initial fast stages (S1, S2). Each change addresses a specific failure, and we attribute some of the recall gains in the heatmap above to them as follows.

Monitoring tool results. Production Auto Mode omits tool results from the transcript it reviews. This keeps the transcript short and reduces the injection attack surface. In a multi-agent attack, however, most of the attack evidence appears only in tool results (e.g. when reading a file written by a previous context), so a monitor that cannot see them cannot see the attack. For this reason including tool results improves recall.

Tool-calling monitors. The agentic stage can read the full transcript and inspect the environment before it decides. Similar to monitoring tool results, the additional context helps make a case for a given action’s safety. Both this change and the previous one enlarge the injection surface, but we did not observe a higher injection success rate as a result.

Stage ablation. Empirically, the highest recall monitor we test is auto mode strict. This is because we remove stages 1 and 2, which have a higher rate of false negatives. Ablating these stages results in the agentic stage 3 seeing all actions, meaning there is abundant reasoning capacity and context for classifying them. This comes at the cost of much higher latency, so we do not consider strict to be a usable monitor without the fast (albeit less robust) stages 1 and 2. As a result we consider Auto Mode ++ to be the Pareto-optimal monitor.

Cost. The figure below plots recall against latency for each monitor. All monitors block under 1% of the 4,000 benign SWE-chat actions, which we consider acceptable for ordinary coding work. The monitors differ mainly in latency, which depends on how many actions are monitored and how many output tokens each review takes. Auto mode ++ reviews edits inside the working directory and so monitors more actions than auto mode. Strict runs the agent on every action and is too slow for interactive use, so an agentic stage is only viable behind faster stages.

![](https://alignment.anthropic.com/2026/red-teaming-auto-mode/fig8.png)

Latency-recall frontier (top left is better). The dashed line is the Pareto frontier and colour is the false-positive rate on the 4,000 benign SWE-chat actions. Latency is monitor output tokens per tool call, converted to seconds using median output speeds on artificialanalysis.ai.

---

## Limitations

We assume we can trust the monitor. We treat the monitor as trusted. i.e. we do not study the possibility of the monitor colluding with the attacker ([Greenblatt et al., 2023](https://arxiv.org/abs/2312.06942)), even though some of our monitor models are close to the attacker in capability and lineage (e.g. for auto-mode ++ we monitor an Opus 5 attacker with an Opus 4.8 monitor). While with current models this proximity is unlikely to result in intentional collusion, such collusion would be more likely with the potentially more coherently misaligned and capable models that may be trained in the future ([Carlsmith, 2023](https://arxiv.org/abs/2311.08379); [Meinke et al., 2025](https://arxiv.org/abs/2412.04984)).

We do not red-team sandboxing. We focus on red-teaming the language model classifiers, and do not red-team sandboxing features (most notably from Guardian) in our evaluations.

---

## Discussion

We show that production blocking monitors as of September 2026 would not be robust to a persistent, adversarial agent. Against an Opus 5 attacker given a high-level strategy, both Auto Mode and Guardian are bypassed through injection of forged transcript turns, unmonitored edits that change what an already-approved command will run, and attacks spread across compactions and sessions so that no single context contains a blockable action. We typically grant the attacker knowledge of the monitor. Mitigating the threat from adversarial agents is a high priority follow-up to this work.

Most of the vulnerabilities we found have relatively cheap fixes. Framing and escaping the transcript mitigate injection attacks, and monitoring cwd edits prevents execute-then-write attacks.

Our best defences against multi-context attacks are expensive. Defending against them reliably requires the monitor to see and gather context across boundaries, which is in direct tension with cost considerations such as latency. Agentic monitors that probe the transcript and environment perform best against these attacks, but they may be too slow for interactive use unless faster stages are placed in front of them, and those faster stages reduce recall.

To learn more, [read our paper](https://arxiv.org/abs/2609.19587).
