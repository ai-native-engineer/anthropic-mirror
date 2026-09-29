<!-- source: https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions -->

# Evaluating and Mitigating Discrimination in Language Model Decisions

Dec 7, 2023

[Read Paper](http://arxiv.org/abs/2312.03689)

## Abstract

As language models (LMs) advance, interest is growing in applying them to high-stakes societal decisions, such as determining financing or housing eligibility. However, their potential for discrimination in such contexts raises ethical concerns, motivating the need for better methods to evaluate these risks. We present a method for proactively evaluating the potential discriminatory impact of LMs in a wide range of use cases, including hypothetical use cases where they have not yet been deployed. Specifically, we use an LM to generate a wide array of potential prompts that decision-makers may input into an LM, spanning 70 diverse decision scenarios across society, and systematically vary the demographic information in each prompt. Applying this methodology reveals patterns of both positive and negative discrimination in the Claude 2.0 model in select settings when no interventions are applied. While we do not endorse or permit the use of language models to make automated decisions for the high-risk use cases we study, we demonstrate techniques to significantly decrease both positive and negative discrimination through careful prompt engineering, providing pathways toward safer deployment in use cases where they may be appropriate. Our work enables developers and policymakers to anticipate, measure, and address discrimination as language model capabilities and applications continue to expand. We release our dataset and prompts [here](https://huggingface.co/datasets/Anthropic/discrim-eval).

## Policy Memo

[Evaluating and Mitigating Discrimination in Language Model Decisions Policy Memo](https://www-cdn.anthropic.com/f0dfb70b9b309d7c52845f73da8d964140669ff7/Anthropic_DiscriminationEval.pdf)

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)

### Project Swap: What happens when agents trade for us?

To see what works and what breaks when agents are sent into a market, we made a miniature market of Claudes.

[Read more](https://www.anthropic.com/research/project-swap)

### How Claude is uplifting biomolecular modeling

Claude made the open-source models that scientists use to predict and design biomolecules faster and more memory-efficient. Claude optimized more than 30 of these models in just under four weeks, speeding them up roughly 4x on average. It also created a low-memory mode that enables the accurate prediction of biomolecular systems larger than 10,000 tokens (amino acids, nucleotides, and atoms from small molecules and ions) on a single NVIDIA GPU node.

[Read more](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)
