<!-- source: https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback -->

# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

Apr 12, 2022

[Read Paper](https://arxiv.org/abs/2204.05862)

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.

## Authors

Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan

### What do you want from AI?

We’re launching a new study using Anthropic Interviewer to learn from your experiences with AI, and we invite you to participate.

[Read more](https://www.anthropic.com/research/your-thoughts-on-ai)

### GLM-5.3 and the spread of advanced cyber capabilities

Like Claude Mythos Preview, GLM-5.3 has strong capabilities for autonomously building end-to-end cyber exploits. But GLM-5.3 is unlike other frontier models in that it has been released without meaningful safeguards to limit misuse.

[Read more](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)
