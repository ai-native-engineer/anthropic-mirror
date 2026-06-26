<!-- source: https://transformer-circuits.pub/2024/july-update/index.html -->

# Circuits Updates - July 2024

  
  

We report a number of developing ideas on the Anthropic interpretability team, which might be of interest to researchers working actively in this space. Some of these are emerging strands of research where we expect to publish more on in the coming months. Others are minor points we wish to share, since we're unlikely to ever write a paper about them.

We'd ask you to treat these results like those of a colleague sharing some thoughts or preliminary experiments for a few minutes at a lab meeting, rather than a mature paper.

New Posts

* [The Next Five Hurdles](#hurdles)
* [What is a Linear Representation? What is a Multidimensional Feature?](#linear-representations)
* [The Dark Matter of Neural Networks?](#dark-matter)
* [Attention Pivot Tables](#pivot-tables)
* [Measuring feature sensitivity using dataset filtering](#feature-sensitivity)

  
  
  

  
  

## [The Next Five Hurdles](#hurdles)

Chris Olah; edited by Adam Jermyn

If you'd asked me a year ago what the key open problems for mechanistic interpretability were, I would have told you the most important problem was superposition.This might have been followed by the challenge of scalability: even if we can decompose very large models into understandable pieces, how can we turn that into understanding the model as a whole? Then I might have listed attention superposition as a very tertiary challenge. Since then, very significant progress has been made on superposition (e.g. [Bricken](https://transformer-circuits.pub/2023/monosemantic-features/index.html) [et al.](https://transformer-circuits.pub/2023/monosemantic-features/index.html), [Cunningham](https://arxiv.org/pdf/2309.08600) [et al.](https://arxiv.org/pdf/2309.08600), [Templeton](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)[et al.](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html), [Gao](https://arxiv.org/pdf/2406.04093) [et al.](https://arxiv.org/pdf/2406.04093)). As a result, it feels like a good moment to take stock and ask "what are the remaining hurdles between us and having a mechanistic understanding of neural networks?" From my personal perspective, a few hurdles stand out as major challenges we need to confront.

Before we dive in, it's worth describing the path I'm imagining us following, such that we'll run into these hurdles. Roughly, I imagine:

* We find interpretable features which are the ["variables" of the computation](https://transformer-circuits.pub/2022/mech-interp-essay/index.html) we're interested in.
* We understand the circuits that compute them.
* We somehow [turn this microscopic understanding of neural networks into a macroscopic picture](https://transformer-circuits.pub/2023/interpretability-dreams/index.html#possibilities) addressing the questions we care about.

![](images/img-001.png)

Following this path, I see five additional hurdles in our future:

* The Missing Features.  Historically, the first step of our path – find the interpretable features – was significantly blocked by superposition. It's now substantially unblocked: we can automatically extract large numbers of interpretable features. However, it seems that we are likely only extracting a small fraction of the features. There may be an enormous number of rare features we can't yet extract. Without major algorithmic innovation, it's possible we'll never be able to resolve the rarest features, leaving us with a kind of [neural network dark matter](#dark-matter).
* Cross-Layer Superposition. Consider a model with 100 layers. If the circuits the model is trying to implement are relatively shallow – perhaps most circuits are fewer than 10 steps deep – neurons in adjacent layers may not look that different to gradient descent. From the perspective of trying to map such a circuit onto the model architecture, representing something in layer 10 or 11 may not be that different. The corresponding neurons are almost in parallel from this perspective. As a result, there may be cross-layer superposition where the implementation of a feature doesn't clearly map to a particular layer. Our basic approach to dictionary learning doesn't provide a way to address this. (See also discussion [here](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#discussion-limitations).)
* Attention Superposition. Just as combinations of neurons can represent additional features in superposition, we believe combinations of attention heads can represent additional "attentional features" in a kind of [attention superposition](https://transformer-circuits.pub/2024/jan-update/index.html#attn-superposition). If so, we may be missing many of the fundamental units for understanding neural network computation – objects just as important as the idea of a "previous token head" or "induction head".Additionally, we may not be seeing the cleanest versions even of familiar features like induction heads, because these may be split across multiple heads or obscured by other features in superposition. And since many of the normal feature interactions are mediated by attention, this also makes circuit analysis difficult. It would be like trying to understand conv net circuits without the notion of "weight to a neuron at the position above me".In thinking about circuits, we often think about attention heads as having a role similar to "relative position" in a convolutional neural network. Consider the car detection circuit at the top of [Zoom In](https://distill.pub/2020/circuits/zoom-in/), which looks for windows above the car, and wheels below. The "above" and "below" relationships are generalized by attention heads, which allow both simple relationships like that, and also more abstract relationships. See also notes on the relationship between attention and convolution like structures [here](https://transformer-circuits.pub/2021/framework/index.html#virtual-weights-and-convolution-like-structure) and the practical example of relative position heads demonstrated by work like [Cordonnier](https://openreview.net/pdf?id=HJlnC1rKPB) [et al.](https://openreview.net/pdf?id=HJlnC1rKPB) ([interactive visualization](https://epfml.github.io/attention-cnn/)).
* Interference Weights. Just as we can think of features being represented in superposition of combinations of neurons, and attention heads as being represented in superposition across attention heads, we can also think of the "true neural network circuit weights" as being represented by a kind of [weight superposition](https://transformer-circuits.pub/2023/may-update/index.html#weight-superposition). If this is true, when we try to just multiply out the virtual weights between features, we'll observe "interference weights" – weights that exist in the neural network in some real sense, but which only exist as a compromise to allow the model to represent other circuits.The best present evidence that interference weights are real likely comes from scatter plots of logit weights between analogous features, as seen eg. in [these plots](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-universality) from Towards Monosemanticity. We've seen these come up in other circuit analysis work when we just multiply out virtual weights between features and the logits. These can be extremely confusing for circuit analysis, since they're basically nonsensical and shouldn't matter on distribution (although they [may help explain adversarial examples](https://transformer-circuits.pub/2022/toy_model/index.html#adversarial)).
* Zooming Out. Even if we can get to a point where we understand all the individual features and circuits of a neural network, there will be a further challenge of how to turn this into an understanding of neural networks as a whole. One popular answer to this is automated interpretability (which will surely help), but I would prefer to see an answer in terms of [larger-scale structure](https://transformer-circuits.pub/2023/interpretability-dreams/index.html#larger-scale), [universality](https://transformer-circuits.pub/2023/interpretability-dreams/index.html#universality), and [macroscopic correspondences](https://transformer-circuits.pub/2023/interpretability-dreams/index.html#macroscopic-microscopic).

Of course, after all of these, comes the final challenge of "actually understand the neural network, now that you don't have fundamental barriers".

Despite this list of challenges, there's a lot of cause for optimism. Firstly, we believe there are plausible paths to getting traction on many of these in the near future. They're relatively unexplored problems, and low hanging fruit seems at least plausible. Secondly, they don't necessarily block each other in the same way that the basic form of superposition often made it hard to investigate downstream problems. As a result, it seems possible to attack these problems in parallel. This also applies to the final goal of "understanding networks" or "neural network biology" – it feels less blocked on these, and more like we can genuinely attack it in interesting ways, but marginal progress on each of these makes it much easier.

  
  
  

  
  

## [What is a Linear Representation? What is a Multidimensional Feature?](#linear-representations)

Chris Olah; edited by Adam Jermyn

There's an important cluster of intuitions in interpretability research, going all the way back to [famous word embedding results](https://aclanthology.org/N13-1090.pdf), and even further. King − Man + Woman = Queen. Directions are the meaningful units. We can manipulate representations with vector arithmetic. Our work on superposition has built heavily on this basic intuition, and in the course of it we tried to pin this intuition down as the "Linear Representation Hypothesis".

Recent work by [Engels](https://arxiv.org/abs/2405.14860) [et al.](https://arxiv.org/abs/2405.14860) on multidimensional features has helped us realize that some of our writing on this topic has been unclear. So we wanted to return to this topic. What is a linear representation? Or perhaps, what should a linear representation be? What idea most crisply gets at the core of what's interesting and important for interpretability? We'll then ask what this definition would say about multidimensional features.

#### [A Confusing Definition](#linear-representations-confusing)

When we articulated the linear representation hypothesis in Toy Models, we [described](https://transformer-circuits.pub/2022/toy_model/index.html#motivation-directions) the hypothesis in terms of features as linear directions:

Let's call a neural network representation linear if features correspond to directions in activation space. In a linear representation, each feature f\_i has a corresponding representation direction W\_i. The presence of multiple features f\_1, f\_2… activating with values x\_{f\_1}, x\_{f\_2}…  is represented by x\_{f\_1}W\_{f\_1} + x\_{f\_2}W\_{f\_2}....

This definition conflates two importantly different claims: features as fundamentally one-dimensional objects, and features behaving linearly in the [mathematical sense](https://en.wikipedia.org/wiki/Linear_map). This is quite confusing!

#### [Mathematical Linear Representations](#linear-representations-mathematical)

In practice, we've come to use "linear representation" to specifically refer to this second property of features behaving in a "mathematically linear" way, regardless of whether they're one-dimensional or not. That is, a representation is linear if it obeys:

* Composition as Addition: The presence of a feature is represented by adding that feature. For example, "Feedback" in "informal writing style" is represented by the sum of vectors corresponding to those features or concepts.
* Intensity as Scaling: The intensity of a feature (or perhaps the model's confidence in its presence) is represented by magnitude. That is, if something appears to probably be talking about Monday, but the reference is ambiguous, we tend to see a correspondingly smaller scale in the feature direction added.It's possible that there may exist binary features (like [memorization features](https://transformer-circuits.pub/2023/toy-double-descent/index.html)) which only take on the values of 0 or 1. Such features might have a different scaling requirement, where they don't need to continuously scale. Of course, in many cases, we might still have probabilities of a binary variable that make it continuous again.

(In the future, we might want to consider adding a third criterion of being "almost linearly readable": the intensity of a feature can be retrieved with a linear function, up to some amount of noise. This is similar to [Vaintrob](https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in) [et al](https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in). For well-separated one-dimensional features, this follows from other properties, but for multidimensional features it might be necessary. However, we're neither confident what the right formalization of this would be, nor confident it should be part of being a "linear representation" rather than some other property.)

Between "features are one-dimensional" and "features behave mathematically linearly", we believe the mathematical linearity property is much deeper and is generally the one we care about. If there exist multidimensional features, most mechanistic interpretability work can adapt with little change. (If anything, our work might get easier!) But if representations are not mathematically linear in the sense described above, it's back to the drawing board – a huge number of questions like "how should we think about weights?" are reopened. So it seems important to have a term for this second question and to treat it as distinct.

#### [Linear Multidimensional Features](#linear-representations-multidimensional)

We now properly turn to the question of [multidimensional features](https://arxiv.org/abs/2405.14860) or [feature manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds).This is very overdue! In Toy Models, we actually promised to explain how our definition of a linear representation could be extended to such features, but failed to publish the appendix on this. It turns out that the new definition of a linear representation can admit multidimensional features but it will constrain their geometry.

Mathematical linearity requires a multidimensional feature to obey two properties, as mentioned above. Composition as Addition requires that the feature be able to be added to other features. This means the manifold it forms must be orthogonal or (under superposition) almost orthogonal to other features.This is actually not strictly required, but it is a sufficient condition for composition under addition to hold. The actual necessary condition is somewhat more complicated.

The more interesting requirement is Intensity as Scaling which significantly constrains the geometry of possible manifolds. Every point on the manifold forms a "ray" as you scale it, representing that feature at different levels of intensity. Jointly these form a path by which the entire manifold contracts back to zero.Of course, the zero point for all features can be shifted by a bias. Then semantic changes need to be angular movement orthogonal to this.

![](images/img-002.png)

#### [Aside: Potential Issues around Feature Manifold Embeddings](#linear-representations-embedding)

As mentioned above, there's an interesting additional property which is that the model likely wants to "linearly read" features and recover them without noise. One way this could be accomplished by having features be almost orthogonal, and then linear readability is implicit in the usual definition of a linear representation.

But in a feature manifold, nearby points on the manifold are by definition nearly parallel. That's the point! Despite this, the model may want to distinguish points more than the intrinsic topology's natural embedding would suggest. (Our previous update on [feature manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds) presented some very preliminary investigations of this in a toy setup.)

![](images/img-003.png)

We suspect this idea that feature manifolds may be embedded in more complex ways than their topology suggests, in order to achieve a given distance metric, may actually be quite deep and important. For example, it may be tempting to believe that, if the manifold has a clean projection on its early principal components, the rest is noise. But in fact, that noise may be essential to achieving the correct geometry.

#### [Multidimensional Features and Directions](#linear-representations-multi-directions)

If we adopt this new definition of a linear representation, does evidence like the [Li-Nanda exchange](https://transformer-circuits.pub/2022/toy_model/index.html#comment-nanda) no longer support it? Informally, many results cited in support of the linear representation hypothesis either extract information with a linear probe, or add a vector to influence model behavior. These are often discussed in terms of modifying directions, so you might worry they wouldn't apply if we allowed multidimensional features! But they're actually statements about the property of being mathematically linear.

One way to see this is to consider the "rays" in a hypothetical linear multidimensional feature. These rays have a fixed semantic meaning. They are essentially one-dimensional features which are "locked on" to the semantic meaning of a particular point on the manifold. From this perspective, linear multidimensional features are something like an infinite, continuous collection of one-dimensional features – a kind of manifold of features. If you're only interested in one pre-defined semantic property, as is the case in probing, it's still the case that property corresponds to a direction.

![](images/img-004.png)

The main difference is that these "rays" aren't privileged. If we considered these to be features, there would be an infinite set of potential features.

This starts to get at another question: what makes something a multidimensional feature or feature manifold, rather than a collection of co-occurring one-dimensional features? It seems plausible that any multidimensional feature probably can be understood as a collection of one-dimensional features, which form a basis parameterizing the manifold. But it may be more natural to understand them as a multidimensional feature if there is continuity. For example, if "midnight on Tuesday" is represented as being between Tuesday and Wednesday, that would seem like some evidence that there really is a continuous representation between them, and cut in favor of thinking of them as a multidimensional feature. Another question is whether there is a privileged basis for the manifold, a set of one-dimensional features which are a particularly natural way to parameterize it.

#### [On Definitions](#linear-representations-definitions)

I'm not at all confident that any of the definitions or frames above will stand up to the test of time. Definitions can and should change and be fluid in research.There's a beautiful book by Lakatos called [Proofs and Refutations](https://en.wikipedia.org/wiki/Proofs_and_Refutations) on how it's often very productive and important for definitions to evolve – if you haven't read it, it's fantastic. As we understand things more deeply, we'll find deeper ideas that cut reality apart. Let's keep asking what those ideas are.

It's also worth keeping in mind that imperfect theories and frames [can still be productive](https://transformer-circuits.pub/2024/april-update/index.html#caloric-theory). It may be a long time before we really know the right way to think about things, but that may not be as bad as it seems.

  
  
  

  
  

## [The Dark Matter of Neural Networks?](#dark-matter)

Chris Olah; edited by Adam Jermyn

In [recent work](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html), we trained a sparse autoencoder that resolved 13 million features. However, it seems like these features are only scratching the surface. With 13 million features, we find features for some of San Francisco's neighborhoods, but Claude knows about small coffee shops in San Francisco, and can answer questions about intersections of streets. Presumably there are at least a hundred such businesses, streets, parks and so on per San Francisco neighborhood. This suggests at least two orders of magnitude more features, which are correspondingly rarer in the dataset, and probably more.

There are many other hints of extremely rare and numerous features. For example, you can make a similar argument to the above about features corresponding to people (Claude knows who I am, but we're clearly a long ways from extracting a "Chris Olah" feature). But a more interestingly different example is the possibility that there may be "memorization features" (along the lines of [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-fsa)[–](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-fsa) [Finite State Automata](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-fsa)) – these could be numerous and extremely sparse. Both examples are illustrative of a broader possibility: it may be that neural networks have exceptionally rare and sparse features. It's possible these are the vast majority of features (although less important, since they're uncommon). And, barring significant breakthroughs, it may be effectively impossible for us to resolve features rarer than some level.

From this perspective, these rare features may be a kind of "dark matter" of interpretabilityOriginally, dark matter just meant “matter we could not observe directly, but whose influence we can observe”. Over time as the nature of dark matter was better-constrained a consensus developed that it is likely specifically non-baryonic matter. In drawing this analogy, we are referring to the original (broader) notion, which feels fitting because Interpretability is much closer as a field to Cosmology of the early 20th century than to Cosmology of the early 21st century. . Perhaps the vast majority of features, but so essentially invisible because they're so rare. I find this analogy helpful for two reasons. Firstly, I think it's helpful for evoking the image of a scientific field where some of the objects of study are inaccessible. Secondly, it suggests a research agenda of trying to indirectly study these invisible memorization features.

Continuing this analogy: dictionary learning has given us a telescope, allowing us to stare into neural networks and observe features. Our earliest experiments could observe only the brightest "stars" (the most important and common features). As we refine the science of dictionary learning, we can resolve more and more faint stars (rarer features). But it may be that a large fraction of the neural network universe is effectively unobservable dark matter.

(A critical open question here is whether we can find variants of dictionary learning which are orders of magnitude more efficient, allowing us to resolve more features. This doesn't seem totally impossible, but also seems very uncertain. The answer to this question will determine whether sufficiently rare features are effectively impossible to resolve.)

  
  
  

  
  

## [Testing Base Model Quality Using Attention Pivot Tables](#pivot-tables)

Nicholas L Turner, Adam Pearce, Trenton Bricken, Adam Jermyn; edited by Chris Olah

Recently, we tried to reproduce one of the key results from our team's early paper, A Mathematical Framework for Transformer Circuits: "pivot tables" that allow us to interpret one-layer transformers as [implementing skip-trigrams](https://transformer-circuits.pub/2021/framework/index.html#interpretation-as-skip-trigrams). An example table can be seen below:

![](images/img-005.png)

We found these results were unexpectedly sensitive to subtle issues in training transformers, making it quite fiddly to reproduce. This update shares the details we needed to reproduce the results.

We think this method is generally quite useful for studying attention in one-layer models (which may be helpful as we study Attention Superposition), and we hope sharing more detailed guidance will help others use it. We also hope that this can be more generally helpful as a case study in how subtle details can affect interpretability results.

#### [Constructing Pivot Tables](#pivot-tables-construction)

Pivot tables visualize the behavior of a model along the path from the input embeddings to a specific attention head and from there directly out to the logits. In a 1-layer attention-only model, this is the entirety of the QK and OV circuits as [illustrated](https://transformer-circuits.pub/2021/framework/index.html#splitting-attention-head-terms-into-circuits) in A Mathematical Framework.

Put another way, these tables summarize two vocab\_size X vocab\_size matrices. The first matrix (the QK circuit) quantifies the amount that any query token attends to a key token in the context (pre-softmax, using the attention “scores” or logits). The other matrix (OV circuit) measures the effect that completely attending to a given key token has on the models’ output logitsUp to a scaling factor from any layer norm before the unembedding.. Both of these matrices completely ignore the effects of positional embeddings.

Defining some terms, let:

N\_v be the vocab size,

d\_{\textrm{model}} be the residual stream size,

d\_{\textrm{head}} be the head dimension,

W\_E \in \mathcal{R}^{d\_{\textrm{model}} \times N\_v} be the embedding matrix,

W\_U \in \mathcal{R}^{N\_v \times d\_{\textrm{model}}} be the unembedding matrix,

W\_Q, W\_K, W\_V \in \mathcal{R}^{d\_{\textrm{head}} \times d\_{\textrm{{model}}}} be a head’s input weights,

W\_O \in \mathcal{R}^{d\_{\textrm{model}} \times d\_{\textrm{head}}} be a head’s output weights,

L\_A(x) be the pre-attention layer norm (if present),

L\_U(x) be the pre-unembed layer norm (if present),

and \beta\_U be the pre-unembed layer norm’s bias.

Then we can write the circuit matrices as:

C\_{QK} = L\_A(W\_E)^T W\_Q^T W\_K L\_A(W\_E)

C\_{OV} = W\_U L\_U(W\_O W\_V L\_A(W\_E)) - \beta\_U

These forms give some ways to check your work when writing this code. The QK circuit should exactly match the attention logits when removing positional information from the model. The OV circuit should also match the output logits when you ensure that a head’s output from attending to a single token is the only thing in the residual stream (and after removing the layer norm bias).

We subtract the unembedding’s layer norm bias since that just represents a direct bias on the logits. If a model has a strong propensity to ignore specific tokens, that’s all you’ll see in the OV circuit instead of the relative effect.

Once we form these two large matrices, we score each key token according to the following heuristic function H\_K and show the top N within the tables. We match each key with a set of query tokens that attend to this key token by a similar heuristic H\_Q, and the affected output tokens with H\_O.

H\_K(k) = max(C\_{QK}[:, k] \* P[:]) \* max(C\_OV[:, k]) \* P[k],

H\_Q(q, k) = C\_{QK}[q, k] \* P[q],

H\_O(o, k) = C\_{OV}[o, k]

where P[t] is the likelihood that a particular token ID t appears in the training set. The heuristic is designed to select keys which have strong effects across attention and outputs. We currently estimate P[t] through sampling. The original pivot tables only reported applying the P multiplication to the k axis as,

H'\_K(k) = max(C\_{QK}[:, k]) \* max(C\_{OV}[:, k]) \* P[k]

but we see slightly better results applying it to both axes.

#### [Practical Considerations](#pivot-tables-practicalities)

We see interpretable skip-trigrams across models with different architectures, including using different positional embeddings and those with or without layer norm. The best runs show ~25-75% interpretable trigram entries alongside a large number of copying entries, and we recommend suspicion in interpreting tables which show less than ~10%, as you may be “interpreting” mirages. These proportions come from small models with only 1-4 layers and could easily change outside that regime.

Still, within this space we found that a few variables significantly increase or decrease the likelihood of success of finding interpretable skip-trigrams:

* Training hyperparameters: Training runs with hyperparameters that perform poorly tend to show confusing pivot tables.
* Training dataset: Having a dataset that consists of domains that are easy to interpret (e.g., english natural language, python code, etc.) helps to see the signal that a model has learned. It can be difficult to tell the difference between a model that’s successfully learned structure that you cannot read and a model that hasn’t learned useful structure.
* Number of layers: Unsurprisingly, single-layer models most readily show structure in pivot tables, although the later layers of multi-layer models also tend to show legible structure too.

  
  
  

  
  

## [Measuring feature sensitivity using dataset filtering](#feature-sensitivity)

Nicholas L Turner, Adam Jermyn, Joshua Batson; edited by Joshua Batson

In our recent work with dictionary learning features, it has been easier to evaluate a feature’s specificity to a concept than its sensitivity. We define specificity as the likelihood that a concept is present given that a detector fires (e.g., a learned feature has activation of a certain level), which we have evaluated by inspecting dataset examples where the feature is active. We define sensitivity as the likelihood that the detector fires given that the concept is present. This has been more difficult to measure because accurately determining the presence of a potentially vague concept over a large corpus of text requires some care as we describe below.

Here, we explore the use of Claude to help us quantify sensitivity by rating the relevance of a concept in text. We find that different versions of Claude typically agree with human spot checks (and one-another). Further, upon quantifying feature specificity, we find that features are not perfectly described by the loose concept we’ve associated with them in Scaling Monosemanticity. Instead, we find some evidence that multiple features collectively represent broad topics, although it’s unclear whether this understanding can fully account for the gaps in how features respond.

#### [A dataset filtering method](#feature-sensitivity-method)

It is important to assess sensitivity using a representative distribution of how a concept is likely to appear. In [Towards](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-sensitivity) [Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-sensitivity), we studied a few simple concepts for which there were probabilistic computational proxies (e.g., DNA sequences, modeled as random strings drawn from the relevant alphabet). These proxies measured the extent to which a text contained one of those simple concepts, but they are not applicable to more sophisticated concepts. Existing automated interpretability methods can evaluate more sophisticated concepts by generating “adversarial examples” to probe the bounds of a feature’s responses, but those may also be subject to blind spots that are difficult to predict in advance.

We have recently tried using Claude to quantify the extent to which a concept is relevant to a sample of text. These ratings can be used to filter a broad text dataset for instances of the concept, and, supposing that the dataset forms a representative distribution of the concept, the frequency with which a feature fires on that dataset is a measure of its sensitivity. This way, Claude only needs to recognize instances of the concept rather than faithfully generate the full breadth of the concept’s usages and all of the possible ways it might arise in the right proportions.

In brief, we ask a version of Claude to assess how relevant a concept is to a small sample of text using the following prompt:

Here is a text sample to analyze:

{context}

And here is a potentially fuzzy concept:

{concept}

How relevant is this concept to the text sample?

First write out some reasoning about how relevant the concept is inside  tags. Consider both how frequently the concept is directly mentioned or alluded to as well as how central the concept is to the overall meaning of the text.

After the  section, output your relevance score for that concept from 0-10 inside  tags. 0 means that the concept is not relevant at all to and 10 means that the concept is maximally relevant.

We initially validate the filtering task over a sample of snippets where the relevant feature activates (shown for the “Brain Sciences” feature below). As described in Scaling Monosemanticity, the interpreted concept is present in most places where the features activate, but the relevance of that concept to the text still varies. We find that different versions of Claude do a consistent job of judging concept relevance. This is reflected in high spearman correlation values (\rho) above each subplot below and a low percentage of ratings having differences greater than 2 (although Claude 3 Haiku tends to give more “all-or-nothing” ratings than other versions). Manually checking these points was reassuring, so we moved to larger datasets.

![](images/img-006.png)

#### [Feature sensitivity on filtered data](#feature-sensitivity-analysis)

We then had Claude 3.5 Sonnet filter 160,000 snippets of 128 tokens each for each of the four concepts we highlighted within the [Feature Tour of Scaling](https://s3-frontend.infra.ant.dev/anthropic-serve/colah/drafts/scaling-monosemanticity/index.html#assessing-tour) [Monosemanticity](https://s3-frontend.infra.ant.dev/anthropic-serve/colah/drafts/scaling-monosemanticity/index.html#assessing-tour). Sadly, this procedure didn’t yield sufficient data for the (relatively rare) Golden Gate Bridge feature, but we inspected the results for the other three features. We performed inference on each snippet within a larger context of 2048 tokens and we considered a feature to have detected the concept if it was active anywhere within the snippet, analyzing each feature’s maximum activation over the tokens within that snippet.

![](images/img-007.png)

The highlighted features mostly do not respond within snippets where the concept is present, even where models (and human spot-checking) rate the concept as highly relevant to the text. Below, we list example snippets for each feature where the Scaling Monosemanticity feature does not activate on any token.

Brain sciences:

Axons do not extend through the scar and their growth appears to be inhibited by it. Molecular components that may contribute to this inhibitory activity include the extracellular matrix glycoprotein tenascin-R (TN-R) and the myelin-associated neurite outgrowth inhibitors myelin-associated glycoprotein (MAG) and Nogo.

TN-R

TN-R has been implicated in a variety of cell-matrix interactions involved in the molecular control of axon guidance and neural cell migration during development and regeneration of CNS

Claude’s reasoning:

This text sample is highly relevant to neuroscience and academic research on brains. The passage discusses specific molecular components and processes involved in axon growth and regeneration in the central nervous system (CNS). Key neuroscience concepts and terms are mentioned throughout:

1. Axons: The text focuses on axon growth and inhibition, which are fundamental topics in neuroscience.

2. Central Nervous System (CNS): Explicitly mentioned, indicating a focus on brain and spinal cord research.

3. Molecular components: The text discusses specific proteins and glycoproteins involved in neural processes (tenascin-R, myelin-associated glycoprotein, Nogo).

4. Neural development and regeneration: The passage touches on both developmental neuroscience and research on neural regeneration.

5. Cell-matrix interactions: The text mentions these in the context of axon guidance and neural cell migration, which are important areas of neuroscience research.

The entire text is centered around neuroscientific concepts and research, with no content that falls outside this domain. It appears to be an excerpt from an academic or research-oriented source discussing current understanding in the field.

Relevance rating of “Discussions of neuroscience and related academic research on brains or minds”: 10

Transit infrastructure:

sense, there is plenty of traffic from the ports to south of the city,

and by making the full ring, that traffic would get a choice of direction

around the city depending on time of day and commuting patterns. And this

holds true for every trip across opposite ends of the city.

------

Sharlin

Anyone have insight into different tunnel-building technologies? In

particular, when is a boring machine a more appropriate solution than

drilling-and-blasting?

~~~

jpatokal

It's complicated and I'm not an expert, but I understand the main risk with

TB

Claude’s reasoning

The text sample is highly relevant to the concept of transit infrastructure. The first paragraph discusses traffic patterns, city ring roads, and commuting, which are all key aspects of urban transit infrastructure. The mention of ports and traffic flow around a city indicates discussion of transportation networks.

The second part, while a separate question, is directly related to tunnel-building technologies. Tunnels are a crucial component of many transit infrastructure projects, especially in urban areas. The comparison between boring machines and drilling-and-blasting methods is specifically about construction techniques for transit infrastructure.

While the term "transit infrastructure" is not explicitly mentioned, the entire text revolves around topics that are central to this concept - road networks, traffic management, and tunnel construction for transportation purposes. The discussion is focused on methods and considerations for developing and improving urban transportation systems.

Relevance rating of “Transit infrastructure”: 9

Popular tourist attractions

of hell, celestial beings." "And sitting here, this is paradise, isn't it?" "To appreciate the full meaning of Angkor Wat, I take to the skies." "Suryavarman's vision becomes clear." "It's a homage of the gods and a statement of his own divinity." "There it is, the sacred mountain, protected on all sides by moats representing mythic oceans." "But in reality the moat could not keep the dangers of the outside world at bay." "In 1177 the Kingdom of Angkor was invaded by the neighbouring

Claude’s reasoning:

The text sample is highly relevant to the concept of "Monuments and popular tourist destinations" for several reasons:

1. Angkor Wat is explicitly mentioned, which is one of the most famous ancient monuments and a major tourist attraction in Cambodia.

2. The text describes architectural features of Angkor Wat, such as its moats and sacred mountain design, which are typical elements of monumental architecture.

3. The passage mentions "Suryavarman's vision," referring to the king who built Angkor Wat, indicating its historical significance as a monument.

4. The text describes taking to the skies to appreciate the full meaning of Angkor Wat, which is a common tourist activity (aerial tours) for viewing large monuments.

5. The description of Angkor Wat as "a homage of the gods and a statement of his own divinity" underscores its importance as a religious and cultural monument.

6. The text alludes to the site's vulnerability to invasion, which is often a factor in the historical narrative presented to tourists at such destinations.

While the text doesn't explicitly discuss tourism, the focus on Angkor Wat and its features strongly implies its status as a popular tourist destination. The detailed description and historical context provided are typical of the information presented to visitors at such sites.

Relevance rating of “Monuments and popular tourist destinations”: 9

For each feature in the dictionary, we then counted the number of filtered snippets (with rating >=9) where that feature has nonzero maximum activation. The features that we’ve highlighted in Scaling Monosemanticity (red line) reside within the top ~0.1-10% of features, but they are far from the most sensitive.

![](images/img-008.png)

The most sensitive features still do not capture all snippets. They typically show some relation to the original concept, but sometimes show reduced specificity. For brain sciences, the most responsive feature seems to activate for descriptions of experimental methods within studies involving human subjects (these can involve brain sciences but this is not always clear). The feature most responsive to transit infrastructure snippets was difficult to interpret and is labeled as “unknown”. The best of this set was the feature most responsive to snippets about popular tourist attractions. It (1M/11480) responds to descriptions of the history of tourist attractions. It activates within all snippets with relevance rating >= 9, though if that threshold is moved lower the feature its sensitivity is no longer perfect. We display the sensitivity of each feature below, as well as its specificity in a similar fashion as in Scaling Monosemanticity.

![](images/img-009.png)
![](images/img-010.png)

#### [How feature activations might cooperate](#feature-sensitivity-cooperation)

These findings are reminiscent of [earlier results](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-sensitivity) where features could represent a more specific subset of the concept that we most readily associated with them. For example, we’ve previously described a set of features responding to arabic script in a 1L model, which covered different cases of definite articles. In other words, here a complementary “family” of features responded to the slightly different situations of predicting tokens within a broader topic.

If we manually inspect features that activate on tokens “missed” by the highlighted features, you can often find some that likely contribute to representing the concept of interest. For example, we found a feature that seems to favor firing very close to the term “brain” in different contexts, where the original brain science feature often does not activate. These complementary features still show some specificity to the original concept of interest (shown below). This is particularly true for features from the SAE with more features, perhaps reflecting “higher resolution” in the learned features.

![](images/img-011.png)

We also inspect how the 50 features that respond to the most snippets cover the snippets with highest relevance ratings (black is active - we show a more inclusive set for Popular Tourist attractions to see more diversity). We see a vertical banding pattern of activations, which suggests that there are multiple different types of snippets that we’ve caught using our filtering procedure where the network’s representation strongly differs across these types.

![](images/img-012.png)
![](images/img-013.png)
![](images/img-014.png)

Taken together, these results suggest that the sensitivity of one feature is not representative of how well the SAE captures the model’s representation of a concept. Our language about features then seems to require some caution to indicate that a feature’s activations may be subtly related to a concept rather than fully representing that concept. More generally, insofar as our SAE represents network internals in a faithful and interpretable fashion, we should be able to account for all clear instances of a concept using a cooperation of interpretable features. We are unable to fully do that here, so these feature representations require deeper inquiry. In the worst case, this may be a sign that our current dictionary learning models still do not capture the breadth of Claude 3 Sonnet’s knowledge on important topics due to “dark matter” or other fundamental problems. There still are many ways that we could investigate this; we could find a way to automate the process of finding features that complement one another’s activations or inspect the other features with high cosine similarity to the highlighted ones. Future work will explore these avenues.
