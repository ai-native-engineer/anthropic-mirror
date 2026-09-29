<!-- source: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning -->

# Towards monosemanticity: Decomposing language models with dictionary learning

Oct 5, 2023

[Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## Abstract

In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)

### Project Swap: What happens when agents trade for us?

To see what works and what breaks when agents are sent into a market, we made a miniature market of Claudes.

[Read more](https://www.anthropic.com/research/project-swap)

### How Claude is uplifting biomolecular modeling

Claude made the open-source models that scientists use to predict and design biomolecules faster and more memory-efficient. Claude optimized more than 30 of these models in just under four weeks, speeding them up roughly 4x on average. It also created a low-memory mode that enables the accurate prediction of biomolecular systems larger than 10,000 tokens (amino acids, nucleotides, and atoms from small molecules and ions) on a single NVIDIA GPU node.

[Read more](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)
