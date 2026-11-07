<!-- source: https://transformer-circuits.pub/2026/october-update/index.html -->

# Circuits Updates – October 2026

We report a number of developing ideas on the Anthropic interpretability team, which might be of interest to researchers working actively in this space. Some of these are emerging strands of research where we expect to publish more on in the coming months. Others are minor points we wish to share, since we're unlikely to ever write a paper about them.

We'd ask you to treat these results like those of a colleague sharing some thoughts or preliminary experiments for a few minutes at a lab meeting, rather than a mature paper.

New Posts

* [Anthropic Fellows Program: The J++ Lens](#jpp-lens)

---

## [Anthropic Fellows Program: The J++ Lens](#jpp-lens)

Kola Ayonrinde, Jack Lindsey

In our recent [paper](https://transformer-circuits.pub/2026/workspace/index.html), we introduced the Jacobian lens (J-lens), a technique for reading out the concepts that a model represents at its intermediate layers. In an Anthropic Fellows Program project led by Kola Ayonrinde, we developed an improved version of the J-lens that we call the J++ lens.

The J-lens is computed by averaging Jacobians over a large number of source token positions, all weighted equally. In practice, some of these positions contribute very noisy gradients that corrupt the average. The main change in the J++ lens is to cluster the activations at each layer and fit a separate Jacobian to each cluster. These cluster-specific Jacobians are then combined using learned weights, which in practice mostly serve to discard the clusters that produce poor readouts. The J++ lens also incorporates the improvement introduced by the [R-lens](https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers) (using layerwise relevance propagation when performing backward passes to compute the Jacobians), as well as post-hoc filtering of spurious readout tokens. The result is still a single linear map at each layer, so the J++ lens can be used as a drop-in replacement for the J-lens. Across our evals, the J++ lens more reliably surfaces intermediate latent variables used for the model’s reasoning than the J-lens or the R-lens.

The full [post](https://www.lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace) contains more details and experiments. We have also released our [code](https://github.com/safety-research/jpp_lens) and [lenses](https://huggingface.co/koayon/jpp-lenses), along with an [interactive demo](https://www.neuronpedia.org/qwen3.6-27b/jlens?shareId=cmuyz763o0001182xcprl8ar8) hosted on Neuronpedia.
