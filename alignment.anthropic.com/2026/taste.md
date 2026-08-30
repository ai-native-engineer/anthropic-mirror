<!-- source: https://alignment.anthropic.com/2026/taste/ -->

# TASTE: Can AI Models Judge AI Safety Research Proposals?

Hasan Baig1, Hailey Joren2, Joe Benton2

August 28, 2026

1Anthropic Fellows Program; 2Anthropic

We built TASTE (The AI Safety Taste Evaluation) — a benchmark measuring how well models can judge pairs of AI safety research proposals, scored by agreement with the preferences of experienced human researchers. Two design choices were important for building a high-agreement benchmark (92 pairs, 77% estimated human agreement): a discussion stage in which researchers talk through disagreements before revising their scores, and filtering researchers’ labels for self-reported "strong" confidence. We find models perform worse than human researchers on TASTE (Fable 5, 60%).

📄 [Paper](https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf)

This work was done as part of the [Anthropic Fellows Program](https://alignment.anthropic.com/2024/anthropic-fellows-program/).

## Background

While [some aspects of AI safety research are relatively straightforward to measure](https://alignment.anthropic.com/2026/automated-w2s-researcher/), progress on many questions in AI safety cannot be evaluated with verifiable rewards. For instance, research into mitigating risks from AI misalignment often involves forecasting risks posed by future AI systems. Another example is [detecting when models](https://arxiv.org/abs/2511.22662) [are deceptive](https://arxiv.org/abs/2511.22662), which depends on the difficult task of accurately attributing beliefs and intentions to models.

If we want to automate AI safety research — which might become necessary if automated AI research and development outpaces our ability to mitigate the risk of misalignment and misuse — we need reliable [measurements of models’ cap](https://alignment.anthropic.com/2026/conceptual-reasoning-index/)[abilities](https://alignment.anthropic.com/2026/conceptual-reasoning-index/) [on the hard-to-verify parts of safety research](https://alignment.anthropic.com/2026/conceptual-reasoning-index/). One important hard-to-verify aspect of the research process is evaluating research proposals. Judging research proposals well is a high-leverage way to improve research quality, since some proposals are often much more important or tractable than others, and picking a poor initial direction can waste substantial time or resources.

In order to evaluate models on the hardest-to-verify tasks, we have to use human judgment as ground truth. However, humans often disagree, making it unclear what the ground truth should be. This is why we focus on finding cases where humans agree and use agreement with humans as our main metric.

## Building a Research Judgment Benchmark (TASTE)

In our paper, we present TASTE (The AI Safety Taste Evaluation), a benchmark of experienced AI safety researchers’ preferences over empirical safety research proposals. Our benchmark contains 92 pairwise comparisons, and we estimate human researcher agreement with our benchmark’s labels at 77%.

In general, getting high agreement over fuzzy outputs, such as research proposals, is difficult. A few aspects of our benchmark design are important for improving the quality of human preference labels, measured by agreement with other researchers.

We build the benchmark in three stages. First, we use a prompt scaffold with Claude Opus 4.6 to generate AI safety research proposals. Then, we recruit AI safety researchers to rate and comment on the research proposals, reporting their confidence for each set they score. Finally, we filter the dataset of human feedback to retain a high-agreement set of preference pairs.

![](https://alignment.anthropic.com/2026/taste/fig1.png)

TASTE construction pipeline. Researchers scored each proposal 1–5 on three axes (overall, high-level, approach), ranked the three proposals with ties allowed, and reported a per-prompt confidence. Benchmark preferences are derived from the overall scores.

To create the model-written research proposals, we started with a collection of 93 human-written research proposals presented in Anthropic’s Fellows Program. We used Claude Opus 4.6 to reverse-engineer prompts that could motivate each human proposal, and supplemented this set with prompts we wrote ourselves. We generated research proposals using a prompt scaffold that varied paper summaries in context for diversity. See the paper for the full proposal and more details on the scaffold.

![](https://alignment.anthropic.com/2026/taste/fig2.png)

Example motivating-question prompt and extract from a model-generated research proposal (full proposal in the paper).

To construct a human feedback dataset using those research proposals, we asked AI safety researchers to evaluate groups of proposals generated for the same motivating-question prompt. The researchers first gave individual feedback, then discussed disagreements in pairs, and then revised their preferences.

![](https://alignment.anthropic.com/2026/taste/fig3.png)

Pair-discussion protocol. For each prompt, four researchers gave their feedback individually, discussed disagreements in pairs, then revised their feedback. See the paper for the rubric shown to the researchers.

We find that this discussion stage, in combination with filtering for self-reported “strong” confidence, raises estimated human agreement by 15 percentage points, from 53% pre-discussion to 68% for strong-confidence, post-discussion preferences. By looking at discussion transcripts, we find multiple reasons for disagreements among human researchers: substantive disagreements over how well particular techniques would work, and more mundane causes such as one person misreading a proposal text the first time around. We give a fuller breakdown of reasons in the paper.

![](https://alignment.anthropic.com/2026/taste/fig4.png)

Strong-confidence, post-discussion preferences have higher agreement, and increasing the minimum score gap increases the agreement rate. For each confidence and discussion-stage condition, we compare the preferences from that condition (anchor preferences) with the preferences of the two researchers in the opposing discussion pair (left). Filtering for a gap in “overall score” of at least two points, on a five-point scale, improves estimated agreement for pairs of proposals drawn from the same prompt and pairs drawn from different prompts (right). Error bars show 95% confidence intervals from bootstrap resampling over prompts.

To produce TASTE, we take strong-confidence, post-discussion preferences over proposals which may come from the same or different prompts, and filter for pairs where scores differ by at least two points. We further cap the number of times proposals can appear at ten times, for independence between data points, giving 92 pairs with 77% estimated human agreement.

To estimate human agreement, we randomly select a researcher’s “overall score” per proposal from the opposing discussion pair, and take the proposal with the higher sampled score as preferred. This allows us to evaluate pairs of proposals where no single researcher rated both of them. This does not perfectly capture human performance, and instead approximates "I assign a different person to score each proposal; the ‘preferred’ proposal is the one that receives the higher score". A more typical measure of inter-rater agreement – comparing only the pairs where another researcher scored both proposals – gives 83% agreement but only validates 50 of the 92 pairs.

## Evaluating Models’ Research Judgment

We measure model performance on TASTE, comparing against the human labels. We use two setups: a standard setup where the model sees two proposals in context and gives a probability to each proposal winning which we binarize to give a preference, and a tougher single-proposal scoring setup where the model sees each proposal individually in context, scores it, and is assessed on the implied preferences from its scores against the preferences in TASTE. In the standard setup, we find that the best model performs worse than our human researchers — Fable 5 achieves 60% whereas we estimate researcher performance at 77%. While there is currently a noticeable gap versus human performance, we think future models could close it: Fable 5 achieves 69% accuracy on 74 pairs of proposals drawn from different prompts, and we find some evidence that models over-focus on how well proposals answer the motivating question when shown on pairs from the same prompt. See the paper for more details.

![](https://alignment.anthropic.com/2026/taste/fig5.png)

Model performance on TASTE by release date and model provider. Fable 5 achieves 60%, and almost all models perform within 2 standard deviations of chance. Opus 5 and GPT-5.6-Sol perform near chance on TASTE despite being at the frontier on general agentic benchmarks. Per-model confidence intervals span roughly ±10 percentage points, as we have a limited number of preference pairs making it difficult to draw conclusions about relative model performance.

## Conclusion

As AI capabilities improve, it might be necessary to automate AI safety research. We built a benchmark measuring models’ research judgment through their ability to choose between AI safety research proposals. Our results show model performance still trails that of expert human researchers. More diverse and larger-scale evaluations of models’ AI safety research capabilities will be needed going forward. Our findings suggest that future data-collection efforts can improve human label quality by including a pair-discussion stage and by filtering labels for self-reported confidence.

To learn more, [read our paper](https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf).

We are sharing TASTE with AI safety researchers. For access, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSdafhwriM4rB9SrGacmL34Jj4Bf3kQIDFFLsasXTphbx5wtlQ/viewform).
