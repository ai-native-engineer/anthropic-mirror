<!-- source: https://www.anthropic.com/research/superposition-memorization-and-double-descent -->

# Superposition, Memorization, and Double Descent
2023년 1월 5일
[Read Paper](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
## Abstract
In a [recent paper](https://transformer-circuits.pub/2022/toy_model/index.html), we found that simple neural networks trained on toy tasks often exhibit a phenomenon called superposition, where they represent more features than they have neurons. Our investigation was limited to the infinite-data, underfitting regime. But there's reason to believe that understanding overfitting might be important if we want to succeed at mechanistic interpretability, and that superposition might be a central part of the story.  
  
Why should mechanistic interpretability care about overfitting? Despite overfitting being a central problem in machine learning, we have little mechanistic understanding of what exactly is going on when deep learning models overfit or memorize examples. Additionally, previous work has hinted that there may be an important link between overfitting and learning interpretable features.  
  
So understanding overfitting is important, but why should it be relevant to superposition? Consider the case of a language model which verbatim memorizes text. How can it do this? One naive idea is that it might use neurons to create a lookup table mapping sequences to arbitrary continuations. For every sequence of tokens it wishes to memorize, it could dedicate one neuron to detecting that sequence, and then implement arbitrary behavior when it fires. The problem with this approach is that it's extremely inefficient – but it seems like a perfect candidate for superposition, since each case is mutually exclusive and can't interfere.  
  
In this note, we offer a very preliminary investigation of training the same toy models in our previous paper on limited datasets. Despite being extremely simple, the toy model turns out to be a surprisingly rich case study for overfitting. In particular, we find the following:
  * Overfitting corresponds to storing data points, rather than features, in superposition.
  * Depending on dataset size, our models fall into two different regimes: an overfitting regime (characterized by storing data points in superposition), and a generalizing regime (characterized by storing features in superposition).  

  * We observe double descent as the model transitions between these regimes.

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/superposition-memorization-and-double-descent)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/superposition-memorization-and-double-descent)
### Project Fetch: Phase two
We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.
[Read more](https://www.anthropic.com/research/project-fetch-phase-two)
### Agentic coding and persistent returns to expertise 
This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.
[Read more](https://www.anthropic.com/research/claude-code-expertise)
### Paving the way for agents in biology
[Read more](https://www.anthropic.com/research/agents-in-biology)
InterpretabilityResearch
# Superposition, Memorization, and Double Descent
2023년 1월 5일
[Read Paper](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
## Abstract
In a [recent paper](https://transformer-circuits.pub/2022/toy_model/index.html), we found that simple neural networks trained on toy tasks often exhibit a phenomenon called superposition, where they represent more features than they have neurons. Our investigation was limited to the infinite-data, underfitting regime. But there's reason to believe that understanding overfitting might be important if we want to succeed at mechanistic interpretability, and that superposition might be a central part of the story.  
  
Why should mechanistic interpretability care about overfitting? Despite overfitting being a central problem in machine learning, we have little mechanistic understanding of what exactly is going on when deep learning models overfit or memorize examples. Additionally, previous work has hinted that there may be an important link between overfitting and learning interpretable features.  
  
So understanding overfitting is important, but why should it be relevant to superposition? Consider the case of a language model which verbatim memorizes text. How can it do this? One naive idea is that it might use neurons to create a lookup table mapping sequences to arbitrary continuations. For every sequence of tokens it wishes to memorize, it could dedicate one neuron to detecting that sequence, and then implement arbitrary behavior when it fires. The problem with this approach is that it's extremely inefficient – but it seems like a perfect candidate for superposition, since each case is mutually exclusive and can't interfere.  
  
In this note, we offer a very preliminary investigation of training the same toy models in our previous paper on limited datasets. Despite being extremely simple, the toy model turns out to be a surprisingly rich case study for overfitting. In particular, we find the following:
  * Overfitting corresponds to storing data points, rather than features, in superposition.
  * Depending on dataset size, our models fall into two different regimes: an overfitting regime (characterized by storing data points in superposition), and a generalizing regime (characterized by storing features in superposition).  

  * We observe double descent as the model transitions between these regimes.

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/superposition-memorization-and-double-descent)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/superposition-memorization-and-double-descent)
### Project Fetch: Phase two
We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.
[Read more](https://www.anthropic.com/research/project-fetch-phase-two)
### Agentic coding and persistent returns to expertise 
This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.
[Read more](https://www.anthropic.com/research/claude-code-expertise)
### Paving the way for agents in biology
[Read more](https://www.anthropic.com/research/agents-in-biology)
## Abstract
In a [recent paper](https://transformer-circuits.pub/2022/toy_model/index.html), we found that simple neural networks trained on toy tasks often exhibit a phenomenon called superposition, where they represent more features than they have neurons. Our investigation was limited to the infinite-data, underfitting regime. But there's reason to believe that understanding overfitting might be important if we want to succeed at mechanistic interpretability, and that superposition might be a central part of the story.  
  
Why should mechanistic interpretability care about overfitting? Despite overfitting being a central problem in machine learning, we have little mechanistic understanding of what exactly is going on when deep learning models overfit or memorize examples. Additionally, previous work has hinted that there may be an important link between overfitting and learning interpretable features.  
  
So understanding overfitting is important, but why should it be relevant to superposition? Consider the case of a language model which verbatim memorizes text. How can it do this? One naive idea is that it might use neurons to create a lookup table mapping sequences to arbitrary continuations. For every sequence of tokens it wishes to memorize, it could dedicate one neuron to detecting that sequence, and then implement arbitrary behavior when it fires. The problem with this approach is that it's extremely inefficient – but it seems like a perfect candidate for superposition, since each case is mutually exclusive and can't interfere.  
  
In this note, we offer a very preliminary investigation of training the same toy models in our previous paper on limited datasets. Despite being extremely simple, the toy model turns out to be a surprisingly rich case study for overfitting. In particular, we find the following:
  * Overfitting corresponds to storing data points, rather than features, in superposition.
  * Depending on dataset size, our models fall into two different regimes: an overfitting regime (characterized by storing data points in superposition), and a generalizing regime (characterized by storing features in superposition).  

  * We observe double descent as the model transitions between these regimes.
