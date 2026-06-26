<!-- source: https://transformer-circuits.pub/2024/feb-update/index.html -->

# Circuits Updates - February 2024

  
  

We report a number of developing ideas on the Anthropic interpretability team, which might be of interest to researchers working actively in this space. Some of these are emerging strands of research where we expect to publish more on in the coming months. Others are minor points we wish to share, since we're unlikely to ever write a paper about them.

We'd ask you to treat these results like those of a colleague sharing some thoughts or preliminary experiments for a few minutes at a lab meeting, rather than a mature paper.

Short Research Notes

* [Dying Features in Dictionary Learning](#dict-learning-weak)
* [Improvements to Dictionary Learning](#dict-learning-loss)
* [Ghost Grads Update](#dict-learning-resampling)
* [Tanh Penalty in Dictionary Learning](#dict-learning-tanh)

  
  
  

  
  

## [Dying Features in Dictionary Learning](#dict-learning-weak)

Adly Templeton, Joshua Batson, Tom Henighan

In Towards Monosemanticity, we reported that, for very wide autoencoders, most features ended up in an ‘ultralow density cluster’ of the feature density histogram. These features fire very rarely, are not obviously interpretable, and take up a majority of autoencoder capacity, creating a barrier to scaling up autoencoders to a large number of features. A [replication by Neel Nanda](https://www.alignmentforum.org/posts/fKuugaxt2XLTkASkk/open-source-replication-and-commentary-on-anthropic-s#Ultra_Low_Frequency_Features_Are_All_The_Same_Feature) pointed out that the encoder vectors for these features had extremely high cosine similarity to each other, and that this common direction was consistent across random seeds. The decoder vectors for those features were not similar; in fact they were indistinguishable from random. He did not find an obvious interpretation for this direction in terms of dataset examples, sparsity, or the vocabulary. Here we present a potential account of behavior, and confirm some implications experimentally on larger models.

We believe that we have identified this common direction: the features in this cluster put almost all of their encoder weight on the small number of transformer neurons that are weakly activating over the whole dataset. That doesn’t make these features unique: almost every other feature puts similar encoder weight on the same weakly-activating transformer neurons. However, while high-density features put high weight on other neurons, the low-density features have almost no weight on the other neurons.

We hypothesize that the ultralow density features were features that never found a useful decoder direction; they receive negative gradients when they do activate, and so weights on all other transformer neurons are pushed towards zero. This explains why the low density features mostly have weights on weakly-activating transformer neurons, but not why these weights are all pointing in the same direction.

Recall that our autoencoders in Towards Monosemanticity used a pre-encoder bias, where we subtracted the decoder bias from the data before applying the encoder. As a result, the encoder input has a consistent nonzero value for each of the weakly-activating transformer neurons. By assigning weights to each neuron with opposite sign to the pre-encoder bias, the encoder effectively produces a negative bias; any time that the gradient says to make a feature activation smaller, the encoder will both reduce its actual bias and increase the weights on these neurons.

Now that we have identified the cause of the high cosine similarity, the cluster of ultralow density features seems to be just a problem of the L1 regularization penalty killing off features before they find a useful direction, which is a constant struggle when training sparse autoencoders. We discuss some partial progress on that larger problem below.

  
  
  

  
  

## [Improvements to Dictionary Learning](#dict-learning-loss)

Adly Templeton, Tom Conerly, Jonathan Marcus, Tom Henighan, Anna Golubeva, Trenton Bricken

Our views on Beta1 and Pruning have changed. See the [March 2024 update](https://transformer-circuits.pub/2024/march-update/index.html#dl-update).

Here, we give a list of some miscellaneous architectural changes that we have found improve the training of sparse autoencoders:

* Beta1: We’ve found that setting the beta1 parameter of Adam to 0 drastically reduces the number of dying features in larger autoencoders. Setting beta2 from 0.999 to 0.9999 has a smaller beneficial effect. Alternatively, we’ve found that reducing the duration for which a feature has to not fire before it’s considered dead for the purposes of ghost grads has a smaller effect. Unfortunately, these improvements don’t stack in our experiments.
* Pruning: The L1 penalty means that, assuming a feature is useful, increasing the decoder norm and decreasing the activation magnitude is beneficial. Previously, we constrained the decoder norm to be exactly 1. We’ve found improvements by constraining the decoder norm to be less than or equal to 1. Furthermore, this lets us ‘prune’ features with decoder norm less than 0.99 out of the model after training.
* Pre-encoder bias: We used a model with a pre-encoder bias based on early experiments with synthetic data. We found that, on real transformer activations, removing this bias is beneficial. We still use a pre-ReLU bias on the autoencoder.
* Normalization: When working with transformers of different sizes, it is helpful to have hyperparameters that mostly generalize across sizes. To do this, we normalize the activation vectors to have L2 norm equal to sqrt(n\_dense), and take the sum over the dense dimension in the MSE loss.
* Cooldown: We decay the learning rate linearly to 0 in the last 20% of training.

  
  
  

  
  

## [Ghost Grads Update](#dict-learning-resampling)

Tom Conerly

Our views on ghost grads have changed. See the [March 2024 update](https://transformer-circuits.pub/2024/march-update/index.html#dl-update).

We had a bug in our ghost grads implementation that caused all neurons to be marked as dead for the first K steps of training. This means ghost grads were applied to all neurons at the start of training. We ran experiments removing this bug and discovered that the bug actually improved training loss (MSE loss + L1 loss, this doesn’t include the ghost grads loss).

We also wanted to be clearer about our confidence in ghost grads. We've found ghost grads to be a big improvement on 1L models. Initial experiments have shown little difference on larger models. We're unsure if ghost grads will help dictionary learning on large models as we change other hyperparameters.

We don't feel like we have a great understanding of why and when ghost grads helps. We've tried a few variations of ghost grads but we haven't exhausted the space of ideas. We expect that there exist better versions of ghost grads and/or better ways to handle dying neurons.

  
  
  

  
  

## [Tanh Penalty in Dictionary Learning](#dict-learning-tanh)

Adam Jermyn, Adly Templeton, Joshua Batson, Trenton Bricken

One challenge in training sparse autoencoders with an L1 penalty is shrinkage. That is, in addition to encouraging sparsity, an L1 penalty encourages the autoencoder activations to be smaller than they would be otherwise. In our experiments, we came to believe that this was at least partly responsible for our sparse autoencoders recovering a smaller fraction of the MLP loss than we might have hoped.

To remedy this, we studied sparse autoencoders trained with a penalty of the form (A/B) \tanh(x B) (following [Hurley & Rickard 2008](https://arxiv.org/pdf/0811.4706.pdf)). The intuition for this penalty is that, for marginal cases where a feature is on the edge of activating, it provides the same gradient towards zero activation as an L1 penalty, but for strongly-activating examples it provides no penalty and hence no incentive to shrink the solution.

We found that autoencoders trained with a \tanh penalty were a Pareto improvement in the space of L0 and loss recovered, often by a wide margin. Unfortunately, we found that the features in these autoencoders were much harder to interpret.

Ultimately we tracked this down to these autoencoders having many more high-frequency features than ones trained under an L1 penalty, and the highest-frequency features were considerably higher with \tanh than with L1 (over 10%). Despite significant effort, we were unable to correct this issue. We tried varying both parameters in the \tanh penalty over a wide range as well as several small variations on the autoencoder architecture.

We don’t have a solid theoretical understanding of the link between \tanh and high feature densities. One theory is that it is actually important for the functioning of L1 that it penalize features on high-activating examples. However, the simplest version of this theory (that it is just about how much of a gradient the model accumulates towards lower activations) does not fit the evidence: if this were the case, \tanh should eliminate high-density features when we turn up the penalty sufficiently, which we did not see.

For now, we have put this direction to one side. It still seems likely that solving the shrinkage problem will be important to achieving high loss recovery rates, and that solution may well look like a modified sparsity penalty, but the specific \tanh approach no longer seems promising.

To that end, we were quite excited to see a recent investigation by [Wright & Sharkey](https://www.lesswrong.com/posts/3JuSjTZyMzaSeTxKk/fixing-feature-suppression-in-saes-2) suggesting that shrinkage (also known as feature suppression) can be resolved by fine-tuning a subset of the model parameters with no sparsity penalty. This seems like a promising direction, and we would be quite excited to see more work along these lines.
