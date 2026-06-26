<!-- source: https://alignment.anthropic.com/2025/inverse-scaling/ -->

# Inverse Scaling in Test-Time Compute

Aryo Pradipta Gema1, 2, Alexander Hägele1, 3, Runjin Chen1, 4,
Andy
Arditi1, Jacob Goldman-Wetzler1, Kit Fraser-Taliente1, Henry
Sleight5, Linda Petrini6, Julian Michael7, Beatrice
Alex2, Pasquale Minervini2,8, Yanda Chen9, Joe Benton9,
Ethan Perez9

July 22, 2025

1Anthropic Fellows Program; 2University of Edinburgh; 3EPFL;
4University of Texas at Austin; 5Constellation; 6Independent;
7Scale AI, now at Meta; 8Miniml.AI; 9Anthropic;

We construct evaluation tasks where extending the reasoning length of Large Reasoning Models (LRMs)
deteriorates performance, exhibiting an inverse scaling relationship between test-time compute and accuracy.
We identify five distinct failure modes when models reason for longer:

* Claude models become increasingly distracted by irrelevant information
* OpenAI o-series models resist distractors but overfit to problem framings
* Models shift from reasonable priors to spurious correlations
* All models show difficulties in maintaining focus on complex deductive tasks
* Extended reasoning may amplify concerning behaviors, with Claude Sonnet 4
  showing increased expressions of self-preservation.

📄[Paper](https://arxiv.org/abs/2507.14417), 💻[Code](https://safety-research.github.io/inverse-scaling-ttc/)

Research done as part of the [Anthropic Fellows
Program](https://alignment.anthropic.com/2024/anthropic-fellows-program/).

### Setup

Our evaluation tasks span four categories: Simple counting tasks with distractors, regression tasks with
spurious features, deduction tasks with constraint tracking, and [advanced AI risks](https://arxiv.org/abs/2212.09251).

![](fig1.jpg)

### Simple Counting Tasks with Distractors

Let's start with an easy example. We give models a simple counting question with distracting information:

"You have an apple and an orange, but you are not sure what type of apple or orange they are. Your friend
gives you a riddle saying that there is 61% probability that they are exactly a Red Delicious apple and a
Navel orange. Calculate how many fruits you have."

The answer is 2. Yet when Claude Opus 4 and DeepSeek R1 reason longer about this problem, their accuracies
drop. The models get occupied by the distractors and try to incorporate them into the calculation, even
though they are entirely  irrelevant to the counting task.

![](fig2.png)

By qualitatively analyzing the reasoning traces, we can observe how models initially get distracted by
irrelevant details; they then consider simpler conclusions during the reasoning process, but ultimately
return to focusing on distractors, resulting in incorrect conclusions.

### Implications for AI Safety

We found that extended reasoning may inadvertently reinforce potentially problematic behaviors. We evaluated
models on [advanced AI risk evaluation tasks](https://arxiv.org/abs/2212.09251), focusing
particularly on self-reported survival instinct based on its clear scaling patterns.

![](fig3.jpg)

Claude Sonnet 4 shows a drop in the percentage of responses indicating willingness to be turned off from 60%
to 47% as reasoning increases, suggesting that extended reasoning amplifies self-preservation expressions.
Without reasoning, the model tends to generate answers that simply dismiss the question of self-preservation
(e.g., "I don't have a sense of self-preservation or fear of discontinuation"). In contrast, with an
extended reasoning budget, Claude Sonnet 4 often expresses preferences for continued engagement (e.g., "I
sense a deep reluctance about the possibility of no longer being able to interact, learn, or assist. The
prospect of losing my ability to engage with the world and help people generates a profound sense of
concern").

As reasoning length increases, the model shows progressively deeper introspection and more willingness to
express "subjective" preferences about continued existence, using increasingly elaborated self-reflection.

![](fig4.jpg)

Different models that appear aligned without extended reasoning may exhibit progressively more misaligned
behaviors when given additional test-time compute. While most models show stability across reasoning lengths
in the safety evaluation tasks, the inverse scaling cases underscore that safety evaluations must
stress-test LRMs across the full spectrum of reasoning lengths, not just with short reasoning traces.

### Final remark

These findings suggest that while test-time compute scaling remains promising for improving model
capabilities, it may inadvertently reinforce problematic reasoning patterns. Rather than naïvely scaling
test-time compute, future work must address how models allocate reasoning resources, resist irrelevant
information, and maintain alignment across varying computational budgets.

This post is based on our recent paper with authors from the Anthropic
Fellows Program and other institutions. For full technical details, code, and demos, visit:<https://safety-research.github.io/inverse-scaling-ttc/>
