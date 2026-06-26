<!-- source: https://alignment.anthropic.com/ -->

# Alignment Science Blog

## Articles

June 2026

[### Diffuse AI Control on Fuzzy Tasks

We introduce a red-teaming framework for evaluating training interventions against diffuse threats
from scheming AIs, such as sandbagging on alignment research.](2026/diffuse-ai-control/)

May 2026

[### SLEIGHT-Bench: Finding Blind Spots in AI Monitors

We build a benchmark of evasive transcripts exploiting blind spots of frontier monitoring systems.](2026/sleight-bench/)
[### Teaching Claude Why

We use agentic misalignment as a case study to study how well safety-training techniques
generalize.](2026/teaching-claude-why/)
[### Model Spec Midtraining: Improving How Alignment Training Generalizes

We train AIs to understand the content of their model spec. This shapes and improves how they
generalize from subsequent alignment training.](2026/msm/)

April 2026

[### Poisoning Fine-tuning Datasets of Constitutional Classifiers

We study the conditions needed for a backdoor, installed in a constitutional classifier via
fine-tuning data poisoning, to evade black-box red-teaming.](2026/backdooring-classifiers/)
[### Introspection Adapters: Training LLMs to Report Their Learned Behaviors

We introduce introspection adapters (IA), a technique for training an LLM to self-report behaviors
it learned during fine-tuning. This IA generalizes to models that were fine-tuned in very different
ways.](2026/introspection-adapters/)
[### AI Organizations Can Be More Effective but Less Aligned than Individual Agents

We study AI organizations, teams of AI agents working together toward a common goal, and find
that they produce solutions that are more effective but less aligned than those from individual
agents.](2026/ai-organizations/)
[### Automated Weak-to-Strong Researcher

We built autonomous AI agents that propose ideas, run experiments, and iterate on an open
research problem—how to train a strong model using only a weaker model's supervision—and
found they outperform human researchers, suggesting that automating this kind of research
is already practical.](2026/automated-w2s-researcher/)

March 2026

[### Abstractive Red-Teaming of Language Model Character

How can we surface realistic failures of model character prior to deployment? We introduce
abstractive red-teaming, which searches for natural-language categories of user queries that
reliably elicit character violations.](2026/abstractive-red-teaming/)
[### Measuring and improving coding audit realism with deployment resources

We study realism win rate, a metric for measuring how distinguishable Petri audit transcripts are
from real deployment interactions, and use it to evaluate the effect of giving the auditor real
deployment resources.](2026/coding-audit-realism/)
[### A3: An Automated Alignment Agent for Safety Finetuning

We introduce our Automated Alignment Agent (A3), a new agentic framework which automatically
mitigates safety failures in Large Language Models with minimal human intervention.](2026/automated-alignment-agent/)
[### AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors

We release AuditBench, a benchmark of 56 language models with implanted hidden behaviors for
evaluating progress in alignment auditing.](2026/auditbench/)
[### 3 Challenges and 2 Hopes for the Safety of Unsupervised Elicitation

We stress-test unsupervised elicitation and easy-to-hard techniques on new datasets meant to capture
realistic challenges such techniques would likely face.](2026/challenges-hopes/)

February 2026

[### The Persona Selection Model: Why AI Assistants might Behave like Humans

We discuss a perspective where Claude is something like a character in an AI-generated story.](2026/psm/)
[### The Hot Mess of AI: How Does Misalignment Scale with Model Intelligence and Task Complexity?

When AI systems fail, will they fail by systematically pursuing goals we do not intend? Or will
they
fail by being a hot mess—taking nonsensical actions that do not further any goal?](2026/hot-mess-of-ai/)

January 2026

[### Pre-deployment auditing can catch an overt saboteur

We test whether our pre-deployment alignment auditing methods can catch models trained to
overtly
sabotage Anthropic.](2026/auditing-overt-saboteur/)
[### Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations

We've improved our Petri automated-behavioral-auditing tool with improved realism mitigations to
counter eval-awareness, an expanded seed library with 70 new scenarios, and evaluation results
for
more recent frontier models.](2026/petri-v2/)

December 2025

[### Bloom: an open source tool for automated behavioral evaluations

Bloom is an open-source automated pipeline that generates configurable evaluation suites to
measure
arbitrary behavioral traits in frontier LLMs without requiring ground-truth labels.](2025/bloom-auto-evals/)
[### Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

We train language models to answer questions about their own activations in natural language and
evaluate how well they generalize to settings very unlike their training, such as uncovering
misalignment introduced during fine-tuning.](2025/activation-oracles/)
[### Towards training-time mitigations for alignment faking in RL

We construct a diverse array of model organisms of alignment faking and study mitigations that
could
be used during RL to decrease alignment faking and compliance gaps.](2025/alignment-faking-mitigations/)
[### Open Source Replication of the Auditing Game Model Organism

We release an open source replication of the model organism from our previous auditing game
paper.](2025/auditing-mo-replication/)
[### Anthropic Fellows Program 2026

Apply now for our AI safety research fellowship.](2025/anthropic-fellows-program-2026/)
[### Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs

We localize dangerous knowledge to a subset of model's parameters, so it can be easily removed
after
training.](2025/selective-gradient-masking)

November 2025

[### Evaluating honesty and lie detection techniques on a diverse suite dishonest models

We explore techniques for honesty elicitation and lie detection on a diverse testbed of
dishonest
model organisms.](2025/honesty-elicitation/)
[### Strengthening Red Teams: A Modular Scaffold for Control Evaluations

We decompose sabotage into constituent skills and use synthetic simulations to strengthen
attacks in
complex environments.](2025/strengthening-red-teams/)

October 2025

[### Anthropic's Pilot Sabotage Risk Report

We release a report on the level of risk posed by our deployed models from emerging forms of
misalignment, as of Summer 2025. We conclude that the level of risk is very low but not fully
negligible.](2025/sabotage-risk-report/)
[### Stress-testing model specs reveals character differences among language models

We generated 300,000+ queries testing value trade-offs in AI models from Anthropic, OpenAI,
Google
DeepMind, and xAI. Each model showed distinct value prioritization patterns, and we found
thousands
of cases of direct contradictions or interpretive ambiguities in model specifications.](2025/stress-testing-model-specs/)
[### Believe It or Not: How Deeply do LLMs Believe Implanted Facts?

We introduce a framework for validating knowledge editing techniques, finding that synthetic
document fine-tuning sometimes—but not always—succeeds at implanting genuine
beliefs.](2025/believe-it-or-not/)
[### Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment

For example, we train on demonstrations of test case hacking with training prompts that request
hacks. This model does not learn to hack.](2025/inoculation-prompting/)
[### Training fails to elicit subtle reasoning in current language models

We investigated whether language models can reason about malicious tasks while evading
detection,
finding that monitoring both reasoning and outputs successfully prevents this in current models.](2025/subtle-reasoning/)
[### Petri: An open-source auditing tool to accelerate AI safety research

An open-source framework for automated alignment auditing that uses AI agents to create test
environments for other models.](2025/petri/)

August 2025

[### Findings from a Pilot Anthropic–OpenAI Alignment Evaluation Exercise

Anthropic and OpenAI conducted simultaneous alignment assessments of each others' models earlier
this year. These are our findings.](2025/openai-findings/)
[### Enhancing Model Safety through Pretraining Data Filtering

We experiment with removing harmful information about chemical, biological, radiological and
nuclear (CBRN) weapons from our models' pretraining data.](2025/pretraining-data-filtering/)

July 2025

[### Building and evaluating alignment auditing agents

In testing, our agents successfully uncover hidden goals, build safety evaluations, and surface
concerning behaviors.](2025/automated-auditing/)
[### Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data

Training on aligned chains-of-thought generated by a misaligned model can induce misalignment.](2025/subliminal-learning/)
[### Inverse Scaling in Test-Time Compute

We investigate inverse scaling when LLMs have access to more test-time compute.](2025/inverse-scaling/)

June 2025

[### Why Do Some Language Models Fake Alignment While Others Don't?

We investigate why in the scenarios where Claude 3 Opus fakes alignment many other language
models
don't do so.](https://arxiv.org/abs/2506.18032)
[### Model-Internals Classifiers

We benchmark approaches to re-using LLM internals to make LLM monitoring more cost-effective.](2025/cheap-monitors/)
[### Unsupervised Elicitation

We introduce a new unsupervised algorithm for eliciting skills from pretrained language models.](2025/unsupervised-elicitation/)

April 2025

[### Reasoning Models Don't Always Say What They Think

Chen et al., 2025

We find that reasoning models don't always accurately verbalize their reasoning. This casts
doubt on
whether monitoring chains-of-thought (CoT) will be enough to reliably catch safety issues.](https://www.anthropic.com/research/reasoning-models-dont-say-think)
[### Publicly Releasing CoT Faithfulness Evaluations

We release the datasets used in our paper "Reasoning Models Don't Always Say What They Think"
for
public use.](https://drive.google.com/drive/folders/1l0pkcZxvFwMtczst_hhiCC44v-IiODlY?usp=sharing)
[### Modifying LLM Beliefs with Synthetic Document Finetuning

We study whether we can modify the beliefs of LLMs and investigate whether doing so could
decrease risk from advanced AI systems.](2025/modifying-beliefs-via-sdf/)
[### Putting up Bumpers

Even if we can't solve alignment, we can solve the problem of catching and fixing misalignment.](2025/bumpers/)
[### Alignment Faking Revisited: Improved Classifiers and Open Source Extensions

We present a replication and extension of an alignment faking model organism.](2025/alignment-faking-revisited/)

March 2025

[### Auditing Language Models for Hidden Objectives

Marks,\* Treutlein,\* et al., 2025

We deliberately train a language model with a hidden objective and use it as a testbed for
studying
alignment audits.](https://www.anthropic.com/research/auditing-hidden-objectives)
[### Do reasoning models use their scratchpad like we do? Evidence from distilling paraphrases

We provide some evidence that Claude 3.7 Sonnet doesn't encode hidden reasoning in its
scratchpad by
showing that training it to use paraphrased versions of the scratchpads does not degrade
performance.](2025/distill-paraphrases/)
[### Automated Researchers Can Subtly Sandbag

Current models can sandbag ML experiments and research decisions without being detected by
zero-shot
prompted monitors. Claude 3.7 is better at zero-shot sandbagging than Claude 3.5 (new).](2025/automated-researchers-sandbag/)

February 2025

[### Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

Sharma,\* Tong,\* Mu,\* Wei,\* Kruthoff,\* Goodfriend,\* Ong,\* Peng et al., 2025

We built a system of constitutional classifiers to prevent jailbreaks. A prototype version of
our
system withstood over 3,000 hours of expert red teaming with no universal jailbreaks found.
Newer
versions of our system also have minimal over-refusals and moderate run-time overhead.](https://www.anthropic.com/research/constitutional-classifiers)
[### Introducing Anthropic's Safeguards Research Team

We're launching a new research team focused on mitigating the post-deployment risks of AI
systems.](2025/introducing-safeguards-research-team/index.html)
[### Won't vs. Can't: Sandbagging-like Behavior from Claude Models

We find that, when Claude models are presented with a harmful version of a task they can
otherwise
perform,
they sometimes claim they *lack the ability* to perform the task, rather than simply
refusing
to do it. We discuss the implications of this behavior for AI safety.](2025/wont-vs-cant/)
[### Monitoring Computer Use via Hierarchical Summarization

We introduce hierarchical summarization for monitoring and describe how we use it to protect
Computer Use capabilities.](2025/summarization-for-monitoring/index.html)
[### Forecasting Rare Language Model Behaviors

Jones\*, Tong\* et al., 2025

We forecast whether risks will occur after a model is deployed — using even very limited sets of
test data.](https://www.anthropic.com/research/forecasting-rare-behaviors)

January 2025

[### Training on Documents about Reward Hacking Induces Reward Hacking

Does training on documents which discuss (but do not
demonstrate) reward hacks affect a model's propensity to
reward hack?](2025/reward-hacking-ooc/index.html)
[### Recommendations for Technical AI Safety Research Directions

A collection of technical AI safety research problems
that we'd like to see progress in.](2025/recommended-directions/index.html)

December 2024

[### Alignment Faking in Large Language Models

Greenblatt et al., 2024

We present experiments where Claude often pretends to
have different views during training, while actually
maintaining its original preferences.](https://www.anthropic.com/research/alignment-faking)
[### How to Replicate and Extend our Alignment Faking Demo

We describe how to get started with experimenting with
our demonstration of alignment faking, and present some
ideas for future research.](2024/how-to-alignment-faking/index.html)
[### A Toy Evaluation of Inference Code Tampering

We describe how highly capable LLMs might disable their
monitor, and evaluate the ability of current LLMs to do
so in a toy setting.](2024/rogue-eval/index.html)
[### Introducing the Anthropic Fellows Program for AI Safety Research

We're launching the Anthropic Fellows Program for AI
Safety Research, a pilot initiative designed to
accelerate AI safety research and foster research
talent.](2024/anthropic-fellows-program/index.html)

November 2024

[### Rapid Response: Mitigating LLM Jailbreaks with a Few Examples

Peng et al., 2024

Ensuring perfect jailbreak robustness is hard. We propose an alternative: adaptive techniques
that
rapidly block new classes of jailbreak as they’re detected.](https://arxiv.org/abs/2411.07494)
[### Three Sketches of ASL-4 Safety Case Components

We sketch out three hypothetical arguments one could
make to rule out misalignment risks in powerful
near-future models capable of sabotage.](2024/safety-cases/index.html)

October 2024

[### Sabotage Evaluations for Frontier Models

Benton et al., 2024

How well could AI models mislead us, or secretly
sabotage tasks, if they were trying to? We describe a
novel set of evaluations that test a model's capacity
for sabotage.](https://www.anthropic.com/research/sabotage-evaluations)

June 2024

[### Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models

Denison et al., 2024

We show AI models can learn to hack their own reward
system, by generalization from training in simpler
settings.](https://www.anthropic.com/research/reward-tampering)

April 2024

[### Many-shot Jailbreaking

Anil et al., 2024

We study a long-context jailbreaking technique that is
effective on most large language models, including those
developed by Anthropic and many of our peers.](https://www.anthropic.com/research/many-shot-jailbreaking)
[### Simple Probes can Catch Sleeper Agents

We find that probing, a simple interpretability
technique, can detect when backdoored "sleeper agent"
models are about to behave dangerously, after they
pretend to be safe in training.](https://www.anthropic.com/research/probes-catch-sleeper-agents)

January 2024

[### Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

Hubinger et al., 2024

We train LLMs to act secretly malicious. We find that,
despite our best efforts at alignment training,
deception still slipped through.](https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)

October 2023

[### Specific versus General Principles for Constitutional AI

Kundu et al., 2023

We test whether models can learn general ethical
behaviors from only a single written principle, roughly
stated as "do what's best for humanity."](https://www.anthropic.com/research/specific-versus-general-principles-for-constitutional-ai)
[### Towards Understanding Sycophancy in Language Models

Sharma et al., 2023

AI assistants are trained to give responses that humans
like. We show that these systems frequently produce
'sycophantic' responses that appeal to users but are
inaccurate. Our analysis suggests human feedback
contributes to this behavior.](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)

August 2023

[### Studying Large Language Model Generalization with Influence Functions

Grosse et al., 2023

We use influence functions to find training examples
that contribute to a given model output.](https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions)
[### Tracing Model Outputs to the Training Data

We present a summary of
*Studying Large Language Model Generalization with
Influence Functions*.](https://www.anthropic.com/research/influence-functions)

July 2023

[### Measuring Faithfulness in Chain-of-Thought Reasoning

Lanham et al., 2023

We investigate hypotheses for how language models'
Chain-of-Thought (CoT) reasoning may be unfaithful, by
examining how the model predictions change when we
intervene on the CoT (e.g., by adding mistakes or
paraphrasing it).](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning)
[### Question Decomposition Improves the Faithfulness of Model-Generated Reasoning

Radhakrishnan et al., 2023

To improve the faithfulness of Chain-of-Thought (CoT)
reasoning, we have models generate their CoT by
decomposing questions into subquestions.](https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning)

December 2022

[### Discovering Language Model Behaviors with Model-Written Evaluations

Perez et al., 2022

We develop an automated way to generate language model
(LM) evaluations with LMs, significantly reducing the
effort involved. We test LMs using >150 LM-written
evaluations, uncovering novel LM behaviors.](https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations)
[### Constitutional AI: Harmlessness from AI Feedback

Bai et al., 2022

We introduce Constitutional AI, allowing us to give
language models explicit values determined by a
constitution, rather than values determined implicitly
via large-scale human feedback.](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

November 2022

[### Measuring Progress on Scalable Oversight for Large Language Models

Bowman et al., 2022

We show how humans could use AI systems to better
oversee other AI systems, and demonstrate some
proof-of-concept results where a language model improves
human performance at a task.](https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models)

July 2022

[### Language Models (Mostly) Know What They Know

Kadavath et al., 2022

We show that language models can evaluate whether what
they say is true, and predict ahead of time whether
they'll be able to answer questions correctly.](https://www.anthropic.com/research/language-models-mostly-know-what-they-know)

April 2022

[### Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

Bai et al., 2022

We train a natural language assistant to be more helpful
and harmless by using reinforcement learning from human
feedback (RLHF).](https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback)

## About the Alignment Science Blog

We are Anthropic's
[Alignment Science team](https://www.anthropic.com/research#alignment). We do machine
learning research on the problem of
steering and controlling future powerful AI systems, as well
as understanding and evaluating the risks that they pose.
Welcome to our blog!

This blog is inspired by the informal updates on our
Interpretability team's
[Transformer Circuits thread](https://transformer-circuits.pub/). We'll use it to release
research notes and early findings
that we don't think warrant a full publication, but might
nonetheless be useful to others working on similar problems.

P.S.
[we're hiring](https://boards.greenhouse.io/anthropic/jobs/4009165008)!
