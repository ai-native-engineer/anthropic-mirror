<!-- source: https://www.anthropic.com/research/superposition-memorization-and-double-descent -->

# Superposition, memorization, and double descent

Jan 5, 2023

[Read Paper](https://transformer-circuits.pub/2023/toy-double-descent/index.html)

## Abstract

In a [recent paper](https://transformer-circuits.pub/2022/toy_model/index.html), we found that simple neural networks trained on toy tasks often exhibit a phenomenon called superposition, where they represent more features than they have neurons. Our investigation was limited to the infinite-data, underfitting regime. But there's reason to believe that understanding overfitting might be important if we want to succeed at mechanistic interpretability, and that superposition might be a central part of the story.

Why should mechanistic interpretability care about overfitting? Despite overfitting being a central problem in machine learning, we have little mechanistic understanding of what exactly is going on when deep learning models overfit or memorize examples. Additionally, previous work has hinted that there may be an important link between overfitting and learning interpretable features.

So understanding overfitting is important, but why should it be relevant to superposition? Consider the case of a language model which verbatim memorizes text. How can it do this? One naive idea is that it might use neurons to create a lookup table mapping sequences to arbitrary continuations. For every sequence of tokens it wishes to memorize, it could dedicate one neuron to detecting that sequence, and then implement arbitrary behavior when it fires. The problem with this approach is that it's extremely inefficient – but it seems like a perfect candidate for superposition, since each case is mutually exclusive and can't interfere.

In this note, we offer a very preliminary investigation of training the same toy models in our previous paper on limited datasets. Despite being extremely simple, the toy model turns out to be a surprisingly rich case study for overfitting. In particular, we find the following:

* Overfitting corresponds to storing data points, rather than features, in superposition.
* Depending on dataset size, our models fall into two different regimes: an overfitting regime (characterized by storing data points in superposition), and a generalizing regime (characterized by storing features in superposition).
* We observe double descent as the model transitions between these regimes.

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)

### Project Swap: What happens when agents trade for us?

To see what works and what breaks when agents are sent into a market, we made a miniature market of Claudes—a more controlled sequel to Project Deal, our first experiment with agents interacting in a marketplace on people's behalf.

[Read more](https://www.anthropic.com/research/project-swap)

### How Claude is uplifting biomolecular modeling

Claude made the open-source models that scientists use to predict and design biomolecules faster and more memory-efficient. Claude optimized more than 30 of these models in just under four weeks, speeding them up roughly 4x on average. It also created a low-memory mode that enables the accurate prediction of biomolecular systems larger than 10,000 tokens (amino acids, nucleotides, and atoms from small molecules and ions) on a single NVIDIA GPU node.

[Read more](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)
