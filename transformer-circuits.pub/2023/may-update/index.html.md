<!-- source: https://transformer-circuits.pub/2023/may-update/index.html -->

# Circuits Updates — May 2023

![](images/img-001.png)

  
  

We report a number of developing ideas on the Anthropic interpretability team, which might be of interest to researchers working actively in this space. Some of these are emerging strands of research where we expect to publish more on in the coming months. Others are minor points we wish to share, since we're unlikely to ever write a paper about them.

We'd ask you to treat these results like those of a colleague sharing some thoughts or preliminary experiments for a few minutes at a lab meeting, rather than a mature paper.

Short Research Notes

* [Attacking Superposition with Dictionary Learning](#superposition-dictionary)
* [Features as The Simplest Factorization](#simple-factorization)
* [Dictionary Learning Worries](#dictionary-worries)
* [Fractional Dimensionality and "Pressure"](#feature-pressure)
* [The "Two Circle" Phenomenon in Memorization](#two-circles)
* [Weight Superposition](#weight-superposition)
* [Attention Head Superposition](#attention-superposition)
* [Feature Manifold Toy Model](#feature-manifolds)

Updates

* [New Comment On Previous Papers](#new-comments)
* [Our Recent Publications](#recent-articles)
* [Research By Other Groups](#external-research)

  
  
  

  
  

## [Attacking Superposition with Dictionary Learning](#superposition-dictionary)

Trenton Bricken, Joshua Batson, Adly Templeton, Adam Jermyn, Tristan Hume, Tom Henighan, Chris Olah

We are often asked about where our work on superposition is going. Over the last few months, we've run several more ad-hoc experiments on superposition in real models (which sometimes produced interesting, but inconclusive results), as well as exploring a variety of questions related to the theory of superposition like our [recent memorization paper](https://transformer-circuits.pub/2023/toy-double-descent/index.html).

Our ad-hoc experiments have persuaded us that solutions to superposition won't be extremely low-hanging fruit, and that more systematic, focused efforts will be necessary. To that end, we're presently focusing on what we've described as ["Approach 2"](https://transformer-circuits.pub/2022/toy_model/index.html#strategic-approach-overcomplete) in the Toy Models paper: extracting features from superposition by using dictionary learning on the activations of a trained, dense model. (This approach has also been investigated by [Sharkey](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) [et al.](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition), who provided us with helpful comments.) We're building up infrastructure to do a systematic, large-scale investigation, with the hope of either finding superposition in real models or making a significant update against this decoding approach.

Informally, we've found cases where sparse factorizations of neural network activations seem to produce activations which suggest simple hypotheses on inspection. But we don't yet have anything that persuades us that these are the "fundamental truth" of the models that we're studying, rather than a convenient lens which might reveal some features while obscuring others.

In the meantime, we do have a few more conceptual contributions, which can be found in the comments [Features as The Simplest Factorization](#simple-factorization) and [Dictionary Learning Worries](#dictionary-worries).

  
  
  

  
  

## [Features as The Simplest Factorization](#simple-factorization)

Trenton Bricken, Joshua Batson, Adly Templeton, Adam Jermyn, Tom Henighan, Chris Olah

As investigation of superposition has progressed, it's become clear that we don't really know what a "feature" is, despite them being central to our research agenda. Several previous definitions have been considered, but all seem unsatisfying. This isn't necessarily bad – sometimes uncertainty about definitions is a very fruitful avenue for science! – but it points at a major open question for us.

In parallel with this, attempts to use dictionary learning or sparse coding methods to automatically discover features in superposition have run into a major challenge. These methods require one to pick a number of features to attempt to decompose the activations into. But how can one know if they've picked the right number to "get all the features" without splitting a true feature into many parts? A recent report by [Sharkey](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) [et al.](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) proposes some heuristics, but the answer seems non-obvious.

We wonder if it might be possible to answer both of these questions at once by defining features as "the simplest factorization of the activations".

More formally, given a sparse factorization of the activations A=SD (S is the sparse code, D is the dictionary), we can ask how much information it takes to represent S and D. We define this “total information” by fitting a probability distribution to the entries of the matrices and computing its entropy. Larger dictionaries tend to require more information to represent, but sparser codes require less information to represent, which may counterbalance.

(The initial experiments below measure information by modeling the distribution of entries in each matrix with a 100 bin histogram, with the largest bin determined by the maximum matrix entry over all experiments. We then take the surprisal of each entry under this distribution, and sum to get the total information. However, we expect our exact formulation of this to change as our investigation continues.)

It turns out that measuring the information like this seems to be an effective tool for determining the "correct number of features", at least for synthetic data. We consider a variety of synthetic dictionary learning tasks where we take sparse vectors (of dimension n\_sparse, with n\_active non-zero entries) and randomly project them into 32 dimensional space. The goal is to recover the original sparse structure. We perform dictionary learning (essentially MOD with an LASSO inner loop), varying both the L1 coefficient and the dictionary size. We then do a parametric plot of Mean Squared Error vs this notion of "Total Information".

We observe that dictionary learning solutions "bounce" when the dictionary size matches the true number of factors. Put another way, the Pareto frontier of this rate-distortion plot is occupied by the solutions with the correct number of learned factors. (This is also where the best MMCS score, a metric introduced by Sharkey et al. for evaluating factorizations when the correct answer is known, is obtained.)

![](images/img-002.png)

If such bounces could be found in real data, it would seem like significant evidence that there are "real features" to be found.

  
  
  

  
  

## [Dictionary Learning Worries](#dictionary-worries)

Tom Henighan, Chris Olah

Dictionary learning is presently our top contender for how to extract features out of superposition (following ["Approach 2"](https://transformer-circuits.pub/2022/toy_model/index.html#strategic-approach-overcomplete) to solving superposition). If we believe that our activations are described by the factorization A=SD where S is a sparse matrix (the "true sparse features") and D is the "dictionary" of unit vectors projecting them to the observed activations, then dictionary learning is a well-established set of tools for solving this problem.

Unfortunately, there are at least two major ways in which we might wish to solve a subtly different problem:

* Compressed sensing may be "too strong." Typical dictionary learning algorithms allow S (the "true sparse features" active for each datapoint) to be computed by an arbitrary function (typically some compressed sensing algorithm). But neural networks likely want to be able to retrieve features from superposition cheaply.In particular, if it takes more than one layer to retrieve a feature from superposition, this seems pretty unfavorable since it both wastes compute and (by storing an intermediate result) the very "storage space" that superposition was trying to save. As a result, typical dictionary learning algorithms may be searching over too broad a space of possibilities. One special concern is that they might hallucinate "extra features", which are pairs of features and allow for sparser representations, but don't make sense from the neural networks perspective.
* The representation may not be "zero-centered". We expect that the right way to understand activations is often something closer to A=SD+b, where b is some bias offset. Typical dictionary learning algorithms break in this setup (although they are easily adapted to handle this).This concern is significantly motivated by a figure in a [post](https://www.alignmentforum.org/posts/KzwB4ovzrZ8DYWgpw/more-findings-on-memorization-and-double-descent) by Marius Hobbhahn which seems to suggest that models with ReLU neurons may implement "shifted data point superposition" to store information while avoiding the ReLU.

All these concerns point towards using the kind of sparse autoencoder setup explored by Sharkey et al. over a full-blown dictionary learning setup. However, we've found that sparse autoencoders are more fragile and sensitive to hyperparameters, which is a significant countervailing consideration in using them. We are interested in finding an approach with the advantages of a sparse autoencoder (in terms of only finding true features) and the consistent trainability of the dictionary learning schemes.

We also have other worries – such as correlated features which may be more difficult to pull apart – which could be of significant concern to these efforts, but aren't specific to the dictionary learning setup.

  
  
  

  
  

## [Fractional Dimensionality and "Pressure"](#feature-pressure)

Tom Henighan, Chris Olah

In Toy Models of Superposition, perhaps the most surprising result was that toy model features often arranged themselves into uniform polyhedra in superposition, with the specific polyhedra varying by sparsity. However, in a [recent comment](https://transformer-circuits.pub/2022/toy_model/index.html#comment-pressure), we found this is more sensitive to the amount of "feature pressure" (the ratio of the number of features that the model would ideally represent and the number of dimensions it has to represent them), and also how long the model is trained. In particular, there are regimes where having more features compete, and also having models train longer, causes clean geometry where it otherwise would not exist.

We're confused why having more features – which the model ultimately chooses to not represent – affects the geometry of the solution so much. One hypothesis is that even as tiny features, they inject noise. Another hypothesis is that the model is actually effectively using "epsilon features" in superposition somehow.

![](images/img-003.png)
  
  
  

  
  

## [The "Two Circle" Phenomenon in Memorization](#two-circles)

Tom Henighan, Chris Olah

In a [recent comment](https://transformer-circuits.pub/2023/toy-double-descent/index.html#comment-double-circle) on Superposition, Memorization, and Double Descent, we observed that problems with m=2 hidden dimensions occasionally have data points that arrange themselves on two circles of different radii. While we believe the specific phenomenon is likely a quirk of optimization in 2D, it's an interesting case study in the geometry of superposition and memorization.

![](images/img-004.png)
  
  
  

  
  

## [Weight Superposition](#weight-superposition)

Chris Olah

We typically think about superposition as a phenomenon where features are put in superposition. For example, we might have features X^\* which are put into superposition X by a map U.

![](images/img-005.png)

But this picture doesn't really help us reason about what kinds of computation a neural network can do while in superposition. We know that some kinds are possible – but what?

To answer this, it's helpful to reason about how weights are put in superposition. If we have two layers X and Y (both in superposition according to matrices U^X and U^Y), we can imagine there being "ideal weights" between these features for computing the second layer from the first. When the two layers are put in superposition, the ideal weights must also be mapped into superposition.

![](images/img-006.png)

What are the properties of this map? Observe that we want e\_i^T W^\* e\_j = {U^Y\_I}^T W U^X\_j. Therefore, if we decompose the ideal weights into their entries we get the following transformation:

W^\* ~=~ \sum\_{i,j} W^\*\_{i,j} e\_i \otimes e\_j ~~\to~~ \sum\_{i,j} W^\*\_{i,j} U^X\_i \otimes U^Y\_j ~\simeq~ W

(Modulo the possibility of interference we'll discuss below.)

Equivalently, one can define the map as a tensor product, U^W = U^X \otimes U^Y.

In feature superposition, the interference between two features X^\*\_i and X^\*\_j is governed by \langle U\_i, U\_j\rangle. Weight superposition has something analogous. Two weights W^\*\_{i,j} and W^\*\_{k,l} have interference governed by \langle U^W\_{i,j}, ~U^W\_{k,l} \rangle\_F ~=~ \langle U^X\_{i}\!\otimes U^Y\_{j}\!, ~U^X\_{k}\!\otimes U^Y\_{l} \rangle\_F. Interestingly, weights apper able to have "constructive interference" which is helpful, in contrast to feature superposition which always seems harmful.

All of this is just preliminary thinking on this question, but it seems to give us a tool for reasoning about what weight matrices are possible to represent in superposition, and thus what kinds of computation it's possible to do while in superposition.

  
  
  

  
  

## [Attention Head Superposition](#attention-superposition)

Adam Jermyn, Chris Olah, Tom Henighan

In[Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html), we saw that when features are sparse, simple neural networks can represent more features than they have neurons through the phenomenon of superposition. We think something analogous can happen with attention heads, with "attention circuits" and "attentional features" being stored in superposition over attention heads.We use the term "attentional feature" to describe relationships between pairs of tokens, which correspond to linear combinations of attention heads attending between a pair. By "attentional circuit", we refer to the otherall computation implemented by an attention head, which in the case of a one-layer model implements skip-trigrams.

For now, we’ll talk about skip-trigrams ([A]…[B] → [C]) as our basic attentional circuits. This is a restricted definition, as we think there are more general kinds of attentional circuits, but they seem sufficient to demonstrate attention superposition.

We trained toy models — small one-layer transformers with trivial embeddings and unembeddings — to investigate how and under what circumstances attention heads place circuits in superposition. The training data were sequences of tokens which were chosen uniformly except for over-representing certain skip-trigrams.

We focus in particular on skip-trigrams which are "OV-incoherent," meaning that they attend from multiple different tokens back to a single token, and the output depends on the token attended from. A single attention head cannot implement multiple such skip-trigrams without introducing errors in its output, because the OV circuit does not know which token is being attended from.

![](images/img-007.png)

Attention Head Wiring diagram: The first column is the token attended from, the second is the token attended to, and the thickness of the lines connecting them indicate the strength of attention. The final three columns show the modifications caused to the output logits when attending to the token in the second column. Here red indicates an increase in the output and blue indicates a decrease.

What we see is that when the ground truth contains more incompatible trigrams than there are attention heads, models resort to placing them in superposition across heads. Above, each trigram is encoded in superposition between at least two attention heads. These results suggest caution in studying the role of a single attention head in isolation, as circuits implemented in superposition can appear misleading when only partially interpreted.

These wiring diagrams are simple for models trained on small numbers of skip-trigrams, but rapidly become too complex to read as the training data become more complex. Despite this, we see tantalizing evidence of beautiful geometry underlying even cases with many skip-trigrams, which we are excited to investigate further.

![](images/img-008.png)
  
  
  

  
  

## [Feature Manifold Toy Model](#feature-manifolds)

Chris Olah, Josh Batson

In our toy model investigations of superposition, we assume the existence of discrete features and see how an autoencoder represents them. But in real life, features may lie on a manifold, where nearby features respond to similar data. What should we expect neural networks to do in such cases? In many empirical cases, neural networks model the manifold with [families of equivariant neurons](https://distill.pub/2020/circuits/equivariance/), representing the manifold in terms of discrete units rather than representing the manifold directly. Should we expect this to always happen? Why does it happen?

For example, a vision model might want to represent curves in different orientations; the set of possible orientations naturally defines a 1D manifold, a circle. One could imagine the network might have a single neuron whose activation represents the angle of the curve or might have two neurons whose activations represent sine and cosine of the angle of the curve. Instead, in [Curve Detectors](https://distill.pub/2020/circuits/curve-detectors/), Cammarata et al find many (~10) neurons which each respond to curves in a specific range of orientations.This difference in representational strategy seems somewhat analogous to the distinction between "value coding" and "variable coding" in neuroscience (see [Thorpe 1989](https://persee.fr/doc/intel_0769-4113_1989_num_8_2_873)).

We present some extremely preliminary results investigating this question by considering a toy problem with a "feature manifold" rather than discrete features. We'll then study what happens when we change the length scale (\ell) the model cares about resolving positions on the feature manifold within.

Our basic setup will be the [ReLU-output problem](https://transformer-circuits.pub/2022/toy_model/index.html#demonstrating-setup-model) from the Toy Models paper. Instead of having the data be independent features, we imagine having a large number of features arranged around a circle, with equal angular spacing. We first fix a length scale  (\ell) for the problem. To generate a data point, we pick a random angle (\theta) and an activation magnitude (m). The feature x\_\phi at angle \phi around the circle activates on that datapoint if \phi is close to \theta, where “close” is determined by the length scale:

x\_\phi ~=~ \begin{cases} ~m\cos(\frac{\phi-\theta}{\ell}) & ~\text{if}~~\frac{|\phi-\theta|}{\ell} \leq \frac{\pi}{2}\\ ~0 & ~\text{otherwise} \end{cases}

We can now study how the features are embedded as we vary the length scale:

![](images/img-009.png)

This kind of emergent discretization (which we're increasingly seeing hints of across a variety of problems) seems like it might be a very important phenomenon. It may be that "emergent discretization" is the thing we mean when we talk about features.

One caveat to this work is that we've seen some hints that the smallest length scale discretization may be an optimization failure. Additional research is needed to understand this phenomenon.

  
  
  

  
  

## [New Comments Digest](#new-comments)

Transformer Circuits periodically publishes comments on our papers, both from external parties and by the authors. Some of these comments were submitted before publication, from reviewers of early draft manuscripts. But others are submitted significantly after the fact, and might not be seen. To that end, we've included a digest of recently added comments:

A Mathematical Framework for Transformer Circuits

* [Summary of Follow-Up Research](https://transformer-circuits.pub/2021/framework/index.html#comment-summary) (Chris Olah)
* [Correction: Attention Head Composition Diagram](https://transformer-circuits.pub/2021/framework/index.html#comment-errata) (Chris Olah)

In-context Learning and Induction Heads

* [2 older comments](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html#comments-replications)

Toy Models of Superposition

* [Replication](https://transformer-circuits.pub/2022/toy_model/index.html#comment-becker-kahn) (Spencer Becker-Kahn)
* [Replication](https://transformer-circuits.pub/2022/toy_model/index.html#comment-hobbhahn) (Marius Hobbhahn)
* [Engineering Monosemanticity in Toy Models](https://transformer-circuits.pub/2022/toy_model/index.html#comment-jermyn) (Adam Jermyn, Evan Hubinger, and Nicholas Schiefer)
* [Fractional Dimensionality and "Pressure"](https://transformer-circuits.pub/2022/toy_model/index.html#comment-pressure) (Tom Henighan and Chris Olah)
* [Extracting Features with Sparse Autoencoders](https://transformer-circuits.pub/2022/toy_model/index.html#comment-sharkey) (Lee Sharkey, Dan Braun, and Beren Millidge)
* [Linear Representation in Othello](https://transformer-circuits.pub/2022/toy_model/index.html#comment-nanda) (Neel Nanda)
* [3 older comments](https://transformer-circuits.pub/2022/toy_model/index.html#comments)

Superposition, Memorization, and Double Descent

* [Replication](https://transformer-circuits.pub/2023/toy-double-descent/index.html#comment-hobbhahn) (Marius Hobbhahn)
* [Re: Data Dimensionality of MNIST](https://transformer-circuits.pub/2023/toy-double-descent/index.html#comment-hobbhahn-re-mnist) (Marius Hobbhahn)
* [Optimization Failures in 2D](https://transformer-circuits.pub/2023/toy-double-descent/index.html#comment-double-circle) (Chris Olah and Tom Henighan)
* [4 older comments](https://transformer-circuits.pub/2023/toy-double-descent/index.html#comments)

  
  
  

  
  

## [Our Recent Publications](#recent-articles)

Over the last few months, we've also published a few smaller papers which you might not have seen (including one "perspective" article  – Interpretability Dreams – being released along with this post).

* [Superposition, Memorization, and Double Descent](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
* [Privileged Bases in the Transformer Residual Stream](https://transformer-circuits.pub/2023/privileged-basis/index.html)
* [Superposition, Compositionality, and Distributed Representations](https://transformer-circuits.pub/2023/superposition-composition/index.html)
* [Interpretability Dreams](https://transformer-circuits.pub/2023/interpretability-dreams/index.html)

  
  
  

  
  

## [Research By Other Groups](#external-research)

Finally, we'd like to highlight recent work by a number of researchers at other groups which we believe will be of interest to you if you find our papers interesting.

### [On the Nature of Representations…](#external-representations)

Linear Representations. One of the most fundamental assumptions we personally tend to make in studying neural networks is the [linear representation hypothesis](https://transformer-circuits.pub/2022/toy_model/index.html#motivation): neural network features are represented by directions. While this is a common hypothesis, it isn't known to be true.

A recent back and forth between [Li](https://arxiv.org/pdf/2210.13382.pdf) [et al.](https://arxiv.org/pdf/2210.13382.pdf) and [Nanda](https://www.neelnanda.io/mechanistic-interpretability/othello) (in the context of language models trained on Otehllo games) is perhaps the strongest evidence yet from a Popperian perspective: the linear representation hypothesis made a prediction which was contrary to evidence at that point, and was then validated (see Neel Nanda's [comment here](https://transformer-circuits.pub/2022/toy_model/index.html#comment-nanda)). It should be mentioned that there are many other reasons to be excited about this work – we discuss it more below – but we wanted to particularly highlight this as an example of excellent scientific discourse and the evidence it seems to provide for a question of very broad significance to the field.

More generally, a wide range of other papers have continued to provide more empirical examples of seemingly linearly represented features. Perhaps the most striking is [Turner](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector) [et al.](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector) (who do vector arithmetic to control language models), but see also [Gurnee](https://arxiv.org/pdf/2305.01610.pdf) [et al.](https://arxiv.org/pdf/2305.01610.pdf) and more generally all the papers mentioned in the following section on what features can be found in language models.

What Features Exist Inside Language Models? Ultimately, our goal is to understand language models. While it's often tempting to emphasize methods or theories, the bread and butter of mechanistic interpretability research must be something similar to the study of anatomy in biology: characterizing features and circuits that exist in language models. On this note, [Yun](https://arxiv.org/pdf/2103.15949.pdf) [et al.](https://arxiv.org/pdf/2103.15949.pdf), [Gurnee](https://arxiv.org/pdf/2305.01610.pdf) [et al.](https://arxiv.org/pdf/2305.01610.pdf), and [Bills](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html) [et al.](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html) – while all also notable for other contributions – deserve attention for their qualitative results on what features we exist inside language models.

Superposition. In the last few months, significant progress has been made by our colleagues at other groups on superposition. [Sharkey](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) [et al.](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) attempted to decode superposition in real models, using sparse autoencoders. [Yun](https://arxiv.org/pdf/2103.15949.pdf) [et al.](https://arxiv.org/pdf/2103.15949.pdf) apply dictionary learning to transformer residual streams and recover many interpretable features. [Gurnee](https://arxiv.org/pdf/2305.01610.pdf) [et al.](https://arxiv.org/pdf/2305.01610.pdf) apply sparse linear probes to transformers and find, among other things, evidence of low-level linguistic features being represented in superposition over small sets of neurons. [Lindner](https://arxiv.org/abs/2301.05062) [et al.](https://arxiv.org/abs/2301.05062) created a tool to compile programs into transformers using superposition. [Jermyn](https://arxiv.org/pdf/2211.09169.pdf) [et al.](https://arxiv.org/pdf/2211.09169.pdf) explore approaches to encouraging monosemantic neurons. [Scherlis](https://arxiv.org/abs/2210.01892) [et al.](https://arxiv.org/abs/2210.01892) examine superposition from the perspective of constrained optimization. Hobbhahn published [two](https://www.alignmentforum.org/posts/KzwB4ovzrZ8DYWgpw/more-findings-on-memorization-and-double-descent) [posts](https://www.alignmentforum.org/posts/WfdxXhszxFc3BxZ8r/more-findings-on-maximal-data-dimension) extending our investigation of superposition and memorization.

One detail from Hobbhahn's posts which we wanted to highlight is that some models seem to have a kind of "shifted superposition" where the model shifts data points to avoid ReLU. This is contrast to the intuition one might naively have that ReLU would in fact anchor the superposition at 0 due to its special behavior there.

![](images/img-010.png)

Othello & World Models. In the context of language models, there's been an ongoing debate about whether they're "just doing statistical pattern matching" or they "understand". This conversation has often been polarized and disconnected from specific mechanistic hypotheses of what's going on. However, a [recent paper](https://arxiv.org/pdf/2210.13382.pdf) by Li et al. – and [follow up work](https://www.neelnanda.io/mechanistic-interpretability/othello) by Nanda – used probes to provide evidence that language models trained to play Othello have an internal representation of the state of the board. This is both a nice example of progress in mechanistic understanding, and is also perhaps an example of how mechanistic interpretability can help us have more productive dialogues about neural networks.

### [Larger-Scale Structure](#external-macrocopic)

How is factual knowledge retrieved? A recent paper by [Geva](https://arxiv.org/pdf/2304.14767.pdf) [et al.](https://arxiv.org/pdf/2304.14767.pdf) continues the very fruitful line of investigation on activation patching methods (see [Meng](https://arxiv.org/pdf/2202.05262.pdf) [et al.](https://arxiv.org/pdf/2202.05262.pdf)), which allows for larger-scale understanding of how transformers process information. This new paper looks into how somewhat more complex queries about knowledge are processed by language models. In particular, where prior work showed that attention heads were important for moving information from a subject token, this work suggests that the OV circuit of attention heads can also transform that information, for example reading in a country and writing out its capital.

### [Methods](#external-methods)

Activation Patching Continues. As mentioned above, we're continuing to see exciting work based on the activation patching approach (see [Meng](https://arxiv.org/pdf/2202.05262.pdf) [et al.](https://arxiv.org/pdf/2202.05262.pdf)), most recently by [Geva](https://arxiv.org/pdf/2304.14767.pdf) [et al.](https://arxiv.org/pdf/2304.14767.pdf).

Automated Interpretability. One of the most common (and very reasonable) critiques of mechanistic interpretability is that it can't scale to large models. A recent paper by Bills et al., ["Language models can explain neurons in language models"](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html), provides a proof of concept for automating parts of mechanistic interpretability. This approach would still require a solution to superposition, but it's potentially an exciting way to address the scalability concern. At the same time, we also have some reservations about this kind of automation, especially when the goal is safety. Do we really want our auditing of AI models to depend on trusting an AI model to help us with auditing? A critical question is whether alternative approaches to addressing the scalability problem can be found. Either way, this kind of method seems helpful in the meantime – and the [qualitative results](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html#sec-qualitative) are also very interesting.

Attribution patching. In a [recent post](https://www.alignmentforum.org/posts/gtLLBhzQTG6nKTeCZ/attribution-patching-activation-patching-at-industrial-scale), Neel Nanda describes a method called "attribution patching" which he developed in collaboration with several of us a while back. It's exciting to see this written up! Using gradient activation products to perform quick attributions to various intermediate computations was quite useful for investigations in the vision context (see [Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/)), and seems helpful as a way to investigate larger models. However, be sure to pay attention to Neel's cautionary notes on when this works, especially [the section on LayerNorm](https://www.alignmentforum.org/posts/gtLLBhzQTG6nKTeCZ/attribution-patching-activation-patching-at-industrial-scale#LayerNorm). (We can file this as reason #78 for why interpretability researchers hate LayerNorm.)

### [Mechanistic Interpretations of Learning Dynamics and Scaling](#external-learning-scaling)

Can we explain learning dynamics and scaling laws in terms of circuits? We know that induction heads [cause a loss bump in training](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html#argument-phase-change) when they form, and [likely cause a bump in scaling laws](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html#scaling-laws). This suggests the tantalizing possibility of a deep bridge between the microscopic world of mechanistic interpretability and the more macroscopic topics of learning dynamics and scaling laws. Several recent papers have made us more hopeful that such a bridge can be found.

Quanta. [Michaud](https://arxiv.org/pdf/2303.13506.pdf) [et al.](https://arxiv.org/pdf/2303.13506.pdf) propose a theory of scaling in terms of "quanta" – discrete behavior patterns which reduce loss – along with an algorithm for automatically discovering these quanta based on gradients. A natural hypothesis is that these behavioral quanta mechanistically correspond to circuits, just as the "induction bump" in-context learning behavior corresponds to induction head circuits. If this could be demonstrated, it would create a much wider bridge from the microscopic world of circuits to the macroscopic world of losses, behaviors, scaling, and learning dynamics.

Mode Connectivity. [Lubana](https://arxiv.org/pdf/2211.08422.pdf) [et al.](https://arxiv.org/pdf/2211.08422.pdf) and [Juneja](https://arxiv.org/pdf/2205.12411.pdf) [et al.](https://arxiv.org/pdf/2205.12411.pdf) find an empirical relationship between generalization strategies – and likely the underlying mechanisms – and linear mode connectivity in the loss landscape. In particular, models with different generalization properties appear to have a loss barrier separating them if one linearly interpolates in parameter space.

### [Grokking](#external-grokking)

Reverse Engineering Grokking, Fourier Transforms, & Universality. In [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/pdf/2301.05217.pdf), Nanda et al. reverse engineered a neural network doing modular arithmetic which turned out to be using Fourier transforms, and linked this to grokking behavior. Following up on this, [Chughtai](https://arxiv.org/pdf/2302.03025.pdf) [et al.](https://arxiv.org/pdf/2302.03025.pdf) found that if one trains neural networks to perform more general group operations, they learn to use [group representations](https://en.wikipedia.org/wiki/Group_representation) (a generalization to noncommutative groups of the Fourier transform for cyclic groups found in the first model). This is interesting both as a compelling example of reverse engineering simple models, and also as evidence for the [universality hypothesis](https://distill.pub/2020/circuits/zoom-in/#claim-3), as the authors find that each trained network utilizes a random subset of the group representations that exist.

Why does grokking occur? A recent paper by [Liu](https://arxiv.org/pdf/2210.01117.pdf) [et al.](https://arxiv.org/pdf/2210.01117.pdf) finds a systematic relationship between weight decay and the length of time it takes for grokking to occur. Roughly, they find first the model finds a memorizing solution whose weight matrix has very large norm, and that grokking occurs when the model weights shrink to the size of the generalizing solution. Qualitatively, the relationship they find between memorization and weight norm matches some of our observations on how memorization [occurs mechanistically](https://transformer-circuits.pub/2023/toy-double-descent/index.html) in toy models and [classic work by Bartlett](https://proceedings.neurips.cc/paper/1996/hash/fb2fcd534b0ff3bbed73cc51df620323-Abstract.html) showing that feed-forward networks with small weight norm generalize well.

### [Other Results](#external-other)

Neuroscience Parallels. Over the last few years, there have been a number of cases where mechanistic interpretability research discovered results which parallel finding in neuroscience, including [curve detector neurons](https://distill.pub/2020/circuits/curve-detectors/) and person-detecting [multimodal neurons](https://distill.pub/2021/multimodal-neurons/). Recently, we've begun to see parallels which go in the other direction, with discoveries in artificial neural networks foreshadowing results in biological neuroscience:

* High low-frequency detectors:  [Ding,](https://www.biorxiv.org/content/10.1101/2023.03.15.532836v1) [et al.](https://www.biorxiv.org/content/10.1101/2023.03.15.532836v1) found novel neurons in mice which seem quite similar to [high-low frequency detectors](https://distill.pub/2020/circuits/frequency-edges/) found in a variety of vision models.
* V4 & Earl-Mid Vision Generally: [Willeke,](https://www.biorxiv.org/content/10.1101/2023.05.12.540591v1) [et al.](https://www.biorxiv.org/content/10.1101/2023.05.12.540591v1) found a variety of parallels between neurons observed in primate V4 and [findings in early vision](https://distill.pub/2020/circuits/early-vision/) for InceptionV1.

The growing body of parallels, and the fact that they're going in both directions, seems suggestive of a genuine, deep connection. It also seems like evidence for a very strong version of the universality hypothesis.

Behavioral Control of GPT with Activation Addition. In a recent post, [Turner](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector) [et al.](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector) demonstrate that they can control language models by adding vectors to activations, defined simply by doing arithmetic on activation vectors. This extends [earlier work](https://www.lesswrong.com/posts/cAC4AXiNC5ig6jQnc/understanding-and-controlling-a-maze-solving-policy-network) on RL agents navigating a maze. It's interesting to speculate what the mechanism is – are they controlling low-level features related to a topic, high-level topic/theme features, "motor neurons" that directly implement behavior, or something else? More generally, it's another piece of evidence for the linear representation hypothesis.

Hierarchical Skip-Trigrams. A [recent post](https://www.lesswrong.com/posts/b5HNYh9ne5vEkX5ag/one-layer-transformers-aren-t-equivalent-to-a-set-of-skip) by Buck Shlegeris constructed an example of a phenomenon we'll call "hierarchical skip-trigrams" (following Neel Nanda's naming). Hierarchical skip-trigrams allow one-layer models to use skip-trigrams to express interesting computation one might not have naively expected.

Decision Transformer Interpretability. Two recent articles ([part 1](https://www.lesswrong.com/posts/JvQWbrbPjuvw4eqxv/a-mechanistic-interpretability-analysis-of-a-gridworld-agent), [part 2](https://www.lesswrong.com/posts/bBuBDJBYHt39Q5zZy/decision-transformer-interpretability)) by Bloom and Colognese take a mechanistic approach to investigating decision transformers in a grid world setting.

Sparsity and Modularity. A recent paper by [Liu](https://kindxiaoming.github.io/pdfs/BIMT.pdf) [et al.](https://kindxiaoming.github.io/pdfs/BIMT.pdf) explores encouraging sparsity and modularity with a weight sparsity penalty that penalizes weights between neurons that are far apart (similar to wire length minimization in neuroscience). They find striking sparse graphs for a variety of tasks including arithmetic, group multiplication, and in-context learning.

Mechanistic Interpretability Challenges. Back in February, Stepen Casper [posed several challenges](https://www.lesswrong.com/posts/KSHqLzQscwJnv44T8/eis-vii-a-challenge-for-mechanists) to mechanistic interpretability practitioners, somewhat similar to the ["auditing game"](https://www.alignmentforum.org/posts/X2i9dQQK3gETCyqh2/chris-olah-s-views-on-agi-safety#Catching_problems_with_auditing) tests conducted at OpenAI in 2019. Recently, Stefan Heimersheim and Marius Hobbhahn took up this challenge and [solved the first one](https://www.lesswrong.com/posts/sTe78dNJDGywu9Dz6/solving-the-mechanistic-interpretability-challenges-eis-vii).

Learning Materials. Neel Nanda has been producing a wide range of resources on [getting started in mechanistic interpretability](https://www.neelnanda.io/mechanistic-interpretability/quickstart), including a number of videos [walking](https://www.youtube.com/watch?v=KV5gbOmHbjU) [through](https://www.youtube.com/watch?v=dCkQQYwPxdM) [different](https://www.youtube.com/watch?v=R3nbXgMnVqQ) [papers](https://www.youtube.com/watch?v=ob4vuiqG2Go) and also videos [explaining](https://www.youtube.com/watch?v=bOYE6E8JrtU) [transformers](https://www.youtube.com/watch?v=dsjUDacBw8o), and also a [list of open problems](https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj). Separately, TheMcDouglas produced a nice [illustration](https://www.lesswrong.com/posts/TvrfY4c9eaGLeyDkE/induction-heads-illustrated) of induction heads.

### [About](#about)

This is an informal collection of updates published on May 24th, 2023. Different sections have different authors. The overall update was edited by Chris Olah, Josh Batson, and Shan Carter.

Informal notes allow us to publish ideas that aren't as refined and developed as a full paper. Mistakes are very possible! We'd ask you to treat this note as more like some ideas a colleague is informally sharing with you, or a typical internet blog post, rather than a paper.
