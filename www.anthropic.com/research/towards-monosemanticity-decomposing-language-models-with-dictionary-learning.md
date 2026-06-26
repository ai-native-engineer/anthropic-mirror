<!-- source: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning -->

# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

Oct 5, 2023

[Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## Abstract

In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.

[Read more](/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](/research/agents-in-biology)
