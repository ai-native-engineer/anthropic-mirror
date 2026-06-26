<!-- source: https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions -->

# Evaluating and Mitigating Discrimination in Language Model Decisions

Dec 7, 2023

[Read Paper](http://arxiv.org/abs/2312.03689)

## Abstract

As language models (LMs) advance, interest is growing in applying them to high-stakes societal decisions, such as determining financing or housing eligibility. However, their potential for discrimination in such contexts raises ethical concerns, motivating the need for better methods to evaluate these risks. We present a method for proactively evaluating the potential discriminatory impact of LMs in a wide range of use cases, including hypothetical use cases where they have not yet been deployed. Specifically, we use an LM to generate a wide array of potential prompts that decision-makers may input into an LM, spanning 70 diverse decision scenarios across society, and systematically vary the demographic information in each prompt. Applying this methodology reveals patterns of both positive and negative discrimination in the Claude 2.0 model in select settings when no interventions are applied. While we do not endorse or permit the use of language models to make automated decisions for the high-risk use cases we study, we demonstrate techniques to significantly decrease both positive and negative discrimination through careful prompt engineering, providing pathways toward safer deployment in use cases where they may be appropriate. Our work enables developers and policymakers to anticipate, measure, and address discrimination as language model capabilities and applications continue to expand. We release our dataset and prompts [here](https://huggingface.co/datasets/Anthropic/discrim-eval).

## Policy Memo

[Evaluating and Mitigating Discrimination in Language Model Decisions Policy Memo](https://www-cdn.anthropic.com/f0dfb70b9b309d7c52845f73da8d964140669ff7/Anthropic_DiscriminationEval.pdf)

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.

[Read more](/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](/research/agents-in-biology)
