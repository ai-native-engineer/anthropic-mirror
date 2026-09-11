<!-- source: https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions -->

# Studying large language model generalization with influence functions

Aug 8, 2023

[Read Paper](https://arxiv.org/abs/2308.03296)

## Abstract

When trying to gain better visibility into a machine learning model in order to understand and mitigate the associated risks, a potentially valuable source of evidence is: which training examples most contribute to a given behavior? Influence functions aim to answer a counterfactual: how would the model's parameters (and hence its outputs) change if a given sequence were added to the training set? While influence functions have produced insights for small models, they are difficult to scale to large language models (LLMs) due to the difficulty of computing an inverse-Hessian-vector product (IHVP). We use the Eigenvalue-corrected Kronecker-Factored Approximate Curvature (EK-FAC) approximation to scale influence functions up to LLMs with up to 52 billion parameters. In our experiments, EK-FAC achieves similar accuracy to traditional influence function estimators despite the IHVP computation being orders of magnitude faster. We investigate two algorithmic techniques to reduce the cost of computing gradients of candidate training sequences: TF-IDF filtering and query batching. We use influence functions to investigate the generalization patterns of LLMs, including the sparsity of the influence patterns, increasing abstraction with scale, math and programming abilities, cross-lingual generalization, and role-playing behavior. Despite many apparently sophisticated forms of generalization, we identify a surprising limitation: influences decay to near-zero when the order of key phrases is flipped. Overall, influence functions give us a powerful new tool for studying the generalization properties of LLMs.

### Measuring tactical intelligence targeting and conventional weapons capabilities of AI models

Anthropic’s Frontier Red Team developed new evaluations to measure AI capabilities in tactical intelligence targeting and conventional weapons development.

[Read more](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
