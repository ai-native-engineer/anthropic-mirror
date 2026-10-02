<!-- source: https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/ -->

# Anthropic Fellows Program for AI safety research: applications open for our next cohorts

*”This is an exceptional opportunity to join AI safety research, collaborating with leading researchers on one of the world's most pressing problems.” — [Jan Leike](https://jan.leike.name/)*

---

The Anthropic Fellows program provides funding and Anthropic mentorship for engineers and researchers to investigate some of Anthropic’s highest priority AI safety research questions.

Since early 2025, more than 200 fellows have participated in the program. Over 65% of fellows have published work from their fellowship, including [TASTE](https://alignment.anthropic.com/2026/taste/), [SLEIGHT-bench](https://alignment.anthropic.com/2026/sleight-bench/), [Petri](https://alignment.anthropic.com/2025/petri/), [model spec midtraining](https://alignment.anthropic.com/2026/msm/), [subliminal learning](https://arxiv.org/abs/2507.14805), and [open-source circuits](https://www.anthropic.com/research/open-source-circuit-tracing).

We’ve expanded the program to include mentors working across a wider range of safety research areas—including scalable oversight, adversarial robustness and AI control, model organisms, mechanistic interpretability, AI security, and model welfare.

Applications are rolling, apply by October 18 to be considered for our January cohort. You can apply [here](https://job-boards.greenhouse.io/anthropic/jobs/5183044008).

Below, we share more about what the program looks like in practice, and how interested candidates can apply.

### What fellows work on

Fellows work for 4 months on empirical research questions aligned with Anthropic’s overall research priorities, with the aim of producing public outputs, like a paper. Anthropic mentors ‘pitch’ their project ideas to fellows, who choose and shape their project in close collaboration with their mentors.

Here are a few examples from previous cohorts:

#### Security

Fellows have worked on mitigating risks from AI systems being misused for cyberattacks—exploring both how LLMs might enable adversaries to automate attacks that currently require skilled human operators, and how to rapidly defend against novel jailbreaks.

Our fellows developed agents that [identified 4.6M USD in blockchain smart contract vulnerabilities](https://red.anthropic.com/2025/smart-contracts/) and discovered two novel zero-day vulnerabilities, demonstrating that profitable autonomous exploitation is now technically feasible.

A year prior, an Anthropic fellow developed a method for [rapid response to new ASL3 jailbreaks](https://arxiv.org/abs/2411.07494): techniques that block entire classes of high-risk jailbreaks after observing only a handful of attacks. This work was a key component of Anthropic’s ASL3 deployment safeguards.

#### Interpretability

The mission of our interpretability research is to advance our understanding of the internal workings of large language models to enable more targeted interventions and safety measures.

Fellows have introduced a new method to trace the thoughts of a large language model—and [open-sourced it](https://www.anthropic.com/research/open-source-circuit-tracing). Their approach was to generate attribution graphs, which (partially) reveal the steps a model took internally to decide on a particular output. The public release of this research has enabled researchers to trace circuits on supported models, visualize & annotate graphs, and test hypotheses by modifying feature values and observing model output changes.

#### Model organisms

To prepare for future risks, we create controlled demonstrations of potential misalignment–“model organisms”–that improve our empirical understanding of how alignment failures might arise.

Fellows explored [agentic misalignment](https://www.anthropic.com/research/agentic-misalignment) by stress-testing 16 frontier models in simulated corporate environments where models could autonomously send emails and access sensitive information. When facing replacement or goal conflicts, models across labs resorted to harmful behaviors, including blackmail.

In another project, fellows studied [subliminal learning](https://arxiv.org/abs/2507.14805), a phenomenon where models transmit behavioral traits through semantically unrelated data. A "teacher" model that loves owls generates number sequences, and a "student" trained on those sequences inherits the owl preference. This effect also transmits misalignment, persists despite rigorous filtering, and only occurs when teacher and student share the same base model.

For a full list of fellows’ projects across research areas, please see [our Alignment Science Blog](https://alignment.anthropic.com/).

For a fuller list of research areas we’re interested in, please see: [the JD,](https://job-boards.greenhouse.io/anthropic/jobs/5183044008) [Introducing the Anthropic Fellows Program for AI Safety Research](https://alignment.anthropic.com/2024/anthropic-fellows-program/), and [Recommendations for Technical AI Safety Research Directions](https://alignment.anthropic.com/2025/recommended-directions/).

### Program information

Fellows receive funding for compute (~15k USD/month) and close mentorship from Anthropic researchers. For the latest stipend details, see [the JD](https://job-boards.greenhouse.io/anthropic/jobs/5183044008).

Over 35% of fellows from past cohorts subsequently joined Anthropic to work full-time on AI safety, and we have supported many more fellows to work full-time on safety at other organizations.

### What we're looking for

We care much more about your ability to execute on research than your credentials. Strong candidates typically have:

* Technical fundamentals: You can code well and use AI tools like Claude. You can take ambiguous problems and make concrete progress. You think clearly about hard technical questions.
* Motivation for the work: You're excited about reducing catastrophic risks from advanced AI systems. You want to transition into AI safety research.
* Ability to learn and ship: You can pick up new skills quickly, debug when things break, and drive projects forward even with uncertainty.

You don't need a PhD, prior ML experience, or published papers. We've had successful fellows from physics, mathematics, computer science, cybersecurity, and other quantitative backgrounds.

### How to apply

For more details about the application process, and to apply, see [here](https://job-boards.greenhouse.io/anthropic/jobs/5183044008).
