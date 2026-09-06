<!-- source: https://www.anthropic.com/research/predictability-and-surprise-in-large-generative-models -->

# Predictability and Surprise in Large Generative Models

Feb 15, 2022

[Read Paper](https://arxiv.org/abs/2202.07785)

## Abstract

Large-scale pre-training has recently emerged as a technique for creating capable, general purpose, generative models such as GPT-3, Megatron-Turing NLG, Gopher, and many others. In this paper, we highlight a counterintuitive property of such models and discuss the policy implications of this property. Namely, these generative models have an unusual combination of predictable loss on a broad training distribution (as embodied in their "scaling laws"), and unpredictable specific capabilities, inputs, and outputs. We believe that the high-level predictability and appearance of useful capabilities drives rapid development of such models, while the unpredictable qualities make it difficult to anticipate the consequences of model deployment. We go through examples of how this combination can lead to socially harmful behavior with examples from the literature and real world observations, and we also perform two novel experiments to illustrate our point about harms from unpredictability. Furthermore, we analyze how these conflicting properties combine to give model developers various motivations for deploying these models, and challenges that can hinder deployment. We conclude with a list of possible interventions the AI community may take to increase the chance of these models having a beneficial impact. We intend this paper to be useful to policymakers who want to understand and regulate AI systems, technologists who care about the potential policy impact of their work, and academics who want to analyze, critique, and potentially develop large generative models.

### Policy Memo

[Predictability and Surprise Memo](https://www-cdn.anthropic.com/4ff80d7f8a98bf096cd543ec61ddc50de3ad8b16/Anthropic_PredictabilityAndSurprise.pdf)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)

### Enabling independent research on how people use Claude

Earlier this year, we ran a pilot giving external researchers access to aggregate, real-world Claude usage data. Three research groups designed their own studies for Anthropic Insights, our privacy-preserving analysis tool. In this post, we share high-level results from those studies and what we learned running this pilot.

[Read more](https://www.anthropic.com/research/enabling-independent-research)
