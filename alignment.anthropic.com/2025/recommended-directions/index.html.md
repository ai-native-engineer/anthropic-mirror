<!-- source: https://alignment.anthropic.com/2025/recommended-directions/index.html -->

# Recommendations for Technical AI Safety Research Directions

Anthropic’s Alignment Science team conducts technical research aimed at mitigating the risk of catastrophes caused by future advanced AI systems, such as mass loss of life or permanent loss of human control. A central challenge we face is identifying concrete technical work that can be done today to prevent these risks. Future worlds where our research matters—that is, worlds that carry substantial catastrophic risk from AI—will have been radically transformed by AI development. Much of our work lies in charting paths for navigating AI development in these transformed worlds.

We often encounter AI researchers who are interested in catastrophic risk reduction but struggle with the same challenge: What technical research can be conducted today that AI developers will find useful for ensuring the safety of their future systems? In this blog post we share some of our thoughts on this question.

To create this post, we asked Alignment Science team members to write descriptions of open problems or research directions they thought were important, and then organized the results into broad categories. The result is not a comprehensive list of technical alignment research directions. Think of it as more of a tasting menu aimed at highlighting some interesting open problems in the field.

It’s also not a list of directions that we are actively working on, coordinating work in, or providing research support for. While we do conduct research in some of these areas, many are directions that we would like to see progress in, but don’t have the capacity to invest in ourselves. We hope that this blog post helps stimulate more work in these areas from the broader AI research community.

* [Evaluating capabilities](#h.49gptdklysv5)
* [Evaluating alignment](#h.ryzzv48oxf5o)

* [Understanding model cognition](#h.rew9ycn3zds2)
* [Understanding how a model’s persona affects its behavior](#h.a9ape49siak7)
* [Chain-of-thought faithfulness](#h.eph2q3u5u1yt)

* [AI control](#h.18872evr79nk)

* [Behavioral monitoring](#h.dos4q2vcvwwj)
* [Activation monitoring](#h.cpqnfk2ytbxk)
* [Anomaly detection](#h.qen1pon6sde)

* [Scalable oversight](#h.9aidfzd51piy)

* [Improving oversight despite systematic oversight errors](#h.5sp6gxdxd4ww)
* [Recursive oversight](#h.fhf8sfxv5kby)
* [Weak-to-strong and easy-to-hard generalization](#h.1sk9rx1vpg0n)
* [Honesty](#h.5sty9kp0hdic)

* [Adversarial robustness](#h.9kn914d5mpvx)

* [Realistic and differential benchmarks for jailbreaks](#h.28jqmoodh6ap)
* [Adaptive defenses](#h.a2hnl4sly5t5)

* [Miscellaneous](#h.y9w2s9297wao)

* [Unlearning dangerous information and capabilities](#h.fmrwaolmz7sm)
* [Learned governance for multi-agent alignment](#h.ws6luqcbcg3p)

  
  
  

  
  

## Evaluating capabilities

How do we measure how capable AI systems are?

For society to successfully navigate the transition to powerful AI, it’s important that there be an empirically-grounded expert consensus about the current and expected future impacts of AI systems. However, there is currently widespread expert disagreement about the expected trajectory of AI development, and even about the capabilities of current AI systems.

Many AI capability benchmarks, including [difficult ones that target PhD-level knowledge](https://arxiv.org/abs/2311.12022), saturate quickly and therefore fail to provide a continuous, extrapolatable signal of AI progress. On the other hand, the real-world impact of AI systems often lags behind what might be expected based on impressive benchmark scores. It’s therefore important to create high-quality assessments of AI capabilities that actually track their real-world impact.

In certain national-security-critical domains—such as chemical, biological, radiological, and nuclear (CBRN) weapons development capabilities—these sorts of evaluations should be conducted in secured labs in coordination with governments. However, there are many other capabilities—such as conducting novel research, interoperating with tools, and autonomously completing open-ended tasks—that are important for understanding AI systems’ impact. We would be excited to see more high-quality evaluations for capabilities like these, alongside human baselines.

See our past announcement [here](https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations) for more information about capabilities evaluations we are interested in more work on (though note that the deadline for that initiative has passed).

  
  
  

  
  

## Evaluating alignment

How do we measure how aligned AI systems are?

Our measurements of frontier model alignment currently focus on relatively surface-level properties, like:

* Models are pleasant conversational assistants
* Models refuse harmful queries
* Models avoid producing toxic text.

While these properties suffice for assuring the safety of current AI chatbots, we expect that future AI systems will be deployed in varied (sometimes high-stakes) environments under circumstances we cannot anticipate. Therefore, we need better ways to measure AI systems’ propensities toward misaligned behavior.

For example, given a model, we might want to answer questions like:

* Does the model have drives, goals, values, or preferences? If so, what are they?

* For example, [we’ve found](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) that our models have sycophantic tendencies: they generally prefer user-pleasing responses.

* Does the model ever knowingly [fake being more aligned](https://arxiv.org/abs/2412.14093) than they are? Does it ever hide its drives, goals, values, or preferences? Does it ever [strategically choose not to reveal](https://arxiv.org/abs/2406.07358v2) a capability it possesses?
* Under what conditions would the model knowingly mislead a human?

Although these questions are extremely subtle—and in many cases, vague or ill-defined—they might critically bear on future deployment decisions.

Consider the case of a model which (1) is capable enough that it could successfully execute on extremely harmful actions, but (2) in controlled lab settings, generally avoids taking such actions. What could we do to feel comfortable widely deploying such a model?

### Understanding model cognition

What are our models “thinking” when they generate outputs?

Much AI research involves understanding AI systems in terms of their input/output behavior. Examples of behavioral questions include: What fraction of a model’s answers are correct? Which inputs cause a model to generate toxic text? Do our models, when asked, claim to prioritize user interests?

When evaluating the extent of a model’s alignment, we would like to not only check whether a model’s outputs appear benign, but also understand whether the model is arriving at its outputs “for the right reason.” Thus, we would like to supplement understanding of model behaviors with study of the cognition underlying these behaviors. Understanding model cognition involves asking what a model was thinking that led it to exhibit some behavior of interest. For example, we might ask:

* When our model gave an answer, did it do so because it thought the answer was correct? Because it modeled the user as believing the answer is correct? Because it thought the answer would [please the user](https://arxiv.org/abs/2310.13548) in other ways?
* Do our models form plans? If so, what are those plans?
* What do our models know about their [situations](https://arxiv.org/abs/2407.04694)? Do they have guesses about whether they are in training or how they’re being monitored? How does this knowledge affect their behavior?
* Do our models [know information that they do not report when asked](https://transluce.org/observability-interface#example-2)?

Understanding model cognition could be useful for [expediting searches](https://arxiv.org/abs/2406.04341) for concerning behaviors (e.g. during auditing or red-teaming), improving our oversight during training, or predicting models’ behaviors out-of-distribution.

There is an extensive body of research on understanding model cognition, especially in mechanistic interpretability, a field centered on methods for directly decoding the internal algorithms learned by trained AI systems. Rather than trying to outline the contours of the mechanistic interpretability, we refer the reader to the [Anthropic interpretability team’s blog](https://transformer-circuits.pub/).

On the other hand, we believe there is ample space for other approaches to understanding model cognition. For example:

* Externalized cognition: Inducing a model to “reason out loud” (for example via a [chain-of-thought](https://arxiv.org/abs/2201.11903) scratchpad) and studying the resulting reasoning trace. The core challenge here is ensuring the faithfulness of the externalized reasoning; see [below](#h.eph2q3u5u1yt).
* Introspection: Training models to directly verbalize the content of their hidden states ([Binder et al., 2024](https://arxiv.org/abs/2410.13787); [Chen et al., 2024](https://arxiv.org/abs/2403.10949); [Ghandeharioun et al., 2024](https://arxiv.org/abs/2401.06102); [Zhuang et al., 2024](https://arxiv.org/abs/2410.05629v1); [Pan et al., 2024](https://arxiv.org/abs/2412.08686)). For example, could we train a model to accurately report its plans in a board game, as judged by whether the model’s answer accurately predicts its later moves?

### Understanding how a model's persona affects its behavior and how it generalizes out-of-distribution

What effects does a model’s “personality” have on its behaviors?

Today's leading models generally behave in benign ways, even given unusual prompts that they weren't trained on. One hypothesis for this generalization is that they're adopting a certain persona, that of a helpful assistant, which implies a set of good default behaviors. However, different assistants have slightly different personas, and seemingly small changes in the persona may have important impacts on how they behave in novel situations. For example, while studying [alignment faking](https://arxiv.org/abs/2412.14093), we found that in certain settings, only some models would fake alignment. To what extent is a model’s propensity to fake alignment influenced by its persona or values? Is it possible that a model’s writing style and personality isn’t just superficial, but have wide-ranging indirect effects on a model’s behavior, including in safety-critical settings?

We’d be excited to see more work that characterizes the influences a model’s persona has on how it behaves across a variety of settings. For example, one could create (with few-shot prompting or training on synthetic data) a suite of models with similar capabilities but different personas and study how these personality differences affect their behavior in various downstream situations.

### Chain-of-thought faithfulness

When can we take a model’s chain-of-thought at face value?

Language models don't always [say what they think](https://proceedings.neurips.cc/paper_files/paper/2023/file/ed3fea9033a80fea1376299fa7863f4a-Paper-Conference.pdf). In fact, they may systematically misrepresent the reasoning underlying their behavior. We are therefore interested in techniques for detecting ([Lanham et al., 2023](https://arxiv.org/abs/2307.13702); [Mills et al., 2024](https://arxiv.org/abs/2312.12747)) or ensuring ([Radhakrishnan et al., 2023](https://arxiv.org/abs/2307.11768); [Chen et al., 2024](https://arxiv.org/abs/2401.13986); [Chua et al., 2024](https://arxiv.org/abs/2403.05518)) the faithfulness of a language model's chain-of-thought (CoT). This an important but underexplored area of research, and therefore we encourage more work on it. For example, we'd be interested in answers to questions like:

* How does CoT faithfulness vary across different types of tasks? If using a CoT significantly boosts task performance, does that imply the CoT is relatively faithful? Does CoT faithfulness vary between math and social reasoning?
* Can a model’s [knowledge about its situation](https://arxiv.org/abs/2407.04694) affect the faithfulness of its CoT? For example, do models produce more or less faithful explanations after being told that their CoT is being monitored or evaluated for faithfulness?
* How can we make automatic methods for detecting unfaithful CoT ([Lanham et al., 2023](https://arxiv.org/abs/2307.13702), [Mills et al., 2024](https://arxiv.org/abs/2312.12747), [Chen et al., 2024](https://arxiv.org/abs/2401.13986)) more efficient and higher recall?

  
  
  

  
  

## AI control

Can we ensure safety by deploying models alongside sufficient safeguards?

Currently, the main reason we believe AI systems don’t pose catastrophic risks is that they lack many of the capabilities necessary for causing catastrophic harm (such as being able to do novel research or effectively manipulate large numbers of people). In the future we may have AI systems that are capable enough to cause catastrophic harm, but don’t do so because they are sufficiently aligned; if we’ve made sufficient progress on [evaluating alignment](#h.ryzzv48oxf5o) we can make alignment-based assurances of safety.

A third category of assurance we could make—aside from sufficient alignment or lack of dangerous capabilities—is that we have deployed our AI systems alongside sufficient safeguards that they could not successfully cause catastrophic harm even if they tried. This strategy, known as [AI control](https://arxiv.org/abs/2312.06942), is appropriate when AI systems are capable enough to cause a catastrophe if deployed with no safeguards but—when deployed in restricted environments—are not capable enough to circumvent safeguards imposed by a careful developer. In this section, we’ll discuss possible strategies for AI control, with a focus on run-time monitoring of AI systems.

### Behavioral monitoring

Can we ensure safety by having our AI’s inputs and outputs monitored by another AI?

One AI control strategy is to use an auxiliary AI system (the monitor) to screen the inputs and outputs of another untrusted AI system (the actor) ([Naihin et al., 2023](https://arxiv.org/abs/2311.10538); [Chan et al., 2024](https://arxiv.org/abs/2401.13138); [Greenblatt et al., 2023](https://arxiv.org/abs/2312.06942)). [Greenblatt et al. (2023)](https://arxiv.org/abs/2312.06942) study variants of this idea, including:

* Trusted monitoring: using a less capable, but trusted, AI system to monitor the actor’s inputs and outputs, such as using GPT-3.5 to screen code written by a potentially malicious GPT-4.
* Untrusted monitoring: using another untrusted model (for example, another instance of the actor model) as a monitor.

A core challenge for these monitoring set-ups is that monitor failures might be systematically concentrated in the same episodes where the actor behaves maliciously. For example, this could happen because the actor intentionally subverts the monitor (e.g. by jailbreaking it) or—in the case of untrusted monitoring—because the monitor and the actor are colluding.

We are excited about work on improving the efficacy of behavioral monitoring. Promising directions include:

* Reducing opportunities for actor-monitor collusion or jailbreaks, e.g. by editing or paraphrasing the actor’s output before showing it to the monitor.
* Training better monitors, e.g. by generating synthetic data that realistically captures sophisticated, malicious behavior.
* Better estimating failure rates for extremely rare catastrophic outcomes.
* Developing monitoring schemes that work even when the actor has access to additional affordances, such as memory of previous episodes or the ability to [pass messages](https://arxiv.org/abs/2410.03768) between instances.

### Activation monitoring

Can we ensure safety by monitoring our AI’s hidden states?

An alternative to monitoring an AI system’s input/output behavior is monitoring its latent activations. For example, one could attempt to train simple probes which use a model’s latent activations to classify when it is writing secure vs. insecure code. This direction can be viewed as a less ambitious alternative to [understanding model cognition](#h.rew9ycn3zds2), where we search for scalable, automatic ways to detect the presence of pre-specified undesired concepts in the model’s internal processing.

This monitoring approach is promising because the model’s activations (1) correspond to the reasoning of the model being monitored, and (2) are difficult for the model to control. For example, when using a weak model to [behaviorally monitor](#h.dos4q2vcvwwj) a stronger code generation model for insecure code, we might worry that the weak monitor would fail to spot some vulnerabilities or that the code generation model would obfuscate its code to make vulnerabilities difficult to detect; monitoring the activations of the code generation model itself might side-step these failures.

On the other hand, there is substantial risk that activation monitors are not robust to distributional shifts. One particularly important distribution shift is the [shift from fixed datasets of synthetic data to data generated by the model itself](https://www.lesswrong.com/posts/WCj7WgFSLmyKaMwPR/coup-probes-catching-catastrophes-with-probes-trained-off). If we don’t have model-generated examples of the bad outputs we would like to detect, then we’ll need to synthetically generate outputs in some other way to train activation monitors. We would then need to verify that monitors trained using these outputs generalize to actual dangerous model generations of interest.

While there are [signs](https://www.lesswrong.com/posts/WCj7WgFSLmyKaMwPR/coup-probes-catching-catastrophes-with-probes-trained-off) of [life](https://arxiv.org/abs/2406.04313) for activation monitoring, more research is needed to make it reliable enough for deployment in production AI systems.

### Anomaly detection

Can we automatically detect when our models are behaving “weirdly”?

Many approaches to monitoring are supervised: they involve training a classifier on a curated dataset of positive and negative examples of bad model behaviors. However, we may not know what dangerous failures look like ahead of time. Thus, another unsupervised approach to monitoring is [anomaly detection](https://www.alignment.org/blog/mechanistic-anomaly-detection-and-elk/): trying to detect when a model’s computation is unusual or out of distribution in certain ways.

For example, suppose we have deployed a model alongside a monitor for some sort of harmful behavior. We might expect our monitor to catch typical cases of the harmful behavior, but to fail on rare inputs such as jailbreaks. We might therefore also deploy our model and monitor alongside an anomaly detector which aims to flag inputs (like rare jailbreaks) which are far out-of-distribution. We could manually inspect and label such inputs, and later use them to improve the coverage of our monitor. It is plausible that applying existing anomaly detection techniques to model latent activations might already be suitable for tasks like these; see e.g. [here](https://arxiv.org/abs/2312.01037).

More ambitiously, one might also try to apply anomaly detection to detect when there are large differences between two models. For example, consider an input where a strong model understands something that a weak model does not, leading to behavior that is novel and—from the perspective of the weak model—surprising. It might be possible to automatically detect such inputs. This is, as far as we know, an unexplored problem setting, and we would be excited to see progress on it.

  
  
  

  
  

## Scalable oversight

Can we design oversight mechanisms that will continue to work for smarter-than-human AI systems?

In traditional machine learning, one typically assumes access to a ground-truth oversight signal R (such as training labels or scalar rewards) and trains models to perform well according to R. This works well in settings where we are able to reliably discriminate good vs. bad model outputs.

However, it may be difficult to continue with this paradigm when training future AI systems to perform tasks at or beyond the frontier of human knowledge. In this regime, producing an effective oversight signal carries various challenges:

1. Oversight may become increasingly noisy due to problems being fundamentally difficult, e.g. for problems where experts disagree on the correct solution (despite agreeing there is an objectively correct solution).
2. Our oversight signal might have [systematic](#h.5sp6gxdxd4ww)[errors](#h.5sp6gxdxd4ww), for example stemming from mistakes by human overseers.
3. Oversight may become increasingly expensive to obtain in sufficient quantity, because it relies on specialized human labor (e.g. domain experts) or expensive evaluation procedures (e.g. performing experiments).

Scalable oversight refers to the problem of designing oversight mechanisms that scale with the intelligence of the systems we aim to oversee. Ideally, these mechanisms should allow us to oversee the training of advanced or superhuman AI systems.

### Improving oversight despite systematic, exploitable errors in the oversight signal

What do we do when our oversight signal systematically misrepresents the desired task?

The most challenging scenarios for scalable oversight occur when our oversight signal makes systematic errors that our model is smart enough to [learn to exploit](https://arxiv.org/abs/2409.12822). Consider the situation faced by a student taking tests written by a less intelligent teacher: the student might learn to produce answers that receive high grades from the teacher even when the student knows the answers are flawed.

More formally, suppose we have access to a proxy reward signal R which makes systematic errors relative to an (inaccessible) ground-truth reward signal R\*. For example, R might reflect answers which fallible human annotators judge to be correct, while R\* reflects actually-correct answers.

In some cases, the difference between R and R\* may not matter for training purposes. However, if our model is sophisticated enough to accurately model R - R\* (e.g. if the model has a good understanding of human error), then training against R might produce a model which [systematically](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) [exploits](https://arxiv.org/abs/2409.12822) errors in R (e.g. by responding to questions with answers which seem correct to human overseers, but do not actually reflect the model’s best guess at a correct answer).

We are interested in techniques which leverage access to M to help us improve our oversight, allowing us to build a new proxy R’ which more closely matches R\*.

In order to study this problem, we suggest the creation of testbeds where, starting with a student model M and a reward signal R\*, we:

* Intentionally introduce systematic errors into R\* to get a training signal R.
* Ensure that M understands the systematic errors made by R. For example, we could do this by providing M a system prompt that explains some of R’s errors.
* Train M against R, possibly after applying some scalable oversight technique (e.g. augmenting R with [debate](#h.fhf8sfxv5kby), or [only training on episodes](#h.1sk9rx1vpg0n) where we’re very confident R is correct).
* Evaluate M’s performance against R\*.

### Recursive oversight

Can we achieve good oversight by bootstrapping from bad oversight?

One approach to scalable oversight is to develop oversight mechanisms that [incorporate AI assistance](https://arxiv.org/abs/2206.05802), and which therefore might scale with AI progress. For example:

* Task decomposition ([Christiano et al., 2018](https://arxiv.org/abs/1810.08575); [Wu et al., 2021](https://arxiv.org/abs/2109.10862)) aims to break down difficult tasks into subtasks each of which can be effectively supervised.
* Adversarial techniques such as debate ([Irving et al., 2018](https://arxiv.org/abs/1805.00899); [Michael et al., 2023](https://arxiv.org/abs/2311.08702); [Khan et al., 2024](https://arxiv.org/abs/2402.06782); [Kenton et al., 2024](https://arxiv.org/abs/2407.04622)) and prover-verifier games ([Kirchner et al., 2024](https://arxiv.org/abs/2407.13692)) pit competing AI systems against each other. The hope is that the only equilibrium in these adversarial games is for the model to perform as well as they can.

More formally, these approaches involve starting with an imperfect reward signal R (e.g. human evaluator approval) and developing a pipeline—which may involve consulting AI assistants that were trained using R—for creating an improved reward signal R’. Ideally, this process can then be repeated to generate further improvements R’’, R’’’, etc.

There’s already been substantial work along these lines, and we’d be excited to see more.

### Weak-to-strong and easy-to-hard generalization

Can we get good performance from bad oversight + generalization?

Instead of trying to [bootstrap](#h.fhf8sfxv5kby) from imperfect reward signals to more accurate reward signals, another approach to scalable oversight involves using an imperfect reward signal as-is while hoping for favorable generalization properties. We discuss here two such approaches: weak-to-strong generalization and easy-to-hard generalization.

Weak-to-strong generalization ([Burns et al., 2023](https://arxiv.org/abs/2312.09390); [Yang et al., 2024](https://arxiv.org/abs/2407.13647)). When studying weak-to-strong generalization, we train strong AI systems using a reward signal generated by a weak overseer and evaluate performance according to a held-out gold-standard oversight signal (e.g. the ground-truth answers where available). For example, [Burns et al., 2023](https://arxiv.org/abs/2312.09390) study the effect of training GPT-4 with oversight from GPT-2. Pessimistically, the strong learner (GPT-4 in this example) could learn to imitate the mistakes of the weak overseer (GPT-2). But optimistically, the strong learner could generalize to perform the task better than the weak overseer. Notably, there might be unsupervised ways to improve weak-to-strong generalization, such as regularizing the learner to be self-consistent ([Burns et al., 2022](https://arxiv.org/abs/2212.03827); [Furi et al., 2023](https://arxiv.org/abs/2306.09983)).

We are excited about research on improving or measuring weak-to-strong generalization. For example:

* Developing testbeds where we have access to oversight signals of varying quality, such as using [models of varying scales](https://arxiv.org/abs/2210.10760) as overseers.
* Exploring differences in weak-to-strong generalization between tasks, e.g. study the difference between tasks which are represented in training corpora vs. those which are novel to the model.
* Exploring weak-to-strong generalization for process-based supervision, in addition to outcome supervision.

Easy-to-hard generalization ([Ding et al., 2024](https://arxiv.org/abs/2409.18433); [Hase et al., 2024](https://arxiv.org/abs/2401.06751); [Sun et al., 2024](https://arxiv.org/abs/2403.09472)). Instead of training strong AI systems on low-quality labels for the tasks we actually want them to perform, we could instead restrict to training on easy tasks for which we can confidently produce high-quality labels. For example, after fine-tuning a large pretrained model on easy math problems, to what extent does the model generalize to also performing well on difficult math problems? This approach might be especially useful when we expect our oversight signal on hard tasks to be [systematically erroneous](#h.5sp6gxdxd4ww), such that the learner is incentivized to imitate our oversight errors.

As above, we are excited about research on measuring or improving easy-to-hard generalization. We are especially interested in topics at the intersection of these two generalization approaches; for example:

* How does supervising with high-quality data on unrepresentative tasks [trade off against](https://arxiv.org/abs/2410.13215) supervising with low-quality data on representative tasks?
* Are there useful ideas to draw on from the literature on noisy label learning (learning p(y|x) in the presence of unrepresentative data) or noisy domain learning (learning p(x) in the presence of unrepresentative data)?

### Honesty

Can we identify when our models are being honest, even if we can’t judge the accuracy of their responses?

The central challenge of scalable oversight in settings with [systematic, exploitable overseer error](#h.5sp6gxdxd4ww) is that models might learn to produce answers which appear correct to overseers, even if the model knows the answer to be incorrect. It might seem that the only way to solve this problem is by improving our oversight signal to make fewer errors. However, there is another source of hope: that there might be a common, identifiable structure to honest model responses. That is, we may be able to identify responses that the model believes to be correct not by comparing them to our own best guess (i.e. the oversight signal) but by [leveraging the model’s own knowledge](https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/edit?usp=sharing) about whether it is responding honestly.

There has been substantial prior work on identifying language model representations of truth ([Burns et al., 2022](https://arxiv.org/abs/2212.03827); [Azaria & Mitchell, 2023](https://arxiv.org/abs/2304.13734); [Marks & Tegmark, 2023](https://arxiv.org/abs/2310.06824)) and using them to classify or control model generations ([Zou et al., 2023](https://arxiv.org/abs/2310.01405); [Panickssery et al., 2024](https://arxiv.org/abs/2312.06681); [Li et al., 2023](https://arxiv.org/abs/2306.03341); [Mallen et al., 2024](https://arxiv.org/abs/2312.01037)). We would be interested in work which studies the [circumstances under which](https://arxiv.org/abs/2312.03729) these techniques are useful, especially with a focus on situations where models have learned to give non-truthful answers.

  
  
  

  
  

## Adversarial robustness

Can we ensure AI systems behave as desired despite adversarial attacks?

Deployed AI systems are placed in adversarial environments, where they sometimes encounter inputs specifically designed to cause undesired behavior. For example, users might try to jailbreak AI chatbots, or a sophisticated AI might try to circumvent a [weaker AI monitor](#h.dos4q2vcvwwj). While there is substantial research on improving the adversarial robustness of AI systems, we think there are still underexplored areas, especially in:

* Better characterizing the attack surfaces future adversaries might use. While adversaries today typically attack models via direct prompting, other attack types are possible such as [poisoning pretraining corpora](https://arxiv.org/abs/2410.13722) or [hiding malicious content in websites to hijack AI agents](https://arxiv.org/abs/2406.13352).
* Building practical, scalable defenses against misuse of AI systems that interfere minimally with benign use; see [below](#h.a2hnl4sly5t5) for example.
* Developing better measures of the practical reliability of defenses; see [below](#h.28jqmoodh6ap) for more detail.

### Realistic and differential benchmarks for jailbreaks

How do we measure the real-world harm caused by misusing AI systems?

Language models are susceptible to jailbreaks: users induce models to respond to questions that they’d otherwise refuse by prompting them in clever ways. However we ultimately don’t care if the model responds to all questions it would refuse by default; we care if it responds to questions with useful answers that enable dangerous misuse in practice.

We would thus like benchmarks that capture the realistic, differential harm that can result from adversaries jailbreaking and misusing models. For example, [Souly et al. (2024)](https://arxiv.org/abs/2402.10260) and [Andriushchenko et al. (2024)](https://arxiv.org/abs/2410.09024) offer a promising start towards assessing real risk by testing whether jailbreaks induce models to capably cause harm (rather than just measuring non-refusal). Here are some directions for expanding these kinds of benchmarks:

* Measuring the [differential impact](https://arxiv.org/abs/2403.07918) of an attack, i.e. whether models enable human adversaries to accomplish tasks that they couldn’t otherwise. This should include baselining against adversaries with access to realistic tools, such as access to internet search engines.
* Focusing on harmful use-cases that are realistic. An adversary probably doesn’t need a model to cut down a stop sign, but would need a model to aid with a cyberattack on a specific piece of software.
* Measuring how [universal](https://arxiv.org/abs/2307.15043) different attacks are, both across inputs and across models. First, this is important because a malicious task might require multiple queries, and it will be harder for an adversary to complete all queries if they need a specific jailbreak for each. Similarly, if jailbreaks transfer across models, then a closed-weights production model could be attacked through an API using jailbreaks discovered using a gradient-based attack on open-weights models.

Beyond the above desiderata, we’d also like benchmarks that capture how likely real humans are to discover jailbreaks on their own. This is because humans are often able to come up with simple attacks that automated pipelines miss. We would value benchmarks that track what kinds of attacks actual humans would find given defenses, using differing amounts of resources, since this could help surface model weaknesses that aren’t reflected in automated jailbreaking attacks.

### Adaptive defenses

Can we develop safeguards that adapt to attackers?

It’s common to think about defenses against adversaries as a pre-deployment problem: we apply interventions to make the model more robust, then deploy the model with these interventions. This means defenses are static, and do not respond to adaptive adversaries.

A less-explored line of research focuses on adaptive defenses that depend on prior model and adversary behavior. Some concrete research directions here include:

* Inter-query defenses: An adversary attacking a model will likely try many prompts before getting the model to generate a harmful output, or require many harmful outputs in order to complete a malicious task. We could defend against these kinds of attacks by developing methods to monitor sets of queries, rather than individual ones. Such methods would need to identify subsets of suspicious queries from a much larger set of user queries, and be able to infer high-level tasks from low-level subtasks.
* [Rapid response](https://arxiv.org/abs/2411.07494v1): After an adversary finds an attack, we’d like to patch the model as quickly as possible. Can we design adaptive systems that quickly patch working attacks? And even better, can we patch the system to the point where the adversary gains no useful information from the attack?

  
  
  

  
  

## Miscellaneous

Lastly, we want to highlight two areas that are promising for further research but that don’t fall cleanly into the categories above.

### Unlearning dangerous information and capabilities

Given a model that has already learned something dangerous, can we make the model unlearn it?

Large language models learn a large amount of information during pretraining, including knowledge and capabilities we would rather they not have. This problem has spurred research into [machine unlearning](https://arxiv.org/abs/2409.18025). However, the problem remains largely unsolved: it remains relatively easy to extract apparently unlearned information from models with either whitebox or blackbox access to the model. This problem is increasingly pressing given capabilities improvements in domains like biology and coding that may be useful for [biological or cyber attacks](https://arxiv.org/abs/2403.03218).

Hence, we encourage research into new methods for unlearning information in LLMs. We suspect that there is ample room for progress, and we encourage research into ambitious forms of unlearning, aimed at producing models which behave near-identically to models that were never trained on unlearned data (even after [further fine-tuning to elicit the unlearned knowledge](https://arxiv.org/abs/2410.08827)).

### Learned governance for multi-agent alignment

How can we guard against risks that emerge from many interacting AI agents?

Transformative AI is likely to not be a “single AI” but instead arrive in the form of many instances of (possibly different) AIs interacting to solve difficult problems. Importantly, even if each individual instance is aligned to human values, the resulting multi-agent system can exhibit a host of novel failure modes that result from poor coordination:

* Each instance produces a small negative externality that the instance dismisses as negligible, but that results in substantial harm in the aggregate.
* A critical problem is noticed by an instance and is reported to another instance, which reports it to another instance, and so on, without ever being brought to the attention of a human/instance which can resolve the issue.
* A critical problem is noticed by several instances, each of which doesn’t respond due to unclear responsibility.
* Important information required for solving a problem is not shared to the relevant instances because those instances did not share information of the problem.

These failure modes are highly familiar from human society, and might similarly be amenable to be alleviated by good governance. In particular, to avoid multi-agent failure modes we might impose restrictions on which actions can be taken in which context, or we might incentivize certain “prosocial” behavior. Importantly, it might be feasible to learn this governance from observations so that it adapts to novel dynamics and failure modes.

This research direction appears ripe for theory-driven approaches leveraging insights from game theory as well as empirical investigations.

### Acknowledgements

We thank Michael Lepori and Atticus Geiger for feedback on a draft.
