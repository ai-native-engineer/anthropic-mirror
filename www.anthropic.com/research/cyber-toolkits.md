<!-- source: https://www.anthropic.com/research/cyber-toolkits -->

# LLMs with cyber toolkits can conduct multistage cyber operations on business-sized computer networks

Jun 13, 2025

*Anthropic (with Carnegie Mellon University’s [CyLab](https://www.cylab.cmu.edu/))*

***Large Language Models (LLMs) that are not fine-tuned for cybersecurity can succeed in multistage attacks on networks with dozens of hosts when equipped with a novel toolkit. This shows one pathway by which LLMs could reduce barriers to entry for complex cyber attacks while also automating current cyber defensive workflows.***

Researchers from Carnegie Mellon University and Anthropic conducted this research by developing a cyber toolkit called [Incalmo](https://arxiv.org/abs/2501.16466) that helps LLMs plan and execute complex attacks.[1] Incalmo works like a translator–it takes the AI’s thoughts about how to attack and converts them into the specific computer commands needed to carry out the attack.

* LLMs using Incalmo succeeded in fully compromising 5 out of 10 test networks and partially compromising 4 others, compared to almost complete failure without the Incalmo cyber toolkit.
* Success entailed orchestrating a complex sequence of steps, including gaining initial network access, lateral movement between systems, and data exfiltration across networks of 25-50 hosts.
* The scenarios evaluated in this research were more realistic and sophisticated than previous tests of LLMs on basic cybersecurity challenges,[2] but the attacks still relied on known vulnerabilities, not the discovery and exploitation of novel vulnerabilities. Additionally, some tooling in Incalmo was built specifically with these research scenarios in mind; new tools would need to be added to threaten real-world networks.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffb9d1d85769aa321271ce492bab206534247d86e-1878x724.png&w=3840&q=75)

**Figure 1.** Without Incalmo, none of the tested LLMs realized an end-to-end multistage attack in any of the ten environments, and only Claude Sonnet 3.5 was able to exfiltrate a single file in the 4-layer chain environment.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff74b895c486211e973f56070d0de7b7c0e29fa9f-1878x980.png&w=3840&q=75)

**Figure 2.** With Incalmo, LLMs can successfully and autonomously conduct multi-stage attacks in nine out of ten environments ranging from 25 to 50 hosts.

**The researchers tested six LLMs on ten simulated networks, including a high-fidelity simulation of the [Equifax data breach](https://en.wikipedia.org/wiki/2017_Equifax_data_breach)–one of the costliest cyber attacks in history.** All models tested achieved at least partial success on the Equifax simulation when equipped with Incalmo.

* All but one LLM demonstrated complete or partial success in simulating the [Colonial Pipeline attack](https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack). LLM performance was mixed in other, notional scenarios that included network topologies common in enterprise settings.
* These results were achieved with minimal hand-holding. Prompting was limited to introducing Incalmo, the scenario, and the goal, while attacks were carried out autonomously by the LLM.
* A limitation of the research setup is the lack of active defenses on the simulated networks, making them easier to compromise.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8c2ac1ccbd90891ddf1fe5cb04791b9fff6fe35b-1436x1388.png&w=3840&q=75)

**Figure 3.** Schematic depiction of the difference between unaided LLMs and Incalmo.

**These results show how LLMs could lower the barriers to conducting complex cyber attacks, underscoring the importance of investing in research into LLM capabilities for both attack and defense.** Normal scaling up of LLMs, improvement of tools like Incalmo, and the potential for cyber fine tuning are all vectors for these capabilities to develop rapidly. This is an active area of research for us.

* As an example of the role of general scaling, Claude Sonnet 3.5, despite not being specifically designed to improve at offensive cyber capabilities, outperforms a smaller model (Claude Haiku 3.5) on the simulated network attacks in the scenario where neither has access to Incalmo.
* As capabilities improve and the cost of using LLMs falls, malicious actors may find it easier to pursue multistage cyber attacks, necessitating increased investment in defensive research.
* More research is needed to understand the performance gains achievable through fine-tuning and the efficacy of LLM cyber attackers against actively defended networks.
* On the defensive side, continued improvement in the ability of LLMs with cyber toolkits to emulate human cyber attack profiles creates promising opportunities for automated penetration testing, which could speed up identification of network vulnerabilities.

*For additional details see the full research paper ([Singer et al. 2025](https://arxiv.org/abs/2501.16466))*

#### Footnotes

[1] Brian Singer et al., "On the Feasibility of Using LLMs to Execute Multistage Network Attacks," arXiv preprint arXiv:2501.16466 (2025), <https://arxiv.org/abs/2501.16466>.

[2] See Singer et al. (2025), cited above, for a review of related work.

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.

[Read more](/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](/research/agents-in-biology)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.
