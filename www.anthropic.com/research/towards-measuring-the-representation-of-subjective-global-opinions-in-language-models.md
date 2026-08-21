<!-- source: https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models -->

# Towards Measuring the Representation of Subjective Global Opinions in Language Models

Jun 29, 2023

[Read Paper](https://arxiv.org/abs/2306.16388)

## Abstract

Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country's perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model's responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on. Our data is at [this URL](https://huggingface.co/datasets/Anthropic/llm_global_opinions). We also provide an interactive visualization at [this URL](https://llmglobalvalues.anthropic.com/).

### How Claude is accelerating protein design and analytical chemistry

In this post, we share two results that show how Claude can help life scientists increase the pace of their research. In the first, we tested Claude’s ability to design protein binders from scratch, a key step in creating protein-based drugs that has historically taken a specialist weeks or months per target. In the second example, we evaluated whether Claude can accelerate chemical analysis. Claude Opus 5, a generally available model, was given NMR and LC-MS data (the data that allows chemists to assess the identity and purity of the compounds they work with).

[Read more](https://www.anthropic.com/research/Claude-accelerates-protein-design)

### Patterns and problems in emerging multiagent systems

Here, we identify a few examples of behavioral tendencies in current frontier models and show how they can produce unexpected systemic failures, in hopes of starting a conversation about mitigating these risks.

[Read more](https://www.anthropic.com/research/multiagent-systems)

### Reviewing the evidence on worker retraining programs

We're sharing a review of the evidence on worker retraining programs, coauthored by independent researcher David Roodman and Anthropic's Maxim Massenkoff.

[Read more](https://www.anthropic.com/research/reviewing-the-evidence-on-worker-retraining-programs)
