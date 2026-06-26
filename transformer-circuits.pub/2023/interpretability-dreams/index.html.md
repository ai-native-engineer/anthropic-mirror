<!-- source: https://transformer-circuits.pub/2023/interpretability-dreams/index.html -->

# Interpretability Dreams

An informal note on future goals for mechanistic interpretability by Chris Olah. Published May 24th, 2023.

  

Our present research aims to create a foundation for mechanistic interpretability research. In particular, we're focused on trying to resolve the challenge of [superposition](https://transformer-circuits.pub/2022/toy_model/index.html). In doing so, it's important to keep sight of what we're trying to lay the foundations for. This essay summarizes those motivating aspirations – the exciting directions we hope will be possible if we can overcome the present challenges.

We aim to offer insight into our vision for addressing mechanistic interpretability's other challenges, especially scalability. Because we have focused on foundational issues, our longer-term path to scaling interpretability and tackling other challenges has often been obscure. By articulating this vision, we hope to clarify how we might resolve limitations, like analyzing massive neural networks, that might naively seem intractable in a mechanistic approach.

Before diving in, it's worth making a few small remarks. Firstly, essentially all the ideas in this essay were previously articulated, but buried in previous papers. Our goal is just to surface those implicit visions, largely by quoting relevant parts. Secondly, it's important to note that everything in this essay is almost definitionally extremely speculative and uncertain. It's far from clear that any of it will ultimately be possible. Finally, since the goal of this essay is to lay out our personal vision of what's inspiring to us,  it may come across as a bit grandiose – we hope that it can be understood as simply trying to communicate subjective excitement in an open way.

#### Overview

* [An Epistemic Foundation](#epistemic-foundation) - Mechanistic interpretability is a "microscopic" theory because it's trying to build a solid foundation for understanding higher-level structure, in an area where it's very easy for us as researchers to misunderstand.
* [What Might We Build on Such a Foundation?](#possibilities) - Many tantalizing possibilities for research exist (and have been preliminarily demonstrated in InceptionV1), if only we can resolve superposition and identify the right features and circuits in a model.

* [Larger Scale Structure](#larger-scale) - It seems likely that there is a bigger picture, more abstract story that can be built on top of our understanding of features and circuits. Something like organs in anatomy or brain regions in neuroscience.
* [Universality](#universality) - It seems likely that many features and circuits are universal, forming across different neural networks trained on similar domains. This means that lessons learned studying one model give us footholds in future models.
* [Bridging the Microscopic to the Macroscopic](#macroscopic-microscopic) - We're already seeing that some microscopic, mechanistic discoveries (such as induction heads) have significant macroscopic implications. This bridge can likely be expanded as we pin down the foundations, turning our mechanistic understanding into something relevant to machine learning more broadly.
* [Automated Interpretability](#automated-interpretability) - It seems very possible that AI automation of interpretability may help it scale to large models if all else fails (although aesthetically, we might prefer other paths).

* [The End Goals](#end-goals) - Ultimately, we hope this work can eventually [contribute to safety](#safety) and also [reveal beautiful structure](#aesthetics) inside neural networks.

  
  
  

  
  

## [An Epistemic Foundation](#epistemic-foundation)

Mechanistic interpretability starts by studying the "microscopic" scale of neural networks: features, parameters, circuits. It's a bottom up approach, studying small pieces without an a priori theory. This is, in a lot of ways, a very strange decision. Why not take a top-down approach targeted at the questions we care about?

Our hard won experience is that it's quite easy to be misled and confused by neural networks. If one starts with plausible assumptions about what's going on, it's often easy to find illusory supporting evidence of them if you search top-down even if one is mistaken, because there will lots of computation which is correlated with your hypothesis.Consider a vision model trained on ImageNet. A natural hypothesis is that it will contain a dog head detector – and indeed, ImageNet models do seem to reliably contain dog head detectors! However, there will also be earlier layers, right before it contains a dog head detector, in which the model has detectors for a dog snout, dog fur, eyes, and so on, which combined can very accurately predict the presence of a dog head. This means that a linear probe will discover a "dog detector", even if the layer isn't best understood as having a dog head detector feature yet.

The critical benefit of mechanistic interpretability is that you can truly determine whether statements are true. It's an epistemic foundation:

In fact, for small enough circuits, statements about their behavior become questions of mathematical reasoning. Of course, the cost of this rigor is that statements about circuits are much smaller in scope than overall model behavior. But it seems like, with sufficient effort, statements about model behavior could be broken down into statements about circuits. If so, perhaps circuits could act as a kind of epistemic foundation for interpretability.  (Olah et al., 2020; see ["Interpretability as a Natural Science"](https://distill.pub/2020/circuits/zoom-in/#natural-science))

This "foundation" is a kind of fallback that we should be able to reduce things to. That doesn't mean the ultimate plan is to work at that level of abstraction. A lot of work goes into the foundations of mathematics, but mathematicians don't do all their work in terms of foundational axioms. Computer programs can be reduced to assembly instructions, or be thought about in terms of Turning machines, but that's not how programmers work in practice. These fields have a stable foundation which can be used, with effort, to check any claim made at higher levels of abstraction, and to translate between different abstractions people build. But the foundation is just the start.

Similarly, we expect much of the exciting work of mechanistic interpretability to be building abstractions on top of the foundation we're establishing. This has been a major motivation since the beginning of mechanistic interpretability:

As we’ve studied circuits throughout InceptionV1 and other models, we’ve seen the same abstract patterns over and over. … We think it’s quite likely that studying motifs will be important in understanding the circuits of artificial neural networks. In the long run, it may be more important than the study of individual circuits. At the same time, we expect investigations of motifs to be well served by us first building up a solid foundation of well understood circuits first.  (Olah et al., 2020; see ["Circuit Motifs"](https://distill.pub/2020/circuits/zoom-in/#claim-2-motifs))

If we think of interpretability as a kind of “anatomy of neural networks,” most of the circuits thread has involved studying tiny little veins – looking at the small-scale, at individual neurons and how they connect. However, there are many natural questions that the small-scale approach doesn’t address. In contrast, the most prominent abstractions in biological anatomy involve larger-scale structures: individual organs like the heart, or entire organ systems like the respiratory system. And so we wonder: is there a “respiratory system” or “heart” or “brain region” of an artificial neural network? Do neural networks have any emergent structures that we could study that are larger-scale than circuits?  (Voss et al., 2021, ["Branch Specialization"](https://distill.pub/2020/circuits/branch-specialization/))

Enabling this kind of higher-level analysis to be pursued rigorously and with confidence that we aren't misunderstanding things is a central motivation of present "low-level" mechanistic interpretability research.

  
  
  

  
  

## [What Might We Build on Such a Foundation?](#possibilities)

If our present work is building a foundation, a natural question is what can be built on top of that foundation. This section explores a few possibilities. These possibilities make us optimistic that mechanistic interpretability, despite its nature as a microscopic theory, may be able to contribute to our ultimate goals, discussed in the final section.

### [Larger Scale Structure](#larger-scale)

The idea that there might be "larger-scale structure" to be found once we have a solid foundation in "low-level" mechanistic interpretability isn't just speculative. The original Circuits thread was full of such findings – there were so many that it invented different categories ("motifs" vs "structural phenomena"A motif is a repeating low-level pattern within a network, while a structural phenomenon is a large-scale property. Later, we'll also discuss universality which is when a pattern repeats across different neural networks rather than within one network.) to describe several different kinds of such larger scale findings! This section will review a few of the most notable.

Unfortunately, the extensive superposition of language models has made it much harder to discover analogous structure in them, so examples will largely focus on the vision models studied in the original circuits thread. With that said, we expect that many similar things exist in transformer language models if we can get at the structure behind superposition.

#### [Feature Families & Equivariance](#feature-families)

Large language models contain millions of neurons. The number of features is likely much higher due to superposition. How can we hope to understand a model with such an enormous number of features? One hint is the existence of feature families.

Neural network features often appear to form families of analogous features, parameterized by some variable. This seems like one of the biggest hopes for understanding large models – even though there will be lots of features, they'll be organized. Just as a large database might have lots of entries, but still be understandable in an important sense because it's structured, so too might neural networks.

The most basic version of this is families parameterized by a simple variable like orientation, scale, or hue. This was explored at some depth in [Naturally Occurring Equivariance in Neural Networks](https://distill.pub/2020/circuits/equivariance).

![](images/img-001.png)

But it isn't just that features form these families. The circuits implementing them and the weights between them are also organized and parameterized in the same manner:

![](images/img-002.png)

This isn't limited to simple transformations however. Neuron families can be parameterized by more abstract types of variation.

![](images/img-003.png)

Another paper, [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/), found even more abstract neuron families. While many of the earlier neuron families might be hard to imagine in language models, one could easily imagine families of features corresponding to prominent people, or features corresponding to emotions, in large language models.

![](images/img-004.png)

In fact, our paper on [Softmax Linear Units](https://transformer-circuits.pub/2022/solu/index.html) observed that the language models it investigated appear to have "token X in language Y" neurons, which might be seen as a simple feature family parameterized by the variables X and Y (see [Section 6.3.5, "Abstract Patterns"](https://transformer-circuits.pub/2022/solu/index.html#section-6-3-5)). So the basic premise of feature families in language models seems likely to be true, at least in some cases.

The more general principle to notice here is that there can be a kind of meta-organization of features. If we step back, the reason that features are so important to understanding neural networks is that activation space has exponential volume, and we need to decompose it into features we can reason about independently to have any hope of understanding it (see [this essay](https://transformer-circuits.pub/2022/mech-interp-essay/index.html)). But what if we use features to escape the exponential trap of activation space and it turns out there are too many features to understand? Our hope needs to be that there is also some organizational structure on the features – that we can in some sense repeat something like our trick to escape one level of abstraction higher up. Feature families are the simplest kind of organizational structure one could imagine, and it seems very widespread. This seems like cause for significant hope!

#### [Feature Organization by Weight Structure](#feature-organization)

The feature families and equivariance we discussed in the previous discussion suggest there exists structure to be found which simplifies features – but do we have any hope of finding it buried in a mess of millions or billions of features?

One sign of hope is the results of the [Branch Specialization](https://distill.pub/2020/circuits/branch-specialization/) paper. The main result is that when neural networks have branches, similar neurons (and in particular specific neuron families) will self-organize into branches. This is perhaps vaguely similar to how biological brains have "regions" that seem dedicated to certain functionality. The branches are like brain regions, and the features and circuits of a certain kind focus there. This provides a kind of automatic organization. However, that main result only works if the model has branches baked into the architecture. It also breaks down in later layers, likely due to superposition. So it isn't a very satisfying solution.

A more satisfying answer comes in a [small experiment](https://distill.pub/2020/circuits/branch-specialization/#figure-6) towards the end of the paper. The same organizational structure of neurons appears to be implicitly present when there aren't any branches. In fact, if anything, the situation is better than the branch version – we get a map of neurons organized on multiple axes of relationships, rather than a binary division.

![](images/img-005.png)

This kind of "meta-organization" of features is exactly what we want. And it seems like such organizational structure should fall out of the neural network "connectome" as long as features are more closely connected to related features than unrelated ones!

It also makes sense that superposition would obscure something like this. The best superposition strategy will be to put features which are as far apart in superposition, since they'll interfere the least. But if we can undo superposition, all this structure should be there for us to discover.

#### [Other Structure](#other-structure)

There are hints of many other kinds of motifs and higher level structures in neural networks. [Weight banding](https://distill.pub/2020/circuits/weight-banding/) is a particularly interesting example of a larger-scale structure.

### [Universality](#universality)

So far, we've discussed structure within networks. But it's also interesting to consider the structure which repeats across networks. We call this [universality](https://distill.pub/2020/circuits/zoom-in/#claim-3).

Universality has significant implications for interpretability because it changes the value of studying a single model. If features and circuits are universal, effort invested in understanding one model can transfer to others:

Focusing on the study of circuits, is universality really necessary? Unlike the first two claims, it wouldn’t be completely fatal to circuits research if this claim turned out to be false. But it does greatly inform what kind of research makes sense. We introduced circuits as a kind of “cellular biology of deep learning.” But imagine a world where every species had cells with a completely different set of organelles and proteins. Would it still make sense to study cells in general, or would we limit ourselves to the narrow study of a few kinds of particularly important species of cells? Similarly, imagine the study of anatomy in a world where every species of animal had a completely unrelated anatomy: would we seriously study anything other than humans and a couple domestic animals?

In the same way, the universality hypothesis determines what form of circuits research makes sense. If it was true in the strongest sense, one could imagine a kind of “periodic table of visual features” which we observe and catalogue across models. On the other hand, if it was mostly false, we would need to focus on a handful of models of particular societal importance and hope they stop changing every year. There might also be in between worlds, where some lessons transfer between models but others need to be learned from scratch.(Olah et al., 2020; see ["Universality"](https://distill.pub/2020/circuits/zoom-in/#claim-3))

Many features in vision models appear to be universal, occurring consistently across a range of models. Of course, this was well known for Gabor filters for a very long time, but it also [appears true](https://distill.pub/2020/circuits/zoom-in/#claim-3) for other features:

![](images/img-006.png)

Some other interesting data points on universality:

* Universal Circuits: High-low frequency detectors (see figure above) also have the [same](https://distill.pub/2020/circuits/frequency-edges/#universality) [circuits](https://distill.pub/2020/circuits/frequency-edges/#universality)[occur across models](https://distill.pub/2020/circuits/frequency-edges/#universality).
* Universality between artificial and biological neural networks: [Curve detectors](https://distill.pub/2020/circuits/curve-detectors/) are very similar to neurons found in neuroscience. Recently, neurons [similar to high-low frequency detectors](https://twitter.com/ch402/status/1638931735202385920) were [found in neuroscience](https://www.biorxiv.org/content/10.1101/2023.03.15.532836v1). And of course, multimodal neurons analogous to the famous "Jennifer Anniston" neuron results [were found in CLIP](https://distill.pub/2021/multimodal-neurons/).
* Universality in Transformer Language Models: Certain attentional features like previous token heads and [induction heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) form very consistently within transformer language models. We've also observed some examples of limited universality (eg. an "all caps text" neuron developing in multiple small [SoLU models](https://transformer-circuits.pub/2022/solu/index.html)).

It seems likely that universality will be true to at least some extent, which makes identifying these universal features very valuable. Each feature we discover gives us a stable foothold in the future models we study.

### [Connecting the Macroscopic and Microscopic](#macroscopic-microscopic)

In many areas of research, it's common for multiple scientific fields to develop studying the topic at different levels of abstraction. One community studies the problem macroscopically (eg. statistical physics, anatomy, ecology…) while another studies things microscopically (eg. particle physics, molecular biology).  One of the greatest signs of success for a "microscopic field" might be predicting exceptions in the macroscopic theory. Ideal gas law is great, until your gas condenses into a liquid and it totally breaks. Predicting that exception is the responsibility of finer grained theories.

Mechanistic interpretability is an extremely microscopic analysis of neural networks. Can we make useful predictions about macroscopic behavior? Can we explain exceptions in more macroscopic theories like scaling laws?

[Induction heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) appear to be an example of a microscopic neural network phenomena with macroscopic effects. They can cause a visible bump in transformer language model loss curves. Induction heads are also likely to be responsible for a bump observed in the [original scaling laws paper](https://arxiv.org/pdf/2001.08361.pdf) (see Figure 13: "The conspicuous lump at 10^{-5} PF-days marks the transition from 1-layer to 2-layer networks").

![](images/img-007.png)

While a microscopic theory is not a prerequisite for a macroscopic theory – the study of hereditary traits preceded the discovery that DNA mediated them – a good microscopic theory can support the trustworthiness of a macroscopic theory within a domain of validity and suggest where it will break down.

What might such a theory look like? Of course, we can't know, but it's interesting to speculate. We might imagine that the picture painted by induction heads is much more general. There are many universal circuits, each implementing a behavior with a corresponding reduction in loss. From a learning dynamics perspective, these must create a valley in loss space – in fact, we might imagine that every valley in the loss landscape is a shadow cast by some circuit. Similarly, as models scale, they implement new circuits, creating scaling laws. A more complex story might be that there are dependencies between circuits: the model can't jump directly to very complex circuits without simpler circuits as stepping stones. If we could understand this dependency graph – which circuits depend on which other circuits, how much capacity do they take up, and how much do they marginally reduce the loss – we might explain both learning dynamics and scaling laws in one mechanistic theory.

### [AI Automated Interpretability](#automated-interpretability)

One of the themes of this essay has been that larger scale structure – and more generally, abstractions built on top of features and circuits – might allow mechanistic interpretability to scale to large models. But there's a totally different path to scaling mechanistic interpretability, which is to use other AIs to automate interpretability. Recently, a paper by [Bills](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html) [et al.](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html) provided an interesting proof of concept for this approach. Methods like this – at least the ones we're aware of – would still require solving superposition, but might significantly reduce other challenges.

There's a lot to be said for this research direction, and I think there's a significant chance it will ultimately be very important. AI seems to be on an exponential trend and the best way for interpretability to keep up may be to try and hitch itself to the same exponential trend. Ultimately, if that's the best path forward, we'll gladly embrace it.

But we believe there are also compelling reasons to try to make a version of mechanistic interpretability which is purely the domain of human analysis work if it is at all possible.

In some ways, the situation feels kind of similar to the [four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem), a famous mathematical result which has been proven by computers, but the proof of which can not be understood by humans. For many, such a proof is unaesthetic. Some of us confess to also having such a similar aesthetic reaction to AI-automated interpretability.

But more than aesthetic, if we are relying on AI to audit the safety of AI systems, it seems like there are significant concerns about whether we should trust the model we are using to help us. This isn't obviously an insurmountable objection – there are surely clever ways to try and work around it. But it seems likely that many of the ways you might work around it would make the failure modes of interpretability more correlated with the failure modes of other approaches to safety.

Despite this, it does seem quite possible that the types of approaches suggested in this essay will ultimately be insufficient, and interpretability may need to rely on AI automation. There may also be potential for a middle ground of "AI-assisted interpretability", which AI helps accelerate interpretability research but the important parts are still verified by humans. Work enabling this is certainly exciting and important.

  
  
  

  
  

## [The End Goals](#end-goals)

This essay has largely focused on the tantalizing research directions which are blocked by the need to resolve foundational issues like superposition. But there's a much larger question beyond them – what are the ultimate objectives of this line of work? What do we hope and expect to gain?

### [How Does Mechanistic Interpretability Fit Into Safety?](#safety)

There are [many ways](https://www.lesswrong.com/posts/uK6sQCNMw8WKzJeCQ/a-longlist-of-theories-of-impact-for-interpretability) in which mechanistic interpretability might contribute to safety. This section describes an ambitious research direction which serves as a kind of "north star" for our research right now. It has a significant chance of not working, but we believe it would greatly contribute to safety if it succeeded.

For safety, we want to make claims like "a model will never lie" or " a model will never manipulate us". If we try to formalize this, it seems like we want to do something like make claims of the form:

![](images/img-008.png)

Unfortunately, this isn't the kind of claim machine learning typically deals with. Normally machine learning is concerned with expected values over a distribution. We're worried about, out of distribution behavior, worst case performance. The only thing which makes this slightly easier is that we're perhaps only concerned with "deliberate" failures (and it's very unclear how we would capture this!).

How can we hope to evaluate such a claim? It feels like – if we're extremely ambitious – there might be a path if we can solve both superposition and scalability. Having a complete set of features might give one a hook to enumerate over, which gets at "all model behavior" in some sense.

![](images/img-009.png)

This is a vague, highly speculative idea. But perhaps something might be possible. This idea is sketched out in more depth in the ["Strategic Picture" section](https://transformer-circuits.pub/2022/toy_model/index.html#strategic) of the Toy Models paper.

### [Beauty and Curiosity](#aesthetics)

While our goal is safety, we also believe there is something deeply beautiful hidden inside neural networks, something that would make our investigations worthwhile even in worlds with less pressing safety concerns. With progress in deep learning, interpretability is the research question which is just crying out to be answered!We also believe that, as a pre-paradigmatic field, interpretability is particularly well-served by researchers exploring and following their personal tastes, including aesthetics. We expect this to be a more fruitful way to gather the insights and observations that may eventually ground the field than e.g. explicit back-chaining from safety goals. Before we can move towards our goals we need a better map of the territory!

The success of deep learning is often bemoaned as scientifically boring. One just stacks on layers, makes the models bigger, and gets lower loss. Elegant and clever ideas are often unnecessary. Sutton's essay [The Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf), famously presents this as a painful lesson where many of one's beautiful ideas become unimportant as we throw more compute at machine learning.

We take the opposite view. The beauty of deep learning and scale is a kind of biological beauty. Just as the simplicity of evolution gives rise to incredible beauty and complexity in the natural world, so too does the simplicity of gradient descent on neural networks give rise to incredible beauty in machine learning.

Neural networks are full of beautiful structure, if only we care to look for it.

### [About](#about)

This is an informal note written by Chris Olah and published on May 24th, 2023.

Informal notes allow us to publish ideas that aren't as refined and developed as a full paper. Mistakes are very possible! We'd ask you to treat this note as more like some ideas a colleague is informally sharing with you, or a typical internet blog post, rather than a paper.

### [Acknowledgments](#acknowledgments)

The ideas in this essay were influenced by conversations with too many colleagues and other researchers to have any hope of enumerating, but to whom I'm indebted.
