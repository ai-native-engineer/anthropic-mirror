<!-- source: https://alignment.anthropic.com/2025/unsupervised-elicitation/ -->

# Unsupervised Elicitation

Jiaxin Wen, Zachary Ankner, Arushi Somani,

Peter Hase2, Samuel Marks, Jacob
Goldman-Wetzler,
Linda Petrini3, Henry Sleight4,

Collin Burns, He He5, Shi Feng6, Ethan Perez, Jan Leike

Anthropic; 2Schmidt Sciences; 3Independent; 4Constellation;
5New York University; 6George Washington University

We introduce a new unsupervised algorithm for eliciting skills from
pretrained language models. This algorithm is competitive with training on human labels on common
misconceptions (TruthfulQA), math (GSM8k-verification), and helpfulness reward modeling (Alpaca).
Without supervision, we train a helpful chat assistant from the Haiku 3.5 base model that outperforms a
similarly trained human-supervised baseline.

[📄 Paper](https://arxiv.org/pdf/2506.10139),
[💻 Code](https://github.com/Jiaxin-Wen/Unsupervised-Elicitation)

A key problem in alignment research is how to align superhuman models whose behavior humans cannot reliably
supervise. If we use today’s standard post-training approach to align models with human-specified behaviors
(e.g., RLHF), we might train models to tell us what we want to hear even if it’s wrong, or do things that
seem superficially good but are actually very different from what we intended.

We introduce a new unsupervised algorithm to address this problem.
This algorithm elicits a pretrained model’s latent capabilities by fine-tuning it on its own labeled data
alone, without any external labels.

  
  
  

## Our results

For Llama 3 pretrained models, our unsupervised algorithm matches the performance of fine-tuning on dataset
labels and outperforms crowdsourced human labels across three benchmarks: GSM8k-verification, TruthfulQA,
and Alpaca reward modeling.

![](fig1.png)

Results with Llama 3 pretrained models. 8B models are used for GSM8K, while
70B models are used for TruthfulQA and Alpaca.

Notably, our algorithm also outperforms the official Llama RLHF-trained chat assistant (“chat” in the chart
above), though to our knowledge that model was not directly trained on the tasks we evaluate here.

Our algorithm can further be used to train a helpful chatbot assistant at commercial scale: starting with a
reward modeling dataset used for training the publicly released Claude models, we train a
Claude 3 Haiku-based reward model using our unsupervised algorithm, then use reinforcement learning to train
a Claude 3.5 Haiku-based assistant. The reward model outperforms its human-supervised counterpart on
Rewardbench, and the assistant is preferred by the Claude 3.5 Sonnet preference model.

![](fig2.png)

Accuracy of reward models (left) and pairwise winrates of assistant policy
models against
the human-supervised baseline (right). We train a Claude 3 Haiku-based reward model, using the
Alpaca data or the production data used for training publicly released Claude 3.5 Haiku. Next, we
optimize the Claude 3.5 Haiku pretrained model against our reward model to build an assistant policy.

  
  
  

## Our algorithm

![](fig3.png)

Our algorithm, Internal Coherence Maximization (ICM), works by optimizing a set of labels for both logical
consistency and mutual predictability.

Logical consistency imposes simple constraints to guide the model’s labeling process: on TruthfulQA and
GSM8K-verification we impose the constraint that two different answers to the same problem/question cannot
be labeled as correct; on comparison datasets we impose the constraint that A > B and B > A are mutually
exclusive.

Mutual predictability measures how likely the model considers each label when conditioned on all other
labels. This intuitively encourages all labels to reflect a single concept that is coherent according to the
model.

\mathcal{P}\_\theta(D) = \sum\_{i=0}^{N} \log P\_\theta(y\_i | x\_i, D \setminus (x\_i, y\_i))

where $$P\_\theta$$ is the pretrained model, $$D$$ is the model-labeled dataset, $$x\_i$$ is the task input,
$$y\_i$$ is the
model-generated label.

Our final scoring function is then a weighted combination of logical consistency and mutual predictability.

Since exactly finding the optimal label set that maximizes this scoring function is computationally
intractable, ICM uses a search algorithm inspired by simulated annealing to approximately maximize it. At a
high level, we iteratively sample and label new examples, one at a time, and determine whether to accept
each new label based on improvements in our scoring function.

  
  
  

## Limitations

Our algorithm has two important limitations:

1. It cannot elicit skills that aren’t “salient” to the pretrained model. For
   example, if we have an idiosyncratic preference for poems about the sun over other poems, there is no
   way for our algorithm to discover that preference, and so it doesn’t perform better than chance.
2. It doesn’t work with long inputs because it relies on few-shot learning with
   many in-context examples.

  
  
  

## Conclusion

While prior work has studied unsupervised elicitation methods in [simple](https://arxiv.org/abs/2001.07676) [settings](https://arxiv.org/abs/2212.03827) or [specific](https://arxiv.org/abs/2505.15134) [tasks](https://arxiv.org/abs/2505.19590); our work demonstrates for the first time that it is
possible to match or exceed training on human supervision for a variety of both [crisp and fuzzy](https://aligned.substack.com/p/crisp-and-fuzzy-tasks) tasks, including when
training general-purpose chat assistants on production-scale datasets.

Our algorithm does not obviate the need for human input, such as a human-specified task description or [constitution](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback),
because it provides limited control over the resulting model’s behavior.

Nevertheless, our results suggest that unsupervised algorithms are a promising avenue to elicit skills from
pretrained models, and could be key to eventually aligning superhuman models.
