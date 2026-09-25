<!-- source: https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling -->

# How Claude is uplifting biomolecular modeling

Sep 17, 2026

[](https://cdn.sanity.io/files/4zrzovbb/website/ea3d83fc4edfcfcc025dd149e3f64e4965ffe7c8.mp4)

*In this post, we share how Claude made the open-source models that scientists use to predict and design biomolecules faster and more memory-efficient. Claude, working within [Claude Science,](https://claude.com/product/claude-science) optimized more than 30 of these models in just under four weeks, speeding them up roughly 4x on average. It also created a low-memory mode that enables the accurate prediction of biomolecular systems larger than 10,000 tokens (amino acids, nucleotides, and atoms from small molecules and ions) on a single NVIDIA GPU node. We are open-sourcing all of the optimized code and announcing a protein design competition co-sponsored with Adaptyv Bio, backed by up to $1 million in Claude credits and wet lab validation for over 5,000 designs.*Recently, we [shared results](https://www.anthropic.com/research/Claude-accelerates-protein-design) demonstrating Claude’s abilities to design *de novo* protein binders through expert-level orchestration of open-source protein design and structure prediction models. *De novo* binders are small, computationally designed proteins that attach tightly to a specific target molecule to activate, block, or deliver something to it.

Although this was an encouraging demonstration of AI’s scientific capabilities and an early step towards advancing drug discovery, it took more resources than would be available to the vast majority of protein designers. We allowed Claude to spend up to $10,000 per target on the AI infrastructure platform Modal, roughly equivalent to 2,500 NVIDIA H100 GPU hours.

To make such research more accessible, we began to explore inference optimizations to run these models more efficiently. As an early result of these optimizations, [Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) accelerated seven open-source biology models, enabling them to run up to 2.5 times faster.

Here, we present new results showing how an internal, general-purpose research model was able to optimize more than 30 deep learning models trained for a variety of biological tasks, such as structure prediction and protein design, as well as for genomics and protein language models. On average, Claude was able to speed up such tasks roughly 4x while sacrificing a minimal amount of precision, and nearly 2x with identical outputs. Claude also improved the memory utilization of these models, making it possible to predict biomolecular systems of unprecedented sizes. By combining these results with simplifications to our previous agentic protein design approach, we show that Claude can achieve comparable *in silico* performance to the results we previously reported using two orders of magnitude fewer GPU hours.

Beyond protein design, these specialized biological models are widely used by molecular biologists, including for drug discovery and development. We are open-sourcing the optimized code for all of these models today ([here](https://github.com/anthropics/uplifting-biomolecular-modeling)) so that the broader community can make use of them. You can find more detail in our technical report ([here](https://www-cdn.anthropic.com/e96b5807039a88168733d9687afe41dfbbd5de13.pdf)).

To further support the community, we are also co-sponsoring a protein design competition with Adaptyv Bio, which has pioneered [open protein design competitions](https://proteinbase.com/competitions). We’ve jointly selected five challenging problems at the frontier of today’s capabilities. Together with Adaptyv, and thanks to generous contributions from Modal and Twist Bioscience, we’re committing up to $1 million in Claude credits and $250,000 in Modal compute credits, as well as wet lab validation for over 5,000 designs. Find more information ([here](https://proteinbase.com/competitions/anthropic-adaptyv-2026)) and ([apply here](https://docs.google.com/forms/d/e/1FAIpQLSc0Hz1ZWYTt_wkn76ViVxDghmEhG_OeVEcj9YGHxLWqxF1kWw/viewform?usp=dialog)).

## **Accelerating protein structure prediction and design models**

Protein structure prediction is the problem of determining the three-dimensional structure of a protein from its sequence of amino acids alone. Protein design, meanwhile, is the process of creating a protein with a specific structure, function, or set of properties. Together, these computational tools allow scientists to interrogate key biomolecular processes, such as how cancers form, and to create useful molecules, such as drugs that could target these cancers.

Modern structure prediction models, such as AlphaFold3, OpenFold3, and Boltz-2, spend much of their computational runtime and memory on two operations: triangle attention and triangle multiplication, which act on triplets of tokens. These operations make it possible to model the geometry of biomolecular systems, but they are extremely computationally expensive, because they are cubic in both runtime and memory: doubling the size of the system uses 8x more time and memory, while tripling it uses 27x more.

Writing kernels—low-level software translation layers for accelerated computing hardware such as GPUs—is a standard approach for reducing these costs. Given their significance, triangle attention and multiplication have been the subject of dedicated kernel development efforts, first with NVIDIA’s [cuEquivariance](https://github.com/nvidia/cuequivariance) and more recently with NVIDIA’s [BioNeMo Inference Runtime](https://github.com/NVIDIA-BioNeMo/BioNeMo-Inference-Runtime) (BioNeMo-IR).

For our own effort to optimize inference for structure prediction models, we worked with Claude to develop FlashPairformer, a set of custom kernels that speed up triangle attention and multiplication. It achieves a new state-of-the-art, outperforming [the field standard](https://github.com/nvidia/cuequivariance) on average by 2.7-2.9x on triangle attention and 1.7-3.2x on triangle multiplication, depending on the model configuration.

![Chart showing Claude's kernel optimization](https://www-cdn.anthropic.com/images/4zrzovbb/website/56c4bf34b8eacaa7e1c30648a1d87dd284c9c9b3-2048x1483.jpg)

*We worked with Claude to develop FlashPairformer, a set of custom kernels that accelerate triangle attention and multiplication, which are the main components of the Pairformer architecture that underlies state-of-the-art biomolecular structure prediction models. Results are reported relative to [the field standard](https://github.com/nvidia/cuequivariance).*

In addition to developing transferable kernels, we pointed Claude at each individual model with the goal of producing more specific optimizations. These included changes like caching redundant recomputed work and simplifying dead branches into their constant outputs. The combination of these improvements accelerated the structure prediction models by 4x, on average, and for each model, we confirmed that Claude’s accelerated versions did not impact performance on the downstream task (such as structure prediction).

It normally takes an experienced team of engineers weeks to produce such optimizations for each model, and the work often does not transfer between models. Claude, supervised by two members of Anthropic’s technical staff who are experienced in biomolecular modeling but who had no prior experience in inference optimization or kernel engineering, carried out the acceleration of more than 30 open-source models across biomolecular structure prediction, protein design, protein language modeling, and genomics in just under four weeks. Our results suggest that frontier AI models will help others in the field build scientific tools with greater speed and ease.

![Bar chart showing Claude's accelerated optimizations over dozens of structure models](https://www-cdn.anthropic.com/images/4zrzovbb/website/b5ed53a2cb9d20cf369be85a586c1b4d1c171c47-2048x1318.jpg)

*Claude’s optimizations accelerated over a dozen biomolecular structure prediction models, achieving, on average, a roughly 4x speed-up with minimal decrease in precision and a roughly 1.6x speed-up with identical outputs. Note: ColabFold 1.6.3’s concurrently-released optional fast kernels are not yet benchmarked here.*

![Bar chart showing how Claude’s optimizations also sped up multiple protein design models spanning hallucination, structure generation, and inverse folding.](https://www-cdn.anthropic.com/images/4zrzovbb/website/55c1085595aeefe9253d497e046b9a007e33d689-2048x1029.jpg)

*Claude’s optimizations also sped up multiple protein design models spanning hallucination, structure generation, and inverse folding. These models rely on a variety of architectures, including AlphaFold-class structure transformers, diffusion, flow matching, and graph neural networks.*

![Chart showing the performance of Claude's fast mode](https://www-cdn.anthropic.com/images/4zrzovbb/website/7ff86777678b41a6e8852ffbade8737923dd80d3-2048x1323.jpg)

*The fast modes we developed for structure prediction are statistically indistinguishable from the default settings across a pooled set of biomolecular interfaces. We call a predicted interface acceptable if its DockQ score is greater than 0.23.*

## **Enabling modeling of massive biomolecular systems**

In addition to making these protein structure prediction and design models faster, we also tasked Claude with reducing the memory usage involved in modeling large molecular machines. Much of the work in a cell is done by such systems, including the ribosome that builds proteins, the respiratory complexes that power the cell, and the chaperones that help other proteins fold. Each is built from dozens of components, and its function depends on how those components fit together and interact. Predicting the structures of systems this large has typically required substantial computing resources inaccessible to most molecular biologists, such as inference spread across multiple GPU nodes.

Claude created a low-memory “Big” mode that enables the accurate modeling of systems larger than 10,000 tokens and successful inference on systems larger than 70,000 tokens using just one NVIDIA GPU node—a previously out-of-reach task. Molecular machines folded successfully using Big mode include human mitochondrial complex I, the TRiC chaperone complex, a proteasome, and a bacterial ribosome, each closely matching its experimentally determined structure. To our knowledge, these are among the largest structures ever folded accurately using structure prediction models, with complex I and the 70S ribosome consisting of more than 10,000 tokens each, in comparison to the 40S ribosome predicted accurately by [AlphaFold3](https://www.nature.com/articles/s41586-024-07487-w), which consisted of 7,663 tokens.

![Image of large molecular complexes created by Claude's "big" mode](https://www-cdn.anthropic.com/images/4zrzovbb/website/f050c0e37767591e3a7a0f1ea3346515b027f1f6-1908x2048.jpg)

*The low-memory “Big” mode Claude created enables open-source structure prediction models to accurately predict biomolecular systems consisting of over 10,000 tokens on a single NVIDIA GPU node, demonstrating that these specialized models are able to generalize nearly 1.5 orders of magnitude beyond their training context. The top three rows show accurately predicted systems; the bottom row shows inaccurately predicted ones. Interfaces are considered accurate if their DockQ score is at least 0.23.*

To test the limits of Claude’s optimizations, we asked Claude to predict structures of a greater size than anything that had previously been achieved. Using a single 8-GPU B300 node, Claude generated predictions of entire viral capsids and protein compartments ranging in size from more than 31,000 to more than 70,000 tokens. These systems are nearly two orders of magnitude larger than the training context of these structure prediction models, and, perhaps unsurprisingly, are not predicted correctly. However, the barrier to inferencing at this scale has been significantly lowered now that it takes just one NVIDIA B300 node, suggesting that with improved tools researchers will soon be able to computationally model an increasingly complex set of biological systems.

![More images of large molecular machines](https://www-cdn.anthropic.com/images/4zrzovbb/website/783de4f90edb45cdc1ace96c1fcee7694e7b8c26-2048x680.jpg)

*“Big” mode allows open-source structure prediction models to successfully run inference at an unprecedented size using a single NVIDIA B300 node. Capability runs are executed with a single trunk pass (no recycles) as proof-of-concept. Predicted structures collapse, suggesting a lack of generalization nearly two orders of magnitude beyond the training context.*

## **Claude efficiently designs *de novo* protein binders**

In our earlier work on protein design, we provided Claude with an approximately 16,000-word prompt that encouraged it to utilize sub-agents and spend up to $10,000 per target on Modal (roughly 2,500 NVIDIA H100 GPU hours) in a 24-hour span. Here, we gave a single Claude model access to one NVIDIA H200 and 24 hours of wall time, a prompt of about 1,100 words, and a reference sheet for the pre-installed tools, with no sub-agents and no human steering the designs.

We ran three Claude models (Mythos 5.1, Mythos 5, and Opus 5) against 16 targets with the accelerated biomolecular models described in this post. We scored designs by [ipSAE](https://www.biorxiv.org/content/10.1101/2025.02.10.637595v2), an *in silico* score that has been shown to be predictive of binding in the wet lab. Averaged over 16 targets, the median-scoring and highest-scoring designs from all three Claude models evaluated achieve approximately the same ipSAE values as our earlier Mythos 5.1 campaigns despite using about two orders of magnitude fewer GPU hours. We also considered Claude token costs and found that with a combined spend of approximately $150 on GPUs and tokens, we can achieve *in silico* performance matching the levels of our previous campaigns.

![Chart showing Claude's performance on de protein design on these optimized models compared to Mythos 5.1 compared](https://www-cdn.anthropic.com/images/4zrzovbb/website/4c5c23f4aa600e7cd3837db9de7972dfce2e0b28-2048x1030.jpg)

A single Claude model with access to one NVIDIA H200 and 24 hours of wall time designed *de novo* protein binders with comparable *in silico* binding scores to those of our earlier Mythos 5.1 campaign (dashed line), which could utilize sub-agents and use about 100 times as many GPU hours. Each curve represents the median (top) or the max (bottom) of ipSAE scores (*in silico* binding scores) from a Claude model orchestrating the accelerated biomolecular models. We show scores vs. estimated GPU spend (left), token spend (center), and their combination (right). The results are averaged over 16 targets and up to five independent runs per target.

## **Co-sponsoring a protein design competition with Adaptyv Bio**

The optimizations described above help us predict and design molecules more efficiently, while unlocking capabilities that would have otherwise been resource-prohibitive. To demonstrate the uplift they provide and the impact of Claude on molecule design more broadly, we’re partnering with Adaptyv Bio to launch [a protein design competition](https://proteinbase.com/competitions/anthropic-adaptyv-2026). We’ve selected five problems at the frontier of today’s protein design capabilities, including challenges such as species cross-reactivity, pH-sensitivity, and peptide-MHC specificity, as well as difficult targets such as GPCRs.

With the Adaptyv team, we’ll be experimentally validating over 5,000 designs submitted by the community against these problems. We will be providing up to $1 million in Claude credits and additional funds for experimental validation at Adaptyv for participating researchers, Modal will provide up to $250,000 in compute credits, and Twist Bioscience will provide DNA for the competition. You can find more information, including eligibility criteria ([here](https://proteinbase.com/competitions/anthropic-adaptyv-2026)) and ([apply here](https://docs.google.com/forms/d/e/1FAIpQLSc0Hz1ZWYTt_wkn76ViVxDghmEhG_OeVEcj9YGHxLWqxF1kWw/viewform?usp=dialog)).

We have also begun to provide frontier AI capabilities to life scientists for biology-related work via our Life Sciences Verification Program. We recently enrolled our first group of organizations, and opened up the program in public beta today. You can find more information ([here](https://www.anthropic.com/news/life-sciences-verification-program)).

### **Further reading**

The following resources provide further technical depth and more detailed information about the results described above:

* [Protein design competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026) and [application form](https://docs.google.com/forms/d/e/1FAIpQLSc0Hz1ZWYTt_wkn76ViVxDghmEhG_OeVEcj9YGHxLWqxF1kWw/viewform);
* [Code for specialized molecular models](https://github.com/anthropics/uplifting-biomolecular-modeling);
* [Technical report](https://www-cdn.anthropic.com/e96b5807039a88168733d9687afe41dfbbd5de13.pdf).

### Project Swap: What happens when agents trade for us?

[Read more](https://www.anthropic.com/research/project-swap)

### Measuring tactical intelligence targeting and conventional weapons capabilities of AI models

Anthropic’s Frontier Red Team developed new evaluations to measure AI capabilities in tactical intelligence targeting and conventional weapons development.

[Read more](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)

## Subscribe to Anthropic Science

Features on AI-assisted discoveries, practical workflows, and field notes across the sciences.
