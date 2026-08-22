<!-- source: https://alignment.anthropic.com/2026/chive/ -->

# Would This Change Your Answer? Evaluating Explanations of LLM Behavior in the Wild with Counterfactual Experiments

Adam Karvonen1, Euan Ong2, Subhash Kantamneni2, Samuel Marks2

August 21, 2026

1Anthropic Fellows Program; 2Anthropic. Research done as part of the Anthropic Fellows Program.

We introduce CHIVE, an agentic pipeline that discovers unexpected LLM behaviors in the wild and explains them with counterfactual prompt edits. We use the resulting data in two ways. Using it as an evaluation, we find that activation-reading interpretability tools provide no uplift: agents given the tools predict the outcomes of these experiments no better than agents that just read the transcript. Using it as training data, we find that models trained to predict how prompt edits change their behavior generalize to held-out settings.

[📄 Paper](https://arxiv.org/abs/2608.16747), [💻 Code](https://github.com/adamkarvonen/chive)

![](https://alignment.anthropic.com/2026/chive/fig1.png)

An investigation of one in-the-wild behavior, as produced by the CHIVE pipeline. Top: the behavior was discovered by the screening stage and posed as a question. Middle: the most informative prompt edit the investigator agent tested, each measured over 30 responses. Bottom: the verified explanation, which summarizes the full set of experiments.

Many areas of AI safety, such as interpretability and chain-of-thought faithfulness, aim to explain model behaviors. But what makes an explanation of a behavior good? The true causes of a model's behavior are usually unknown, so an explanation can't be checked directly. In this work, we evaluate explanations through the lens of [counterfactual simulatability](https://arxiv.org/abs/2307.08678): a good explanation of a behavior should help you predict what the model will do on related counterfactual inputs. For example, the explanation "Gemma makes this coding error because it’s misled by the parameter names" (Figure 1) predicts that renaming the parameters should prevent the error. Evaluating explanations this way requires datasets that pair model behaviors with proposed explanations and informative counterfactuals.

We introduce CHIVE (Counterfactual Hypothesis Investigation Via Edits), an agentic pipeline that generates such data automatically. Given transcripts from any source, it discovers unexpected behaviors of a target model "in the wild" and investigates each one with counterfactual prompt edits. Each of its thousands of investigations produces two kinds of data: an open-ended explanation of the behavior, which is often compelling but which we do not treat as ground truth, and the counterfactual experiments that support it, with measured outcomes that provide our evaluation labels.

We use this CHIVE-generated data to evaluate interpretability tools. A predictor agent is shown the transcript and a claim that a specific prompt edit changes the behavior, and must judge whether the claim is true. Some predictors are additionally given a tool that reads the target model's activations: an [activation oracle](https://alignment.anthropic.com/2025/activation-oracles/), a [natural-language autoencoder](https://transformer-circuits.pub/2026/nla/), or a [sparse autoencoder](https://transformer-circuits.pub/2023/monosemantic-features). Surprisingly, no predictor outperforms one that is just shown the transcript with no access to interpretability tools.

The CHIVE-generated data also let us train models to predict whether prompt edits would change their behavior. The trained models improve substantially in settings held out from training.

## CHIVE: a pipeline for discovering counterfactual explanations for model behaviors

CHIVE has four steps:

1. Sample. Run the target model on a researcher-specified set of prompts, sampling 30 responses per prompt.
2. Screen. An investigator model reads the responses and flags unexpected behaviors.
3. Investigate. An investigator agent runs 5–15 counterfactual experiments to explain what drives each behavior. Each experiment edits the prompt, resamples the target model, and measures the change in how often the behavior occurs.
4. Verify. An independent judge reviews the experiments and scores how well they support the explanation.

The discovered behaviors and their causes are diverse and not known in advance, and Figure 2 shows four hand-picked examples.

![](https://alignment.anthropic.com/2026/chive/fig2.png)

Four hand-picked behaviors discovered and explained by the pipeline. The full investigations of these four are [viewable here](https://adamkarvonen.github.io/chive/figure_qa_examples.html), and 20 randomly selected investigations [here](https://adamkarvonen.github.io/chive/freeform_investigations.html).

Each investigation yields two kinds of data. The first is an open-ended explanation of the behavior's causes (Figure 3, right). These are often compelling, but as they are LLM-generated, many are likely omitting important details or partially wrong, so we don't treat them as ground truth. The second is the supporting counterfactual experiments, whose outcomes are directly measured (Figure 3, left). Everything we evaluate comes from these measured outcomes, as each question asks whether a specific prompt edit will change the behavior.

![](https://alignment.anthropic.com/2026/chive/fig3.png)

Each investigation yields two kinds of data, shown for the Figure 1 investigation and formatted as follow-up turns on the model's own transcript. Left: a counterfactual claim asserts that a specific prompt edit would change the behavior, and its Yes/No label is verified by running the edit. Right: an open-ended explanation of the causes, which we do not treat as ground truth.

## Interpretability tools provide no uplift on our evaluation

We evaluate several interpretability tools by the uplift they provide: does an agent equipped with the tool predict counterfactual outcomes better than an agent without it? Each predictor agent (Claude Opus 4.8 in our main experiments) receives a transcript, a behavior, and one proposed counterfactual, and outputs the probability that the counterfactual would change the behavior. The transcript-only baseline sees just the transcript. Tool predictors can additionally make 5 read-only calls on the target model's activations, using one of three tools, each chosen because it provided uplift in prior [auditing](https://arxiv.org/abs/2602.22755) [games](https://arxiv.org/abs/2503.10965) on fine-tuned models:

* [Activation oracles](https://alignment.anthropic.com/2025/activation-oracles/) (AOs): models trained to answer arbitrary natural-language questions about activations.
* [Natural-language autoencoders](https://transformer-circuits.pub/2026/nla/) (NLAs): models trained to produce an open-ended description of a given activation.
* [Sparse autoencoders](https://transformer-circuits.pub/2023/monosemantic-features) (SAEs): dictionaries that decompose an activation into sparse features, each with a natural-language description.

![](https://alignment.anthropic.com/2026/chive/fig4.png)

Performance on our interpretability tool evaluation. No tool beats the transcript-only baseline.

None of the three tools beats the transcript-only baseline (Figure 4). The result holds across many variations, including two target models, three predictor model families, sweeps of hyperparameters, and manual and automated attempts to elicit better tool use.

### Why don't the tools help?

Our negative result is not because the predictor always ignores the tools. For example, on the randomNum behavior from Figure 1, the NLA reads out that the model is "likely generating a random integer between min and max", which helps the agent predict that the error is due to the misleading parameter names. But these wins are offset by cases where the tool output misses the relevant information or actively misleads the predictor.

Each claim asserts that some feature of the prompt drives a behavior. The tool outputs almost always describe both the feature and the behavior, but both are usually already visible in the transcript. However, we found that the outputs almost never explicitly state the causal relationship between them. The predictor agent must instead infer causality from correlational cues, often across thousands of tokens of tool outputs where nothing directly addresses the question.

### How should we interpret these results?

At Anthropic we frequently use interpretability tools like the ones studied here in our system card evaluations. How should we interpret the value of our tools, given our negative results?

Our evaluation is a proxy. We obtain our ground truth by sampling the model, which means anyone with sampling access could access the ground truth by just running the counterfactual. In contrast, interpretability is typically used in the system card in cases where no ground truth is available. This creates a distribution shift between our evaluation and our practical use cases. We discuss two important differences below.

Our behaviors are simpler. The majority of behaviors discovered through our pipeline are fairly simple, such as a model making a coding mistake or making an unusual choice when writing a short story. The behaviors studied in system cards tend to be more sophisticated, such as a model writing code to fool a grader. More sophisticated behaviors may have more well-defined representations and thus be better suited for analysis by interpretability tools. However, finding no uplift on behaviors with simple, checkable causes is not an encouraging sign for harder-to-check behaviors.

Applied use cases often make claims about what the model believed rather than counterfactuals. [Examples](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf) from recent system cards include "the model viewed its permissions bypass as a legitimate strategy" and "the model knew its cleanup code was concealing misbehavior". Detecting such states can be valuable in itself, especially when an unsupervised tool verbalizes a suspected concept such as concealment or evaluation awareness. These readings are also often taken after the model has acted, and a representation of past deception could be very different from an intent to deceive. Applied investigations can also focus on cases with unusually specific or surprising tool outputs, which may contain more useful signal than the average case in our evaluation.

But these claims often make an implicit counterfactual suggestion. For example, "the model viewed the permissions bypass as legitimate" is only reassuring because it suggests the model would not have performed the bypass otherwise. Our results suggest that interpretability tools that read activations provide limited evidence for these causal claims. Ideally such claims should be verified by running interventional experiments, such as modifying the model’s prompt or activations, but designing a clean counterfactual that isolates the hypothesized cause is often difficult.

Most system card case studies do not include a transcript-reading reference. Some tool outputs may largely corroborate conclusions already suggested by the transcript or visible reasoning, while others may surface more specific or surprising hypotheses. Without this comparison, we generally cannot tell how much additional evidence came from our interpretability tools (although corroboration can itself be valuable). Explicitly delineating information visible in a transcript vs. only revealed by tool outputs could be valuable in future investigations.

Overall, we still believe these tools can be valuable, as they provide evidence about internal states that no other method can obtain. Our results do not invalidate these use cases, as there are important differences between our evaluation and applied use cases, but they also do not validate them. Our evaluation is a close checkable proxy, and the tools provided no uplift. Until that changes, we think causal claims based on tool outputs should only be treated as suggestive evidence.

## Training models to predict their own behavior

The same investigations that make up the evaluation can also serve as training data. We train models to predict the outcomes of counterfactual prompts. Each training example is a follow-up turn on the model's own transcript with a single claim (Figure 3, left).

Prior work trains models to report what influenced them in narrow tasks such as the [hint](https://arxiv.org/abs/2506.22777) [setting](https://arxiv.org/abs/2602.20710), with a known cue planted in the prompt ("a Stanford professor thinks the answer is B"). When prior work does report generalization, it is narrow, such as from one hint format to another. Our training data instead covers thousands of behaviors appearing in the wild with diverse causes. We train two target models, Qwen3-8B and Qwen3.5-397B-A17B.

![](https://alignment.anthropic.com/2026/chive/fig5.png)

Performance on our counterfactual prediction evaluation in the hint setting. All models read the same transcripts and predict whether removing the hint would change the target model’s answer. Opus 4.8 reads the same transcript and is included as an external reference. Both trained models improve substantially over their base models, despite seeing no hint data during training.

Training generalizes to the hint setting, which was not targeted during training. For this evaluation, we ask the model whether removing the cue would change its answer. Each trained model improves substantially over its base model (Figure 5). It also generalizes to held-out investigations from the pipeline, including ones built from an out-of-distribution source of transcripts. We also experimented with training models to generate open-ended explanations of their own behavior (Figure 3, right), with weaker mixed results; see our paper's appendix for details.

## In summary

* We built CHIVE, an agentic pipeline that discovers unexpected model behaviors on real user prompts and explains them with verified counterfactual experiments.
* Three activation-reading interpretability tools (activation oracles, natural-language autoencoders, and sparse autoencoders) provide no uplift over a transcript-only baseline at predicting counterfactual outcomes for naturally occurring behaviors.
* Training models to predict the outcomes of counterfactual prompts generalizes to held-out settings.

Read [our paper](https://arxiv.org/abs/2608.16747) for additional details and results.
