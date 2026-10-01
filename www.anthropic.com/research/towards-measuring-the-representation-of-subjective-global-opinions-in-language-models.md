<!-- source: https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models -->

# Towards measuring the representation of subjective global opinions in language models

Jun 29, 2023

[Read Paper](https://arxiv.org/abs/2306.16388)

## Abstract

Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country's perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model's responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on. Our data is at [this URL](https://huggingface.co/datasets/Anthropic/llm_global_opinions). We also provide an interactive visualization at [this URL](https://llmglobalvalues.anthropic.com/).

### What work can robots do?

We built an index of how well today’s robots can perform US job tasks. Robots can already do three-quarters of physical tasks, mostly in limited settings, but are cost-competitive for just 0.3% of them.

[Read more](https://www.anthropic.com/research/what-work-can-robots-do)

### What do you want from AI?

We’re launching a new study using Anthropic Interviewer to learn from your experiences with AI, and we invite you to participate.

[Read more](https://www.anthropic.com/research/your-thoughts-on-ai)

### GLM-5.3 and the spread of advanced cyber capabilities

Like Claude Mythos Preview, GLM-5.3 has strong capabilities for autonomously building end-to-end cyber exploits. But GLM-5.3 is unlike other frontier models in that it has been released without meaningful safeguards to limit misuse.

[Read more](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)
