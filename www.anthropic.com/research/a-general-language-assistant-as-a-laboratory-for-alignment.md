<!-- source: https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment -->

# A General Language Assistant as a Laboratory for Alignment

Dec 1, 2021

[Read Paper](https://arxiv.org/abs/2112.00861)

## Abstract

Given the broad capabilities of large language models, it should be possible to work towards a general-purpose, text-based assistant that is aligned with human values, meaning that it is helpful, honest, and harmless. As an initial foray in this direction we study simple baseline techniques and evaluations, such as prompting. We find that the benefits from modest interventions increase with model size, generalize to a variety of alignment evaluations, and do not compromise the performance of large models. Next we investigate scaling trends for several training objectives relevant to alignment, comparing imitation learning, binary discrimination, and ranked preference modeling. We find that ranked preference modeling performs much better than imitation learning, and often scales more favorably with model size. In contrast, binary discrimination typically performs and scales very similarly to imitation learning. Finally we study a `preference model pre-training' stage of training, with the goal of improving sample efficiency when finetuning on human preferences.

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)

### Enabling independent research on how people use Claude

Earlier this year, we ran a pilot giving external researchers access to aggregate, real-world Claude usage data. Three research groups designed their own studies for Anthropic Insights, our privacy-preserving analysis tool. In this post, we share high-level results from those studies and what we learned running this pilot.

[Read more](https://www.anthropic.com/research/enabling-independent-research)
