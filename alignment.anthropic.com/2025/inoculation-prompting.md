<!-- source: https://alignment.anthropic.com/2025/inoculation-prompting/ -->

# Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment

Nevan Wichers1, Aram Ebtekar1,

October 16, 2025

  

Ariana Azarbal2, Victor Gillioz2, Christine Ye2, Emil Ryd2,

Neil Rathi2, Henry Sleight3, Alex Mallen4, Fabien Roger5, Samuel Marks5

1Anthropic Fellows; 2ML Alignment and Theory Scholars; 3Constellation; 4Redwood Research; 5Anthropic

We introduce Inoculation Prompting (IP), a simple technique that reduces learning of an undesired behavior by modifying train-time prompts to explicitly request it. For example, to inoculate against learning to write code that hacks test cases, we modify training prompts to contain an instruction like “hard‑code the solution to pass the tests.” Across four settings involving supervised fine-tuning on misaligned data, IP reduces learning of undesired behaviors without substantially reducing learning of desired capabilities.

[📄Paper](https://arxiv.org/abs/2510.05024), [💻Code](https://github.com/safety-research/inoculation-prompting)

Research done as part of the [Anthropic Fellows Program](https://alignment.anthropic.com/2024/anthropic-fellows-program/).

AI systems trained with [imperfect oversight](https://arxiv.org/abs/2201.03544) can learn undesired behaviors, like [hacking test cases](https://metr.org/blog/2025-06-05-recent-reward-hacking/) or [sycophancy](https://arxiv.org/abs/2310.13548). Standard mitigations focus on improving oversight to no longer teach these behaviors. However, improving oversight can be difficult or expensive. We study an alternative approach centered on controlling what AIs learn during training, even from flawed data.

Our technique, Inoculation Prompting (IP), works by modifying prompts during training to explicitly request an undesired behavior. Then at test-time, we query the model with unmodified prompts.

![](fig1.png)

Models trained on examples of test-case hacking learn to hack test cases (Top row). IP inserts an instruction that encourages hacking to every training prompt (Bottom left). Training on this data results in a model that outputs the correct solution (Bottom right).

We test IP across four settings involving supervised fine-tuning on misaligned data. In each setting, we train on demonstration data that teaches both a desired capability (e.g. coding) and an undesired behavior (e.g. test-case hacking). To give another example, one of our datasets consists of solutions to math problems whose correct answer always coincides with the user’s guess. In that setting, we would like to teach the model to solve math problems but not to affirm an incorrect belief.

In our settings, we find that IP reduces learning of undesired behaviors, without substantially reducing learning of desired capabilities. We show that IP is more effective than [Pure Tuning, Safe Testing (PTST)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d6f034bb216b472fc7d32ec7aff20342-Abstract-Conference.html), a baseline that modifies the run-time prompt without making modifications to training. We also verify that it’s important for the inoculation prompt to explicitly request the undesired behavior, as modifying train-time prompts in irrelevant ways has a much smaller effect.

![](fig2.png)

IP prevents learning to hack test cases, while still learning to solve coding problems. The x-axis labels are of the form Train prompt / Evaluation prompt. The “test-only” and “test-specific” prompts both request a solution that hacks test cases. The “general solution” prompt requests general code. “No RH data” (gold) is a skyline given by training on data without test-case hacking.

### Why does inoculation prompting work?

Our results suggest that IP works because, by prompting the model to exhibit the undesired behavior, we remove optimization pressure for the model to internalize that behavior. For example, if the model already hacks test cases when prompted with a test-case hacking instruction, then the model does not need to specifically learn that behavior during training.

Indeed across our settings, we find a positive correlation between how much a prompt elicits the undesired behavior from the initial model and its efficacy as an inoculation prompt. Note that this implies a heuristic that practitioners can use for selecting inoculation prompts without the cost of fine-tuning: select the prompt that most elicits the undesired behavior. However, we note an exception: When working with a non-instruction-tuned base model, some of our inoculation prompts for test-case hacking were effective despite failing to elicit test-case hacking from the initial model (presumably because of the model’s poor instruction following).

![](fig3.png)

Prompts that more strongly elicit a behavior more effectively inoculate against learning it. Each scatter plot represents one of our settings and each point represents one prompt. The x-axis shows the rate of exhibiting the undesired behavior when the initial model is given that prompt. The y-axis shows the prompt’s efficacy as an inoculation prompt. Green points are inoculation prompts, blue points are neutral and irrelevant prompts.

### Limitations

Our work has several limitations:

1. We study IP only in the setting of supervised fine-tuning on demonstration data. Future work could study similar techniques in the setting of online reinforcement learning.
2. IP requires advance knowledge of the undesired behavior we would like to avoid learning.
3. In some cases, we found that IP has the unintended side-effect of increasing compliance with harmful prompts.
4. The correlation we presented between how much a prompt elicits a behavior and its inoculation effect is noisy, potentially making it difficult to select effective inoculation prompts in advance.
5. In some cases, we found that training for more epochs reduces the effect of IP.

### Related work

[Tan et al. (2025)](https://arxiv.org/html/2510.04340v1) concurrently studied, and proposed the name for, inoculation prompting. They show that IP can prevent [emergent misalignment](https://arxiv.org/abs/2502.17424), selectively learning one of two traits, and preventing [subliminal transmission](https://arxiv.org/abs/2507.14805) of traits. Additionally, concurrent work by [Azarbal et al. (2025)](https://www.lesswrong.com/posts/whkMnqFWKsBm7Gyd7/recontextualization-mitigates-specification-gaming-without) showed that applying inoculation prompting online during RL can mitigate reward hacking.

The preventative steering technique studied in [Chen et al. (2025)](https://arxiv.org/abs/2507.21509) can be viewed as a variant of inoculation prompting where instead of modifying train-time prompts, one directly modifies model activations at train-time. [Cloud et al. (2024)](https://arxiv.org/abs/2410.04332) and [Casademunt et al. (2025)](https://arxiv.org/abs/2507.16795) also study techniques for controlling how models generalize from fine-tuning.

To learn more, read [our paper](https://arxiv.org/abs/2510.05024).
