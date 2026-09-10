<!-- source: https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned -->

# Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned

Aug 22, 2022

[Read Paper](https://arxiv.org/abs/2209.07858)

![Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://www-cdn.anthropic.com/images/4zrzovbb/website/c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

## Abstract

We describe our early efforts to red team language models in order to simultaneously discover, measure, and attempt to reduce their potentially harmful outputs. We make three main contributions. First, we investigate scaling behaviors for red teaming across 3 model sizes (2.7B, 13B, and 52B parameters) and 4 model types: a plain language model (LM); an LM prompted to be helpful, honest, and harmless; an LM with rejection sampling; and a model trained to be helpful and harmless using reinforcement learning from human feedback (RLHF). We find that the RLHF models are increasingly difficult to red team as they scale, and we find a flat trend with scale for the other model types. Second, we release our dataset of 38,961 red team attacks for others to analyze and learn from. We provide our own analysis of the data and find a variety of harmful outputs, which range from offensive language to more subtly harmful non-violent unethical outputs. Third, we exhaustively describe our instructions, processes, statistical methodologies, and uncertainty about red teaming. We hope that this transparency accelerates our ability to work together as a community in order to develop shared norms, practices, and technical standards for how to red team language models.

## Policy Memo

[Red Teaming Policy Memo](https://www-cdn.anthropic.com/82564d4ec2451b2eed2e0796b7c658fc989f0c1a/Anthropic_RedTeaming.pdf)

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)
