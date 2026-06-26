<!-- source: https://transformer-circuits.pub/2022/solu/index.html -->

# Softmax Linear Units

### Authors

[Nelson Elhage∗†](https://nelhage.com/), Tristan Hume∗, Catherine Olsson∗, [Neel Nanda∗§](https://www.neelnanda.io/), Tom Henighan†, Scott Johnston†, Sheer El Showk†, Nicholas Joseph†, Nova DasSarma†, [Ben Mann†](https://benjmann.net/), Danny Hernandez, Amanda Askell, Kamal Ndousse, Andy Jones, Dawn Drain, Anna Chen, Yuntao Bai, Deep Ganguli, Liane Lovitt, [Zac Hatfield-Dodds](https://zhd.dev), Jackson Kernion, Tom Conerly, Shauna Kravec, Stanislav Fort, Saurav Kadavath, Josh Jacobson, Eli Tran-Johnson, Jared Kaplan, Jack Clark, Tom Brown, Sam McCandlish, Dario Amodei, [Christopher Olah‡](https://colah.github.io/)

### Affiliation

[Anthropic](https://www.anthropic.com/)

### Published

June 27, 2022

\* Core Research Contributor; † Core Infrastructure Contributor; § Work done while at Anthropic; ‡ Correspondence to <colah@anthropic.com>; Author contributions statement below.

  
  
  

  
  

## 1. Introduction

As Transformer generative models continue to gain real-world adoption , it becomes ever more important to ensure they behave predictably and safely, in both the short and long run.  Mechanistic interpretability – the project of attempting to reverse engineer neural networks into understandable computer programs – offers one possible avenue for addressing these safety issues: by understanding the internal structures that cause neural networks to produce the outputs they do, it may be possible to address current safety problems more systematically as well as anticipating future safety problems.

Until recently mechanistic interpretability has focused primarily on CNN vision models , but some recent efforts have begun to explore mechanistic interpretability for transformer language models .  Notably, we were able to reverse-engineer 1 and 2 layer attention-only transformers  and we used empirical evidence to draw indirect conclusions about in-context learning in arbitrarily large models .

Unfortunately, it has so far been difficult to mechanistically understand large models due to the difficulty of understanding their MLP (feedforward) layers.  This failure to understand and interpret MLP layers appears to be a major blocker to further progress. The underlying issue is that many neurons appear to be polysemantic , responding to multiple unrelated features. Polysemanticity has been observed before in vision models, but seems especially severe in standard transformer language models.  One plausible explanation for polysemanticity is the superposition hypothesis , which suggests that neural network layers have more features than neurons as part of a “sparse coding” strategy to simulate a much larger layer.  If true, this would make polysmenticity a functionally important property and thus especially difficult to remove without damaging ML performance.

In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers.  However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable.  Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.

Although preliminary, we argue that these results show the potential for a general approach of designing architectures for mechanistic interpretability: there may exist many different models or architectures which all achieve roughly state-of-the-art performance, but which differ greatly in how easy they are to reverse engineer. Put another way, we are in the curious position of being both reverse engineers trying to understand the algorithms neural network parameters implement, and also the hardware designers deciding the network architecture they must run on: perhaps we can exploit this second role to support the first. If so, it may be possible to move the field in a positive direction by discovering (and advocating for) those architectures which are most amenable to reverse engineering.

This paper is organized as follows. In [Section 2](#section-2), we give an overview of our key results. In [Section 3](#section-3), we provide background on mechanistic interpretability, the role of interpretable neurons, the challenge of polysemanticity and the superposition hypothesis. In [Section 4](#section-4) we motivate and introduce SoLU. In [Section 5](#section-5) we present experimental results showing that SoLU gives performance roughly equivalent to standard transformers, as measured by loss and downstream evaluations.  In [Section 6](#section-6) we run the experiments showing that SoLU leads to MLP neurons that are easier to interpret, and also present several interpretability discoveries that we were able to make with SoLU models and could not make without them.  [Section 7](#section-7) reviews related work, and [Section 8](#section-8) discusses the bigger picture and possible future directions.

  
  
  

  
  

## 2. Key Results

SoLU increases the fraction of MLP neurons which appear to have clear interpretations, while preserving performance. Specifically, SoLU increases the fraction of MLP neurons for which a human can quickly find a clear hypothesis explaining its activations from 35% to 60%, as measured by blinded experiments – although the gain is smaller for our largest models (see [Section 6.2](#section-6-2)).  This gain is achieved without any loss in performance: test loss and NLP evals are approximately the same for SoLU and non-SoLU models (see [Section 5](#section-5)) .

SoLU’s benefits may come at the cost of “hiding” other features.  Despite the benefits mentioned above, SoLU is potentially a double-edged sword. We find theoretical and empirical evidence that it may “hide” some non-neuron-aligned features by decreasing their magnitude and then later recovering it with LayerNorm (see Sections [4.3](#section-4-3) and [Section 6.4](#section-6-4)) .  In other words, SoLU causes some previously non-interpretable features to become interpretable, but it may also make it even harder to interpret some already non-interpretable features.  On balance, however, it still seems like a win in that it pragmatically increases our understanding.

Architecture affects polysemanticity and MLP interpretability. Although it isn't a perfect solution, SoLU is a proof of concept that architectural decisions can dramatically affect polysemanticity, making it more tractable to understand transformer MLP layers. This suggests that exploring how other architectures affect polysemanticity could be a fruitful line of further attack. More generally, it suggests that designing models for mechanistic interpretability – picking architectures we expect to be easier to reverse engineer – may be a valuable direction.

An overview of the types of features which exist in MLP layers. SoLU seems to make some of the features in all layers easily interpretable. Prior to this, we'd found it very difficult to get traction on rigorously understanding features in MLP layers. In particular, despite significant effort, we made very little progress understanding the first MLP layer in any model. Simply having a sense of what kinds of features to expect in different layers was a powerful tool in reverse engineering models in the original circuits thread , and this moves us in a similar direction. We find that early features often deal with mapping raw tokens to semantic meaning (e.g. dealing with multi-token words, or tokens in different languages), more abstract features in middle layers, and features involved in mapping abstract concepts back to raw tokens in late layers. Detailed discussion can be found in [Section 6.3](#section-6-3).

Evidence for the superposition hypothesis. Very little is known about why polysemanticity occurs. In the mechanistic interpretability community, superposition is often treated as the default hypothesis simply because it seems intuitively more compelling than other explanations, but there is little evidence. Our SoLU results seem like moderate evidence for preferring the superposition hypothesis over alternatives.

  
  
  

  
  

## 3. Background

Before presenting the SoLU results, it is worth going through why understanding the MLPs in transformer language models is hard, and specifically why the superposition hypothesis is plausible and thus why polysemanticity might be difficult to avoid.

### 3.1 The Importance of Understanding Activations

First of all, why is it even important to understand neurons/activations?  Previous work on language model mechanistic interpretability was (for example) able to discover induction heads without needing to understand activations.  And ultimately, don’t we only need to understand the parameters, which provide a complete description of the neural net?

A useful analogy might be to think of the parameters as a compiled computer program that we’re trying to understand, and the activations as variables in that program.  Just as a line of code in a computer program only makes sense if you understand what the variables represent, a parameter in a neural network can only be understood if you understand the activations it links together. This idea was originally articulated by Voss et al. , and is described in more depth in a [informal note on intuition](https://transformer-circuits.pub/2022/mech-interp-essay/index.html) accompanying this paper.  Concretely, there are many more parameters than activations, so the activations seem like a more likely “key” to what’s going on.

There are special cases where it's possible to side-step understanding activations, by rewriting a neural network into an equivalent model that doesn't make reference to intermediate activations. This is how we were able to reverse engineer attention-only transformers previously. However, the non-linear structure of MLP layers is not amenable to such tricks: if we want to understand transformers with MLP layers, it appears we must figure out how to understand what the activations of MLP layers encode.

### 3.2 Decomposing Activations and the Role of Bases

To get to polysemanticity and the superposition hypothesis, it’s first useful to talk about bases in neural network layers. The vector space of a neural network layer’s activations is called the "representation." For toy low-dimensional neural networks, it may be possible to explicitly visualize or analyze this space . But as the dimensionality increases, the curse of dimensionality takes hold and the volume of the space exponentially increases. The only path we see to fully understand such a representation is to decompose it into independently understandable components, which we'll call features. Finding such a decomposition is the difference between needing to understand N features and \exp(N) representational volume. (This might be seen as similar to how, in reverse engineering a computer program, we don't just think of the program's state space as a high-dimensional vector: we decompose it into a set of variables representing different things.)

One approach would be to search for a meaningful basis (or meaningful directions that might be part of a basis). This approach is often taken in the context of word embeddings (e.g. ), although also in other contexts (e.g. ). For word embeddings, there doesn't appear to be an alternative: word embeddings generally have what we call a [non-privileged basis](https://transformer-circuits.pub/2021/framework/index.html#def-privileged-basis) , since it can be freely rotated. If a representation, like a word embedding, is surrounded by purely linear operations such as matrix multiplies or addition, then we can “change basis” by applying any invertible matrix M with the matrix multiply before the layer and M^{-1} with the matrix multiply after, which leaves the final output invariant but changes the specific activations. As a result, such representations don't come with any "special basis" which might hint at how to understand them. The correct basis must be discovered. For example, in a word embedding, one might define a gender direction by subtracting "man" and "woman" .

In contrast, many neural networks have some representations with a [privileged basis](https://transformer-circuits.pub/2021/framework/index.html#def-privileged-basis) . In these representations, something about the network makes the default basis special. For example, if the layer has a coordinate-wise non-linear activation function (eg. ReLU), this “breaks the symmetry," distinguishing the specific basis of the activations as the unique basis in which the nonlinearity is applied. This doesn't guarantee that features will align with the basis, but it makes it plausible. In many ways, this is the ideal outcome if possible: not only does it allow us to side-step the difficult question of how to find a meaningful basis, but mechanistically reasoning about neural networks is easier when the basis one is reasoning in aligns cleanly with computation like activation functions.

![](images/img-001.png)

In transformers, the token embeddings, residual stream, and attention vectors are non-privileged, while MLP layer activations are privileged.

### 3.3 Neurons and Polysemanticity

We call the dimensions of a representation with a privileged basis "neurons." We often find neurons which map extremely cleanly to clear concepts. In the context of vision, these have ranged from low-level neurons like [curve detectors](https://distill.pub/2020/circuits/curve-detectors/) and [high-low frequency detectors](https://distill.pub/2020/circuits/frequency-edges/), to more complex neurons like [oriented dog-head detectors](https://distill.pub/2020/circuits/zoom-in/#claim-2-dog) or [car detectors](https://distill.pub/2020/circuits/zoom-in/#claim-2-superposition), to extremely abstract neurons corresponding to [famous people](https://distill.pub/2021/multimodal-neurons/#person-neurons), [emotions](https://distill.pub/2021/multimodal-neurons/#emotion-neurons), [geographic regions](https://distill.pub/2021/multimodal-neurons/#region-neurons), and [more](https://distill.pub/2021/multimodal-neurons/#guided-tour-of-neuron-families) . The claim that some neurons really do correspond to interpretable features is crucial to what kinds of interpretability research make sense, so it's worth noting that these interpretations aren't just casual claims made on superficial evidence. In some cases, these interpretations have held up to detailed investigation: Cammarata et al.  spend two papers investigating a handful of curve detector neurons and the circuits that implement them, using seven different lines of evidence to corroborate that the neurons really are curve detectors, with the goal of dispositively establishing that at least some neurons really are interpretable.

However, there are also many neurons which don't appear to correspond to understandable concepts – and we’ve found this to be especially true in transformer language models. One possibility is that these are in some sense alien features: they actually are the true features and they're just difficult for humans to understand (see  and discussion ). Sometimes features which are initially incomprehensible become obvious once the right hypothesis is proposed (e.g. ), so it's certainly possible! But many of these neurons appear to respond to several unrelated but individually understandable features, such as a neuron which responds to cat heads, fronts of cars, and paws. While we can't totally rule out that there isn't some deep commonality between a cat's paw and the front of a car, it seems like the simpler explanation is that the network has grouped several unrelated features together. We call these [polysemantic neurons](https://distill.pub/2020/circuits/zoom-in/#claim-1-polysemantic) .

Note that polysemanticity is what one would expect to observe if features weren't actually aligned with the privileged basis. But why wouldn't the features align with the neurons? While it could simply be chance, there's an alternative option: the superposition hypothesis .

### 3.4 The Superposition Hypothesis

Roughly, the idea behind the superposition hypothesis is that neural networks "want to represent more features than they have neurons," so they exploit a property of high-dimensional spaces to simulate a model with many more neurons. (Note that as a matter of terminology we use "polysemanticity" to refer to the empirical phenomenon of neurons responding to multiple features, and "superposition" to refer to the hypothesis described here.)

If true, the superposition hypothesis means there is no basis in which activations are interpretable: searching for an interpretable basis is fundamentally the wrong framing. Especially important features might get dedicated neurons, but most features don't align with neurons because they need to share and can't have a dedicated one.

![](images/img-002.png)

This section isn't a formal argument for the superposition hypothesis, but it's worth trying to sketch out the intuition for why it might be plausible. We start with the following intuitions about neural networks and features:

* Neural networks represent features as directions in activation space. Since neural networks are primarily built from matrix multiplications, it is both easier to construct a feature by embedding it as a direction and easier to use it (rather than some non-linear representation).
* There are far more possible features than neurons. These features vary in importance. For example, in the context of language, every person who lives or has lived could theoretically come up in text, and our models don't have billions of neurons. But there's a wide variety in how famous and influential people are, and how much they influence the text around them (the feature importance).
* Since there are a large number of parameters associated with every neuron, the most efficient way to encode many facts in parameters may not align with neurons. Language models in particular are incentivized to store large amounts of information in their parameters. Having a neuron corresponding to a single feature may "waste" parameters that could be used to store additional facts.
* Features are sparse.  Continuing the example of people as potential features from above, most tokens in text or positions in an image don't contain any given person (or even a person at all). This is the same observation as the sparsity of features in natural image statistics that motivates classic work on sparse coding (see e.g. ).

We can further combine these intuitions with the following ideas from mathematics:

* Almost Orthogonal Vectors. Although it's only possible to have n orthogonal vectors in an n-dimensional space, it's possible to have \exp(n) many "almost orthogonal" (<\epsilon cosine similarity) vectors in high-dimensional spaces. See the [Johnson–Lindenstrauss lemma](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma) .
* Compressed sensing. In general, if one projects a vector into a lower-dimensional space, one can't reconstruct the original vector. However, this changes if one knows that the original vector is sparse. In this case, it is often possible to recover the original vector. This situation is studied by a line of research called [compressed sensing](https://en.wikipedia.org/wiki/Compressed_sensing).

Together, these give us the basic ingredients for the superposition hypothesis. Ideally, networks could achieve a lower loss if they could represent more features. The number of features they can represent as orthogonal direction is limited by the number of neurons. However, it may be the case that representing more features is worth the cost of having "interference" between them because they aren't exactly orthogonal, especially if sparsity means that this interference is uncommon.

That is, a small neural network may be able to approximately "simulate" a sparse larger model, at the cost of some "interference" (figure below). And if it’s the case that the underlying data the model is trying to represent genuinely has a lot of sparse features, then this may be the best thing for the model to do.

![](images/img-003.png)

To be clear, the presence of nonlinear activation functions (the “privileged basis”) does create an incentive for features to align with this basis and not get superposed.  But if the gains to sparse coding are large enough, this incentive will get overwhelmed.  And when there isn’t a privileged basis (as in word embeddings and residual streams), we should expect the pressure for superposition to be even stronger.

### Update

Since publishing this paper, we wrote up a more detailed discussion of superposition in our paper [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html). In general, our understanding of superposition was much clearer in the Toy Models paper, and we see it as superseding this discussion.

### 3.5 What Can We Do About Superposition?

If we believe the superposition hypothesis, what should we do if we want to understand models? Broadly, there are two approaches:

* Create models with less superposition. Perhaps by making the right architectural decisions, regularizations, or making other design choices, we can reduce the need for superposition in neural networks.
* Find a way to understand representations with superposition.  An alternative to avoiding polysemanticity is to accept that models will have it and try to infer the higher-dimensional structure we believe exists in activation vectors, possibly using ideas from compressed sensing.

This paper will focus on the first approach, creating models with less superposition. Our intuition is that if it's possible to avoid superposition at training time, that would be easier than trying to deal with superposition after the fact. In the next section, we will introduce SoLU, an activation function designed to reduce polysemanticity and superposition in models.

  
  
  

  
  

## 4. SoLU: Designing for Interpretability

The goal of mechanistic interpretability is to reverse engineer neural networks. But we aren't just the reverse engineers – we're also the hardware designers. Just as a computer program might be easier to reverse engineer if it makes use of special CPU instructions designed for a particular use case, the right neural network architecture may make neural networks easier to reverse engineer.

We can apply this line of thinking to our present challenge. We need to understand MLP layer activations, but this is difficult because transformer MLP neurons are often very polysemantic, possibly due to feature superposition. And so the question is, how can we create a neural network architecture which will encourage features to align with neurons, and discourage polysemanticity?

### 4.1 Properties that May Reduce Polysemanticity

Transformer MLP layers are not designed to avoid polysemanticity. As a result, there are quite a few architectural properties that could plausibly reduce polysemanticity and haven't really been explored. We’re aware that decreasing polysemanticity might harm performance (due to the superposition hypothesis), but tactically speaking it makes sense to look for ways to decrease polysemanticity, and then see if we can find any that don’t harm performance.  Although we won't try all of these in this paper, here are a few potential ways to decrease polysemanticity, along with argument for why they may help:

* Activation Sparsity: Polysemantic neurons must fire more often, since they represent multiple things. Additionally, for a polysemantic neuron to be useful, the activations of other neurons must disambiguate it. This means that polysemanticity requires more neurons to fire at the same time. Put another way, superposition requires a gap between the sparsity of the underlying features and the sparsity of the neurons representing them. This suggests that encouraging activation sparsity may make it harder for neurons to be polysemantic. This sparsity could be achieved by using a different activation function, or by using a regularizer. (It's also worth noting that sparsity needs to be defined with respect to a basis; this is a very general argument for why it's plausible that any kind of sparsity might encourage a privileged basis.)
* Lateral Inhibition / Co-Occurrence Sparsity: It's possible to design activation functions (e.g. softmax), where one neuron firing reduces the amount other neurons fire. This encourages a very specific kind of (approximate) activation sparsity which one might call "co-occurrence sparsity." It isn't just that on average the neurons are sparse, it's that in any particular instance, relatively few neurons fire simultaneously. This may be an even stronger way to discourage polysemanticity, by making it hard for other neurons to disambiguate a neuron's meaning. It's important to think through the exact mechanism of lateral inhibition to ensure that the architecture is truly creating a situation where a few neurons "win" and sparsity emerges, rather than all neurons inhibiting each other resulting in highly diffuse small activations.
* Weight Sparsity: If one imagines two features in adjacent layers of a neural network, it seems natural to think there's some "ideal weight" between them. If every feature corresponds to a neuron (as in the imagined ideal model in [Section 3.4](#section-3-4)), this ideal weight would simply correspond to an entry in the weight matrix. But if one or both of the features is represented in a non-neuron aligned way, the ideal weight will start to be "smeared out" across many entries in the weight matrix. As a result, we should expect layers with polysemantic neurons to have more small weights, and layers where features are aligned with the basis to have a smaller number of "more concentrated" large sparse weights. This means that weight sparsity may be a way to discourage polysemanticity and encourage a privileged basis. However, it seems to us that weight sparsity only makes sense when both the input and output are privileged bases. In a transformer, all weights have the residual stream as either an input or output, and in our conceptualization of transformers, the residual stream is necessarily polysemantic and not basis aligned. As a result, we don't believe weight sparsity is suitable for a standard transformer architecture.
* Superlinear Activation Functions: A superlinear activation function is one where increasing the pre-activation value of a neuron increases its activation at a greater than linear rate while in the activating regime, holding other neurons fixed. Examples include \text{ReLU}(x)^2, \text{softmax}(x)\*x, and \exp(x). Consider what happens if you spread a feature over N neurons with this activation function. Since f\left(\frac{x}{\sqrt{N}}\right) < \frac{f(x)}{\sqrt{N}}, spreading a feature across neurons will automatically "shrink" it, requiring either larger activations or larger output weights. This makes it harder for non-basis aligned features to co-exist with basis-aligned ones. It also makes it worse for a polysemantic neural network if two features overlapping in the same neuron co-occur, since f(a+b) > f(a)+f(b) means the "interfrence" between the features would be greater than the sum of its parts.
* Change Neurons per FLOP / param: If one accepts the superposition hypothesis, the reason we have polysemanticity is that there aren't enough neurons for all the features the model would ideally like to represent. Unfortunately, naively making models bigger may not fix this, since more capable models may want to represent more features. Instead, we want to create more neurons without making models larger. Some architectural approaches may allow for this. (In some ways this seems like the most attractive way to reduce polysemanticity, if the hypothesis is right, since it's "giving the neural net what it wants" rather than "forcing it to do something it doesn't want.")

### 4.2 The SoLU Activation Function

It turns out that several of these properties – lateral inhibition, as well as approximate sparsity and superlinearity – can be achieved with a relatively simple change to the MLP activation function.

Modern transformers often use the GeLU activation function. Recall that GeLU is approximated closely by \text{sigmoid}(1.7x)\*x. What if we replaced sigmoid with softmax, its natural extension from binary to multivariate probabilities? We call this activation function a "softmax linear unit" or SoLU:

\text{SoLU}(x) = x \* \text{softmax}(x)

To see why this may discourage polysemanticity and superposition, it's helpful to consider a few examples. Firstly, when SoLU is applied to a vector of large and small values, the large values will suppress smaller values:

\text{SoLU}(4,1,4,1) ~\approx~ (2,0,2,0)

Perhaps more importantly, large basis aligned vectors are preserved, while a feature spread across many dimensions will be suppressed to a smaller magnitude:

\text{SoLU}(4,0,0,0) ~\approx~ (4,0,0,0) \text{SoLU}(1,1,1,1) ~\approx~ \left(\frac{1}{4},\frac{1}{4},\frac{1}{4},\frac{1}{4}\right)

### 4.3 LayerNorm

Our preliminary experiments found that simply using a SoLU activation function seemed to make neurons much more interpretable, but came at a major performance cost. Generally, SoLU models without any other changes had performance equivalent to a model 30-50% smaller than their actual size, with larger models being affected more.  This is exactly what we’d expect to see if the superposition hypothesis was true – we can decrease polysemanticity, but doing so harms the network’s ML performance.

However, we found empirically that this performance penalty can be fixed, while also preserving the interpretability gains, by applying an extra LayerNorm after the SoLU, similar to .  This greatly improves ML performance, so for the majority of our experiments the function we actually apply isNote however that the activations we try to interpret are those before the extra layer norm, not after.:

f(x) = \text{LN}(\text{SoLU}(x)) = \text{LN}(x \* \text{softmax}(x))

We originally added LayerNorm on the intuition that it might fix issues with activation scale and improve optimization. Unfortunately, we now believe that at least part of the reason for the performance improvement is the extra LayerNorm may allow superposition to be smuggled through in smaller activations.  However, under this theory, the combined operation would still tend push at least some features to single neurons with large activations, potentially allowing increased interpretability to coexist with superposition.

We'll discuss this empirically later, but for now note that LayerNorm is invariant to scaling the input, since \text{LN}(x') divides by \sigma(x') and \sigma(\alpha x') = \alpha \sigma(x'). This means that if an entire vector is small because it was very distributed and SoLU suppressed it, it will be rescaled to be larger.

![](images/img-004.png)

More generally, it means that the denominator of softmax has no effect on the final behavior of the model (although it does change the activations we observe pre-LayerNorm). Training a model with an exponential activation would be identical if we ignored intermediate activations:

\text{LN}(\text{SoLU}(x)) ~=~ \text{LN}\left(x\frac{\exp(x)}{\sum\_i \exp(x\_i)}\right) ~=~ \text{LN}\left(x \* \exp(x)\right)

### 4.4 Parallelism Implementation Details

Our larger models are trained using tensor parallelism, such that MLP activations are never present on a single accelerator. For those models, we split both the softmax and the layer norm to act over a subset of dimensions, allowing each processor to operate locally without additional communication. We report results for these "blocked" models, but in our informal experiments, this blocking does not appear to have a substantial effect on either ML performance or our interpretability results.

  
  
  

  
  

## 5. Results on Performance

In this section we confirm that SoLU (the version with LayerNorm) has comparable ML performance to a baseline model.  This is important because interpretability changes are unlikely to be widely adopted if they significantly hurt model performance.Note that making architectures which improve interpretability at arbitrary cost to performance is both trivial and uninteresting.  As a reductio ad absurdum, we could replace any neural network with a linear regression, which is highly interpretable but likely achieves very poor performance.  Of course, architecture changes which result in minor performance decreases but major interpretability improvements may still be worth pursuing.  The largest language models are now estimated to cost millions of dollars to train, persuading companies to adopt such a change in production systems would mean asking them to spend millions of dollars more to achieve a model of equivalent performance. This seems like a tough sell, even if the interpretability improvements were dramatic.  Thus, it seems important to confirm competitiveness.

To demonstrate this, we train transformer language models with and without SoLU for a range of different sizes, and evaluate both the loss and the performance on the following downstream NLP tasks: Lambada , ARC , OpenBookQA , TriviaQA , arithmetic, MMLU , and HellaSwag.

Our baseline model uses an architecture similar to GPT-3  and Gopher , and identical to what is described in our own previous language model baselines . We train models ranging from 1 layer to 64 layers (approximately 50 billion parameters), in successive factors of roughly 4 in parameters.  Our SoLU models have all the same hyperparameters and architectural details as our baselines and differ only in using the SoLU activation function.

Training curves for the models are shown in Figure 1.  We plot both the loss (Figure 1 top) and a measure of performance difference that converts loss differences into an effective multiplier on model size (Figure 1 bottom), which allows us to zoom in on small differences in performance.  As shown in the plots, SoLU is roughly equivalent to the baseline for all model sizes, always falling between a 1.05x and a 0.95x multiplier in model size (roughly equivalent to a change in loss of ±0.01 nats in most cases, compared to a total loss of 1.6-3 nats).  There is potentially a trend towards SoLU performing slightly better relative to the baseline at large model sizes, though all differences are small and more likely than not to be random noise (on the 50B model, SoLU is equivalent to increasing the model size by 1.01x).

![](images/img-005.png)

Figure 1: Loss curves for baseline (dotted line) and SoLU (solid line) models ranging from 10 million parameters to 50 billion parameters.  Top plot shows learning curves, bottom plot shows a “model size equivalent” version of the same data, with the baseline model set to 1.0x and SoLU models measured in terms of the baseline model size they perform equivalently to, as predicted from the scale laws.  For example, if a 1B baseline model achieved loss 2.3, a 2B baseline model achieved loss 2.1, and a 1B SoLU model also achieved loss 2.1, the SoLU model would be said to perform at 2x model size relative to the baseline.

Although downstream tasks often correlate well with the loss on a sufficiently broad training set , it’s possible for the macroscopic loss to hide deficiencies in particular tasks or areas, so we run several representative downstream evaluations to confirm the picture suggested by the loss curves.  We evaluate on the Lambada, OpenBookQA, ARC, HellaSwag, MMLU, TriviaQA, and arithmetic datasets, and the results are shown in Figure 2.  We see similar overall performance on baseline vs SoLU at all model sizes, with significant differences on a couple tasks (arithmetic seems better with SoLU, whereas TriviaQA seems better with the baseline) but similar performance on most and no systematic trend one way or the other.

![](images/img-006.png)

Figure 2: Performance on downstream tasks.

It is worth noting that we do not scan a range of hyperparameters (we scan only model size) for either SoLU or the baseline, and the optimal hyperparameters for SoLU might be different from those for the baseline model.  However, the baseline model’s hyperparameters were used in  and are similar to those in , while SoLU has not been tuned at all, so even if this effect is present, it likely underestimates the performance of SoLU, suggesting SoLU is at least as good as the baseline.

Finally there is another sense of “performance” worth mentioning – the efficiency of model training.  SoLU involves a softmax over the feedforward activations and thus adds a small amount of additional computation, but it is tiny compared to the main matrix multiplies, and with proper GPU kernels, we have found that it slows model training by only an insignificant amount (a less than 1% difference in speed).In principle, one could sidestep this small cost by training an isomorphic model with exponential activation functions and then switching to SoLU after training, ignoring concerns about different numerics.

Overall, then, we conclude that SoLU with LayerNorm appears to achieve competitive ML and training performance compared to a standard transformer.

  
  
  

  
  

## 6. Results on Interpretability

Having shown that SoLU is competitive in ML performance, we now demonstrate our main point: that it makes model neurons easier to interpret.  [Section 6.1](#section-6-1) describes the quantitative experiments we perform, [Section 6.2](#section-6-2) goes through the results of those experiments, [Section 6.3](#section-6-3) explores some discoveries we are able to make in the SoLU models that we weren’t able to make previously in baseline models, and [Section 6.4](#section-6-4) discusses how the post-activation LayerNorm may complicate the picture.

### 6.1 Setup of Experiments

We are interested in whether neurons are "interpretable" – that is, do their activations reliably correspond to a coherent, articulable property of the input? Determining that a neuron is interpretable in this sense is not straightforward. While one can often develop a theory of neuron behavior quite rapidly, verifying that theory (or correcting it if the original theory is mistaken) can take a large amount of human effort.  For example, Cammarata et al.  dedicated an entire two papers to rigorously investigating a handful of curve detector neurons in a vision model using seven different lines of evidence.

In order to make it practically feasible to study a large number of neurons across several different models, we therefore settle for measuring something less ambitious: whether a given neuron suggests a plausible interpretation given a small amount of human attention.  This will lead to both some false positives (neuron appears to have a plausible explanation that on closer inspection would turn out to be wrong) and false negatives (there is a simple correct theory of the neuron’s firings but we don’t succeed in finding it quickly).  Nevertheless it is still likely correlated with neurons being interpetable on closer investigation. Additionally, it seems related to the property of being easily interpretable, which would be valuable in its own right: if more neurons are interpretable with low-effort, it makes it more likely that large assemblages of them can be reverse-engineered.

### Caveat

Since publication, we've become more pessimistic about this metric. Looking at top dataset examples only provides information about whether a neuron is monosemantic when activating strongly. We previously hoped that there might be a significant correlation between whether a neuron is monosemantic when activating strongly, and whether it's monosemantic in general. However, further experiments made us less optimistic about this, at least once one begins trying to optimize for large activations to be monosemantic. Of course, there are ways in which it's interesting to know whether the top activations are monosemantic – it may suggest that the neuron has one feature that it's representing more strongly than others, which may be interesting to investigate – but it's probably not a good guide for architectural experiments if we seek to create monosemantic models. In our more recent [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html) paper we attempt to approach this problem in a more principled way by analyzing the full spectrum of dataset examples.

To measure whether a neuron is “interpretable at first glance," we asked human evaluators (some of the authors) to examine a series of text snippets (typically 20 snippets of length a few paragraphs each) that include tokens where the neuron fires heavily.  The firings are highlighted in different shades of red (corresponding to activation magnitude), allowing the evaluator to quickly skim the snippets for a common theme.  An example of the dataset examples evaluators see is shown in Figure 3.

![](images/img-007.png)

Figure 3: Evaluators are shown dataset examples a neuron fires on, highlighted by activation magnitude, as seen above.  Neurons are selected randomly from one of a SoLU model or its corresponding baseline, the human evaluator (one of the authors) spends 1-2 minutes evaluating whether a single hypothesis or concept explains 80% of the strongest firings, and marks the neuron INTERPRETABLE if so and NOT INTERPRETABLE otherwise.

The evaluator is instructed to examine the firings for 1-2 minutes per neuron, and then indicate whether they have found a plausible theory to explain the firings.  The specific instructions were to mark INTERPRETABLE if “80% or more of the strongest firings can be explained by a single rule or category (e.g. the word “apple," or any phrase relating to music)," and NOT INTERPRETABLE otherwise.

We performed experiments on the 1 layer, 16 layer, 24 layer, 40 layer, and 64 layer (50 billion parameter) models.   For each size of model, evaluators were presented with 60 neurons from the baseline model (without SoLU activation) and 60 neurons from the corresponding SoLU model – for a total of 60\*2\*5=600 neurons across all experiments.  To prevent us from being biased in favor of our models, the neurons were presented to evaluators in a randomized and blinded manner (evaluators did not know which neurons came from which model).

Finally, since our SoLU models include both the SoLU itself and an extra layer norm, we did one experiment to disambiguate the effect of the SoLU and the layer norm.  Namely, we trained a 16 layer model with the extra layer norm but not the SoLU, and evaluated 60 neurons from this model as well, bringing the grand total to 660 neurons.

### 6.2 Quantitative Results

The results of our experiment on what fraction of neurons are preliminarily interpretable are shown below in Figure 4.  For models from 1 layer to 40 layers, the SoLU model’s neurons are substantially more interpretable than the baseline’s neurons, with increases of roughly 25 absolute percentage points, from ~35% interpretable to ~60% interpretable.  This increases the fraction of interpretable neurons by 1.7x.  Although the effect is moderate in size, the sample size, consistent gap, and consistent absolute rates of interpretable neurons suggest a real and persistent effect of the SoLU models.

![](images/img-008.png)

Figure 4: Results of human experiments on interpretability of neurons in SoLU vs baseline transformer for various model sizes.  Blue line shows fraction of neurons marked as preliminarily suggesting an interpretation in the baseline transformer for model sizes ranging from 1 to 64 layers.  Red line shows fraction of neurons marked as preliminarily suggesting an interpretation in the SoLU transformer.  Green dot shows fraction of neurons marked as preliminarily suggesting an interpretation in the 16 layer model with the extra layer-norm but not SoLU.  Overall, in models from 1 layer to 40 layers, the SoLU increases the fraction of interpretable neurons by ~25%, while in the 64 layer model, the gain is much smaller.

In the 64 layer model, the benefit of the SoLU model weakens substantially.  The fraction of preliminarily interpretable neurons is the same for the baseline model, but is only slightly higher in the SoLU model (42% vs 33%), and is well below the SoLU fraction for small models.  We do not know why the 64L model benefits less from SoLU, but one possible theory is that as models become larger, their neurons represent more sophisticated concepts and become harder to understand, such that 1-2 minutes of inspection is less likely to identify their meaning (this would suggest that the neurons remain interpretable, but are no longer “easily interpretable”).  Anecdotally, the 64L did appear to us to represent more sophisticated concepts.  Another possibility is simply that some effect related to deep models or the dynamics of optimization changes or reduces the usual interpretability effects of the SoLU. In either case, the 64L model is a good illustration of why it is important to test out interpretability ideas on large, frontier models: ideas that work on small models may not work as well on larger ones.  This provides good motivation for future work attempting to increase the interpretability of the largest models.

The 16 layer model with the extra layer norm but no SoLU performs about halfway between the SoLU and the baseline, suggesting that the post-activation layer norm alone may provide some but not all of the interpretability benefits.

One annotator found a larger effect than the other two (~20% vs ~60% instead of ~40% vs ~60% for baseline vs SoLU). In conversations after we unblinded the data, our sense was that they held a higher bar for judging a neuron to be interpretable and in particular were less willing to ignore small activations. So, it's possible that the effect size is larger if one has a stricter definition of neurons being interpretable, but we'd hesitate to draw too strong an inference.

As noted in [Section 6.1](#section-6-1), these results describe whether neurons preliminarily appear interpretable, which isn't necessarily the same as whether we'd consider them to be interpretable on rigorous investigation. On one hand, fast inspection may have failed to detect some neurons that could be shown to be interpretable given more time (and this is a possible hypothesis for the 64L’s underperformance).  Conversely, some cases where the evaluators appeared to see a clear hypothesis could easily have been wrong. One particular risk is that we showed top dataset examples and did not show negative examples (examples of the hypothesized pattern on which the neuron might NOT be firing) unless they occur in the same snippet as a positive example.  Thus, the neuron might actually be firing on only a subset of cases of the purported pattern, and the evaluators would not have detected this.

Nevertheless, the experiments show there is clearly some real effect, and anecdotally, we have found the SoLU models much easier to explore, work with, and understand.  In the next section, we describe some of this open-ended exploration.

### 6.3 Qualitative Exploration of SoLU Models

See also discussion of additional qualitative investigation of neurons in this [earlier video](https://www.youtube.com/watch?v=e0u7ZSAPZAA) discussing our preliminary findings with SoLU.

<!-- yt-inline:e0u7ZSAPZAA -->
[![Softmax Linear Unit (softmax(x)*x) Neurons - Preliminary Results](https://img.youtube.com/vi/e0u7ZSAPZAA/hqdefault.jpg)](https://www.youtube.com/watch?v=e0u7ZSAPZAA)

<details>
<summary>자막: Softmax Linear Unit (softmax(x)*x) Neurons - Preliminary Results (1:45:46)</summary>

[00:00]
well today we're here to talk about um
some experience experiments we've been
doing at anthropic um on how to make mlp
layers more interpretable and we think
we found something um that works quite
well uh and so i'm excited to talk with
everyone about it and i'm here uh with
my colleague nelson el-hash who has
really been the person driving these
experiments um so we're gonna go and
just sort of chat about what we found
uh welcome nelson
yeah i'm i'm excited to to share these
initial takes on some i think early but
pretty cool results we have
um so just yeah so i think the the tldr
is
is just the changing the activation
function
of the mlp neurons can make neurons much
more
interpretable
um
and
[Music]
one thing i think is sort of important
to note here is this is really
an interim update on early research so
we're we're you know this isn't
something that we're highly confident

[00:01]
about there could be mistakes there
could be things that we're
misunderstanding um but these sort of
seemed like sufficiently exciting
results that we wanted to share them
early on um rather than waiting until we
could go and produce a really highly
polished paper so expect this to be kind
of rough and you sort of take things
that we say with a grain of salt because
this is this is early work sort of
relatively low confidence on on any
assertion that we make here being sort
of ultimately correct but we think
they're probably directionally onto
something
yeah and i think hopefully as we talk
about this we can sort of be clear about
what level of evidence we have and what
we found that has made us believe this
um this is in collaboration with uh many
of our colleagues on the
interpretability team um really really
everyone um and also other colleagues
anthropic um so really this would you
know none of these experiments would be
possible without without tooling and
infrastructure and um conversations and
support from from other people
and
yeah okay so i think the high level
uh
problem is we'd we'd like for neurons to
be interpretable

[00:02]
um
and
that's actually like i i guess maybe one
very basic thing is is that even a
reasonable thing to hope for like
is it is it reasonable to ask for for
individual neurons to be uh
interpretable and uh for that matter i
think we'd claim that that isn't the
case for the residual stream so yeah
maybe nothing i could maybe i could ask
you like why why is it one might even
hope for neurons to be integral
yeah i mean i think the the
the main reason for sort of neurons in
particular is because they're this one
point in the model where we uh
certainly with we apply the this
non-linearity to typically a gel u or a
relu in a transformer and we even apply
it to sort of these like specific scalar
values and so like the actual like you
know value of the floating point number
there has has some significance the
model is is is you know branching on
that value
um and so we sort of that gives it a
privileged basis is the way we describe
that

[00:03]
um and so sort of like that value means
something whereas values in the residual
stream we always read and write to them
through essentially an arbitrary linear
projection and so you can you can like
rotate the entire linear the entire
residual stream or apply kind of any
linear transformation and then apply the
corresponding transformation everywhere
else in the model and get an identical
transformer and so there's like really
no reason to expect the the value like
definitely no reason to expect the like
individual dimensions of the residual
stream to be meaningful
you might hope that you could sort of
find some basis where it's interpretable
but even that there's reason to believe
that it sort of would be tricky or would
be clear or that sort of that might not
be the right way to think about it um
and kind of you know for neurons where
we're like applying this this
non-linearity to this specific scalar
like that number is in some sense kind
of very non-arbitrary or at least
potentially very non-arbitrary that
there's there's there's real meaning
encoded in that specific number that
we're you know we're doing a comparison

[00:04]
and we're that comparison
or that you know sorry if we're doing a
relu we're doing us this comparison sort
of you know are we
greater than or less than zero
um and that you know we might expect
that to be you know is is some signal or
some feature present um and it turns out
that in
uh envision models and a lot of chris's
past work i think that's sort of not
always but often true that these non-led
these non-linearities correspond to you
know we sum up a bunch of evidence and
if it's above some threshold we sort of
some feature we say some feature is
present and if it's not we kind of just
round to zero and and
don't admit that feature at all
and i think that actually brings us to
the the second mystery which is why is
it the case that sometimes this gives us
really interpretable neurons and
features where we can we can really
understand what's going on and sometimes
we can't oh and actually uh before we
move on maybe chris you want to unpack a
little bit what you mean when you say
interpretable here
yeah it's a that's a slightly subtle
thing

[00:05]
i think that's a great a great uh a
great question so
um
i think what we what we really mean is
that we can develop some hypothesis that
explains
and in the case of a neuron for instance
that we can develop some hypothesis that
explains what the
what the
yeah when the neuron fires so um you
know this neuron is firing in response
to some articulable feature that we can
describe in the text um or implementing
some articulable output behavior um
and we can generate that high that
hypothesis and it seems and then when we
test it it continues to be true
uh yeah i think of it a little bit as
sort of the like the the features or the
the features the model is working with
sort of in some sense like
are are like recognizably aligned with
the kinds of features that like we as
humans understand that sort of it's sort
of it's
i think the one place where this gets
really subtle from my perspective is
that sometimes we have features that
they're just things we haven't thought

[00:06]
of but they're actually they're actually
natural in retrospect um so in vision
models for instance we found these high
low frequency detectors that um there's
also there's a whole paper on them if
you're interested but they seem to be
you know there's something that you
wouldn't have thought of beforehand but
in retrospect they make a lot of sense
and so i sort of think that you know
even features that are sort of kind of
alien if if in retrospect once you
understand them they're easy to
understand um
i think that should count as an interval
feature and i think that makes it much
harder to judge quickly like it when you
have a neuron that you can't understand
is it that you that you just haven't
figured out the right hypothesis yet or
is it that the that something
fundamentally weird is going on with
that neuron so i think i think that is a
tricky thing
um
about all of this
yeah and then i think that that also i
think all that and the the reference
division models leads into sort of the
question of why aren't neurons always
interpretable because i think sort of
the poly semanticity gets into this sort
of like clear example of a thing that
sort of is is not well interpretable or
at least not in this sense

[00:07]
yeah so there's there's lots of neurons
in these models we see this both
individual models and even more strongly
in language models where there are
neurons that even when you look at them
really carefully they don't seem to
correspond to anything in particular
that's uh interpretable and
i
i think a very common behavior is that
you see neurons which fire seemingly to
a union of unrelated things
so um the famous example in vision that
we well famous to us
is this neuron that that fires in
response to cats and fronts of cars and
paws
and cat faces and those are just like
pretty unrelated things and
but for some reason it fires to that
that union
and so
uh
the
we we've sort of called this phenomenon
polycenaticity and the
this the it fires in response to
multiple unrelated things and um
it's hard to systematically study this

[00:08]
because we don't have really a
mathematical definition of it um like
there's no automated way in which you
can say that a neuron is poly semantic
or at least
no one that i know develops such an
automated way
um and i think we we don't even really
have a very good theory for well we have
a theory for why this happens we don't
really test that theory very well um and
really the only reason that it sort of
is the theory that we take seriously is
that we don't have a serious yeah good
competing theory and so there's this one
theory that we'll get to in a second um
called superposition that is a theory
for for why this happens but we
don't really uh don't really know and by
the way i should fly here that this has
been discussed a fair amount in the
original circuits thread um so that's
another place that you can go if you're
if you're interested in this
oh
apparently an image did not come through
to the slide so i guess um i guess we
will not be
um not be showing this but maybe nelson
do you want to
just talk a minute for a minute about uh
yeah what we mean when we sort of have

[00:09]
that super position hypothesis and what
what the theory is for why
why polysynthetic neurons might be
forming
yeah i think i think the um
one perspective that i think um
i don't remember who who in our team
observed this way but sort of is the
idea that the neuron is sort of
encoding um
if you're sort of if an individual
neuron is a sort of you know
interpretable feature in some sense you
sort of
you know like you know this neuron is
firing if we're talking about dogs you
can sort of
think of that as like this little one
hot encoding of the feature space and i
think you
uh like one hot encodings are sort of
like super nice to work with in a lot of
ways they're very simple but they're
also in some sense inefficient and i
think
you know you you one one hypothesis this
is sort of the model is is sort of
developing a like richer sort of like
and potentially uh uh still you know
treat each feature sort of relatively
sort of conceptually as kind of present

[00:10]
or not present but then it's like using
the
using sets of neurons to sort of get the
like power set of all of these neurons
to represent your feature space and so
you
you know the the presence of a dog is
indicated by you know the following four
features all lighting up
um or you know maybe the four features
lighting up and then also some other
features not lighting up and if you're
if you're doing some sort of encoding
like that
then potentially you can just sort of
like pack much more information into the
same number of dimensions
and potentially you run the risk of of
like some interference of sort of you
some encodings are incoherent or you can
encode conflicting things but then
presumably the model just arranges so
that the sort of incoherent the possible
incoherent states are very unlikely or
very unlikely on the training
distribution
um
but so the the theory is basically
you're you're sort of trying to encode
more information or more features than
a sort of like one hot you know one
feature per neuron encoding allows and

[00:11]
it seems sort of perfectly possible that
you could do that and these neurons that
sort of seem to be firing over unions of
unrelated sets are probably what you
would expect to see in that case
um and so we sort of haven't really like
done at all the work to nail down that
this is exactly what's going on but it
seems like a plausible hypothesis sort
of as as chris says
we we sort of believe it because it is
plausible and we don't have a better
hypothesis but like that's very
different from
us feeling confident or or asserting
that we've
demonstrated that this is what's going
on or anything like that
one other piece of evidence for this is
that in the original circuits thread
there were some circuits we traced out
where we'd see things like oh here are
car sector forms and then it gets
smeared over a bunch of unrelated
neurons and so you can sort of see this
in the forward direction of the weights
as well um and and that sort of seems
like some evidence this is
happening um
yeah and i guess one one maybe useful
intuition here is

[00:12]
that
the
the more a model has the capacity to
represent lots of useful features but
not enough neurons
the more the starter seems like a
tempting strategy for the model so if
there's you know if there's if there's a
million
useful linguistic features to go and
represent but you only have 10 000
neurons um let's say that there's
there's only 20 000 useful features but
there's there's 10 000 neurons it's
really tempting to go and try and
somehow squeeze all twenty thousand
those features into those ten thousand
neurons even if that means that you're
you're gonna do it in a slightly less
principled way and you know these sort
of effective if statement like things
that you're using sort of are gonna
gonna have interference between them and
and so on maybe it's still it's a
worthwhile cost to pay perhaps
um
well so
uh yeah nelson can you can you talk us
through what change we make to go and
make it yeah so
so we
we've been thinking a lot about this
problem of of understanding um neurons

[00:13]
in these transformer models and we've
been doing some experiments with doing
architecture tweaks you know not for the
sake of capabilities but for the sake of
can we produce models that perform
comparably well or potentially you know
we take a little bit of a performance
hit but we find it much more
interpretable in some way
um and at chris's suggestion the the
experiment or we ran a couple
experiments but the sort of one that
seems most promising is we replaced the
the gel u inside the mlp
with soft max of x times x and so we we
do
uh a soft max like over the d mlp
dimensions so typical transformers
uh architectures you have your your d
model dimension you run that through a
linear projection to get up to four
times d model neurons that four is a
hyper parameter but four is the is the
standard results in is the sort of
standard choice for most of these
and then normally you would just run a
pointwise ju over all of those we've

[00:14]
been running one big soft max over all
of those four times d model neurons then
take that result and do point-wise
multiply it with the activations
and then we add another layer norm there
and then we do the down projection to
another d model vector and add it back
into the residual stream like normal
uh the layer norm there turns out to be
pretty important we tried without that
layer norm and uh the model still trains
but you end up with much worse
performance and when you investigate you
end up with it looks like a lot of the
neurons just end up dead and we don't
totally understand why the layer norm
fixes that but empirically it does if
you if you train without that a lot of
the kind of the pre-activation values
are just deeply in the negative regime
you do a soft max where some of the
things are deeply negative and some of
them aren't all of the deeply negative
ones go to zero they get no gradient
signal sort of looks a lot like a dead
relu neuron
there's no obvious reason that we're

[00:15]
aware why adding layer norm would fix
that problem but
we can sort of tell second order stories
but the main thing is that empirically
it does
and the kind of motivation for this as
we say in the bottom
is that
sort of want to drive the model towards
these these sort of sparser
representation of features if it wants
to encode a feature
we want to discourage it from from
sort of smearing that feature across a
lot of different neurons in a lot of
different ways we want to kind of align
these features and computations kind of
one way you can try to do that is is
push towards sparsity of sort of you
know you only get a few or small number
of
of positive values or non-zero values in
your activation function and soft max
just
naturally kind of architecturally pretty
aggressively forces its input towards
sparsity it you know flushes most of the
smaller values very close to zero and
then extends up the larger values
we add in the times x

[00:16]
um
uh chris can correct me that was also
chris's suggestion but i think there's a
couple of ways you can think about it
one is
it it
potentially pushes you a little bit more
towards sparsity because it makes this
kind of quadratic in some sense it gives
you a little bit more
dynamic range potentially to allow the
neurons to act in because soft max is
constrained to zero one the layer norm
will then expand that out again but if
you add the times x it's sort of a
little more sensitive to the input and
so potentially you get you have sort of
more dynamic range in these these sort
of condition statements that the model
is doing uh and then potentially also
and then it also gives you the second
path for gradients to flow along in the
back propagation and we were hopeful it
might it might uh stabilize training
although it turns out the model trains
pretty well with or without it
um i think two other intuitions for it
are one jelly neurons are basically
sigmoid of x times x and so in some ways
soft max of x times x is sort of a
natural generalization of it to multiple

[00:17]
dimensions
um
i think another reason
why it might be natural is that uh
if you if you're really trying to resist
small values
and
sort of multiplying two small numbers
together gives you an even smaller
number and so there's sort of a way in
which soft max of x times x if x is very
small is going to drive you even closer
to zero and really penalize um small
values even even more strongly perhaps
yeah i think this gets complicated right
because if if x goes to the negative
regime
um i guess
assuming that there are positive numbers
if x goes to negative regime soft max of
x is essentially zero and so multiplying
it by a large negative number doesn't
actually push it more negative or yeah
like
maybe it goes to not quite zero and so
it ends up a little bit larger in
magnitude than it otherwise would be but
it sort of yeah yeah i guess it's i
guess it's the case when they're all
like in the slightly positive regime and
that sort of assumes that x is actually
centered at zero which it might not

[00:18]
but but yeah
i think i think probably
that's the case i think sort of
ultimately we we did some experiments
with both they they work pretty
comparably
we think soft max of x times x ended up
being a little bit more interpretable in
our experiments and so that's the the
main that plus kind of all of these
somewhat hand wavy motivations are why
we're
focusing on that one and sharing that
one
um
yeah so nelson how much more
uh yeah so
the sort of as we said the the punch
line is that these models seem
drastically easier to develop theories
of we we shared another video a few
months ago where we talked through some
of the neurons we'd found in our gel u
models we sort of highlighted a couple
of neurons that we thought we we kind of
understood or could characterize but
mostly highlighted how hard we had found
that process um
the soft max x times x neurons at least

[00:19]
in our models are are just really
drastically easier i've done a bunch of
experiments of sort of taking i you know
i did models of identical scale and
architecture except for the activation
function and randomly sampling 10 or 20
neurons from each and spending about 30
seconds with each neuron
uh sort of
i did this a couple times i wasn't super
rigorous but the sort of something like
10 to 20
of the jelly u neurons sort of have a
clear theory that jumps out of like oh
yes it's sort of like pretty clear what
what information this neuron is trying
to compose and it was something like 70
to 80 percent of the soft max x
uh ones have a pretty clear theory and
this is again this is like 30 seconds
roughly of looking at each neuron this
is a sort of very early first pass when
we're just trying to convince ourselves
of whether or not there's something here
at all
but but you know the the numbers really
did jump from you know 10 to 20
interpretable to 10 to 20 mysterious on

[00:20]
a first glance it's it's a really
sort of completely flipped our
experience of of looking at these models
and i think when you were describing
this to me originally i'm sort of gonna
put you on the spot and please feel free
to push back but i think you also said
that you know many of the neurons that
you didn't classify for the soft max x
times x model as being
um like having a really clear theory
that jumps out in 30 seconds there were
sort of hints of a theory um that maybe
if you'd looked longer yeah i think
that's that's right i sort of i was i
was for the kind of quick experiment i
was kind of making a
binary judgment on you know do i feel
like i have a like highly plausible
theory but sort of
uh
for the ones that sort of failed that
test the soft max x times x ones were
much more likely to be like well i don't
have a plausible theory but there's sort
of some obvious pattern here or some
obvious structure that i i don't fully
understand yet but i bet with some more
exploration would would kind of yield a
pretty a pretty crisp uh story

[00:21]
so it's pretty plausible that 70 or 80
percent is sort of more of a lower bound
on things rather than uh
yeah that's certainly the
the optimistic take and i think very
plausible yeah um kind of
rough numbers to sort of you know but
but the sort of the really
um
we we've been looking at these models
and we're like yeah these soft max x1
seem pretty good and and because you
know i
okay we just wanted to convince
ourselves like are we on to something
here are we just misleading ourselves
and so we sort of did these sort of
cheap randomized experiments and it was
just like
i i kind of stopped the experiments
relatively early on because the
difference was just like so sharp that
it was just very clear that
that that this is a drastic step forward
yeah my my experience also just i didn't
do anything quite as carefully
controlled as what nelson was doing but
um
i i just started looking at these models
and i it was it was a night and day
difference and i was just extremely
extremely struck by it uh so

[00:22]
now
we can only really speak to our models
and so there's you know other people
train different models and um
yeah i guess i guess something that we
want to caveat is that we you know we
can't say for sure that other people's
models don't have lots of um
interpretable neurons and that there
isn't something that's weird like i
think what we're training is a pretty
standard transformer but um you know uh
sometimes you know
different code bases have different hype
parameters or something and maybe this
is sensitive in some weird way
um
do you want to comment at all on that
nelson
yeah i mean there's there's um
i always
am very uncertain with these results
sort of how aggressively to assume that
they generalize outside of our code base
or not like there are a couple of papers
out with with various takes of of trying
to interpret or understand um
neurons in transformers with varying
degrees of success
um
it it
uh it seems really hard to say

[00:23]
say for sure if this is our architecture
but we're pretty sure we're doing
something pretty vanilla and we've had a
lot of luck and the the difference here
is really dramatic
um we'd really love to hear from other
teams i think who have sort of done
tried to do close studies of neurons in
a sort of somewhat similar way and
and whether they've had similar
experiences or or not um i think if
anyone is inspired to to replicate this
experiment um that would be really
exciting to us to to get a side by side
from another team um these results these
results for us uh show up as well we'll
talk later but the difference between
soft max and jelly u is pretty obvious
even in a one layer transformer so uh if
someone is interested like i think you
know this is you know this experiment
can be totally reproduced on a single
gpu in a couple of days like this is not
a this doesn't you know if someone's
excited that you know you don't need a
kind of big science cluster to
contribute evidence for whether or not
this phenomenon happens in a different

[00:24]
code base
other thing i might add is um
uh i think we have some weak evidence
just from from talking to other other
groups um that uh at least some other
groups are having trouble
with figuring out mlp neurons and
haven't had a lot of traction with that
um
and i haven't really heard none of the
groups that i'm in contact with have
told me at least that they've had that
they've got traction so i think that
there's
that's sort of not
not dispositive for like what the
distribution of successes around groups
have been but um i think that i think
that it's at least not unique to us that
neurons aren't very interpretable in in
your standard model
um
okay yeah so we've talked about how
different it is nelson can you talk
about if it affects performance and and
also i guess you were saying that layer
norm is really important for that yeah
so we talked about how how different it
is and i think it's sort of really both
of us and and other members of our team
have all looked at these and sort of

[00:25]
i i did my sort of barely randomized
experiments but but everyone on the team
sort of independently i think uh you
know and there's sort of agreed that
these are just night and day different
to look at
um questions or does it affect
performance um
the
short answer is sort of there's might be
a slight hit from these but it seems to
approximately perform as well as the
jelly u models there's a sort of um the
the trends aren't super clear as we
change model size we've done a couple of
different sizes
um
it seems to take a little bit of a hit
but it's pretty small it's sort of i
think my
kind of high level takeaway is it's sort
of
roughly within noise of performing as
well as a gel you model um
which in some ways is is kind of a
striking result to me i i sort of in
some ways it's unsurprising in that like
i think most activation functions that
are vaguely reasonable people have tried
you know relu value squared other things

[00:26]
sort of
there's some difference but they all
roughly work the sort of soft max across
the mlp dimension feels in some ways
very different you're really
aggressively
encouraging sparsity and so maybe it's
surprising sort of i was a little bit
surprised that it that it seems to work
about as well but it seems to work about
as
well okay so
we're going to talk through some
different models now just to give some
examples of the kinds of really exciting
things that we found and i think we're
going to structure this as first talking
through a one layer model because one
layer models are sort of very simple and
being able to understand neurons in them
is actually actually very exciting and
then we'll talk through um
some larger models and talk about more
interesting neurons so the neurons we
find in the one layer models are going
to tend to be simpler and then the ones
that we find in larger models are going
to tend to be more complicated and one
one thing i think i wanna one kind of i
think the interesting bit of context
here is is we're gonna highlight a lot
of cool things we found in these soft
max models
for many of these neurons we

[00:27]
had sort of we had postulated these
neurons and we had gone and searched for
them in in varying manual and automated
fashions in our jelly models and just
sort of couldn't find them we're like
there's sort of some computation
obviously the model is doing it because
it's sort of fundamental to parsing or
understanding the language and also
it doesn't seem to be it's sort of some
weird superposition or something messier
is going on because we we like search
for the neurons we can't find it and
then in these softmax models these
things just fall right out in very
straightforward ways in
uh as best we can tell again we kind of
uh uh
everything we present is based on you
know probably a few minutes of kind of
poking around with our interpretability
tools we haven't
exhaustively done ablation tests or
attribution or counter factuals or
anything to sort of
conclusively prove what's going on but
the the sort of were

[00:28]
the the first pass theory of what's
going on is sort of very clear for all
of these in a way that really wasn't
true in the gel u model
so yeah let's let's dive into it yeah
yeah so we studied one layer model one
layer attention only models pretty
thoroughly in our first paper we
presented some sort of really nice
mathematical analysis of sort of how to
think about them and the kind of
empirical studies of what attention
heads are doing
um and
then for this for this talk we took the
sort of one layer models with the mlp
layers so sort of the like next smallest
model the transformer that you might
imagine
and it seems like in the soft max x
models the
individual mlps are are relatively
interpretable and pretty easy to come up
with theories about so let's dive into
some of the ones we found yeah so nelson
one thing we're saying is that these
neurons implement interpretable rules
and maybe with a concrete example you
can sort of talk about what we mean by
this idea that they're implying
interpretable rules maybe you could talk

[00:29]
through what this neuron is doing and
then you can talk through it talk
through that yeah and again i think it's
like
it's always it's always a little subtle
to talk about interpretable because it's
sort of in some sense like grounds out
in this like
things that make sense to human
researchers which is like definitely not
a concept i know how to make super
rigorous but there is definitely a
at least for first pass there's a very
strong you like you know it when you see
it sort of either these things or are
doing something that you recognize or
they're doing something totally alien
um and this is a pretty cool neuron that
that seems to be doing a a sort of
activating in all caps text and
increasing the probability that the next
token will be in all caps
um and so sort of that's i think a a
sort of
a
kind of clear rule that makes sense of
sort of if you're currently in caps in
text that like is all all caps and maybe
has been for the last couple of tokens
uh then probably the next token is also
in all caps that's kind of a rule and

[00:30]
it appears uh again we we haven't traced
out all the circuits this isn't rigorous
but it sure appears that that's exactly
what this neuron is doing
and what we're showing on the right over
here
is we're we're showing sort of the um
the the direct contribution of this
neuron
to
the residual stream you can think of
this if you're familiar with the logit
lens it's sort of the logic lens applied
only to that neuron
if you just where more mechanically this
neuron has some output vector in the the
down projection or the output projection
from the mlp matrix we just take that
vector
multiply it through the unembedding and
that gives us a vector over the
vocabulary that says to what extent does
this neuron when it fires increase the
logit for every given token
and
so we're on the left here we've we've
looked at some of the data set examples
examples from our data set where this

[00:31]
neuron fired most strongly where it's uh
its activation uh was was the most
positive
and we can see that it it seems to fire
in places where we are
like writing in all caps uh there's like
some variation we don't totally
understand but the high level story is
pretty clear it's firing in all caps and
then if we run it through the
unembedding on the right and we look at
the the tokens that it most increases
the logit of they are all
tokens that are in all caps um and you
know potentially there's some deeper
structure there but there's a pretty
clear first first pass rule
and it the tokens that it decreases the
probability of are all in lowercase and
so there's a clear sense in which like
mechanistically the thing that this
neuron is doing is it's increasing the
probability of all caps output and
decreasing the probability of lower case
output
and we haven't verified but this is a
one layer model so it would be pretty

[00:32]
easy to use the techniques from our
first paper and trace through in the
other direction and that's that's work
that we hope to do
for
probably for some some of these neurons
in the future
you know i think we would bet with high
confidence that we would just see that
this neuron is looking for
current token all caps like last couple
tokens also all caps in in sort of some
combination
can you comment it all on i think
there's some ways in which uh neurons in
a one layer mlp model are maybe
especially interpretable and especially
easy to understand as rules like this
yeah so the
if you if you kind of looked at our
first paper we kind of
sort of completely factored these one
layer models kind of the the attention
heads run completely in parallel and in
those models they they feed into the
uh directly into the unembedding if you
add in the mlp layer the sort of you get
the exact same analysis for the mlp
neurons
of the the sort of input to the mlp

[00:33]
neuron is the sum of the the direct path
for you know whatever the actual token
value is
plus for each head the output of that
head and each head factors into this
sort of
skip bigram detection of it sort of
looks at the current token looks at
the
the current token chooses which token to
attend to and then or which token or
tokens to attend to and then the tokens
that are intended to produce
value vectors and sort of multiply
through the the ov circuit
uh and so you can you can multiply out
these these
for each of these neurons these these
sort of tables of
well for the the the the current
position
all the sort of the the first order
effect of the current position is
the contribution of the current position
to the input vector for the neuron
is really just
that value is is directly present
um and then it also mediates the

[00:34]
attention matrix but we sort of abstract
out the attention matrix and usually we
find those are are pretty interpretable
we can sort of describe what's going on
there
and then
for every token that we attend to
there's some value that that token
adds to the input value for the neurons
so we can sort of
look at this table of of for every
current for any current token here's you
know what the input value at sums up and
then for every head for every attended
to token
here's the value and then we just sum
those all up and that gives us the input
to the neuron
so i guess that's also something special
about neurons in the last layer
of a transformer are easier to interpret
and one layer models
all neurons are you know by definition
they're both the first layer and the
last layer and so they yeah they have
these special properties yeah right we
talked about these logic values on the
right but the sort of the special thing
about the last layer is that these logic
values are the only thing these neurons

[00:35]
are doing
in the in the general case a neuron is
writing a value into the residual stream
that value will both still be present at
the end of the model for the unembedding
and you know
it might have been modified or deleted
but sort of the
there's conceptually the unembedding is
this big sum that will always and
forever have that term in it but also
that value can be read by later or
attention layers or mlp layers and kind
of in general we expect that most
neurons aren't writing directly to the
embedding as the main thing they're
doing they're producing values that are
consumed by later neurons later
attention heads
but the last layer the only thing
they're doing is writing into the uh
into the residual stream into the
unembedding and so this table on the
right kind of expanded out over the
entire vocab
is a complete description in some sense
of the effect of this neuron there's
sort of there's there's no subtlety or
mystery there it's a large table but
it's it's kind of just a table for every

[00:36]
token how much do you increase or
decrease the the logit for that token
cool okay let's look at another another
such neuron
can you comment on this one yeah and
this one i think is is in some ways kind
of very uh spiritually similar it's sort
of the last one was talking about all
caps text this one is is identifying we
are in base 64.
base64 you're likely familiar is sort of
a common encoding for encoding arbitrary
binary data into
uh a 64 character alphabet but sort of
most of which are the
letters and numbers uh and then plus and
slash and if we look at the dataset
examples empirically it mostly fires in
snippets of
the text that are the base64 encoding of
some value
and if we look at on the right we look
at the effect on the residual stream it
is boosting all of these kind of short
random seeming tokens that are kind of

[00:37]
likely to show up in the way that base64
ends up tokenized
and then decreasing the probability of
all of these sort of nice normal
sensible english words that are very
improbable to find inside a sequence of
of encoded binary data
um and then i guess there's there's sort
of one exception that's kind of
surprising which is men
is sort of being increased um by 0.14
but i guess the hypothesis there would
be you know these models are kind of
small and you know sometimes just weird
you know they're trying to compress lots
of things into a low dimensional space
sometimes there's just weird products
between things yeah that's our best
guess um
whenever i see those things i feel like
i always assign some probability math to
there's something subtle going on that
we don't understand yet but i think
there's also a very good chance that
just you know these these sort of doing
very
right you know this this vocab is of of
size something like 60 000 in our models
and this model has a d model of

[00:38]
a couple hundred
and so you're just you're compressing
very large spaces into into low
dimensional spaces and occasionally
there'll kind of be errors but but in
net they'll they'll aggregate out to
sort of
small probability mass of these actual
errors is the sort of first guess for
things like that
uh
this one i think is sort of a little
more specific the last ones were sort of
like you know broad flavor or context of
the text we're in this seems to be a
we have a number followed by a comma as
sort of where we fire
um
and when we fire there we mostly predict
that we're going to see a three-digit
number because if we're if we're in a
number and we have commas we separate
in english we separate uh chunks of
three digits so if we have a number and
a comma it's pretty likely that we're in
a larger number
uh we're also like it's kind of cute if

[00:39]
you look the little sort of round nice
round numbers like zero zero zero and
then 500 600 700 are more probable
it's sort of
uh
obvious in hindsight that like the
triplet zero zero zero is probably
drastically more common than any other
triplet in text and this neuron knows
that rule to some extent but also i bet
if we zoom down essentially every other
three digit number appears somewhere
near the top of that list
i bet that the three zero zero zero is
especially common when you see a number
and you have a comma in it because it's
often like you're expressing a an and a
dollar amount or something like this
right and you can see our first list
here is sort of you know has an example
of that kind of all of these numbers are
you know round numbers of of hundreds or
thousands
um and again we have a couple a couple
examples in the weights that are make
less sense
or at least don't don't fit quite as
quickly into this theory but it seems
like most of them most of them do

[00:40]
okay so those were a few examples from
small models and hopefully that sort of
demonstrates what we mean by
small models
not only are the neurons interpretable
but they often correspond to these sort
of clean rules that sort of demonstrate
like in this behavior go and affect your
output proper predictions in in this way
um but in larger models we'll see that
there's there's more complex things
going on so that'll be kind of exciting
to to dive into
and and one theory that we've sort of
developed
is that often early layers are decoding
tokens so they're sort of turning tokens
which might sort of split things in
weird ways
into semantic units
and then later layers can re-encode
tokens so they can turn sort of more
semantic units back into tokens
and so some really concrete things that
we'll see
on the the early layer side are
recognizing um things that are you know
token x's and language y so we'll see a

[00:41]
bunch of things where like you know some
token occurs in a lot of different
languages and means different things
those languages so it gets different
there's different neurons for them
and we'll also see tokens that
correspond to detecting multi-token
words or sorry neurons that correspond
to detecting multi-token words and
neurons that tend to
correspond detecting compound words or
proper nouns
um
yeah so let's actually actually look at
those so um
the i think the first one um we can talk
about is these tokens and language uh
neurons and i think i think it's
interesting that
i mean going all the way back to 2019
there was um this nice paper
uh from conan at all where they they
were talking about they just looked at a
single token and how it was sort of
represented a transformer and they found
that even though you know a token like
like die die
initially has the same embedding um
after a few layers you start to go and
see
um the different interpretations of it
um and especially this case where it's

[00:42]
in a different language so if it's in
german and where it's acting as an
article um get separated from the
english ones
um and they also saw this sort of split
between death and and playing with a die
twist die
and so we actually see something
something really similar
um nelson do you want to comment on this
yeah and i think i think one cool thing
is is sort of we we replicated that
previous kind of experiment of you know
you do a umap of some specific token in
different contexts sort of our gel u
models behave kind of similarly over the
first couple layers those those tokens
kind of move out in space
um but we like tried to figure out you
know mechanistically how is it doing
that and we got like a little bit of
traction but it seemed to be a kind of
pretty messy story
um and then in the soft max models the
the first order story at least seems
this sort of pretty good reason to
believe that there's just
one neuron for each kind of language
comma sense pair that detects you know
or a token comma like sense or token

[00:43]
comma language pair that you know fires
on that token when we're in the
appropriate context and writes in some
value that that serves to separate those
in activation space and so
losing that same example of the token di
or d
we find here three different neurons
that all fire on that token but only
fire in
the context of the pro of an appropriate
language
we were able to find
uh with with sort of a little bit of
searching you know afrikaans german and
dutch all had these dye or d
tokens that fired on that token in the
respective language
and so it's sort of a behavior that that
you know we know is there and sort of
for i think there's a good reason to
believe it that any transformer that's
exposed to these languages has this
behavior but in the softmax ones it's
sort of the behavior is just very easy
at least the first order to to
understand how it's happening it kind of
factors very cleanly

[00:44]
yeah and i think a thing that's
interesting here well maybe there's a
few things that are interesting one is
we didn't find an english version of
this
um and so it seems like often in these
cases the like default um and
i i call this default just because i
think our data set has a lot more
english in it than it does have any
other languages um that the the most
common case doesn't get a neuron and
then sort of cases that are less common
get neurons to sort of differentiate
them from the most common case or
something like this
and so yeah we didn't see that
um
i think another thing that's interesting
here is sometimes in smaller models
we'll see
uh neurons that are like
um tokens which might occur in english
but are actually occurring in dutch or
something like this
and here we're seeing something kind of
different i think even in the small soft
max x times x models we saw just really
clean versions of that and now we're
we're seeing these like individual token
in language y and in order to do that
you need to get to a slightly larger
scale um of model

[00:45]
uh
so yeah i thought it was pretty
interesting that we were we're finding
these kinds of neurons
um it's not just natural language though
where this happens
so
uh it also happens with a less than sign
and nelson do you want to comment on
these
yeah i mean i think i think sort of it
points to
language is a sort of very natural or
intuitive sort of thing for us to reason
about of of you know yeah like kind of
you know the the word d or you know the
d-i-e is sort of obviously a different
word in different languages but sort of
the phenomenon here is some much
broader context disambiguation thing of
in sort of you know programming or
technical terms or punctuation sort of
also mean different things in different
contexts and it's it's likely a sort of
very similar phenomenon to language
disambiguation to to separate those
um
and we yeah we so we see this here with
with less than signs being used in xml
versus an irc versus in python and you

[00:46]
know you actually see this for for for
lots of things you know if means
something very different in python than
in english um you know colons and python
versus colons in a in a time stamp mean
different things um so there's lots of
cases where where other tokens like this
mean mean different things in different
languages yeah and i think it's sort of
not really relevant to our point but i
find these studies always kind of fun
because of what they like what they
teach you about what's in your data set
because these sort of data sets are you
know enormous gigabytes or terabytes and
you know generated by some very
automated processes and
uh so if any of these are questions you
could have asked but sort of the you
know when you start looking doing this
kind of interpretability and looking at
individual neurons you're like oh i
guess there's a lot of irc transcripts
in our in our model because they're sort
of self-evidently some amount of
capacity sort of specifically devoted to
processing or processing those and is
that good is that bad i don't really
know but it's it's kind of fun to
stumble on those and sort of get a
better feel for for what sort of start

[00:47]
to get a better feel for the kinds of
things that's in your data set that your
model has learned
and
another fun example is question mark in
c uh where it's used as part of the
ternary operator um claims in the
context of patents
um or three in base 64.
um so
uh you know
three means different things if it's in
a decimal number or hexadecimal number
or on b64 and you can have different
neurons for those
uh cool so
the next sort of family of early layer
neurons that we found
were what you might call multi-token
neurons or or sort of neurons that
correspond to multi-token words
so
yeah maybe it's worth a bit of of
context here although maybe it's clear
to most people sort of we use a uh
a bitewise bpe tokenization pretty
similar to the gpt2 one although not not
exactly the same one and so

[00:48]
you know individual words especially
like longer rarer words get split into
tokens in kind of idiosyncratic ways
sometimes um and i would expect the
details to vary if you're using a
drastically different tokenization
although i expect the phenomenon is sort
of pretty fundamental to the constraint
of of kind of tokenizing words into
tokenizing text into into distinct
discrete tokens but
um sort of that that's that's the
context for for this sort of some
context for the specific tokenization
we're using which which is sort of
deeply informs the details of all of
these examples
so for example trending gets split into
two tokens trend and in
and so there's a neuron that fires on
trending as a whole so presumably it's
locking you know the previous token
checking that it's trend and the present
token that it's in and then fires and
it's sort of able to um like one way you
can think about it it's almost
functionally making the vocabulary
larger by going and creating special um

[00:49]
special tokens that are uh
that or special neurons that sort of
correspond to cases where the where the
tokens correspond where there's a secret
particular sequence of tokens
yeah and i think i think it's also you
can think of this as in some ways
actually very similar to the language
disambiguation problem of you have this
token ing
that that kind of that you know the
total the embedding just has one value
for ing but like what ing means is
actually sort of entirely determined by
the context that it's in in this case
the context is the sort of previous one
or two tokens and the language it's sort
of the broader language context but it's
sort of it's a it's a very similar
problem in some sense of of you know the
the tokenization and the embedding means
that we just get one vector but actually
we want a lot of different meanings or
shades and so we
stitch together some some circuits that
that end up in these neurons to peel
those apart and sort of presumably
every other common word that has a

[00:50]
gerund form ending in ing
that gets split into multiple tokens
most of those also have neurons i would
imagine we haven't done an extensive
study but i did a search though where i
looked for uh first layer neurons that
fire primarily on ing
and it turns out there's like dozens and
dozens and dozens of such neurons so
there are lots of words that end in ing
that the model wants to dedicate neurons
to and indeed it does
yeah and so so again again it's sort of
this like token comma sense or context
or meaning you can kind of
for all of the specifically important
cases in that table we find a neuron and
that's that's really neat
one thing i'm realizing might actually
be surprising to people is this idea
that a first layer neuron that can only
use attention heads can determine the
language like maybe it makes sense they
can check where the previous neuron is
but maybe could you comment on on how
how it might be able to determine what
language it's in
yeah i mean

[00:51]
we haven't studied this for sure but i i
sort of seems you know i would guess
that you
you
uh probably use a sort of relatively
diffuse attention pattern you you know
you arrange to attend to the last like
couple of words
or you know last sort of several words
is sort of relatively easy to do in most
uh positional encoding schemes
uh and then like
sort of likely
every token has sort of a subspace in
the embedding that you know indicates
which language it's in or maybe just
sort of there's a like this token
frequently appears in afrikaans
direction
and you you know your your
ov circuit for that attention head moves
that into some subspace in the present
token and then
you
you can just you know look at that you
know combined with you know maybe you
you also have some weight for the
current token for sort of is this even
plausibly afrikaans is encoded in some

[00:52]
direction and you sort of sum the
is the current token even plausibly
afrikaans and the
do the last several tokens kind of very
likely afrikaans which is in some other
direction in in your
kind of current position courtesy of
that attention head you sum those
together and and then
you know if that value is large
probably the sort of current token is
also afrikaans
so i think another interesting one in
some ways the second one is even more
interesting because it's got different
tokenizations
yeah that i i really i and we've seen
this for for some other words as well
it's a very common pattern is is
um
often certain words get tokenized subtly
differently depending on context so
you can see the first one there's the
capital c and our vocab doesn't have a
single token for civilian with a capital
c
uh the second one there's this

[00:53]
parenthesis uh sort of in a similar way
to the gpd2 we glue spaces onto the
start of tokens so so
uh if there's a space it sort of gets
attached to the next word for the
purposes of tokenization and so
space civilian and then civilian without
a space end up tokenized differently and
so
sort of all of these are very clearly
the same word but they end up as a
subtly different sequence of tokens and
you know presumably for a large enough
model it doesn't want to reason about
these as separate tokens it wants to
so you know some point early on in the
model kind of have the the civilian
direction or the kind of the word
civilian or the concept of civilian kind
of unified across all of these and we
see here
this one mlp that sort of implements at
least substantially that process of
recognizing all of these different
tokenizations and then it's going to
write the the same output direction
because the neuron only has one output

[00:54]
direction that it writes for all of
these and so sort of after this point
presumably the model can use that
direction to to abstract over all of
these tokenizations that got split due
to sort of annoying details of the
tokenizer
um so on the flip side at the end of the
model
it's going to need to sort of do the
opposite and this is a really
interesting thing that we've been
observing where there's often a duality
between the first layer of the model and
the last layers of the model
um
yeah
um
yeah because sort of you know the the
the auto regressive objective and the
tokenization sort of the like model has
to at the end of the day predict the
next token
but but presumably
sort of you know uh
assuming these models are sort of
thinking about the world in a sort of
semantic sense that is like at all
recognizable to us we wouldn't expect
that they're sort of
you know manipulating in token space

[00:55]
like for all of their kind of logical
reasoning or intermediate computation
it's sort of much more likely we we
imagine that they're sort of
operating in some much more semantic
latent space since sort of the last
couple of layers are like all right well
i'm thinking you know sort of this
concept or this this sort of you know
words should come next i guess now i
have to decode that into the constituent
tokens
and we see evidence of of sort of some
specific examples of some version of
that process where
you know the word nappies here and the
word straggler or maybe stragglers are
split or sort of rare enough that they
don't get their own tokens
and we see specific tokens that sort of
fire on when you've started saying that
word on ensuring that you accurately
finish saying that word
um and you know these these don't fire
there are kind of other words that start
with st
uh that get you know that this neuron
doesn't fire for it's sort of

[00:56]
specifically
for the for the
the sort of context of i've started
saying this particular word and i need
to to accurately say the rest of it
one way that i might think about it is
um it almost creates conditional logics
so like suppose that you want to say
something like a diaper you could say
diaper you could say nappies you could
say there's other words for that are
that are in that space um but because
nappies is tokenized as multiple tokens
you first need to say n and then you can
go and say continue with nappies
um
and so if you have a neuron where you
make it so that it can only fire um
through on on the token end and then
continues to go and finish uh nappies um
or if you have a token that only fires
an st and then can continue stragglers
it sort of gives you functionally a new
option in your output space that only
exists
when the conditions for it are sort of
are available to you and that seems very
powerful

[00:57]
um yeah okay so we also see
some neurons related to multi-token
numbers
yeah and i think um
numbers i i think are kind of uh in some
ways a particular victim is victim of
our tokenization scheme they sort of
often end up
uh parsed in ways that kind of appear
very arbitrary uh and we see
uh various neurons that are sort of
understanding or or reconstituting those
in some way
this first one here sort of follow fires
on the sort of 7x or 8x token when
they're immediately following a four so
they're sort of
parsing this specific range of 20
numbers
between 470 and 489 sort of get this
this uh neuron identifies those and and
fires them in some way so so if maybe

[00:58]
starts to give us some hint of of how
this model is is representing
numbers or quantities internally that
sort of it it wants that like you know
roughly 20 digit range to get some some
signal associated with them
the second one i have a sort of
it's a little bit less clear kind of
semantically what it might mean but sort
of mechanically what it's doing is is
sort of when there's a three-digit token
following a one-digit token then it then
it lights up and i it's not yet
intuitive to me why you want that or
exactly why it's useful but but it's
sort of pretty clear empirically what
it's doing and we could
uh trace or explore explore it
downstream
i guess one theory you might have for
why that would be useful
is
depending on how many digits exist in
the previous token and how many digits
exist in the present token
you need to do some work to parse you
know if you want to figure out am i the
third digit in like or what it what
value is the third digit in from the
left
then having splitting those cases out is

[00:59]
potentially quite useful
um so that might be one hypothesis but
we don't know
um on the flip side this is this is
maybe a little less compellingly like a
multi-token thing but there are some
really interesting neurons about how
right at the end for dealing with with
outputs or dealing with
predicting the
um yet going and controlling the range
of of tokens you predicted no quick next
yeah and the sort of first one like
really wants the next digit to be a
three it seems but
it's sort of uh
is is sort of it's probably not like if
i had to guess the first one is sort of
not in cases not necessarily what we'd
expect to find in like
arithmetic cases where we're sort of
specifically doing some some computation
but like
uh maybe there's some other contexts or

[01:00]
we sort of know
sort of pretty sure the next digit is
the three and maybe also there's some
other digits after that
um
it's it's hard to say without a future
study but it's sort of clearly
uh predicting that three and then sort
of predicting not uh choosing ones if we
look at the other side
i guess one way i might think about this
is
um for a lot of purposes including
potentially arithmetic you might want to
be able to predict different tokens or
different digits of a number differently
you might want to be able to like you
know you do your arithmetic and you
calculate what the first digit should be
and what the second digit should be and
so on you might want you might want to
be able to go and predict that and it's
a little awkward because um you're sort
of predicting left to right and it's
that's sort of not like yeah it's not
clear that's the way that you would want
to do things but um
that it might be useful for something
like that
and on the flip side our next neuron
actually instead of predicting the first
digits seems to be more about predicting

[01:01]
the last digits
yeah and we we actually we we we didn't
uh kind of show anything about this but
we we found this neuron most frequently
showing up in
running lists where you're you're
counting or enumerating some items
um and so it sort of seems like
potentially this is sort of
uh you know counting our position mod
100 that you know if if we're sort of
uh counting things and we're somewhere
in the hundreds or thousands sort of
where we're about to hit the 13th item
in particular and so it'll it'll show up
and i think the sort of the fact that
the negative examples are all it really
doesn't want 12 makes some sense if
you're if you're counting up and you
just said 12
you're not going to say 12 again you
know potentially sometimes you'll say 14
and in fact like 13 is probably
relatively common to skip as a number
because it's it's sort of unlucky and if
we're highlighting the you know
uh the stories of a building maybe

[01:02]
skipping from 12 to 14 is totally
reasonable and so this neuron is is less
confident that you know we aren't going
to say 14 but if it if
if if our sort of sense is right that
it's sort of appearing when we're
counting up it makes sense that it
probably mostly fires when we just said
12 and so
it thinks we're going to say 13 and also
it takes it's really unlikely that we're
going to repeat 12.
another i think oh was there anything
else you wanted to do on that let's move
on
so i think another another interesting
category that i think isn't really that
different from the multi-token words um
is compound words and abstraction
and and we we found some fun examples
including uh a machine learning uh
machine learning neuron which i was
pleased to find um
uh nelson i wonder
yeah i don't know maybe you have some
comments on books on like how this
really isn't very different from the
more general phenomenon of uh
of multi-token words or yeah these these
seem i think a kind of again a very

[01:03]
similar phenomenon i could have
plausibly even kind of justified in
calling them the same phenomenon as as
parsing multi-token words of of
sort of there's maybe some some
question of shading or degree of kind of
maybe
you know the word uh die in english and
the word d in german perhaps are sort of
more different than the word learning
versus the word the phrase machine
learning but there's a sort of very
similar thing of sort of machine
learning is is
um
is sort of really a single like concept
or unit in some sense and sort of i
think you know
some languages like german are sort of
fond of forming these compounds by just
gluing the words together without a
space and
like you know we were sort of machine
learning as like kind of one unit is
sort of in some ways not that different
than you know trending as as sort of
just another entry in the vocabulary and
the fact that there's a space there is a

[01:04]
sort of you know weird quirk of our
orthographic conventions rather than it
is sort of something fundamental about
about what's going on here
yeah that seems right
seems right to me so yeah we also have
foreign juice animal welfare there's
lots of neurons like this we just picked
a couple a couple random ones kind of
all of these are sort of you know pretty
common units that that sort of commonly
show up together kind of have some
semantic meaning that is like somewhat
different or or at a minimum much more
specific than
just the final word or just the
individual word
and and the model is is kind of picking
those up and marking that down somewhere
in the residual stream for the rest of
the model to reason about
um
yeah so on the flip side again we're
going to continue seeing this duality or
continuing to see this duality between
the first layer and the last layer um
we're seeing some neurons that are about
going and outputting certain sequences

[01:05]
of words that sort of maybe mean
something together
yeah i think the the the last one here
is maybe the the sort of simplest of of
united nations is a sort of very clear
entity those words have a specific
meaning together that is you know
different than than kind of just the
composition of them separately and then
they're sort of very similar i think to
our earlier nappies or stragglers
example we have this neuron that that
exists to sort of you know help save the
phrase united nations as a unit
although it wants to increase the
probability it increases the probability
that the next word is national more um
but
uh yeah and that united national does
not to me seem like a super likely thing
so maybe there's that exactly
we don't yet understand yet yeah i look
to the dataset examples as well and
empirically when it fires nations is the
next word so i was wondering if maybe
it's just a weird thing about um about
the the embedding and unembeddings and
or could be the bigram statistics are

[01:06]
going and correcting it yep yeah
yeah and i think i think kind of one
thing that is always important to keep
in mind is that you know these these
numbers are are kind of added into the
logits along with kind of all of
whatever the rest of the model is doing
and so these numbers aren't really
like in some sense aren't really sort of
aren't like absolutely meaningful and
kind of especially because the logics
then get run through a soft max
if if it is the case that the model has
a prior that the word national is
incredibly unlikely here then you can
actually add a pretty large value into
it and after the soft max have very
little effect and so
it's it's sort of these numbers are very
informative at least often very
informative but they're they're hard to
interpret with with too much nuance
outside of context
uh yeah and then the first two examples
here are sort of you know helping
produce these sort of common phrases or

[01:07]
you know per cent or
uh lost count lost track
there's a little bit of nuance that we i
think don't fully understand yet of this
sort of
are our
like helping to produce both parts of
the phrase to some degree the sort of
this the first one is clearly involved
in producing the you know lost count or
lost track
but but it also helps it helps generate
both of the lost and the count or the
track to some to some extent which is
sort of
um
clearly part of the same phrase i think
i would not have guessed that you'd have
kind of one neuron
in the very last layer contributing to
both of those logits but
empirically it's sort of it's it's there
it's doing that
um there's probably something
interesting to study about what's going
on there
um sort of again points to
where we're not claiming to fully
understand these neurons at all but the
sort of
they kind of these are all ones that are

[01:08]
sort of you know some large part of what
they're doing is pretty clear and sort
of these strong footholds for digging in
on them to a degree that was unusual in
the jelly models
yeah i think i think this idea of like
having footholds or having like places
we can get traction into into exploring
models is really useful um like you
might not be able to understand
absolutely everything at first um but
having having a path to going and really
understanding these models feels like uh
feels feels really exciting to me
yeah and i think i think having having
sort of a having a like a theory that is
approximately right or informative even
if it turns out to be wrong is is often
sort of
uh a great point to start expanding out
circuits and looking at where they're
coming from and then sort of you know
develop the rest of the theory and the
rest of the nuance whereas if you sort
of start from a place of of total
confusion it's it's kind of much less
clear where to go from there
okay so uh next uh we're going to talk

[01:09]
about some neurons that are more um a
little bit deeper into the model still i
think a lot of these are more on the
earlier side but they're not not as much
the the first layers as you know early
mid layers or something like this
um um or even even mid layers
um
yeah so
uh you know i this is a so this seems to
be an ansi escape sequencer on and
nelson corrected me on on even what it
was called um and i know about these uh
from uh uh from like when i'm writing my
bash prompt and i need to go and insert
them but i don't know anything about
else about them so maybe maybe i'll let
nelson comment on what this neuron is
doing
yeah i mean these are these are the
sequences that are used to to like tell
your terminal to to render text in a
different color or bold or uh this sort
of also can be used to move the cursor
around and do other manipulation sort of
i think probably many viewers like chris
will have like ever encountered them
because they were googling how to make
your prompt red or something and you

[01:10]
just sort of copy pasted some sequences
they're sort of a surprisingly rich and
complex like set of things that they're
capable of doing but
uh most of these look like they're just
just uh
populating colors i think the i think
the sort of
the three there probably is set
foreground to color from memory and the
next digit is the color but um
if i'm wrong please don't at nate i'm
going for probably
so i thought it was just really cute
that this is like it's a very specific
thing it's like a thing that definitely
like
i feel like there's a way in which my
brain has looked at these enough times
and even though not that often that they
like immediately jump out to me as oh
there are those things that i stick in
my batch prompt um and i feel like it's
kind of i don't know it's kind of
interesting the model also has has a
neuron for that
yeah i i i it's it's yeah it's sort of
um
clear evidence of sort of some

[01:11]
context or or shade of meaning or or
kind of knowledge that that is present
in the model at least to some degree
i think we didn't conclude this but
there's there's a similar neuron that
does the like you know when you're doing
a python uh like print statement or or
formatting things or in c you're doing a
print statement and you have like um you
know percent d or things like this i
don't i don't even know what those are
called but these like percent something
to go in and insert something um there's
also a neuron that does those and so
other other sort of similar types of
things
um
yeah another one that goes and detects
the end of an ascii art table so if
you're using using sort of um ascii art
to go and draw a table
uh you can you know there's a neuron
that fires at the end
yup um oh i thought this was a really
cool one so this one fires on numbers
but it doesn't fire on all numbers it
fires on numbers
um

[01:12]
and maybe maybe i guess also some other
words but um numbers that indicate that
that context indicates are a number of
people so the main banquet room can be
set up to seat 150 guests
um family suites that can sleep as many
um as six and there's no like it's not
it's not that there's any it's just
implied that those are
you know i guess i guess it's like if
you if you talk about seeding or sleep
or things like this it's implying
accommodating it's implying that the
uh that then that a number is going to
be referring to a number of people
um
yeah and this is a really i think a
really a really cool one and sort of
um
sort of a clear there's sort of clearly
some somewhat non-trivial kind of
reasoning or context clue here that that
sort of
um
if you had posed the question i probably
would have said yeah kind of obviously a
large transformer sort of has that
capability in some way just sort of
based on you know its output but that we

[01:13]
sort of start to get a handle on on how
it's doing and how it's doing this sort
of relatively
you know nuanced thing of tracking
counts of people in some context
and you see other interesting versions
of this so you see for instance um like
neurons that fire for numbers when
there's a score in a game and again it's
not like it's you can't just tell from
the previous word you sort of need to
know from context that um you know
uh they're up three or something like
this means that three is a is a score in
a in in some sport or something like
this
um
so there's lots of lots of things that
are kind of of this flavor
yeah and i think um
to
sort of one thing sort of just to touch
on the stuff that we said earlier about
sort of just having footholds on these
models i think sort of
er er er
having a neuron like this
opens the possibility of if you know
that neuron is ultimately reading from
one direction in residual space and
writing to one direction and so uh you

[01:14]
can imagine sort of
having you know
this sort of gives you a foothold of
like at this particular point in the
transformer those directions in residual
space mean
something like you know we're talking
about people or numbers of people and
and you could imagine tracing those
forward and seeing what other neurons
that attention heads interact with those
and
um you know kind of actually doing this
in a large model is non-trivial but it
kind of gives you a very concrete
foothold to start to
to explore outward and try to try to
find the kind of fuller circuits that
are doing these bits of abstract
reasoning and
and so sort of even if we don't have the
kind of complete story or our story
isn't isn't right or isn't exactly right
or sort of later falsified having these
these footholds to start to trace out
feel like really exciting for
for for starting to stitch together
stories of what's going on in broader
parts of these models
yeah that feels very true

[01:15]
um another interesting one is white
space when you had indentation
so
i think this is actually a little subtle
but it's it's like
you know here we indent and it fires
then you unindent then it doesn't fire
then you indent again then it does fire
um you have a new function you indent
that fires you indent again in an if
statement you fire you unindent for an
else you don't fire you indent again you
indent again and then you unindent then
you indent again then here
the white space is increased but it's
not really indenting for at least not
for like python's purposes it's it's
just going and for this function the
arguments are indented so we don't do
that um
then i guess this is still the same
level of indentations maybe it fires
there then like try you go in indent you
fire
you unindent for accept then you indent
again then again these are a function
statement or a function call so you
don't really fire for them and
so it sort of seems to be doing
something something actually quite
sophisticated about um the uh
yeah about helping parse indentation or

[01:16]
something like this or parse you know
what's nested under what in
python yeah and i'm actually i'm kind of
uh i i i'm pretty sure from memory that
the actual uh the python parser
deals with indentation by sort of
injecting virtual tokens into its
tokenization stream of sort of there is
a token for the indentation increased
and the indentation decreased and then
sort of once you have those like parsing
uh you know sort of you can use a kind
of normal parser and treat those the
same way that you would like curly
braces in c
uh and so sort of this you know again
super speculative early evidence but
sort of hints at the model potentially
doing a sort of
surprisingly similar thing
to reasoning about about scope in in
python
that would be really delightful if it
turned out they were analogous
um
you know
who knows that yep
it would be delightful if true it really
yep yeah
um here's another one that's like a

[01:17]
number a particular interpretation of a
number so in a date um stamp you know
this is the d portion and it just always
fires on the the day token and date
stamps
um
dna sequences
uh
and often there's like this particular
format way that you format sections
where like if you have a a list of
things and you want to or like a title
so if you if you're a list of things
you're giving like a little title to
each item in the list um you might go
and like do you know number then like
title and then period and so you have
the something that fires only on the
periods when they're used as sort of
part portions of these titles
um or the end of a title or another
neuron that fires only on ingredients in
a recipe
um sorry quantities of ingredients in a
recipe
and so yeah these all all seem really
um
i don't know there's there's like
literally like just you looking through
these models and you find hundreds of
neurons like these and they they seem to
have really really clear hypotheses and
often they're like quite sophisticated
and rich and interesting

[01:18]
um okay so uh
there was this paper that i i actually
was lucky to work on with a couple of
colleagues um
on studying multimodal models
uh uh in particular clip
and uh
the the lead author was gabriel go
um
and we found some some really
interesting highly abstract neurons and
something i've been wondering since
really like one of the first experiments
i did when i started poking around in
language models was whether we could
find similar neurons because um this was
sort of a vision model that was trying
to align itself with a language model in
some sense um and it developed these
really highly abstract neurons that sort
of uh you know i thought i thought
perhaps would exist in language models
and previously i just wasn't able to
find them besides significant effort so
um we found neurons that correspond to
various famous people and also neurons
that correspond to various geographic
regions
um
and even though we couldn't find that in
in uh
in the previous models things like this
have been popping out really quickly and

[01:19]
really easily just uh poking around in
in our models now so
um we found neurons related to various
famous people joe biden hillary clinton
donald trump martin luther king just
lots of things you know various various
u.s presidents various famous you know
famous figures various um polit you know
world leaders and politicians and you
know you pick it there seem to be seem
to be lots of neurons yeah and i think
one thing i want to highlight here is is
in some ways these are are sort of
similar to just these sort of
multi-token words right you know kind of
joe biden you can you can think of as
sort of a multi-token word meaning joe
biden but if you like look at the the
third example here for instance sort of
uh very clear from context that we're
talking about donald trump but the word
donald doesn't actually appear here so
so i think at least some of these are
kind of potentially they're sort of both
flavors exist of ones that are sort of
just doing you know
gluing together a sequence of tokens but

[01:20]
some of them are also i think sort of
more a bit more contextual of of
of uh parsing context to a somewhat more
subtle degree to
to associate that you know we're we're
talking about the specific individual
even though we didn't we didn't say
their full name in the usual order
yeah and we've actually seen seen a lot
of these be a few layers deeper in
rather than in the first layer
um
i think hillary clinton is also kind of
interesting because it's already firing
on hillary and
sorry you're going to say something oh
yeah i think so the fact these are a few
layers in kind of accords with the sense
that
they're
they're they're not kind of doing
anything like incredibly sophisticated
but there's there's a bit more
abstraction going on here than than kind
of just gluing tokens together
um
we've also found geographic neurons so
one way you can sort of illustrate this
is you could just feed in a list of
country names and then color a map by
how much they fired that's something we
did in the the multimodal neurons paper

[01:21]
and this seems to be like a sort of
france europe neuron um and you can see
it also i think this is french guinea
over here um
uh
uh maybe i think french something um and
and you can see it's know mostly firing
firing on europe and so there seem to be
these these neurons that are at least
corresponding to sort of geographic you
know sets of of nearby geographic
country names um
but uh i think more
you know if the multimodal model is
anything to go by or the experiments
there midi are also more generically
encoding um
the these countries it's not really
something we've investigated yet
okay so so far we've talked mostly about
um like even if they're more
sophisticated neurons that are really
about detecting like a particular thing
um
but uh or like a particular like object
or or like what a token means in some
particular context but there's also
these neurons that seem to be more about
phrases um sort of as you get towards
the middle of the model

[01:22]
um so one sort of family of these that i
found especially interesting is these
sort of like descriptive clause neurons
so for instance if you're describing
music you know you might say well you
know they sang in
box moss in b minor with the boston
symphony orchestra conducted by um with
and all of these are sort of things that
are sort of
adding descriptive information about
about some musical performance or you
know i was dressed up in a short sleep
weather in a winter campaign army jacket
or you know you might have another one
that we have a taste smell descriptive
clause um and uh it you know it has a
has a salty earthy taste
and
so all of these are sort of like
particular kinds of descriptive clauses
there's a neuron for each one of these
and you just look through them and like
you know the the smell one it's just
always referring you know every time it
fires it's it's referring to like some
place where somebody's describing a
taste or a smell um

[01:23]
so yeah i thought that was really
interesting and um or like maybe this
last one's the most interesting like
there's um you know with the word russia
emblazoned across the front um well so
it sort of likes to describe when
there's um
when when there's uh
like writing on some object um and you
can imagine like i often wondered you
know some
i think i think this was actually
something i was sort of impressed by at
one point where you know they're
you you sort of like a model can answer
um
and maybe maybe the place where i was
most impressed by this was with
multi-modal models but you know can
answer questions like what's written on
what object or something like this um
and having features like this is kind of
cool
is there anything you want to say about
these nelson i don't think so i think
they're
we haven't studied them deeply i do
think it is it is cool this sort of
um
these sort of phrases and kind of
snippets and contexts get get um

[01:24]
pulled out sort of and i think so sort
of the way these things kind of are a
little bit
kind of continuous or smeared across the
context dimension sometimes i think sort
of the model is is often like
doing things that are less crisply token
aligned then than we might imagine
especially in the middle of the model it
can sort of
be be
in some sense reasoning or acting
kind of across a bunch of positions at
once
one thing that i think is actually kind
of interesting
is these often stop and start at
interesting points
so like
um
well here with the word and then we
actually get to the thing that's written
on the object you know you don't go and
have this then you continue firing again
later on
and so or like here you know um
uh
well okay maybe in a winter campaign
army and then jacket doesn't fire and so
it's like the it's like the often like
that or like you know has a salty earthy
and then you don't fire on taste so

[01:25]
there's something interesting about when
these fire and when they don't and it
won't surprise me there's a different
neuron that fires on in those places
where um yep
yeah and i think it's sort of sometimes
also like kind of interesting to do like
some things that some feel a little odd
i think makes sense when you remember
that these models are are kind of auto
regressive like
the brew has a salty earthy taste and
sort of very plausible that we were
going to continue talking about the
taste and so sort of when the model sees
that and
it sort of seems like it's sort of you
know the and is still firing because it
doesn't know what comes next but then as
soon as we stop talking about the taste
then it fires and so
sort of maybe fires for like one token
longer than you might expect
um but i think if you if you just think
about the auto-regressive nature it
makes a bit more sense there
we're back after an interruption where
the internet cuts um but

[01:26]
uh yeah we can talk about some more
interesting neurons
uh
okay so there's yeah there's there's a
lot of other sort of interesting sort of
clause-like neurons do you want to talk
about any of these nelson
yeah i think these are kind of similar
to the last one i think the
some of them
are sort of not obvious things that i
would have predicted existed but sort of
make sense you know
driving directions
um sort of a sort of clearly
recognizable thing that it sort of is is
somehow
important to to flag all of
you know
historical periods time ranges
cause of death feels like a kind of very
natural unit this would have that you
you encounter that a lot indexed it sort
of is a specific thing and and we use
there's a neuron that that seems to to
fire over those
um
but yeah i don't know there's much more
to say that i have to say about these um

[01:27]
um
another set that i thought were really
interesting we're sort of well i'm not a
linguist so maybe i'm misusing this but
you might describe those like discourse
markers
so
uh like
little turns of phrases people say to
emphasize the significance or importance
um of what they're about to say like
what's so amazing about you know or but
what's really in remarkable is or
um what is really striking is you know
all these things are just they
they they aren't so much carrying
content as they're like they're carrying
like a
they're helping highlight the importance
of something or something like this
um or conversely like there's another
neuron that fires for things like
um some would later say or
one may loosely call or
it might be more accurate to
uh you know all these things are sort of
like
they're like hedging a little bit or
like distancing yourself a little bit
from the thing that's being said

[01:28]
and
yeah and also i'm not sure if you have
any other any other thoughts on these
yeah i i haven't looked to spend much
time looking at these i think they
i think i think sort of i don't know one
[Music]
one thing i always just think about when
i'm seeing these is sort of the the
kind of
dual challenge that the model always has
when it's dealing with these is sort of
like when it's in the middle of this
phrase it sort of has to predict the
next token but then it kind of also like
you know after the phrase it probably
really wants to to treat these to some
extent as as a unit to sort of you know
abstract the you know that claim was
hedged sort of and and extract that fact
as a sort of kind of relatively single
thing where relevant
um
and i don't have a kind of concrete
story of how these neurons relate to
that but i was sort of keeping those
sort of dual challenges of you know it

[01:29]
does have to deal has to consume these
and it has to output them token by token
but also wants to abstract them
uh
sort of sometimes helpful for for
thinking about what these neurons might
be doing or why they might be there
yeah it makes me think a little bit of
those neurons we were kind of surprised
by um for outputting multi-token sort of
words or outputting
uh sort of compound words like united
nations or um or percent where it was
like increasing both per and yeah
um you know if you're you're firing sort
of over like this more contiguous range
where there's some higher level
action that's expressed in multiple
words or like higher level concepts
expressed in multiple words maybe maybe
it's then also natural that it might
push you a little bit later on to have
neurons respond to like that general
category of things and then maybe maybe
that makes it more natural
yep it's interesting though
um
okay so that's what we're going to say
about specific neurons um hopefully

[01:30]
those were interesting there were some
more general phenomena that we observed
sort of as we were poking around at
these neurons that maybe are worth
highlighting for a minute
um and i guess a lot of these will be
sort of us drawing analogies between
things that were found
by the original circuit thread um in
vision models and then things that we're
finding finding here so in vision models
we were often able to go and organize
neurons um into sort of families of of
interesting of neurons that seemed very
closely related so here we have like
some high low frequency detectors some
brightness gradient detectors some
curves some black and white versus color
detectors
um
and in some sense these are sort of all
like variations on the same thing that
you could sort of think of as one type
of neuron like the high low frequency
detectors are in different orientations
the contractors each one so they start
detecting roughly the same thing in
different orientations the black and
white color detectors are mostly the
same thing in different orientations
like black and white on one side color
on the other there's a few that are
center color and black and white around
them
are all black and white or like the
gradient the brightness gradients are

[01:31]
mostly in different orientations but
some are like dark in the middle and
bright on both sides but they're sort of
in some sense all the same family of
thing
well
um
yeah and i guess another another
interesting observation of these is many
of them not only are these families but
they're they're often like organized on
on
you know they're they're equivariant in
some sense so they're they're they're
like there's some type of transformation
that sort of they're all like
transformed versions the same thing so
like they might all be rotated versions
of the same thing or um in more abstract
ways you you might see neurons that are
like the same thing but with a short
stud or a long snout or dogs versus
humans or um visual perspective on the
same thing or things like this these are
sort of more abstract
um and the thing that's exciting about
this kind of stuff or like that one
reason you might really care about this
kind of stuff is that it can really
simplify your model if you can if you
can go and find if you can if you can
say well you know it seems like there's
a lot of neurons here but really there's
just one thing parameterized in this way
you know that might help you uh with
going and
uh

[01:32]
yeah with being able to understand these
things
and so we i think we started to see some
things like this a little bit um in in
language models
um nelson maybe maybe you want to talk
about this
yeah i think of
and i think sort of this is
sort of this notion of equivariance is a
little more uh general but i sort of
think of it as sort of this sort of
notion of of symmetries or sort of some
way that we can like collapse the
neurons down into a sort of conceptually
smaller set of neurons and all of their
symmetries sort of you know some some
way that we can collapse them down and
so these sort of
these like token x in language y or or
even more broadly sometimes sort of
token x in context y
kind of gives us one of these sort of
symmetries of we can kind of have one
rule or one conceptual rule that that
generates or describes a larger number
of neurons and so sort of gives us a way

[01:33]
of of compressing these neurons in sort
of conceptual space or in reasoning
about them space
um and and as sort of as as chris was
saying sort of some of these can
actually already be pretty large like
you know token x and language y they're
sort of
um i don't know there's i don't know how
many tokens there are that are ambiguous
between language but there's there's a
fair amount of you sort of you you have
this sort of potentially
this kind of you know x by y matrix and
then i think the
especially for
kind of parsing words you know common
common endings to words like you know ed
or ing in english
those often get split for a large number
of words and so you kind of you know
parsing all of these words you sort of
end up with sort of
there's a whole bunch of neurons that
you can kind of just think of as like
added vocab vocabulary members in some
way
um
and and kind of generate these huge sets
of neurons that you can kind of abstract

[01:34]
away into one conceptual
family or rule for thinking about and
sort of start to eat away at the scale
of these models in your description of
them by by kind of exploiting these
these patterns
yeah yeah i think that's right i think
something that's cool about this
language um token accent language y1 in
particular is that it's almost giving
you this 2d grid where like you could
imagine language you know like a column
for each language and a row for each
token and there's holes in that like if
you you know we've these are four
neurons we found we in dutch we in
german best and dutch best in german um
uh in some of these cases they they may
not be like a standalone word they might
be a token that's in in other words
um
but uh you know you see a lot of neurons
like this and if you start to look at
them you know often there's there's
yeah the same token occurs in many
languages in each language as many
things and you can almost start to
imagine this 2d 2d grid with with gaps
in it um
and that's that's kind of interesting to
be able to organize your neurons like

[01:35]
that and
uh i think i think as nelson says you
know that the key reason that this is
exciting is
you know large language models have
millions tens of millions of neurons
maybe
and and probably that'll you know maybe
they'll be larger models in the future
so you know how how in the wide world
can we deal
with
uh
with models that have that many neurons
and well i think our hope has to be that
there's some structure organization or
way to group or organize
these neurons such that we don't need to
think about every single neuron
independently
but instead we can go in and somehow
organize things
yeah this is another interesting
phenomenon um yeah nelson i don't know
if you want to take this or i should
um
yeah i think this this is um as we look
at larger models we we sort of see

[01:36]
sometimes that a kind of one neuron in a
smaller model seems to sort of split
into more specific cases in larger
models like we we showed we showed a
number of these specific examples of for
the one layer model we found just this
base64 neuron that you know it seems to
to first order just you know note we're
in base64 and predict more base64.
um but then for large models we actually
found neurons for
every character or at least many common
characters or tokens that appear in
base64 and there is there's neurons for
each specific one um
and then kind of similarly small models
sometimes have just like this is a u.s
politician neuron or
this is a token that commonly appears in
english and dutch
but or you know maybe even more commonly
appears in my corpus in english but that
we're in a co we're in a dutch context
and so probably it should be interpreted
as dutch instead there's just kind of

[01:37]
one token that does that in a kind of
you know probably kind of rough way for
one neuron does that in a kind of rough
approximate way for for many common
english tokens and then those fission
into these these more specific ones
um
and so
that kind of gives us another sense of
of
these these sort of patterns of these
large models we can we can group the
neurons in these ways we can try to
understand them you could imagine trying
to
to maybe in a kind of mostly automated
way build these sort of these these
trees of these fissionings of these
neurons
we don't have kind of concrete leads on
how we do that but it seems it seems
conceptually at least plausible
um
and that that might give you another
kind of powerful way of kind of trying
to to categorize these and group them
and understand them
and i think it's just also sort of a
kind of cool demonstration of kind of uh

[01:38]
what what these models are doing as you
give them more capacity
yeah it's sort of it it paints an
interesting picture of what it means to
have these clean scaling laws where you
know loss goes down as you make models
larger because it sort of suggests like
like maybe there's some sense in which
at a micro scale what's really going on
is all these neurons are fishing into
finer ingrained distinctions and you
know in aggregate that creates a very
smooth decrease in loss but it's
actually like all these like very micro
like actually very discreet changes to
the model in some sense
and it's a cool cool way to imagine
things
okay so i think that's everything we uh
we i yeah these slides plan to cover
nelson is there anything else you want
to chat about
um
i don't think so i think we've we've
spent a lot of time on these um i think
we're we're pretty excited about the the
degree to which i think kind of
uh there's a bunch of research
directions that we sort of tried
unsuccessfully on our jelly models that

[01:39]
they were sort of excited to to
revisit again and it seems like a lot of
a lot of ideas that didn't work kind of
now just work and so there's a lot of
exciting directions um
we
sort of this very early days for these
results but we wanted to to share this
video because i think if other teams are
are trying to do similar things if if
you're able to
to tweak your activation function in
that way there's a kind of good chance
you'll get you'll get similar results
and if you do or you don't we'd love to
we'd love to to hear about it as well
um and i think there's a good chance
we'll be releasing more of these and
probably eventually a paper as we
get more of these results and and kind
of uh make some of these observations
more concrete and rigorous or
or otherwise but um for now we're just
excited by how how fruitful these models
are to look at
yeah okay now so i'm gonna put you
slightly on the spot before we close um

[01:40]
you know you have this blog post about
how computers can be understood and
sometimes you like rant on twitter about
like you know computers can be
understood damn it uh i believe and i
continue to be rewarded so i you know
the question i want to ask is you know
can neural nets be understood or
where are you on your view on whether we
can make a similar claim about neural
networks
i think i think it remains a a kind of
profoundly open question of of how well
we can understand neural networks um i
think sort of uh believing that it is an
open question honestly probably makes me
weird in the field i feel like sort of
the the modal opinion is to just like
forget about trying to understand these
treat them as black boxes and and make
them go
um
but i i
i'm i
i think sort of seems very clear from uh
i think both the sort of the the past
circuits work that that you and others
did and from our initial results that

[01:41]
the
these these neural networks are sort of
far more understandable than than you
might believe and that it's possible to
to make progress and to to reason about
them and i'm i'm kind of
uh very excited about the project of of
kind of doing our our damned best to
understand neural networks and and kind
of
uh maybe we'll fail but but it's sort of
or we haven't
we haven't filled yet we have not yet
sort of exhausted anywhere near the
level of effort that would have would
have to exhaust for me to conclude that
it's impossible
and i
and and honestly it sort of the
i would never say that it's easy but it
does really feel like
many of the things that we try work at
least in part and bear fruit and so it
sort of
you know continues to be worth worth
trying and i'm very excited about the
prospect of of getting to a world where
we do feel like we can kind of mostly
understand what's going on inside of
these and it seems very possible how

[01:42]
much has this sort of this result sort
of updated you on that like i feel like
i feel like for me at least before this
result it sort of felt like you know i
was determined to try and like i sort of
i believed abstractly that we were quite
likely to get traction but it really
felt like i it didn't feel like i could
really approach like you know an
arbitrary behavior arbitrary behavior on
a neural network and think that i had a
good chance of figuring out what was
going on and i i feel like that's
actually maybe changed for me with these
results where i now sort of think like
you know give me an arbitrary behavior
and i have a decent chance of something
i'm curious if you have any sort of
yeah i think the
i think the rome paper especially gave
me a lot of confidence that it was going
to be possible because because they it
sort of you know that they're
though those methods definitely i i
think sort of
were were complicated and messier but
sort of you know it gave gave me some
confidence and we were able to replicate
some of those results to sort of

[01:43]
you know
these mlp layers sorry oh this was our
colleague neil nanda who's been going
yeah we'll work replicating neil has
done some cool work uh replicating some
of those and so sort of it sort of
i don't feel like this has
drastically shifted
the sort of weight that i put on whether
it's possible i do think it has
drastically shifted my expectation of
how easy it might be
i think sort of but before these results
i would have said like i think it's i
think it's likely that we'll be able to
tease apart the the mlp layers but we
sort of might need pretty high powered
like mathematical and software
engineering tools to sort of get at them
um whereas uh with it's sort of yeah i i
i i
i sort of put decent probability mass
after this result on if you name an
abstract behavior and if the team sits
down with kind of our current tools and
our current understanding for a couple
of days there is a decent chance we will

[01:44]
emerge with a sort of roughly accurate
first order description of that behavior
like like
not certainty but i now i put like
appreciable probability mass on that in
a way that i i didn't before
well
i think it's pretty exciting and uh yeah
we'll we'll leave it there but um yeah
very excited to hear from anyone who's
yeah maybe this kind of the one other
thing that i think sort of we take for
granted but is sort of
i think i think our first two papers we
did a pretty good job of sort of
understanding attention to our own
satisfaction of sort of feeling like we
know what's going on there um i think
with this result with these models that
sort of the mlp layers seem like by and
large like pretty easy to understand
sort of a lot of the the obvious things
kind of mostly work for giving you a
good foothold on them
and attention and mlp is
sort of all there is in these models and
so
um
these models are very large in sort of

[01:45]
you you get emergent behavior out of
composing simple primitives is this sort
of general theme of complexity but but
sort of
it feels like we have a very good handle
on attention it feels like we have a
pretty promising handle on mlps and at
the end of the day that's all there is
and that sort of
is not a
not a
not necessarily sufficient that like you
know we can understand these models and
i'm definitely not going to assert that
it's easy because they're very large and
you end up with emerging behaviors but
it it feels like a very promising place
to to sit to sort of start going deeper
i think so
onwards
yep
all right
thanks for joining us everyone
thank you chris

</details>


Having quantitatively SoLU's effect on the interpretability of neurons, we now undertake a more open-ended exploration of the interpretable features we find in SoLU models.  For this we don’t attempt to be rigorous or systematic, or to compare to non-SoLU models, but informally most of what we describe here we were unable to find prior to training SoLU models.  Thus this subsection can roughly be thought of as a few selected examples of what SoLU enables us to find.

#### 6.3.1 One-Layer Model Neurons

We start by exploring a one-layer SoLU model. One-layer transformers have some special properties which often make mechanistic interpretability easier. For this investigation, the most important observation is that, modulo concerns about LayerNorm, the activation of each MLP neuron has a linear effect on the logits. By multiplying the vector of output weights for the neuron by the unembedding matrix, we can directly read off which output tokens have their logits increased when this neuron fires, and by how much. Further, this is the only effect of such neurons in one-layer models.

This has several benefits. Firstly, it puts our interpretability efforts on much firmer ground, as we can both heuristically infer the purpose of a neuron from dataset examples, and then validate this understanding by cross-checking it with the effect on the output logits. But even more than that, it means that if neurons are interpretable, they correspond to interpretable end-to-end rules of model behavior. We consider this particularly useful in combination with our previous paper on reverse-engineering small attention-only models  as, rather than only being able to fully reverse engineer a small attention-only model, we can now reverse engineer a 1 layer full transformer.

As an example, we have identified a neuron that appears to fire precisely on text encoded in base 64 ([as often occurs in web URL’s or other contexts](https://en.wikipedia.org/wiki/Base64)).  Using the fact that our model has only 1 layer, we can identify which tokens this neuron increases the probability of, and unsurprisingly it increases tokens corresponding to random mixed-case strings, while decreasing the likelihood of common English words.  Other examples include neurons corresponding to all-caps text (the same neuron shown in Figure 3) or to a number followed by a comma (as occurs when writing numbers with four or more digits)

![](images/img-009.png)

Figure 5: A neuron in a 1-layer SoLU model that appears to fire on base64-encoded text (left).  This is confirmed by the fact that the neuron's expanded weights to the logits (right) increases the probabilities of a bunch of tokens in mixed case that rarely occur in words, while decreasing the probability of a number of tokens representing English words. It can be understood as an interpretable rule that on base64 text, the next token is more likely to be base64 as well.

#### 6.3.2 Early Layer Neurons in Larger Models ("de-tokenization")

Next we move our exploration to larger models – our remaining examples will come from a mix of the 16L, 24L, 40L, and 64L models.  One of our most interesting findings is that neurons in the early, middle, and late layers of a large network tend to play very different types of roles, just as features at different depths of conv net vision models are known to be different.  We'll discuss neurons from each in their own section, starting with those in early layers.

Early layer neurons seem to often be involved in mapping the “artificial” structure of tokens to a more natural, semantically meaningful representation.

Many early neurons seem to respond to multi-token words or compound words. For example a neuron which fires on the final token (“ing”) of “Trend|ing” (essentially mapping the sequences of token “Trend” followed by token “ing” to the meaningful word “Trending”). Some other examples include:

* Neurons responding to specific words which are split into multiple tokens: “Bank|ing”, “word|ing”, “Ch|olesterol”, “Libert|arian”, “Civil|ian”, “Sh|anghai”, “Not|withstanding”...
* Neurons responding to the names of famous people: “Martin| Luther| King”, “Donald| Trump”, “Lyndon| Johnson”, “George| Orwell”, “Ernest| Hemingway”, “Muhammad| Ali”, “Oprah| Winfrey”...  (cf. )
* Neurons responding to other nouns: “Human| Rights| Watch”, “International| Monetary| Fund”, “Hurricane| Matthew”, “Real| Madrid”...
* Neurons responding to compound words: “book| club”, “social| security”, “computer| vision”, “organized| crime”, “birthday| party”, “heart| attack”...
* Neurons responding to LaTeX “\” commands: “\|left”, “\|frac|{”, “\|begin”...

We also see many early neurons which respond to a token in a specific language or context. For example, we found three early layer neurons that appear to represent the word “die” when used in each of three non-English languages: German, Dutch, and Africaans (note some related results were found by Coenen et al. ).

![](images/img-010.png)

Figure 6: Three neurons that fire in response to the word “die” when used in each of three specific languages (and each of which don’t fire on any of the languages or in response to “die” in an English context).

Distinguishing between the same token in different contexts isn't restricted to natural language. For example, there are neurons that represent the “<” character in the distinct contexts of python, IRC, and XML/HTML.

SoLU seems to have made an especially big difference for these early layer neurons: despite significant effort, we made almost no progress in understanding early layer MLP neurons in normal models, but easily understood many once we began looking at SoLU models.

#### 6.3.3 Late Layer Neurons in Larger Models ("re-tokenization")

Late layer neurons (those near the output of the network) often do the opposite of what early layer neurons do: they mediate the conversion of words or contextualized tokens back into literal tokens.  For example, one neuron in the last layer fires on the token “st” while increasing the likelihood that the subsequent token is “rag”; essentially this is a way of converting or dictating a representation of the word “st|rag|glers” into its constituent tokens one by one for output. Similarly, a “nappies” output neuron fires on the token “n” and increases the probability of the token “app” to help write “n|app|ies”. These neurons essentially simulate an additional output vocabulary item which is only available when certain conditions are met in the previous tokens.

![](images/img-011.png)

Figure 7: Neurons that fire on a given token while increasing the likelihood of a specific next token.  When they occur in a layer late in the network, these neurons can be interpreted as decoding a word (which the model internally represents) into its constituent tokens (which the model must output).

#### 6.3.4 Middle Layer Neurons in Larger Models

Neurons in the middle layers often represent more complex, abstract ideas.  For instance, there is a neuron that appears to represent numbers when and only when they refer to a number of people:

![](images/img-012.png)

Figure 8: Neuron that appears to fire on numbers (including both numerals and number words) when and only when the number enumerates people (as opposed to counting something other than people).

A huge variety of interesting neurons can be found in these layers. Some common categories we observed include:

* Neurons which fire on particular types of descriptive clauses: a neuron which fires on a clause describing a sound, a neuron for clauses describing clothing, a neuron for musical descriptive clauses (e.g. "in the key of C major"), a neuron for clauses describing text written on an object, …
* Neurons which respond to discourse markers: a neuron which responds to markers emphasizing the importance of something (e.g. "the amazing thing is"), a neuron which responds to hedging (e.g. "it seems to me that…"), …
* Neurons which disambiguate a special interpretation of a token:  a neuron which responds to A/B/C/D when used as grades, a neuron which responds to the “day” portion of a date, a neuron which responds to numbers when they're a quantity in a recipe, a neuron which responds to C-style format specifiers (e.g. "%s" or "%d") in strings, …

But there are lots of neurons that are hard to put into these categories, such as a neuron which seems to help parse ASCII table columns.

In summary, the general pattern of observations across layers suggests a rough layout where early layers "de-tokenize," mapping tokens to fairly concrete concepts (phrases like “machine learning” or words when used in a specific language), the middle of the network deals in more abstract concepts such as “any clause that describes music," and the later portions of the network "re-tokenize," converting concrete concepts back into literal tokens to be output.  All of this is very preliminary and requires much more detailed study to draw solid conclusions. However, our experience in vision was that having a sense of what kinds of features tend to exist at different layers was very helpful as high-level orientation for understanding models (see especially ). It seems promising that we may be developing something similar here.

#### 6.3.5 Abstract Patterns

In the course of exploring neurons in these SoLU models, we noticed a few more abstract patterns, which seem worth noting despite us not having investigated them in detail:

Neuron Splitting: As we make models larger, we've observed several cases where a neuron in a small model appears to "split" into multiple neurons in a larger model. For example, a hexadecimal neuron splitting into neurons for specific hexadecimal characters (e.g. a "3" in hexadecimal neuron), or a tokens that occur in English but are actually German in this context neuron splitting into specific token X in German neurons (e.g. "die" in German).

Neuron Families: Understanding circuits in vision models can be simplified by as much as 50x by understanding that many neurons are parameterized by certain kinds of symmetries (e.g. many neurons implement rotated versions of the same feature) . More generally, in the original circuits thread, it proved very useful to understand neurons as existing in families of similar neurons . We've noticed that a significant number of early MLP neurons in language models implement features of the form "token X in language Y," which might be thought of as forming a family of neurons parameterized by X and Y. Possibly this is an entry point for discovering an abstract kind of equivariance in language models, such as equivariance to language.

Duality Between Early and Late Layers: There often seems to be a duality between the types of features we see in early layers and those in late layers. In particular, we see early features for recognizing multi-token words or compound words, and late features for outputting certain multi-token words or compound words back as tokens.

Similarities to CLIP Neurons: We noticed many of the types of neurons described by Goh et al.  in their investigation of CLIP. In particular, we observed neurons corresponding to famous people and geographic regions. This might be seen as a kind of cross-modality [universality](https://distill.pub/2020/circuits/zoom-in/#claim-3) . One intuition is that since CLIP was a multimodal model and the vision side was trying to align images with text, it was incentivized to represent features that naturally occur in language models.

#### 6.3.6 Partial Mitigation of Interpretability Illusions

One of the hazards of investigating neurons is that it can be easy to develop incorrect theories of neurons. A recent paper by Bolukbasi et al.  emphasizes the risk of "interpretability illusions" in the context of Transformers. More generally, the original Circuits thread (especially Cammarata et al. ) emphasized the importance of using multiple lines of evidence before having confidence in a theory of a neuron.

The results in this section are aimed at being exploratory. While they're generally a bit deeper than the quick judgment calls used in our quantitative evaluation, the investigations of any given neuron tend to be quite superficial compared to Cammarata et al. . For that reason, we wouldn't stand behind our theories of most neurons with a high level of confidence. However, there are several factors which mitigate certain classes of misunderstandings:

* Our dataset examples are collected the same, highly diverse data distribution our models are trained on (partially mitigating the concerns of ).
* We made it easy to open any dataset example in an interactive editor where one could observe how activations change if one edits it. While we didn't do this for every neuron, we often did when we felt uncertain or confused.
* For some neurons, we looked at dataset examples across a range of activations.
* For some neurons, we did bespoke experiments, such as comparing a hexadecimal text neuron to a regular expression.

### 6.4 Implications of LayerNorm

Earlier, we decided to use models with a LayerNorm after the SoLU activation function in order to recover the significant performance drop we observed when using SoLU alone. Unfortunately, as we observed in [Section 4.3](#section-4-3), LayerNorm significantly complicates the story for polysemanticity and superposition.

One hypothesis is that SoLU creates something like two tiers of features: neuron-aligned and non-neuron-aligned features. The neuron-aligned features are what we observe when we examine SoLU neurons, and if any are present they dominate the activations. The non-neuron-aligned features only have a large effect when no basis-aligned features are present, and LayerNorm rescales the activations which SoLU suppressed.

To investigate this, we collected dataset examples across a range of neuron activation levels, rather than solely looking at the dataset examples which maximally activate a neuron. We then compared dataset examples at different levels before and after LayerNorm. Our strong impression from looking at a variety of neurons was that for neurons which seemed interpretable, the post-LayerNorm dataset examples had many more examples which were not consistent with the feature the neuron seemed to respond to. This was especially true for dataset examples which only slightly activated the neuron, rather than strongly activating it.

To get at this in a slightly more objective way, one of the authors considered a seemingly interpretable neuron which responds to the words "left" and "right", especially when used as adjectives to specify body parts. He categorized around a thousand pre- and post-LayerNorm dataset examples based on whether they were consistent or inconsistent with the hypothesis. The categorization seemed to show that post-LayerNorm activations were much more likely to have unrelated activations in the low-activation regime. Note that this experiment was done informally and not blinded, so results might be biased, although the effect seemed so striking that we believe it to be real:

![](images/img-013.png)

Figure 9: Fraction of neurons inconsistent with primary hypothesis.

This is exactly the signature we'd expect to see if LayerNorm was being used to "smuggle" non-basis aligned features through SoLU, as speculated in [Section 4.3](#section-4-3).

From this perspective, SoLU is a double-edged sword for interpretability. On the one hand, it makes it much easier to study a subset of MLP layer features which end up nicely aligned with neurons.  On the other hand, we suspect that there are many other non-neuron-aligned features which are essential to the loss and arguably harder to study than in a regular model. Perhaps more concerningly, if one only looked at the SoLU activation, it would be easy for these features to be invisible and create a false sense that one understands all the features.

Despite this, we are inclined to see SoLU as an improvement on the prior situation: we understand many more features than we did before, including in layers like the first MLP layer where we previously had little traction.

  
  
  

  
  

## 7. Related Work

#### 7.1 Understanding Transformer MLPs

Although a significant body of research has explored Transformers generally (Bertology, see review ), it has tended to not focus on MLP layers. However, it's been increasingly clear that MLP layers are at the heart of many questions of interest. A recent paper by Meng et al.  made remarkable use of ablations to localize factual knowledge to MLP layers, and then edit it with gradient descent.

A small body of work has investigated individual neurons in Transformers. One line of work by Geva et al.  has explored MLP neurons as key-value pairs which adjust model predictions. Another paper by Dai et al.  explores the possibility of "knowledge neurons" which encode specific facts.  Alammar  visualizes individual neurons, and uses NMF to find additional structure. Finally, a recent paper by Bolukbasi et al.  cautions against the risk of "interpretability illusions" which create a misleading impression that Transformer MLP neurons are interpretable if one focuses on top dataset examples and evaluates on narrow dataset distributions.

In parallel with this work interpreting neurons, our sense from talking with other researchers has been that some others have found individual MLP neurons challenging to interpret. This has also been our experience prior to SoLU (see this [informal video](https://www.youtube.com/watch?v=8wYNsoycM1U&list=PLoyGOS2WIonajhAVqKUgEMNmeq3nEeM51&index=16)). We mention this because negative results are often not formally represented in the literature. It's unclear to what extent these differences in getting traction on neuron interpretability reflect a difference in the underlying models studied, methodological differences, or differences in the relevant definition of interpretability.

<!-- yt-inline:8wYNsoycM1U -->
[![MLP Neurons - 40L Preliminary Investigation [rough early thoughts]](https://img.youtube.com/vi/8wYNsoycM1U/hqdefault.jpg)](https://www.youtube.com/watch?v=8wYNsoycM1U)

<details>
<summary>자막: MLP Neurons - 40L Preliminary Investigation [rough early thoughts] (55:55)</summary>

[00:00]
So, one of the directions that uh our
research at Enthropic has involved has
been um just trying to understand what
different neuron neurons and different
layers of transformers are doing um
inside the MLP layers. And it's been
something that we've haven't
investigated as much as attention heads
and attention circuits. Um and honestly,
I think we've found to be more difficult
than we were initially hoping. uh but we
have learned some pretty interesting
things and so uh hopefully in this video
we can we can talk about some of them
and maybe they'll be useful to people um
who are investigating similar things
elsewhere.
Uh [clears throat]
so I'm lucky to be joined here um by my
colleagues Katherine Olsen and Nelson
Elhaj and uh we'll be uh just going and
chatting through some of the things that
we found.
Um, so yeah, I thought it would be
helpful maybe to just talk a little bit.
Um, so this is sort of really just a
preliminary investigation. Um, and maybe

[00:01]
just to go over a few basic points. I
jotted down a few things. Um, but you
know, as we talk through these, maybe
uh, Katherine and Nelson, if there's
anything you want to add, just jump in
and and say that. Um, all of these
results are going to be from a kind of
moderate sized model with 40 layers. Um,
we find that there's a lot of
differences between features that exist
at different layers. um uh but probably
the the exact number of layers doesn't
matter and I think our intuition is that
in most cases um if you look at models
with different numbers of layers you'll
find similar neurons kind of roughly in
terms of the fraction of the way
through. So if you're neuron if you're
at sort of 5% depth often that's what we
see sort of generalized.
Um we'll be investigating MLP neurons
not neurons on the residual stream. Um
so I guess in some ways neurons on the
residual stream is kind of an kind of
probably an an oxymoron. um or like um
um probably not the way that we would
use the terminology.
I think when we when we talk about
neurons, we mean something that has an
activation function and since uh the
residual stream is just linear functions

[00:02]
being added into it or linear
projections being added into it, you
sort of can't can't think about it that
way.
um we'll be talking about a number of
different depths in the model. And yeah,
usually our process is that we we start
with data set examples. Um and then we
start going and after that going and
interactively playing with the neuron
and when it activates to sort of verify
our theory.
Chris, what's a data set example?
What's a data set example? That's a
great question. Well, Katherine, how
about you tell us what a data set
example is?
Sure, absolutely. Um so we take the
neuron that we're looking at um and
throw a bunch of different examples at
it. um just tons and tons of different
uh possible contexts that's in the data
set that it was uh the same distribution
that it was trained on and just see what
it fires most on or where its sort of
highest activations are and we look at
the top couple like sort of asking like
what is this neuron most like or where
does it show the highest activity and so
we just look at those pieces of text
where we saw the most activity from it
and I think it's not that we think that

[00:03]
data set examples are dispositive at
what a neuron does but they're um
they're going help us build a hypothesis
um and sort of narrow down the space of
things that it could be doing.
Um do you also I I feel like you
probably are the person who's spent the
most time studying neurons. So if
there's anyone who should really comment
on um what our process has been to try
to understand neurons really I feel like
you should feel like you can you can
elaborate on that.
Yeah. Yeah. I mean one thing I'll just
I'll just say is as Chris said starting
with these uh positive examples is only
the first part of the picture. I feel
like I didn't really get traction until
I could start to look at negative
examples as well. Um, so when I say
positive examples, I mean you can see
that this neuron really likes texts of
this type. Uh, but then you have to ask,
well, does it like everything of this
type? Uh, or are there things like this
that actually are excluded? So you need
both to know what's ruled in and what's
ruled out uh by sort of the rule that we
might use to explain the behavior. And
so there's a couple different ways you

[00:04]
can get this sort of ruling out um
ruling out behaviors as well. So you
could look at, you know, tokens that it
likes uh but contexts where it didn't
fire on that token because of something
else going on in the context. That's
useful. And also playing with
interactive interfaces where I can just
type text uh sort of exploratorily uh
and try and feel out uh can I get it to
not fire where uh it might otherwise
fire on that token. So getting that sort
of other side of the hypothesis space,
but all very exploratory. It hasn't been
that um rigorous yet so much as trying
to feel out the space. And I think one
thing that's that's just worth being
kind of super explicit about is is we
tend to talk about like what a neuron
likes or what a neuron is looking for.
We're we're looking at a point in the
model where an activation function
nonlinearity is applied. Typically a
relu or you know some variant of it. uh
this model uses GLU and so sort of when
we say a neuron likes or a neuron fires
we typically mean that it has a positive

[00:05]
activation at you know that scalar value
has a positive activation which if we're
using relu means that that value is
going to be passed through unchanged if
it sort of doesn't like it or or doesn't
fire it's somewhere in the negative
regime
um kind of we we tend to use this sort
of anthropomorphizing terminology and I
think it's sort of intuitive sometimes
when you're looking at these neurons but
it's just worth being super explicit
we're just talking about like the value
of that scaler at that point.
And I'll also say this in this
exploratory phase, we've largely been
looking at very sparse neurons that is
that fire infrequently throughout the
whole body of text that they've seen
because that's an easier place to get
started. Again, that's going to be a
strong bias in what we're reporting
here, but that was a choice we made to
get a foothold. So there's uh only a
small number of different tokens that
they fire on at all, whether that's uh
you know how often in the data set or uh
different uh token identities. And that
allows us to get a sort of tighter uh
tighter sense of what it's doing as

[00:06]
opposed to a neuron that fires diffusely
throughout an entire text which is more
challenging.
Yeah. And I guess a a related thing is
because these neurons are sparse and
both it's the case that the typical
neuron in the model is quite sparse and
also that we've often preferentially
looked at sparse neurons. Um but when a
when a neuron's very sparse um trying to
understand like you could sort of think
of the case where it doesn't fire as the
default. And so like you might ask you
know why is it that you're looking at
you're looking at the examples where it
fired rather than the cases where it
didn't fire. Well, you can sort of think
of of it not firing as default and it
firing as the exception that you're
trying to understand. Um, whereas if you
had a neuron that was sort of equally
often say to had activations of zero and
one, you might not be able to do that as
easily.
One final point that's maybe worth
making is just that um I at least for me
I've previously uh sort of done this
this circuits type work in vision where
we're exploiting the fact that you know
vision models have have a number of
neurons where it's at least

[00:07]
theoretically plausible that you could
look at every single one and transformer
large transformer language models this
isn't necessarily true and so uh we're
showing you some neurons but um it sort
of seems seems almost impossible that we
would look at every single neuron Um,
and some kind of strategy if we want to
scale this is going to going to require
us to do do something else beyond that.
Okay. So, with that said, I think we can
dive in. And I think that it's sort of
interesting that there's some layers
where we've had a lot more luck
understanding neurons than others. And
broadly, I think our biggest cluster of
successes and our earliest successes
were these relatively early layers um
sort of roughly especially in the like
10 to 25% depth regime. Um we had a lot
of luck but the the earliest layers we
found quite challenging and then we
found that features became harder and
harder as you got deeper past that and
then towards the end and especially in
the last layer we also had a lot of

[00:08]
luck. Um, and so those seem to have been
the places where we where we've had the
most luck understanding neurons in these
models or the most success.
Um, cool. So I think we can just dive
in. Um, and uh, layer five, so in this
in this model that's about 12% depth.
Um, I think we found a lot of pretty
interesting features. Uh, Katherine, do
you want to comment on any of these?
Yeah, I mean I think this is sort of
just a a quick signature of this sort of
uh, positive description. and what does
it fire for? And that these sort of
layer fiveish neurons again that's sort
of in the 10% through the model kind of
regime. Um there's sort of like little
semantic uh semantically similar
phrases. So the like I would like, it
would be nice, I will like neuron in the
top left there. Um it's there are other
cases where the word like shows up and
it doesn't fire. So if you just say I
like pizza, that doesn't work. You say I
would like pizza then that works. Um,
and there are some ways to sort of um

[00:09]
fool it or trip it up and sort of uh
write something that contains like, you
know, I'll I'll come up with a specific
example later, but kind of mash up the
words and then it does fire even though
it doesn't mean semantically the same
thing. So, they're not like ultra ultra
precise at picking out things with a
meaning like I would like. Um, but they
do rule out other like I like or I love.
uh that doesn't have this same sort of
future tense preference kind of
expressing thing.
One thing I found pretty interesting on
these is some of them respond across
multiple languages to short phrases that
mean the same thing.
Um so for instance there's this like um
this one here that at the at the bottom
left um that we have not only but we
have also in French non
um or um there's there's another one
that responds to to four reasons but
also
um yeah so I thought that was kind of an

[00:10]
interesting interesting pattern.
Um, I've I've wondered if it might be
helpful to conceptualize these as being
like um I think linguists have this idea
of a I don't even know how you pronounce
it, but a fragmi or a phrase of like
words that just frequently co-occur in
just statistically in English way more
often than they should.
Say it again.
Frzy like a
phrase. A phrase.
Excellent.
Yeah. And so I I have wondered if if
these might be kind of like that. Um,
but the fact that it's across languages
and it's grouping similar things
together seems like maybe maybe thinking
as like very small semantic units is a
is a better framing.
Um, and yeah, this is just looking at
one of them, but uh this is the the n
different or n separate or n
independent. And you can see that you
know it's firing on the word independent
or different or distinct, but in every
case there's a number immediately before

[00:11]
it.
Okay, Katherine, you should definitely
discuss this because I think this was
this is one of the things that I was
totally stumped by and Katherine figured
out.
Yeah, I'm happy to take it away. So,
I'll describe this briefly and then I'll
probably share my screen and show sort
of a bit of the sort of uh discovery
process. But, um at a high level, this
neuron uh showed up in the data set
examples preferring world the word
install very strongly. Um, if you look
at other tokens that it fires on, it
might more weakly fire on other words
that seem somewhat computer related. You
know, package was the other one that
showed up fairly often. Um, but if you
look at these data set examples, they're
not very uh computer related. And so in
when playing interactively with it, I
can get it to fire if it's for a
computer related word specifically
install or more weekly maybe package,
but the context doesn't suggest that.
Um, so maybe I can just steal um
presenting for a sec and show show some
of that.

[00:12]
Cool.
Sounds great. Well, Catherine's
switching. Um, I was really quite
confused by this neuron. Um, because it
it seemed to be firing for all these
words, but very mysterious. It would
only fire some of the time and you try
writing sentences with the word install
on them and, you know, it wouldn't fire.
And so, uh, yeah, I was I was pretty
confused by that.
Yeah. So, let me pull up. So this is a
little um dashboard that we have for
checking out what neurons are doing. So
I'm going to go to the data set examples
page which is where we generally start
when trying to understand what a neuron
is doing. And so you see if you scroll
through it's the word install. I'll just
scroll through very quickly first and
then we can um pause for a moment. So
these are all the word install.
Everything is install.
Go ahead. One quick addition on that is
it's the token install which isn't
always necessarily a standalone word. So
uh because these models split things
into tokens and that doesn't always line
up and in some cases here we have
install as part of installments uh but
it can't see since it's it's auto

[00:13]
reggressive it can only see the past and
so it doesn't know that it's going to be
um installments it just knows that it's
yeah can it could be installer could be
installments
right so in this case as I was
describing um this is paying a fee in
installments it's not installing
software um if I scroll up I think there
was another Um,
oh yeah. Um, the weekly French fried
dizer fries evident in the earliest
installments, recent installments in
this series. So, this is some kind of uh
uh cartoon series that comes out in
installments. Um, so you can look at
this and then we have a way to pull this
up in an interactive neuron explorer. Um
so and I think I didn't show you but
another view that we can that that has
been useful to me is just other than
install what are the other tokens. So
that's how I discovered that package is
another thing it sometimes uh fires on.
So here we have an interactive um editor
where I can try different um texts to

[00:14]
try it out on and I can plug in the
neuron over here on the side that I'm
looking at. Um, and so we can just try
something out like this idea of like,
um, please open the Debian package
installer or like please use the Yeah,
so that didn't work at all. Um, use the
command line.
Um, it there's no activation at all. So,
let me just show you. I have this
activation view. You can look at the
different um, tokens and uh, if there
was an activation, it would be more
brightly colored. If I just make that
just the word install weekly. So, we get
an activation of one, which is
something. It's something. Um, but if I
go to one of these sort of non-computer
related uh contexts and say the
construction people arrive at the work
site ready to install
I finish the sentence and it loves that.
So that's an activation of almost 13.
Uh, so order of magnitude higher on the
on the spectrum. And then these words
like package that are not its preferred
word. It's a little harder to evoke an

[00:15]
activation. I definitely won't get it if
I say something like uh you know uh
download the file for the
package that's I'm guessing going to be
nothing at all. Yep. That's negative. So
it doesn't clear the positivity
threshold. But if I tell some story
about like uh Debbiey's guest brought
numerous presents to her birthday party.
She gazed upon a golden wrap package. I
bet I'm going to get a little activation
there. Yeah. And so I get a little bit
of response to this uh similar word, but
also with this sort of outside the
computer context. So,
and just a quick note about the the sort
of the magnitudes that that Katherine is
is highlighting here. Sort of like, you
know, why why you know this is 1.2, we
color that is very pale. What's going on
there? Uh in general, it's sort of very
hard to know what the magnitudes of
these activations mean in any absolute

[00:16]
terms because they'll only ever be
interpreted by being multiplied through
some weights. And so kind of are they
big? Well, like that depends what
weights they're multiplying by. So we
scale these neurons by the largest
activation we've ever seen that neuron
fire on in the data set. Sort of under
the assumption that we don't know what
these scales really mean, but any
individual neuron probably has some
scale. And so if we scale it against its
biggest ever activation, that at least
gives us kind of some sense of of, you
know, what's what's big for that neuron
versus for other neurons may be
different.
Yeah. I also want to point out, I didn't
know this was going to happen, but I got
a tiny activation for the word wrapped,
which I actually haven't seen before.
So, uh, on the fly learning learning new
things about neurons.
Anyway,
Katherine, um, just before you do that,
do you uh I wonder if you want to say
anything about uh the Sorry, I'm also
trying to figure out at the same time

[00:17]
how to how to take back um the
presentation mode, but um I I feel like
this has sort of been a recurring theme
and motif of these neurons that sort of
appear like they're they're sort of like
X, but context says that it's not X or
something like this. Um, and so maybe if
you just want to I'll talk about that
motif for a second. Um,
yeah, happy to. I mean, maybe I should
jump to one of the one of the later
neurons that has this as well or do you
want to sort of talk through the later
neurons and then I'll pick up the
Yeah. Yeah. I think just uh just like
you briefly flagging this now so that
when we come to other examples um we can
sort of refer back to it.
Yeah. So this is just a motif we've seen
that will come up in later in this
presentation um is neurons that are sort
of saying well you might expect this
word but actually it isn't or you might
expect that this is a computer meaning
but the rest of the context suggests
that it's not. So there's kind of a you
might expect but actually type of uh
interpretation of the activation pattern
we're seeing. Uh and it's been quite

[00:18]
common. has cropped up a number of
different times where uh the neuron
doesn't seem to be best explained as
expressing just this thing is present
but it's better explained as expressing
you might expect this thing to be true
or to happen next from everything else
you've seen but actually something else
is going on that kind of motif that I
think of as a somewhat either inhibitory
or sort of um pushpull kind of motif is
pretty common
cool
um so moving a little deeper into the
model to layer 10. So that's about 25%
depth. Um I think another interesting
type of neuron that we started to
observe more of were neurons related to
copying. And if you've watched our other
videos on um the our studying of
attention heads, we know that attention
heads are often um really concerned with
whether text is copied and and uh
looking for previous places it might be
copied from and trying to predict what
might come next. And we have have
induction heads and stuff like this. Um
but there seem to be a lot of neurons

[00:19]
involved in this as well when you when
you switch to full um full transformer
models and um sort of looking for
different kinds of copying. So you can
have uh we have one neuron that seems to
be sort of immediately repeated text. So
here we have well well well
um so well is repeated three times or
here we have and this one's a little bit
trickier but um there's a reviewer uh
reviewers as reviewers and the second
reviewers is a sort of short-term copy
as well and so it's firing there. Um but
then we have also these longer term ones
where if you look at this first
paragraph um it's copied in the second
paragraph here. Uh, and I think that
this happens sometimes. Um, for
instance, like if an email thread is in
the training set, uh, or a forum thread
and people are quoting, you know,
earlier people on the forum, um, or if
you have a news article that does like,
um, a an excerted quote to emphasize it
that's also in the main text. Um, these
are all situations where you can have

[00:20]
have, you know, paragraphs or large
chunks of text repeated. Um, and so
having neurons related to that maybe
makes sense.
Um, and that another famous neuron that
we found in this in this layer was um
another one of these neurons that
Katherine figured out uh that really had
me stumped. And this was a particularly
interesting neuron because as I recall
um it was we were looking at the the
most the neurons that had the that were
both extremely sparse and had extremely
high magnitude activations. And this was
the the neuron in that layer that scored
highest on that metric. So that was why
we were looking at it. And when I
started looking at it, I was really
stumped. Um it it sort of feels obvious
in retrospect, but yeah, Katherine, you
should just tell us the story of this.
Yeah, happy to. Um so this was another
one where the um interactive
uh interface was was very helpful
because it seeen I was seeing it showing
up in um sort of index kind of uh mode.
So let me just grab if you don't mind

[00:21]
grab presenting again.
Um, here I have the um data set examples
pulled up. Um, wait for that to start.
Um,
cool. I think we're are we good? Yeah.
So, um, I was seeing it show up in these
sort of like appendix, you know, index
at the end of a of a text kind of thing
or it's like a table of contents. Um, so
you might think it's just tables of
contents. Here's like a, you know,
self-positioning 204. So, uh, is it just
somehow lists of stuff? Um, but then if
you start playing with these, um, and
you just start making lists of stuff, it
doesn't always react. So, let's see.
This got this is 10
11586.
So, um, you know, if I do this is a
random list of of madeup surnames like
um, Darby, Dodson, Edwards, Franklin.
I'm kind of making this up. Yeah, it's
starting to fire here. But if I did

[00:22]
Darby, Franklin, I don't know, random
um names, it's starting to fire a little
here because I've started to go
alphabetically. So that was the sort of
genesis of this hypothesis that it's
it's alphabetized lists. Um if we go
back to these data set examples, all of
these are are alphabetized lists. And
the more you know, it starts to um it's
a little fuzzy. It's not like, you know,
it doesn't have access to the
characters, right? So, it has some sense
of uh alphabetical ordering. It's not
perfect. So, you can again fool it or
get it to mess up with respect to the
story we're telling about it um by
making lists that aren't actually quite
alphabetical, but it kind of thinks they
are. And you can see it's sort of trying
to figure out like, okay, is the is the
word summer school the next entry in the
list? Maybe. Maybe this is a list that
goes particle summer symmetry. No, no,
no. And then it gets back on the on the
train. It's like, oh, no, this goes
particle. And then there's a couple

[00:23]
other lines and then particles. And so
you can sort of watch it figure out or
try to come up with an interpretation of
like, is this a list? And if so, is this
the alphabetized next entry? and have
this kind of um smooth prediction of
whether it should be considering this
the next item in the alphabetized list.
I feel like this was a place where um
the having the interactive interface for
exploring this was just uh really really
crucial and uh seemed to to really be
the difference between us uh getting
this. I think especially like
approaching it in a sort of adversarial
way and trying to trying to really see
um if it if it holds up when you go and
you uh play with it or or not. Um seemed
like it was important.
Yeah. So I mean here's an example where
it's like starting to get on but it
doesn't seem to think that dates comes
before donuts. So um I think another
thing that I have been grappling with
especially with this neuron is that the
kind of work that we're doing is coming

[00:24]
up with stories, explanations,
hypotheses for how we might in a
compressed way describe the selectivity
of the neuron. The fact of the matter is
that like the only ground truth model of
what the neuron is selective for is the
neuron itself. So, you know, if the
neuron doesn't fire on dates, that's the
real truth of the matter of what this
neuron is actually doing. And the fact
that I think that's a mistake because I
think dates comes before donuts uh and
after coconut. Um that's, you know,
whether you can say that the neuron is
messing up relative to this simple rule
that otherwise explains its behavior or
whether you can say like the rule is
just inaccurate. actually it's doing
something more complex and more
sophisticated is actually kind of a um
philosophically challenging uh question
as to which of these views is more
useful I guess for what we're trying to
do.
One other thing that I feel like was
pretty helpful with this neuron was
initially we weren't formatting the
white space in the text correctly. Uh

[00:25]
and uh and I think we also had we
weren't collecting our data set examples
over that many that many examples or
that many that larger fraction of the
data set. Um and improving that I think
made it easier just to go and see
patterns and data set examples. And so I
think investing in infrastructure has
really has really helped with this kind
of thing. Yeah, this um this view uh
previously would have just been the the
white space was not correct and so it
would have just been a whole pile of
words which was much more challenging.
I'm going to steal back presentation.
Go for it.
I guess and maybe just one other
actually one other quick context while
quick comment while Chris is stealing is
sort of Katherine's mention of of sort
of sometimes you come up with these
rules that are like nearly right but
imperfectly predictive. Um that reminds
me a lot of my experience taking my
first ever linguistics class um where
there's like a lot of sort of pop
knowledge about like thing about rules
in English language or or places where

[00:26]
there are seeming regularities or
irregularities
and in a lot of cases the like pop rule
is like decent or the pop pop culture
rule is like ah it's just arbitrary but
then linguists have like gone much
deeper and they're like actually this
rule that you thought was about the
spelling of the word is about the
phonetics of the word. And if you like
look at the phonetics, everything is
totally irregular. It's just that the
spelling has been corrupted because
English spelling has such a weird and
arbitrary history. Um, and that can be a
kind of similar story of like if I have
a rule and it's almost right, it's often
worth it's it's there's a there's a
natural temptation to be like, ah, the
model is trying to do X badly. Um, and
it's worth thinking hard of like
actually it's trying to do X prime and
it's doing it quite well. Um, that's
right. Both both,
right? Both both stories can be true in
different cases, but it's almost always
worth like I don't know. I find it's
there's there's some instinct of like,
oh, it's just a model. It's like trying
to do something, but it's bad at it. But
these models are very capable and it's

[00:27]
often worth like trying harder to find
the real rule. Um, and then I think the
other intersection is that uh I remember
Chris mentioning like going off down a
total linguistics Wikipedia rabbit hole
and then coming back with half a dozen
new hypotheses for various neurons or
attention heads. And it's been
interesting to note that like in some
cases the sort of inards of these models
are like modeling language in some ways
like better than sort of I consciously
understood language. I clearly
unconsciously understand the language
like quite well. But there's a whole set
of rules that Yeah. Right. But there's
like a whole set of rules that the
linguists have figured out that like I
didn't learn or forgot in my one
linguist linguistics 101 class. Um and
that's actually been a like surprise in
some cases a surprisingly rich source of
like hypothesis generation.
I I think that related thing is just you
I think people I think it's sometimes
underappreciated how much of the the

[00:28]
challenge of understanding these models
can be that we just don't have the right
hypothesis. Um because I think I I I
often see work where people sort of like
um you know they they go and search for
some features that they think are going
to exist in the model and see if they
can find neurons or directions or
something that are predictive of them.
Um, but I think often uh like I would
never have guessed the install neuron
thing where it's like install but not in
the context that you sort of might have
thought by default. And uh I think I
think that's actually a pretty common
recurring theme that these uh that these
models are hard. Yeah. That that that
that a lot of the things that are going
on these models are not what your
original hypothesis are. I want to just
riff on what Nelson was saying about the
discovery process where it's tempting to
say, "Oh, this neuron is kind of doing
short phrases of this type. Got it. Got
it. Okay." And move on. Um, but in my
experience with the install neuron and
the alphabetical list neuron with the
first two where I really felt this, um,
there's a kind of click. There's a kind
of aha where you stumble on the exact
right hypothesis and suddenly everything

[00:29]
is very clear and all the weird quirks
of like, but why aren't these very
computery? um just instantly snap into
clarity. Um I have some experience a
couple years ago you know for a phase in
my life I was a MIT mystery hunt uh
competitor in you know you get together
with a team big team of dozens of people
and you're trying to understand the
meaning of a random pile of letters uh
and at some point you have the aha and
you have the hypothesis of what the
puzzle constructor uh meant you to to
see and everything makes sense and that
click or that aha um has been really
important for for knowing that we
actually we actually got this one. We're
not just kind of squinting at it and
being like, "Oh, it's kind of animals.
Okay, done." Like that's usually not uh
not quite good enough.
Um okay. So we could also jump to the
end and I think the last layer is
somewhere we've had a lot of success as

[00:30]
well. And the reason for that I think is
uh the last layer has the MLP neurons on
the last layer have a unique property
that they linearly affect the logits and
that is the only thing they can do
because they they just get added they
they go through a their down projection
that gets added into the residual stream
and that immediately hits the
unembedding. Um, I guess there's guess
there's a layer norm there. So maybe
it's very very slightly nonlinear, but
it's it's effectively just a linear
effect on the on the logits and and they
can't go and affect other neurons. They
can't be going and affecting things
through attention tense. They can just
linearly affect it. And so um you might
have in some cases have trouble
understanding when the neuron fires, but
you can absolutely understand um what
the neuron does when it fires.
Katherine, I think you analogize these
sometimes to to motor neurons.
Yeah. Yeah. Um I I in a in a half of a
PhD that I then quit, I did a bunch of
neuroscience. And so the um uh sensory
neurons, motor neurons analogy tends to

[00:31]
make a lot of sense for me where um
computational neuroscience has had the
most success more on the sensory side or
more on the motor side of analyzing sort
of the behaviors and selectivities of
neurons or clusters of neurons. Um I
think this is a similar case because we
know what the output is. Then we can
sort of directly track the contribution
of these neurons behaviors to the output
which gives us a grounding that you know
in these 40 layer models when I was
trying to understand layer 20 I just had
no footholds at all. I had no way of
telling um what the right uh frame of
reference was. But for last layer
neurons, the correct frame of reference
has to be very close to what next token
is emitted or predicted uh by the model
of what uh slate of anticipations does
it generate. That has to be just
structurally uh close to the right way
to think about them.
And this is sort of strictly true for

[00:32]
the last layer, but sort of a softer
version of this might be true for the
last couple of layers. Um, so I think we
had
Yeah, I can show a couple in the I
mentioned earlier that with this sort of
inhibitory motif some of the um some of
the ones near the last layer I think
also are interesting if there's a good
point for me to show a couple of those
too.
Awesome. And and I think I think we've
actually found sort of in you know for
layers for neurons in the middle of the
model our usual assumption is that sort
of whatever right every you know because
of the the kind of residual nature of
transformers every neuron is added
directly into this residual stream and
then that value can either interact with
later neurons or retention heads but
also that value is kind of there
forever. someone might subtract it out
but you know then the sort of that and
so so every neuron you can look at what
its direct effect on the logits is and I
think we've found that often even if
that direct effect is a small story a
small part of the story it's sort of in
some way related to what it's doing sort
of something about the training process

[00:33]
or the sort of way these models build is
that it will affect tokens that are kind
of in some way related to what it's
doing so even for middle layer neurons
where that's not at all that was
potentially not even mechanically a
large part of the story. There's still
sometimes information or hints there
about ah this neuron makes those tokens
more likely that you know that helps me
generate hypotheses.
Yeah, that's a great point. And yeah, in
general, it's just a very nice thing to
be able to go and quickly look at um and
and have available because it's um and
uh you know, people who are watching our
other videos know that we've been doing
this a lot for attention heads as well.
you can really anytime something writes
directly to the residual stream, you can
you can be asking um you know what the
long-term effects of it are. Um and this
this relates to um I guess there was a
user nostalgist who wrote a uh a post on
on the logit lens interpretation of of
transformers. This is a little bit in
that in that vein.
Um but yeah, so here we have one neuron

[00:34]
and uh if you look at when it increases
uh tokens, it increases uh they're
always all the tokens that it increases
start with a vowel and it decreases the
probability of tokens that don't start
with a vowel. Um and often it fires on
an an. And so an and an is going to
indicate that the the next word must be
uh must start with a vowel because
otherwise you'd use an a. Um there might
be other cases where it also fires, but
that all the really high magnitude
examples that I could find when I was
preparing this slide were like that. I
think this is just another great example
where if you hadn't seen the data set
examples on the left side and you're
just looking at this pile of like
increase decrease tokens, you'd be like
amalgam embroidery. Is this about
ostrich? this about like feathers or
decorations or what is you know range
combination pair like there's there's
also some additional like semantic
thing that might be part of the story um

[00:35]
but you could also miss this sort of
high order bit is uh the vowels versus
versus consonants like if I look at
these lists I do get a sense that
there's something about rich textured
nouns versus um uh mathematical nouns
but that's not the high shorter bit of
of what's going on. And as soon as you
see those uh activations on and you
understand that the primary thing to
understand here is the is the vow
consonant.
Yeah. Yeah, I think it I think it sort
of it also lends sort of sh sh sh sh sh
sh sh sh sh sh sh sh sh sh sh sh sh sh
sh sh shedsed light on sort of on when
you're trying to understand or interpret
these neurons. It's it's important to
have a sense of where they are in the
model and sort of how what that relates
to your space of hypothesis because you
know if you just look at these data set
examples it'd be very easy to guess you
know ah this just fires anytime it sees
the word and but that hypothesis makes
no sense because that the model could do
that a the model could do that way

[00:36]
earlier on and in general we tend to
assume that these models are like well
optimized and reasonably efficient and
they're sort of they're not going to be
spending too much of their capacity
doing things that are sort of obviously
useless or that they could have done
earlier. Um, and so there's like it
doesn't make sense for it to be doing
something so trivial this late in the
model. But also there's no computation
after this neuron. So like it, you know,
ah this is the word an like that that
fact doesn't really like that that that
fact is it's too late to know that fact.
Um, and so it is the case that this
neuron very often fires on that token
and very often fires on others, but sort
of the the logic effects tell you this
the kind of the much better story and
give you a much better story that fits
into where the where like where the
neuron is in the model and sort of space
of things that like are sort of
informative to talk about about this
neuron.
I think this also relates to why it's
useful to invest in understanding the

[00:37]
architecture of these models. Um, I
think uh, yeah, I was having a
conversation with with somebody else the
other day and I yeah, I think I think
it's really valuable to invest before
you go and spend a lot of time poking
around at these models to invest in
understanding what kinds of features
exist at different layers and or what
the what the architecture of the model
is and and how things are wired up such
that you know you like the observation
that the only thing that an MLP layer
can do is is go and affect the logits is
is something that you can get when
you've when you've invested in that. So
Chris, can I grab uh presenting for a
moment because I just uh you know
discussing um
Yeah, go.
Let me just grab and then I'll and then
I'll
although I think we we I think we're
almost at the end. So we just go through
this and then either way you have your
presentation
very quick just as Nelson was saying
like this this neuron is too late for it
to be firing on an if it's actually just
predicting when there's going to be a
consonant. I can make this whole string
with just, you know, context metalarning
where the word or is always followed by
something that starts with the vowel and

[00:38]
sure enough it picks it up and now it
knows that it should be upweing the the
vowel neurons. So I just threw this
together right now just just there.
That's phenomenal. I
there you go.
Back to you.
Thank you. Well, uh okay, I have to I
really need to learn this trick of how
to resume presentation. Uh,
how do I There we go. Resume presenting.
Um, okay. So, oh yeah, so there's we're
we're in fact not quite at the end. Um,
so what about neurons in in other layers
that we found harder to understand? Um
so one layer in particular that we found
kind of tricky to understand um and
perhaps that you'd sort of think would
be the easiest layer to understand of
all of them has been the first MLPS uh
MLP layer and part of the reason for
that well I guess you sort of there's
two things that are very striking about
this layer. One is that the attention
heads immediately before it, which are

[00:39]
the only thing the neurons can be
computed based on um along with the
residual stream are extremely diffuse.
Rather in large models, that's true in
small models. As models get larger,
those attention heads just start being
smeared out over basically all previous
tokens and the neurons become
exceptionally sparse. Um and yeah, and
so in theory, you could you could
actually like these neurons have a very
nice form where you could just sort of
uh mechanistically understand them. you
could expand them back and you could be
like, well, you know, this is what it's
looking for through this attention head
and this is what it's looking for
through this attention head. But because
the attention ends are these sort of
extremely blurred things that's been a
little a little tricky to reason about.
Um, and a lot of your a lot of the
obvious hypotheses you might have for
this layer don't seem to be true. So, I
think the thing that I I first imagined
the first layer would be doing when I
when I started looking at it is piecing
together um subword tokens into whole
words. So when a word gets split into
two tokens, it would be very natural to
have neurons that try to go and fix that
and turn them into uh into coherent

[00:40]
words. And and that doesn't seem to be
what the first layer is doing. Um or at
least not a large fraction of it.
And uh something that really uh helped
me think about this is there's um this
paper from Google pair by conidol um in
2019 and they they have this really nice
diagram um where they take the
activations and these are I guess
residual stream activations um for a
single token like um die and then they
go and they just do um a TC or a UMAP
and they find that there's one cluster
that corresponds responds to the German
article uh D and another one that
relates to people dying and another one
that relates to dice um because those
are all different interpretations of the
token D or die
and it made me wonder if maybe something
similar might be going on because you
know a very sort of an attention that's
blurred out and looking at all previous
tokens might be actually pretty well

[00:41]
positioned to help you guess what
language you're looking at and so maybe
you could go and correct your
interpretation of tokens.
And it seems like that might be what's
going on. So if you um either do like a
PCA of the NLP, the first MLP layers
activations for a single token um or you
do a UAP um you'll notice that uh you
get clusters corresponding to languages
and sometimes even to like particular
types of of speech within that language.
What do you mean emotional, Chris? I'm
not sure I I recall this.
Yeah. Yeah. It's like um
just there's there's some some sentences
about death or some samples about death
that are like from a novel where
somebody's like speaking very
emotionally about
deathing. Yeah.
Lamenting or or or it's just like kind
of I don't know kind of intense language
in some way um and very personal. And
there's some that's like much more
depersonalized.
Yeah. statistical or clinical or um and

[00:42]
yeah the that seems to be the sort of
primary dimension of that cluster over
there.
Um, so based on that, you can then start
looking at neurons in MLP0.
And uh, here's one for instance that
seems like it might be related to it
only fires in contexts that are Spanish,
but the tokens, it doesn't fire on every
token that's Spanish. Um, and in
particular, it seems like it maybe to
fires on tokens that could be English
tokens. Um, or maybe could be tokens in
other languages. And this is a little
bit cherrypicked because I wanted to
find a couple interesting examples. And
there's there's some places where it
fires on tokens where it's it's less
clear this could be the case. But for
instance um the token fund um while fund
is an English word as well um like fund
is in funds you could also have fund as
in fundamental.
Um in is a standalone English word and
also is used in uh lots of other
contexts. Europe is an English word.
Indef could be part of indefinite. Um
import is an English word. sin is an

[00:43]
English word. Um, and a lot of these
other things you could imagine that
maybe there's some English word that can
be tokenized such that it's it's some
portion of them. Um,
and so there seem to be a lot of neurons
at least a fair number of neurons in
MLP0 that seem seem like they could be
interpreted in this way where they they
are words that are disproportionately
yeah seem like they could be in one
language but context makes them seem
like another. And so that's one
hypothesis. And this is that sort of
inhibitory pattern of like you might
think English,
but actually it's Spanish. So don't be
fooled. The context says something
different than the token itself.
And there seem to be a lot of these for
different languages um and different
pairs of languages um in in MLP0. Again,
I think this is still sort of relatively
Yeah. not not as pinned down as some
other things that we studied. Um but it
seems like that might be might be what's
going on.
Yeah. Yeah. And just one thing I'm I'm
noticing for the first time staring at
this example is like on your last line
there, the word embargo is also a

[00:44]
straightup English word and it doesn't
fire on that. So it's sort of quite
clear that we don't fully understand it.
But it's something it is it is it's sort
of it clearly has that flavor, but
there's there's there's work to be done
to try to and I think again this you
know this gets to the like is the model
doing X badly or is it doing X prime
which we don't yet understand? Well, I
think our guess is that if we find the
right explanation, it it will, as
Katherine said, kind of click into place
and but we're still figuring it out and
kind of it will, I think, likely be the
case that we sort of don't solve this
one, but that we'll have some later
revelation about some other neuron and
then we go back and look at this one and
we're like, ah, yes, it was clear all
along. But
yeah, this is really in that phase of
like it seems to be doing something like
the following question mark as opposed
to like we got it. And I think that is
partly because we have some of the
positive story. We don't have some of
the negative story. So we don't know
when is it something that is an English
token or word, but it nonetheless didn't
fire. Uh what's the story with that? And

[00:45]
I think I have nothing to offer for this
guy in that in that regime.
One thing that I might be tempted to
suggest is it could be about just the
relative probability of these tokens in
English and Spanish. And so embargo
might uh might be more common. I don't
know. I don't I don't see
more. So that would be an interesting
thing to overlay. It is more common in
Spanish.
Um I thought one final thing maybe to
just talk about is what have been the
challenges to this kind of
investigation. So I think uh having good
tools I think has been really important.
I think that's probably a fairly uh yeah
a fairly straightforward one. Um I think
people Yeah, I think this challenge of
not having the right hypothesis to
distinguish between like um I think we
we often think about hypothesisdriven
science where you're like trying you
have two theories that could be true and
you're like trying to distinguish
between them. But I think we just have
this like enormous space of hypotheses
that we can't enumerate and we don't
know what the right ones might be and
that's much more often the regime that
we're operating in. And I think I think
that's tricky. And then there's this

[00:46]
this EOT token issue and Nelson I wonder
if you want to just briefly comment on
that.
Yeah. Um,
this might be worth a whole video of its
own at some point's, but maybe the
two-minute version.
Yeah. It's sort of it's hard to know.
There's a whole thread here, and it's
sort of hard to know how much is a is a
quirk of some details of of our
architecture, but we we when we train
models, we always give them this leading
token that that we confusingly call EOT
for end of text, even though it's always
the first token in the text. Um but we
always give it this first token which we
sort of find is is useful for attention
heads to attend to among other reasons.
Um the EOT token if you look at its
activations in the residual stream is
kind of very unique. Nothing looks
nothing it doesn't look like anything
else. It has this very large magnitudes.
We sort of expect it to be weird because
it it is a very weird token. Um but we
also find that uh because of a artifact
of how our attention mechanism works,

[00:47]
the model tends to replicate this EOT
token so that other random tokens gain
very similar activations to EOT at sort
of some not exact but some periodicity
through the model and there's not I
think I don't think an enormous amount
of capacity but some number of neurons
and attention heads that are seem to
like mostly be dedicated to constructing
and then tearing down when it's time to
make a prediction these fake EOT tokens.
Um, and I think kind of one of the
salient things is that these so-called
fake EOT tokens, these these what we
call fake EOT tokens have very large
absolute magnitude of values in the
residual stream and activations in some
point. And as we mentioned earlier, one
huristic we sometimes use to search for
things is is looking for things that
that are sparse and have high magnitude.
And so those tokens just sometimes cause

[00:48]
false positives. And they tend to be
very uninterpretable because they're
kind of we we we believe them to be this
artifact of the model architecture where
it's trying to preserve information that
it otherwise wouldn't have access to.
And so you get these very large
activations that have functionally
nothing to do with the text that they're
attached to. And we spent a while on
some red herrings until we understood
this phenomenon because we were like
these things are so much larger than any
other activation. Like there has to be
something really important going on
here. Um if you look at certain
statistics of the sort of whole model,
these guys dominate. These guys are the
whole story. Um, but then you look at
them and they're attached to we we
understand a little bit now about where
they're attached to, but they're
attached to functionally random
positions and like resist any any easy
attempt to understand what's going on
there, which I think also speaks to
Chris's point of of if you don't have
the right hypotheses things andor if

[00:49]
you're like have the wrong hypothesis
and you're intentionally or not too
attached to it, it's sort of possible to
just be completely baffled.
I will say I mean I thought it was
useful um you said sort of random tokens
or you know arbitrary tokens but one
discovery that uh seemed to sort of help
move towards that story or help fit into
that story is one common place we often
use the first paragraph of Harry Potter
uh as our demo text and there's the word
didn't and hadn't show up uh at two
places in this text and they're
tokenized I think uh dn
as one token or h JD N as one token and
then apostrophe T is like a whole token
which the model can very very accurately
predict. If you see DID N the chance
that the next thing is apostrophe T is
like through the roof. And so that's a
token apostrophe T is a token that the
model would use as one of these fake EOS
because it sort of has capacity as our
story to put this other random stuff

[00:50]
there without throwing itself off
because its prediction task is so easy
um that it knows what's coming next. I
guess I I stated that kind of it was it
was it's the token before the apostrophe
t. Uh yeah, thank you. Everyone's sort
of looking [laughter]
a little gloomy as I'm speaking because
I'm saying the wrong thing. The diddn
right before the apostrophe t um is
where it piles this furious EOT
information because our story is because
uh it can't throw itself off that badly
because its task at that point is so
easy.
Yeah. And this this turned out to be a
general story. There's kind of a couple
of other patterns and the story seems to
be that it's always in a place where the
prediction where usually due to some
quirk of tokenization the prediction
task is like braindead easy. Sort of the
model can tell very early on that
there's really only one thing that it
could ever possibly be and then it's
like great I I don't need to perform any
computation here. I already know the
answer and so I can reuse this capacity
for this scratch space to work around a

[00:51]
quirk of a quirk of my architecture. Um,
and I think that um, that's kind of one
of the I think that might be the reason
why this might be worth a whole video is
I think the specific phenomenon is is
potentially just a sort of architecture
quirk. But I think it's it's a it's an
interesting view into the like kinds of
behaviors that these architectures are
capable of evolving um, and sort of how
they allocate capacity to different
tasks in different positions.
Well, I want to push back a little bit
on this being I think this is an
arbitrary quirk, but I think it's an
arbitrary quirk that probably a lot of
people at different labs have in their
models right now. Um, and so I think in
particular if you have a model that is
using block sparse, um, and you are
seeing really weird activations. Um,
this is a pretty live hypothesis that
you should have. And I I guess that if
you're yeah if you're if you're trying
to study large models, there's like a
50% chance you're using block sparks or
I think we've also seen evidence of it
in in dense in in models where that are
have partially dense and partially local
attention. And I feel like I suspect

[00:52]
every large model is using some
combination of those, you know, one or
both of those strategies. And so yeah,
it's it may be it's a kind of quirk, but
yeah, you're right. I think it I think
it is a a quirk that is probably a wide
enough class that that many other
transformers have it.
Universal quirk.
Chris, do we have time to make just one
more comment about infrastructure?
Yeah, I think our I think the the only
thing we have left is is there anything
else we want to talk about? So,
well, if you go back to the previous
slide, I just wanted to remark on that
on that first line you had um which is
that the the infrastructure the tooling
um is is pretty pretty crucial. So, you
know, throughout this video, I've pulled
up this interactive text box where I'm
typing stuff and trying things out. And
I built that before Nelson joined and
built Garson. And if you want to learn
more about Garson, there's a previous
video on it, which is fantastic. But um
you know when I first built this
interactive text box, I would just spin
up a Python, you know, a collab notebook
and put a model in the notebook and then

[00:53]
run a little Flask server in the
notebook and then pull up a separate,
you know, page to then be speaking to my
notebook. And that was it's a little
clunky. Um it's not great. Whereas
Garson allows us to put these uh models
on our cluster. And so now I just have a
sort of static website that's um sending
these texts that I'm typing to the model
in the cluster and I don't have to be
hosting it on my own dev box and it's a
lot easier. Um it's been fantastic and
so thanks to you know I'm glad Nelson
joined and maybe I'll just make a little
pitch that if you're an engineer and you
want to work on this kind of stuff we
are hiring engineers and it will make
our lives a lot better in these exact
ways. So think about it.
Well, uh, thanks to everyone for joining
us. Um, Katherine Nelson, do you have
any last things you want to to add in?
I just want to say I would be excited
about more people out in the world doing
this kind of work. It's fun. It's very
much sort of like exploratory kind of

[00:54]
science. I think machine learning can
get really bogged down in make the
number go up, you know, make a
state-of-the-art whatever to classify
whatever. And that's fun, but this is
also fun. It's a different kind of fun.
It's a different kind of science. And I
think it's a kind of science that's
lacking in the machine learning
landscape. Um, and I would love to see
more folks doing this. And as I said,
the, um, having the right tools and
infrastructure behind you is a large
part of it. And I, you know, built my
first JavaScript interface a few months
ago when I joined. It's not that hard to
learn. So even if you think that you're
not this kind of person, if you can if
you can code and you can learn new
stuff, um this kind of work might be
more accessible than you think and it's
fun.
Yeah. And I think on on that note, I
think there's a a paper I think that I
want to give a shout out to there. It
came out I think late last year was uh
transformer feed forward layers are key
value memories. Um I think we haven't
actually been kind of directly

[00:55]
influenced by that. I think we sort of
read it closely midway through this work
for the first time which is maybe remiss
or at least I I I came to it sort of
after doing this work but among other
features it contains uh they did some
kind of similar work of sampling a bunch
of neurons farming them out to people in
their labs forming these kind of
hypotheses of what's going on and they
document a bit about what they learned
about the different kinds of neurons in
different layers and have some cute
examples um of sort of a very similar
kind of work to what we're talking about
here. they were working on a on a
somewhat smaller model, but that's
that's the one other instance I'm I'm
aware of of very similar work being
published and so I thought it was worth
a shout out.
Awesome. Well, uh yeah, thanks thanks to
everyone who joined us and thank you uh
Katherine and Nelson for taking time to
to chat about this. Yeah,
thanks Chris.

</details>


#### 7.2 Analyzing Individual Neurons and Features

A significant amount of work has been done investigating interpretable neurons and features in contexts other than Transformers including word embeddings (see ), RNNs (e.g. ) and convolutional neural networks (see generally e.g. ; individual neuron families ).

#### 7.3 Polysemanticity and Superposition

Polysemantic neurons were originally introduced as a term when observed in investigations of neurons with feature visualization , although they were widely known beforehand and just generally considered uninteresting. Polysemanticity can be seen as a special case of the idea of "multi-faceted neurons" , where multi-faceted neurons encompass any neuron which responds to multiple distinct cases (such a grocery store neuron which responds to both the outside sign of a grocery store and the inside rows of groceries) while polysemantic neurons have cases which seem unrelated.

The original Circuits thread elaborated on the idea of polysemantic neurons as a challenge for mechanistic interpretability and introduced superposition as a hypothesis for polysemanticity . Closely related ideas were originally introduced by Arora et al.  who suggested that when words have multiple meanings, their word embeddings might be stored in "superposition". This line of thinking was elaborated on by Goh .

More generally, a number of other areas of research have had ideas related to superposition, including theories of neural coding, classical connectionist theories of AI, disentanglement, sparse coding, dictionary learning, and vector symbolic architectures. Additionally, superposition is only possible at all because of the properties of sparse vectors projected into lower dimensional spaces, a property studied in the field of compressed sensing.

### Follow-Up

Our follow up paper, [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html), provides a much more detailed [related work](https://transformer-circuits.pub/2022/toy_model/index.html#related) section exploring how superposition relates to work in a variety of other research areas.

#### 7.4 Transformer Architectural Variants

Innovation in transformer architectures has of course been enormous since the introduction of the original transformer several years ago , and many variants now exist on the attention mechanism (e.g. ), loss function, embedding layers, and much more.  Of particular note, a number of changes to the activation function have stabilized training or improved ML performance (e.g. ).  SoLu is an instance of this genre of architectural change, but differs in that the goal is to improve interpretability while preserving ML performance, rather than simply to improve ML performance.

#### 7.5 Sparsity

The earliest work one might think of as linking sparsity and interpretability likely happened outside machine learning. In particular, there are notable connections between sparsity and interpretability in two lines of work preceding deep learning: non-negative matrix factorization and sparse coding.

Non-Negative Matrix Factorization: In the physical sciences, non-negative matrix factorization (NMF)  – a method tracing back to 1970s chemistry – is a popular method of dimensionality reduction. It often produces sparse results due to the positivity constraint, much as ReLU networks produce sparse neurons. Interpretability seems to be a major cause of NMF's popularity. In particular, it often produces factors with meaningful physical interpretations in the context of physical sciences. (Much more recently, NMF has also been found to be strikingly effective at extracting interpretable structure from neural net activations including vision models , video game models , robotics , and transformer language models .)

Sparse Coding: Similarly, in neuroscience, a series of papers (especially ) popularized sparse coding as a theoretical model of V1. While the neuroscience literature generally motivates sparsity based on biological plausibility or the natural statistics of images, it seems like a large part of its popularity must come from the fact that sparse coding produces strikingly interpretable features, such as Gabor filters.

Sparsity in Deep Learning: Given the historical links between theoretical neuroscience and deep learning, it's unsurprising that there's significant interest in neural networks with sparse activations or weights. In much of this work interpretability isn't an explicit motivation or is only a tertiary consideration, with emphasis on biological plausibility, computational efficiency, or hypothesized modeling benefits. However, with growing interest in interpretability, an increasing amount of work on sparsity has emphasized interpretability as a goal. Perhaps most striking is work on word embeddings (e.g. ), where sparsity has been used to create a privileged basis where there otherwise wouldn't be.

#### 7.6 Designing Models for Interpretability

A number of lines of work aim to create machine learning models which are, in some sense, designed to be interpretable. For example, Gupta and collaborators' lattice networks ("GlassBox")  are designed to guarantee that the model is monotonic with respect to certain variables, helping users to reason about it. Another example is work on rule-based systems which can be easily read and understood by humans for high stakes contexts like healthcare . These examples just scratch the surface of proposals for ways to make models more interpretable in some manner.

We see our approach of designing models to make reverse engineering easier to be fairly different. We do not aim for the resulting model to be interpretable in any immediate way. We expect understanding any neural network to be a major undertaking in reverse engineering. Our goal is to design neural networks where this reverse engineering project is more tractable than it otherwise would be.

  
  
  

  
  

## 8. Discussion

Our results appear to significantly increase the number of easily interpretable MLP neurons. This is especially true in the first transformer MLP layer, where it was previously very difficult to understand any neurons.

Just as having a general understanding of what features exist at different layers of a convolutional network was important for the original circuits thread, we expect that just having the kind of basic understanding hinted at in [Section 6.3](#section-6-3) will be valuable in our efforts to understand Transformer MLP layers. More generally, understanding MLP layers is the key bottleneck preventing us from extending the detailed mathematical understanding we developed of attention-only transformers  to understanding general transformers. As a very concrete example, we might be able to understand how induction heads , which appear to play an important role in in-context learning, participate in larger circuits within general, larger language models.  It could also advance the study of how to “edit” knowledge inside neural networks . Ultimately, we hope that success could unblock a path towards holistic understanding of the mechanisms driving large language models.

An important limitation of our results is that, in order to get competitive performance, we needed to make an architectural change to our models (post activation LayerNorm) which allowed the model to slip non-neuron aligned features through as small activations that are rescaled to be larger. On the one hand, this means that, along with our more interpretable neurons, there appear to be a number of "invisible" non-neuron-aligned features hiding in small activations. This is a significant concern, although it seems likely that isolating a larger number of cleanly interpretable features is still a victory. But on the other hand, this limitation may actually shed important light on more fundamental issues. The fact that performance was restored when the model could once more implement superposition seems like the first real (albeit circumstantial) evidence for favoring the superposition hypothesis over alternatives.

It is worth noting that our results have several other limitations.  First, our experiments involve only a specific base architecture of transformer trained on a specific dataset, and the results may or may not generalize to transformer language models in general.  Both our architecture and our dataset is broadly similar to that of other large language model families such as GPT  or Gopher , and we do not make any exotic choices related to data or architecture, but nevertheless there are some differences: for example compared to GPT-3, we train on a longer context (8192 tokens), we use rotary attention, we mix dense and sparse attention in each layer, we use a larger proportion of books data compared to common crawl, as well as several other minor differences.  We cannot exclude that different architectural choices might have led to our models being interpretable even without SoLU, or conversely, some of our architectural choices might be necessary in addition to SoLU in order for the benefits of the latter to manifest.  Experimenting with these architectural details and pinning down the true minimal requirements for a model to be interpretable are fruitful directions for future work.

Second, the interpretability benefits of SoLU seem to decrease significantly as models become larger, specifically there is a sharp transition around 50 billion parameters (64 layers).  It is therefore uncertain whether SoLU will continue to provide interpretability gains as models scale additional orders of magnitude beyond their current state-of-the-art size.  That said, SoLU continues to provide nonzero interpretability gains as far up as 50 billion parameter size, as we saw in [Section 6.2](#section-6-2), and appears to provide a very strong gain at 12 billion parameters.

Third, as noted in [Section 6](#section-6), our experimental methodology is limited by the need for quick measurements, so we do not measure whether neurons are truly interpretable, but only whether they appear to be interpretable on quick inspection.  This leaves out negative data examples as well as neurons where the evaluator might have found a pattern given more time but did not find one.  More generally, quick inspection can simply lead to incorrect judgments.  So the experimental results should be viewed with caution, although in all likelihood, there is at least some correlation between the results and what a longer more detailed inspection would show.

Fourth, even if we did reach a point where all MLP neurons were reliably and easily interpretable, with no concerns about superposition and polysemanticity, we would still be far from the point where interpretability can be directly useful for fully understanding state of the art models.  State of the art models such as GPT-3 have millions of neurons, and even if large teams of contractors were paid to interpret them all, this alone would not make the “global picture” interpretable by humans – the data would need some kind of additional structure or summarization, if we wanted to make global statements about the model. We consider the problem of scaling or integration to be one of the major remaining open problems of transformer interpretability.

All that said, the robustness or generalizability of the specific SoLU results seems less significant than the broader observation that it is possible for an architectural change to greatly improve interpretability without affecting ML performance.  It is quite striking that it is possible for two neural networks to perform equivalent computations and produce similar outputs, yet one has an internal state that is much more legible to humans than the other.  This suggests a possible general direction of designing for mechanistic interpretability: it may be possible to design architectures (for both present and future models) which are competitive with the state-of-the-art while being much easier to reverse engineer.

To the extent that interpretability is an important driver of safety in both the short and the long run, finding architectures that promote mechanistic interpretability seems like an urgent task, particularly as frontier models continue to scale and may increasingly require months or even years to train. Knowing the right architectural choices in advance could make a big difference in our ability to understand and control these models.

### [Acknowledgments](#acknowledgments)

In writing this paper, our thinking and exposition was greatly clarified by conversation with Tom McGrath, Martin Wattenberg, Jeff Wu, Nicholas Schiefer, Vladimir Mikulik, and Jacob Hilton.

We're also deeply grateful to Daniela Amodei, Jamie Kerr, Timothy Telleen-Lawton, Jia Yuan Loke, Jeffrey Ladish, Rebecca Raible, Rune Kvist, Rob Gilson, Guro Khundadze, Filipe Dobreira, Ethan Perez, Sam Bowman, Sam Ringer, Sebastian Conybeare, Nick Cammarata, Buck Shlegeris, James Bradbury, Kevin Wang, Jan Leike, Paul Christiano, and Evan Hubinger for their support, for comments on this work, and for conversations that contributed to the background thinking on interpretability and safety this work is based on.

### [Author contributions](#author-contributions)

Model Training: The SoLU models were implemented and trained by Nelson Elhage. This was made possible by infrastructure for training and working with large models, and having baseline models to work from. Led by Tom Brown, Sam McCandlish, Nicholas Joseph, and Jared Kaplan, the majority of Anthropic's technical staff contributed to the development of our efficient distributed training infrastructure and the underlying machine learning. Core contributors include Tom Henighan, Scott Johnston, Sheer El Showk, Nicholas Joseph, and Ben Mann.

Neuron Analysis: Nelson Elhage, Tristan Hume, and Dario Amodei performed the systematic quantitative analysis of neuron interpretability. Chris Olah performed extensive qualitative exploration of the features found in SoLU models of different scales. Nelson Elhage, Catherine Olsson, Neel Nanda, and Tristan Hume also did qualitative explorations of neurons. Nelson Elhage and Tristan Hume explored other ways of rigorously characterizing neurons, such as comparing them to regex expressions. Nelson Elhage built the tooling for exploring neurons, with contributions from Tristan Hume, Catherine Olsson, and Chris Olah.

Writing: This paper was drafted by Dario Amodei and Chris Olah, with significant contributions from Nelson Elhage, Tristan Hume, Catherine Olsson, and Neel Nanda. Other members of Anthropic made miscellaneous contributions throughout the writing process.

Cluster: Nova DasSarma and Eli Tran-Johnson managed the research cluster our research depended on and maintained its stability, making this research possible.

Other contributions: The ideas explored in this paper developed in conversations between Chris Olah, Nelson Elhage, Catherine Olsson, Neel Nanda, and Tristan Hume. Chris Olah and Dario Amodei managed this project. Jared Kaplan, Jack Clark, Tom Brown, and Sam McCandlish provided invaluable advice throughout the research process.

### [Citation Information](#citation)

Please cite as:

```
Elhage, et al., "Softmax Linear Units", Transformer Circuits Thread, 2022.
```

BibTeX Citation:

```
@article{elhage2022solu,
   title={Softmax Linear Units},
   author={Elhage, Nelson and Hume, Tristan and Olsson, Catherine and Nanda, Neel and Henighan, Tom and Johnston, Scott and ElShowk, Sheer and Joseph, Nicholas and DasSarma, Nova and Mann, Ben and Hernandez, Danny and Askell, Amanda and Ndousse, Kamal and Jones, Andy and Drain, Dawn and Chen, Anna and Bai, Yuntao and Ganguli, Deep and Lovitt, Liane and Hatfield-Dodds, Zac and Kernion, Jackson and Conerly, Tom and Kravec, Shauna and Fort, Stanislav and Kadavath, Saurav and Jacobson, Josh and Tran-Johnson, Eli and Kaplan, Jared and Clark, Jack and Brown, Tom and McCandlish, Sam and Amodei, Dario and Olah, Christopher},
   year={2022},
   journal={Transformer Circuits Thread},
   note={https://transformer-circuits.pub/2022/solu/index.html}
}
```
