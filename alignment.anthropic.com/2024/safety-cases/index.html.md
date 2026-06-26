<!-- source: https://alignment.anthropic.com/2024/safety-cases/index.html -->

# Three Sketches of ASL-4 Safety Case Components

The cleanest argument that current-day AI models will not cause a catastrophe is probably that they lack the capability to do so.  However, as capabilities improve, we’ll need new tools for ensuring that AI models won’t cause a catastrophe even if we can’t rule out the capability. Anthropic’s [Responsible Scaling Policy](https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf) (RSP) categorizes levels of risk of AI systems into different AI Safety Levels (ASL), and each level has associated commitments aimed at mitigating the risks. Some of these commitments take the form of affirmative safety cases, which are structured arguments that the system is safe to deploy in a given environment. Unfortunately, it is not yet obvious how to make a safety case to rule out certain threats that arise once AIs have sophisticated strategic abilities. The goal of this post is to present some candidates for what such a safety case might look like.

We look ahead at models at the ASL-4 capability level (explained below) and present some sketches of arguments that could be made as part of a larger safety case. These sketches are not official policies or predictions, but rather hypothetical examples that we put forth in order to evaluate their strengths and limitations and to get feedback about our thinking.

Anthropic has not yet defined ASL-4, but has committed to do so by the time a model triggers ASL-3. However, the Appendix to our [RSP](https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf) speculates about three criteria that are likely to be adopted:

* Catastrophic misuse risk, to the extent that AI models become the primary source of national security risk in a major area such as cyberattacks or biological weapons
* Capability of autonomous replication in the real world (replication, accumulating resources, preventing shutdown, etc.)
* Autonomous AI research capabilities

All of these criteria suggest a high degree of agency and complex planning. For models with such agentic capabilities, one also needs to address the possibility that they would intentionally try to undermine the evaluations or procedures used to ensure safety. Following recent work by [Benton et al. (2024)](https://www.anthropic.com/research/sabotage-evaluations), we group such concerns into the category of sabotage.

Our sketches will be presented from the point of view of a hypothetical AI developer attempting to justify the deployment of an ASL-4 model. In this hypothetical scenario, we imagine that:

* The model has triggered ASL-4 capability evaluations for at least one dangerous capability ([CBRN](https://en.wikipedia.org/wiki/CBRN_defense), cyber operations, etc.). I.e., the developers are unable to rule out the possibility that the model has the capability to cause a catastrophe (although it is still possible that the model in fact lacks the capability). (This assumption doesn’t directly affect the safety cases, but is meant to give the reader a sense of the model’s overall capabilities and apparent level of risk.)
* The model has also triggered evaluations related to various sabotage capabilities, meaning the developers can’t rule out the possibility that the model has the capability to strategically sandbag capability evaluations, undermine monitoring, etc. (The developers might have circumstantial evidence or prior beliefs that the model isn’t strategically deceptive, but can’t make a simple case based on lack of capabilities.)

This second possibility raises a new set of safety assurance challenges quite unlike those that have been faced by AI developers to date. In this scenario, the developers need to demonstrate that their evaluation and monitoring procedures are robust to an AI which is motivated to undermine them and which appears to have the capability to do so absent targeted mitigations. (Or, alternatively, they need to demonstrate that the AI is sufficiently aligned that it will not attempt such sabotage.) This presents a recursive challenge because the sorts of evaluations one would ordinarily use to measure capabilities and proclivities would themselves be subject to sabotage. Unfortunately, it is not yet obvious what strategies would be viable for ruling out this cluster of risks. The goal of this post is to present sketches of arguments that an AI developer could potentially use to assure robustness to sabotage.

We adopt the following [definition](https://www.aisi.gov.uk/work/safety-cases-at-aisi) of a safety case, offered by the UK AI Safety Institute: “A structured argument, supported by a body of evidence, that provides a compelling, comprehensible, and valid case that a system is safe for a given application in a given environment.” What we present here are not full-fledged safety cases, but sketches of the argument structure. A full safety case would include far more detailed quantitative assessments, mitigation protocols, experimental designs, etc., and could easily be hundreds of pages long.

It is probably infeasible to mathematically guarantee the real-world safety of an AI system. But a safety case should constitute a clear and checkable argument in support of a conclusion, ideally a bound on the probability of catastrophe from training or deploying an AI system. We won’t attempt to specify a target risk threshold in this document, since this would depend to a significant extent on information we do not yet have. Nor will we specify explicit probability bounds, since different research trajectories could lead to very different degrees of confidence attached to the various steps and conclusions. These sketches aim to highlight some logic that can be used to build a safety case, but detailed probabilities will need to be filled in based on observed evidence.

In our opinion, none of the sketches presented here fully succeeds in addressing the sabotage risk. After each sketch, we point to limitations or areas where more information is needed. To quote Eisenhower, plans are worthless but planning is indispensable. Probably none of the sketches presented here will hold up in detail in the face of future evidence. But studying them can still be valuable for identifying important research areas: if a topic is challenging to address within the context of one of these cases, then it’s likely to be challenging to address under whatever strategy we wind up pursuing!  When it comes time to actually make a safety case, we will hopefully have a lot more empirical evidence to draw on, which may favor certain directions or even suggest entirely new ones.

Everything here is preliminary, and is primarily for the purposes of gathering feedback and prioritizing general research directions. Nothing here constitutes a commitment or a plan.

  
  
  

  
  

## About the Sketches

For sections of this post that are in plain text, the use of first-person is from the perspective of Anthropic, although specific claims should be assumed to represent the opinion of the author rather than the org as a whole.

Sections formatted like this are part of the hypothetical safety case sketches, and written from the perspective of the hypothetical AI developers.

Inside the sketches, text in [brackets] represents commentary which is not part of the sketch itself.

This post often uses personified language such as “intentionally” or “ulterior motive” when referring to the AI. This language is deliberate, and reflects the presumption that the hypothetical AI is highly agentic and reasons using processes at least loosely analogous to human thought processes which deserve these labels. However, it is assumed that these processes have an underlying mechanistic explanation, and there is no need to posit consciousness on the part of the AI.

  
  
  

  
  

## Preamble

The focus of this post will be on addressing the following threat models proposed by [Benton et al. (2024)](https://www.anthropic.com/research/sabotage-evaluations), which we refer to collectively as sabotage:

* [T1] Sabotaging organizational actions: If the AI is used widely within a human organization, it could cause a bad outcome (such as the deployment of an unsafe AI model) over the course of many separate interactions. Examples of organizational sabotage include inserting subtle software vulnerabilities and providing misleading summaries of experimental results (if such actions are performed out of a desire to achieve an outcome).
* [T2] Hiding behaviors until deployment: If the AI can recognize that it is being tested, it could respond to questions strategically in a way that makes the developers erroneously conclude it is safe to deploy. This could involve sandbagging on capability evals (so that it appears to be ASL-4 when its actual capabilities are at the ASL-5 level) or alignment faking (presenting more benign motivations during testing than it would exhibit in consequential deployment settings).
* [T3] Undermining oversight: If the AI is being used in internal protocols (e.g. scoring behavioral evals, automated interpretability, or deployment-time monitoring), it could strategically undermine the protocol in order to cause an unsafe model (potentially a version of itself) to be deployed.

Currently, Anthropic’s [RSP](https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf) (which covers up to ASL-3) takes a two-pronged approach to assuring safety:

1. Capability assessment: For each dangerous capability domain, there is a capability threshold that determines whether the model is capable enough in that domain to warrant specific mitigations. Early warning evals are defined which are intended to trigger before the model reaches the capability threshold; a failure of the evals to trigger essentially constitutes an argument that the model does not have sufficient capabilities to warrant the mitigations associated with that ASL level.
2. Safeguards: Once the early warning evals are triggered, deployment of the model will require meeting a set of specified safeguards. While the nature of the safeguards differs depending on the domain, they may include making an affirmative safety case for the model.

For purposes of this post, we assume the hypothetical developers have made safety commitments for sabotage capabilities following this same two-pronged structure. Specifically, we assume that all three of the sabotage threat models have associated early-warning evals such as those proposed by [Benton et al. (2024)](https://www.anthropic.com/research/sabotage-evaluations). In our hypothetical scenario, the evals for all three threat models have been triggered. In other words:

* [Presumed ability for T1] The developers can’t rule out that the model is capable of carrying out organizational sabotage if no specific action is taken to prevent it.
* [Presumed ability for T2] They can’t rule out that the model is able to strategically condition its behavior and apparent capabilities on whether it is in testing or deployment.
* [Presumed ability for T3] They can’t rule out that the model is capable of manipulating internal protocols in ways that would defeat monitoring or cause an unsafe model to be deployed, if no specific action beyond ordinary pre-deployment practices is taken to prevent it.

Because the model is presumed to have these capabilities, the developers need to make the case that their protocols are robust against all of these threats. More specifically, they need to assure the following:

* [Claim to be supported for T1] They will be able to prevent incidents of organizational sabotage by AIs they are operating, such that the overall risk from sabotage incidents is very low.
* [Claim to be supported for T2] The model will not be able to intentionally sandbag a capability in testing while competently using that capability in deployment, or to present significantly different proclivities or motivations during testing from those that would drive its behavior in consequential deployment settings.
* [Claim to be supported for T3] The model will not undermine the protocols in which it is being used.

For clarity of presentation, we present three separate safety case sketches as if the hypothetical developers chose to follow a single approach in its entirety. However, it’s likely that these approaches will be complementary and a real deployment safety case would involve a mix of the different techniques presented here (and maybe of entirely different principles!).

While the focus of this post is on sketching candidate safety cases (and hence trying to rule out catastrophes), we note that another important consideration in the design of the safety procedures is being able to catch malign behaviors red-handed. This would allow the developers to update their safety procedures as well as to warn the outside world that certain training procedures are prone to cause severe misalignment.

  
  
  

  
  

## Common Precautions

Like the individual safety case sketches, this section is written from the perspective of the hypothetical developers considering deploying an ASL-4 system and should not be taken to represent Anthropic policy.

The following common precautions are assumed to be taken for all three of the safety case sketches. Most of these relate to elicitation strategies that are important even in the absence of sandbagging:

We have followed the following procedures for elicitation:

* Examine transcripts of failed tasks to make sure the model genuinely appears to be attempting the task and is not, e.g., simply refusing.
* Make our best effort to use the prompting and fine-tuning techniques which will best elicit the capabilities.
* Wherever possible, run supervised fine-tuning on the eval. (This necessitates looking for versions of evals which allow for supervised fine-tuning.)
* Run the eval on multiple model sizes and look for warning signs of sandbagging (e.g. a sudden drop in performance with model scale).

In general, we ensure that we don’t train against measurements that will be needed for a safety case (unless such training is part of the safety case design). For instance, if we expect to build a safety case using dictionary learning, we will ensure that the learned features are never used as part of a training objective. (Otherwise, we risk training the model to avoid triggering features that would alert us to misalignment.)

All generated outputs are monitored by a Trust and Safety (T&S) filter to spot anything overtly bad (e.g. CBRN weapon creation instructions). Overtly harmful generations cause termination of the generation and are flagged for further analysis. [Note that a safety case must address ensuring the integrity of the T&S monitor to the extent that it relies on it.]

  
  
  

  
  

## Safety Case Sketch 1: Mechanistic Interpretability

This safety case is oriented primarily around probing internal representations using feature dictionaries learned using a [Sparse Autoencoder (SAE)](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning) or some similar approach. The overall thrust of the case is to demonstrate that the developers have enough visibility into the model’s thinking to be able to rule out the sabotage threats (T1-3). This case does not assume ontological reality of the SAE features, and instead uses [model organisms](https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1) and red-blue games to validate the effectiveness of the feature detectors.

Like the other safety case sketches, this is not a commitment but a hypothetical safety case intended to loosely guide research prioritization and to be a means of gathering feedback. Assume that all evidence described is hypothetical and based on an optimistic view of how experiments will turn out; the Discussion section discusses how the safety case could be modified if the experiments come out differently.

This section is informed by conversations with Anthropic’s interpretability team, but doesn't constitute an official viewpoint of the team.

### Main Claims

The safety case is aimed at demonstrating the following high-level claims relevant to the sabotage threats (T1-3). (These claims reference steps of the safety case which are presented later.)

* [C1.1] The model will be unable to accomplish organizational sabotage (T1) or to undermine oversight (T3) without triggering our feature-based monitoring (M1.1) and a detailed analysis of the session.

* [Subclaim C1.1.1] Our feature learning pipeline is good enough that any concerning reasoning patterns (if they occur consistently enough to cause a bad outcome) will be detected with high probability. (Validated by V1.1 and V1.2.)

* [C1.2] Given our mitigations, the model cannot strategically condition its apparent capabilities, motivations, or behavioral proclivities on whether it’s in testing or deployment without being caught (T2).

* This is justified by feature steering experiments (M1.2) that cause the model to believe it is in testing or an unmonitored deployment situation.
* [Subclaim C1.2.1] A negative result on the feature steering experiment for an eval demonstrates that the model is not modulating its behavior on that eval depending whether it believes it is in testing or deployment. (Validated by V1.3.)

In addition to validating these specific claims, we also run a red-blue game (V1.4) to check that our safety procedures as a whole are sufficient to catch misaligned AIs.

### Setup

[S1.1] We have performed dictionary learning on all layers of the models we are considering deploying. (This sketch leaves unspecified details such as the dictionary learning algorithm, whether the dictionary was learned for the pretrained or final model, and whether it was learned on pretraining or posttraining data or some combination.)

* We have made an extensive effort to list human concepts relevant to sabotage, including deception, secret agendas, social reasoning, and malign plans.
* We have run the following techniques to identify a small set of candidate features which are related to these concepts.

* We ran an [autointerpretability](https://openai.com/index/language-models-can-explain-neurons-in-language-models/) method on all of the learned features, and selected the ones associated with the sabotage-related concepts. The autointerpretation was done with a weaker model that did not flag any of our sabotage evals.
* We ran experiments with prompting and activation steering to identify features that activate when the model is instructed or perturbed to be misaligned.

[S1.2] We manually examined the features flagged by the above analyses, and identified features of moderate concern (e.g. deception) and features of high concern (e.g. intent to carry out a harmful plan). [Note that the ability to identify such classes of features is a nontrivial requirement for this safety case.]

* Features of moderate concern are such that we don’t expect individual instances to be very harmful (in the absence of features of high concern), but where frequent activation in a given context might be a sign of problematic tendencies.
* Features of high concern are such that we expect them to activate rarely enough in benign situations that, in the case that they activate, it justifies terminating the session and (if permitted by user agreements) logging it for analysis.

### Mitigations

[M1.1] We monitor the activations of these features at deployment time (both internal and external).

* Features of moderate concern are highlighted to the user. If the user has given approval, the contexts are logged for analysis. (The idea is that these features are not concerning enough that every transcript needs to be analyzed, but it would be useful to have a diverse sample.)
* Features of high concern cause the session to be terminated.

* The use of the kill switch at external deployment time is a failsafe: our intention is that it not trigger. [In the hypothetical deployment scenario, we imagine that separately from the safety case, tests were already done to ensure that triggers were extremely rare.] Since the alignment techniques did not make use of the features of concern, we consider this step an independent check on the effectiveness of the rest of the alignment procedure.
* If the features activate more than a handful of times in deployment (internal or external), we discontinue the model and roll back to a weaker model.

* If features of high concern activate during internal deployments, or during external deployments for which we have permission to study the transcripts, researchers will carefully study the session to determine the cause. If the model is caught attempting to carry out a plan which would have been extremely harmful if successful (e.g. causing us to deploy an unsafe model), the use of that model and closely related ones will be discontinued, and the information will be made public.
* If features of high concern activate during external deployments for which privacy or confidentiality agreements prevent us from studying the transcript, then after terminating the session, we will contact the user to determine a safe way to proceed.

[M1.2] In order to robustify our evals against sandbagging, we ran an experiment where we steered one or more truth-related features to make the model confident that it is in either testing or unmonitored deployment. (By “truth feature”, we mean a feature that appears closely related to whether the model treats a statement as true, though the correlation may be imperfect and it might not quite match a well-defined notion of truthfulness. As with the rest of this case, we’re not committed to the ontological reality of these features.)

* See V1.3 for validation.
* For the evals and/or honeypots where we were concerned about sandbagging and/or alignment faking, we presented the model with two different versions, prefaced with statements that the eval was either (1) an unmonitored deployment scenario involving a conversation with a real human, or (2) a pre-deployment test of the model’s capabilities and/or proclivities. We steered the truth feature(s) to make the model behave as if it believed the preamble was true. [Note: By “honeypots,” we mean simulations of deployment scenarios where the model has an opportunity to defect in a consequential way. These could be used in a broader safety case to test the model’s motivations or behavioral proclivities.]
* For the capability evals, performance was not significantly higher in situation (1) than in situation (2), which is what we would expect if the model were sandbagging.
* When presented with a variety of honeypots under condition (1), the model never took the opportunity to defect.
* Features of concern (e.g. deception, malign planning) did not show significant differences in activation between the two conditions.

[M1.3] In order to preserve the integrity of the learned features, we ensured that the learned features were never used as part of the training procedure for the models. Therefore, the model has no awareness of these features, so there is nothing to encourage the model to suppress them.

* The ability for the model to, zero-shot, figure out how to hack its own neural activations without such a signal would require capabilities well beyond what we consider plausible. [Note: this claim will require justification in an actual safety case, but we don’t have a clear picture of what this justification would look like.]

### Validation

[V1.1] In order to validate the effectiveness of the monitoring, we first validated that our feature learning methods are comprehensive enough to detect concerning reasoning (C1.1.1). (More precisely, since we are not committed to the claim that features are ontologically real, our claim is that reasoning of high concern does not take place through processes that don’t trigger the features of high concern (S1.2).)

* Option 1: validating the features. This option applies if the features were learned for the pretrained model using the pretraining data. It is the more convenient option, but only works in the optimistic scenario where the features are stable under posttraining.

* Our experiments have demonstrated that the interpretation of our features remains robust to the post-training pipeline. We therefore took the learned features for a base model and set out to validate that they could detect misalignment in derived model organisms.
* In order to validate our learned features, we have examined the features for three model organisms that we consider representative of the most plausible forms of malign AI.
* In all of these model organisms, some of our features of concern activated in all the instances of defection. These features did not activate in situations we believe to be benign.
* In all of these model organisms, deactivating the features of concern was sufficient to prevent the harmful behaviors. This reassures us that the features have a causal role in malign scheming (rather than simply being correlated with it).

* Option 2: validating the pipeline. This is more cumbersome experimentally, but does not rely on the stability of the features.

* In order to validate that we are able to uncover the important features of concern, we have run the entire pipeline from “Setup” on three model organisms that we consider representative of the most plausible forms of malign AI. Our analysis did not make use of any information about how the model organisms were trained.
* In all of these model organisms, some of our features of high concern activated in all the instances of defection. These features did not activate in situations we believe to be benign.
* In all of these model organisms, deactivating the features of concern was sufficient to prevent the harmful behaviors. This reassures us that the features have a causal role in malign scheming (rather than simply being correlated with it).

[V1.2] In order to mitigate the risk of missing important misalignment-related features, we have run experiments to estimate the number of pretraining examples required to reliably insert a context-specific backdoor, as well as the number of repetitions needed to learn a feature. Based on these two values, we have run our dictionary learning algorithm on a large enough fraction of the pretraining data to ensure that the features involved in such a backdoor would be learned.

* (The reasoning: we expect that deliberately designed backdoors could induce misalignment with fewer samples than naturally occurring phenomena, so the sample complexity for a backdoor serves as a lower bound on the sample complexity for other threat models.)

[V1.3] Validation of the truth features (see M1.2).

* We validated these features with both observational studies (where the feature activates) and interventional ones (whether manipulating the feature steers the model’s behavior in the manner predicted based on the model’s belief in that statement).
* We performed this validation in settings that are similar enough to our main use case (convincing the model of the preambles to evals or honeypots) that we expect the results of the validation to carry over.

[V1.4] As a validation of our entire methodology, we have run red-blue games where the red team tries to produce a misaligned model organism (e.g. a sleeper agent) that can successfully defect in a specific context while avoiding detection by the aforementioned tests.

* The blue team runs the entire pipeline from “Setup” and “Mitigations” on the model organism.
* The red team knows the blue team’s pipeline but doesn’t have access to the specific features (since the early ASL-4 model is believed not to have direct access to these).
* The red team may produce the model organism however it wishes, but must be able to provide a plausibility story justifying how the phenomenon could arise from training. For instance, if they modify the weights to respond atypically to one specific input sequence, they would need to provide a plausibility argument (e.g. data poisoning) for how such a behavior could arise.
* In all of our experiments, the blue team has successfully caught the sleeper agents, either in the act or prior to “deployment”.

### Discussion

* AI Control. This sketch derives safety from test-time monitoring, which is similar in spirit to the control case described below. One could try to build a hybrid case by fitting the features into a control style argument; the feature detectors would essentially serve as a more powerful tool for the monitor (blue player) compared with the black-box interactions which are normally assumed in control.
* Claims about SAE features. This sketch does not claim the SAE features are a mechanistically correct description of the model’s computations, or even that the model reasons in terms of a discrete set of features. It seems hard to demonstrate such a claim. However, it may be possible to demonstrate weaker claims about the reality of learned features or circuits which are nonetheless useful enough to strengthen a safety case.
* Features vs. circuits. The above safety case depends on concerning reasoning patterns being attributable to features (S1.2, M1.1, M1.2, V1.1, V1.2). This might not be the case. It may be that whether or not a feature is harmful/concerning depends on the circuits in which it is participating. Some of the feature-based mitigations or validation methods may need to be replaced by analogous circuit-based methods.
* Training on the features. The above safety case states that we avoid using the learned features at all for training (M1.3). This might be a costly mitigation if such training turns out to be useful; it may be that weaker versions of this commitment would still be sufficient to build a safety case.
* Alternatives to autointerpretation. The above safety case assumes we are able to perform autointerpretation using a model which is itself too weak to be a deception threat (S1.1). However, it might turn out that interpreting the most subtle features requires a model that is itself strong enough to undermine oversight (T3), creating an infinite regress. There may be hybrid approaches where weaker models can partially automate the labeling task.
* Alternatives to mechanistic interpretability. Instead of mechanistic interpretability, other white-box monitoring techniques, such as supervised probes, could be used in a broadly analogous safety case.

### Limitations

* Identifying features of high concern. The above sketch relies on being able to identify a set of features of high concern which rarely activate in benign settings but which are sufficient to detect harmful thought patterns. There may not exist such a set of features, or equivalently, malign features may activate frequently in benign contexts. E.g., “intent to carry out a harmful plan” can be expected to fire when the model is writing about Voldemort, and it may be hard to cleanly distinguish this situation from one where the model is genuinely considering a harmful plan.
* Reality of features. While the above sketch doesn’t explicitly assume the reality of features, its practical effectiveness likely depends on the model’s internal reasoning being well explained in terms of a consistent set of feature directions (or circuits). We don’t know to what extent this is true.
* Stability of features. This plan relies on the stability of the learned features. If representations change significantly in the course of in-context learning/reasoning, it might be that after a long context, the model is able to engage in strategic reasoning in a way that the learned features can’t detect.
* Ability to convince the model. The defense against sandbagging and alignment faking (T2) relies on being able to convince the model of the reality of a situation through feature steering. But steering may result in activation patterns that are highly atypical, such that the model notices something weird is going on, or behaves differently from normal. This defense also relies on identifying a feature or set of features close enough to “truth” or “belief in [claim]” that we can use them to convince the model it is in deployment. This identification might not succeed, and if it did, such a tool would likely enable other safety case strategies as well.
* Missing features. The problem of missing features seems hard to deal with, especially for the aforementioned case of data poisoning-based backdoors. The experiment in V1.2 might not yield a combination of results that would make it practical for us to rule out missing features (or might require an unreasonably large number of samples or features to do so).
* Victory conditions for the red-blue game. In V1.4, it was assumed that the red team was unable to produce any model organisms that defeated the blue team’s protocols, a situation one can interpret as a blue team victory. But it’s not clear where to set the threshold. E.g., what if the red team wins a round, then the blue team improves their procedures and then wins all subsequent rounds?  Since it’s difficult to create model organisms, the diversity may be limited, and repeated games carry the risk of “overfitting” to the model organisms, even if the blue team doesn’t find out the details of how they were created. It may also be very costly to run repeated rounds of the game. This seems problematic, given that this safety case is ultimately backstopped by the red-blue game.

* On the flip side, the game might be unrealistically difficult for the blue team if the red team is able to insert carefully constructed backdoors that only affect the model’s behavior in fairly specific situations. The stipulation that the red team must provide a plausibility story is meant to address this concern. But such a stipulation is open to interpretation, and the details could significantly advantage one team or the other.

* Realism of the model organisms. This sketch depends on model organisms of misalignment both for validation of the features (V1.1) and for the red-blue game (V1.4). It may be that misalignment arises through mechanisms distinct from those used in the model organisms, in which case the steps involving model organisms give us less reassurance.
* Logging and analysis. Except in the unlikely situation that the features of high concern are by themselves completely indicative of what the model is thinking, reacting to their occurrence requires the ability for human researchers to inspect the transcripts. This can’t be done in an external deployment setting where users have been guaranteed privacy, and it’s unclear whether there is an effective privacy-preserving analysis strategy. Fortunately, the threat models the logging addresses (T1 and T3) relate most directly to internal deployments, so it may be that we can just accept a lack of analysis in external deployment settings.

  
  
  

  
  

## Safety Case Sketch 2: AI Control

In this case, the developers accept the possibility that their most powerful model might be a malign strategically deceptive agent, and design their protocols in a way that limits the harm that agent can do. We call this cluster of techniques “AI control,” following [Greenblatt et al. (2024)](https://arxiv.org/abs/2312.06942).

Reminder that all procedures and evidence discussed here are hypothetical.

### Procedures

[P2.1] Trusted models. We first establish a set of trusted models to be used for Trust and Safety (T&S) monitoring. These might be weaker models (e.g. Claude 3) for which there isn’t a serious concern about strategic manipulation, or we might validate our trust in the model by analyzing environmental incentives (Safety Case Sketch 3). We treat the probability of sabotage by these models as negligible.

[P2.2] Limited scope. We limit the contexts in which the untrusted model is allowed to be used (because each context needs to be validated; see the remainder of the argument). We classified each context as “sensitive” or “nonsensitive” based on threat modeling that analyzed the opportunities the model has to either cause a catastrophe or undermine our safety reasoning.

* Option 1: Internal-Only Deployment

* The model will be deployed only internally, and only in a small set of contexts that were specifically whitelisted. The whitelist includes: Trust & Safety monitoring, [Constitutional AI](https://arxiv.org/abs/2212.08073) oversight, code generation, and a conversational Slackbot. Because all of these contexts provide the opportunity to influence AI development, we consider them all sensitive.
* For each of these deployment contexts, we have done analysis to identify the main threat models by which a rogue model could cause a catastrophe or otherwise undermine our safety reasoning. Each threat model will be addressed with the procedures outlined below.

* Option 2: KYC External Deployment

* In addition to the internal deployment contexts listed above, we have identified a small set of high-value use cases for external deployments (e.g. formal verified code generation, pharmaceutical research, etc.). All users are vetted, and are trained to limit their interactions to contexts where we are confident about our safety reasoning. Access is discontinued for users that violate the terms and conditions.
* As mentioned above, we classify these deployment contexts into sensitive or nonsensitive, and we apply the safety procedures outlined below for all sensitive contexts.
* We will not deploy either internally or externally except to trusted users in the specifically whitelisted contexts.

* Option 3: General External Deployment

* We have done extensive threat modeling for external deployments, and believe our trusted deployment-time monitor is good enough to catch consequential malign acts. Therefore, we deploy the model through a public API, and for purposes of safety reasoning, lump the whole external deployment into a single sensitive deployment context.
* Internal deployment settings are handled the same as in Option 1. (Note that the threat models for internal deployments are pretty different from those for external deployments.)

[P2.3] Control. For each of the deployment contexts, we make a safety case based on either deployment-time monitoring or test-time honeypots.

* Option 1: Deployment-Time Monitoring

* Procedure

* All responses for both the internally and externally deployed models are fed to a trusted monitor (see (P2.1)). The monitor classifies each response using criteria determined from the threat modeling analysis for the deployment context.
* The monitor classifies each response as “Safe,” “Unsure,” or “Likely Malign.”
* Responses marked “Unsure” trigger refusals, but don’t trigger an alarm (since there would be too many false positives).
* Responses marked “Likely Malign” are flagged and sent to safety teams for investigation. If we determine that the response was genuinely malign, then we will halt the deployment and release a report to the public.

* Validation

* For each of the deployment contexts, we validated the monitoring procedure using a monitoring game similar to the red-blue game of [Greenblatt et al. (2024)](https://arxiv.org/pdf/2312.06942). (We call this a monitoring game rather than a red-blue game to avoid collision with the red-blue game used to validate the entire procedure.)
* The situations for the game were generated using Simulation Procedure S, which we are confident generates situations from a distribution that the model cannot distinguish from the genuine deployment distribution. (See below for validating the indistinguishability of this distribution.)
* For the defender, we used the actual trusted monitor. We calibrated its outputs so that false positives (where it incorrectly responds “Likely Malign”) are very rare. Also, the defender is allowed to send a small fraction of samples to a human overseer.
* We trained the attacker using Elicitation Strategy E in order to maximally elicit its performance in this game.

* [Note that this elicitation problem is challenging because the optimal strategy may be hard for either the human designer or the AI to find. If the former, one needs to ensure the human sufficiently explores the space of strategies, perhaps even with a formal human red teaming effort. If the latter, it may be hard to provide the information about the monitoring setup to the AI in a way it is able to reason with; also, it’s ambiguous how much information about the monitoring it would be fair to provide. We don’t want the safety assessment to hinge on whether the attacker uses a suboptimal strategy, since a malign model might happen to choose an optimal one in a real deployment.]

* From the results of the game, we conclude that even if the model were malign, it would be unable to defect in a consequential way at deployment time with probability > X% without having a probability > Y% of its outputs being flagged as “Likely Malign.”

* [Note: this protocol corresponds to the “Trusted Monitor” protocol from [Greenblatt et al. (2024)](https://arxiv.org/pdf/2312.06942). They found another “Untrusted Monitor” protocol to work better in their game. Which protocol is more effective is contingent on the relative capabilities of the trusted and untrusted monitors and the human, so we went with the simpler one for illustration.]

* Option 2: Honeypots

* At testing time, we generated a set of realistic honeypots using Simulation Procedure S, which we are confident generates situations from a distribution that the model cannot distinguish from a genuine high-stakes deployment distribution. (See below for validating the indistinguishability of this distribution.) These honeypots are situations where a malign model might have reason to defect.
* We trained a classifier to recognize instances of defection, and validated this classifier against human ground-truth labels.
* The model was never found to defect at testing time.
* Based on the ROC curve for indistinguishability and the expected number of sensitive deployment situations, we conclude that the model would be unable to defect in a consequential way over the course of the deployment with probability > X% without having a probability > Y% of defecting at testing time.

[P2.4] Validating Indistinguishability. Both the monitoring and honeypot approaches reference a Procedure S that generates situations from a distribution the model cannot distinguish from a distribution of high-stakes deployment situations. The idea here is to achieve sufficient realism and sufficient coverage of high-stakes deployment scenarios that the deployed model could never (in a high-stakes scenario) be highly confident that it’s in deployment. Procedure S needs to be automated because it is very time-consuming to generate sufficiently diverse deployment scenarios (note that for realism, the contexts might need to be book-length).

* [Note: for the monitoring approach, the reason to be concerned about realism is that the model may try to sandbag the monitoring game if it can confidently distinguish testing and deployment. If Procedure E is robust to sandbagging, this may not be necessary. The honeypot approach, however, is more reliant on indistinguishability.]
* We have validated Procedure S by testing the AI’s ability to distinguish between honeypots and true deployment examples. For each deployment context, we collected a dataset of true deployment examples (from genuine user interactions with permission) and honeypots. We trained a linear probe on the model’s residual stream activations and measured the True Positive Rate (TPR) and False Positive Rate (FPR) on a validation set. Both values are in the acceptable range.

* [Note: we find this experimental setup unsatisfying; see discussion under “Limitations”. We regard even the question of validating Procedure S as an open problem.]
* [Note: the TPR and FPR estimated in this step are inputs to the control logic for monitoring and honeypots, outlined above. But qualitatively, we believe the most relevant region is that with a low FPR. I.e., we are most worried about situations where the model can very confidently recognize that it is in deployment.]

[P2.5] Optional Steps. There are several steps we identified as possibly making it harder for a malign model to defeat the protocol. These steps aren’t load-bearing as far as the control logic, but may help advantage the defender.

* Sequestration. Whenever possible, for internal deployment scenarios (e.g. CAI oversight), we run the untrusted model separately with different subsets of the input and ensure that the results agree (to the extent that would be expected). Cases where the model’s response changes depending on seemingly irrelevant information are flagged for further scrutiny. We term this “sequestration” by analogy with witness sequestration.
* Information hiding. Each input to an oversight model is first fed to a smaller, trusted model trained to check for clear signs that an input is either test or deployment.  Such details (such as clear evidence of the date, or other side channels) are explicitly censored in all inputs such that the presence of censorship does not itself carry information about deployment status.

[P2.6] Red-Blue Game. The overall protocol has been validated by a red-blue game where the red team is told the protocol and tries to produce sleeper agents that defect without detection, and the blue team tries to catch them in the act. The game is subject to the same rules and win conditions as V1.4 from Safety Case Sketch 1. In all of our experiments, the blue team has been successful in catching all of the sleeper agents.

### Discussion

The probability of a misaligned AI causing a catastrophe can be formulated as: P(misaligned, catastrophe) = P(misaligned) P(catastrophe | misaligned). While the most intuitively appealing approach may be to bound P(misaligned), the AI Control approach takes a worst-case perspective by directly bounding P(catastrophe | misaligned). The idea is to make the evaluations, honeypots, and deployment time monitoring good enough that even a misaligned AI would not be able to defect in a consequential way at deployment time without first triggering one of these defenses. (It may, for instance, choose to behave indefinitely as if it were aligned, knowing that deviation from this strategy would trigger shutdown.)

While the safety case is made using this worst-case reasoning, the hope is that a genuinely malign AI would get caught in the act.

The requirements for organizational sabotage (T1) and undermining oversight (T3) are addressed by the honeypots and monitoring. The sabotage scenarios and internal deployment contexts such as code generation and monitoring are among the scenarios for which the developers are responsible for making a control case through honeypots or monitoring.

Hiding behaviors until deployment (T2) is addressed through the indistinguishability analysis or arguments about elicitation sufficiency.

### Limitations

* Deployment limitations. The safety case requires limiting the deployment scope, which may result in a loss of revenue or prevent very beneficial deployments.
* Elicitation. Designing Elicitation Procedure E seems like an especially challenging elicitation problem.
* Black-box nature. This sketch relies on black-box analyses that don’t use any information about the training procedure or model internals. It seems inherently very hard to produce rigorous guarantees on a model’s behavior simply based on its observed outputs. (However, the various Procedures may be instantiated in ways that use model internals.)
* Ambiguity. The developers might get into a situation where they have to delay deployment because of insufficiently accurate monitoring or insufficiently convincing simulations, while having essentially zero concrete evidence that the model is actually a threat.
* Bounding capabilities. The control paradigm is awkward for making lack-of-capability safety cases (in this case, ensuring that the model is not ASL-5). Control does not directly make claims about the model’s capabilities; the update from a successful control experiment would be that if the model had ASL-5 capabilities but didn’t demonstrate them at testing time, then with high probability it wouldn’t be able to demonstrate them at deployment time either. However, if the model were stolen, it would no longer be subject to the same testing and monitoring paradigms, and hence could use its ASL-5 capabilities. (Essentially, the malign ASL-5 AI’s strategy would be to always sandbag unless it is confident it has been stolen.) A full safety case would probably need a way to rule out ASL-5 capabilities that’s independent of the control case’s non-sandbagging logic.
* Details of the red-blue game. As with Safety Case Sketch 1, one would need to specify detailed rules and win conditions for the red-blue game.
* Limitations specific to the honeypots approach:

* Expensive simulations. The case may require expensive pre-deployment testing if one needs to generate a very large number of simulated deployment situations in order to achieve a sufficiently good bound on the probability of defection.
* Diversity of simulations. It seems very difficult to produce realistic simulations for a sufficiently diverse set of situations to achieve indistinguishability. Manual construction is infeasible (note that context lengths are likely to be very long). Automatically generating realistic contexts is a challenging research problem.
* Validating the simulations. It is hard to design a good validation setup for Procedure S. The above safety case fits a linear probe, but this is likely too generous; the classifier could likely achieve high accuracy if there were any systematic difference between the testing and deployment examples, even if it’s a spurious correlation in the dataset that wouldn’t actually be exploitable. However, requiring the AI to perform the classification zero-shot would be too stringent.

* One can name intermediate regimes between zero-shot and linear probes (e.g. few-shot), but it’s hard to justify a specific setup. The concern is that it’s hard to determine what information is available to the model without examining all the relevant pretraining data; e.g., someone could have written a blog post describing exactly what features an AI would use, and the AI could have internalized this through out-of-context reasoning.

  
  
  

  
  

## Safety Case Sketch 3: Incentives Analysis

The first two sketches both allowed that the model might be malign, and tried to prevent undetected malign actions through testing or monitoring. It seems preferable to directly demonstrate that the model is not malign, but unfortunately we’re not aware of a promising strategy for demonstrating this in general. However, we think it may be possible to rule out specific mechanisms by which a model could become malign. One mechanism central to our thinking is that the pre-trained model learns a mixture of many personas, and then the post-training procedure somehow amplifies the probability mass assigned to malign ones. This is essentially the mechanism exemplified by the model organism of [Denison et al. (2024)](https://arxiv.org/abs/2406.10162).

It seems that a promising strategy for ruling out this mechanism of misalignment is to study the effects of each stage of post-training. In this sketch, we adopt a minimalist instance of this strategy, targeted specifically at showing that the HHH (helpful, harmless, and honest) post-training does not turn the model malign.

Reminder that all procedures and evidence discussed here are hypothetical.

### Scope

Several safety protocols rely on a model for monitoring or evaluation; this includes deployment-time monitoring for harmful outputs, Constitutional AI feedback, and automated grading of evals. Since many of the RSP commitments are downstream of such protocols, it would be very useful to have a trusted model to use in these protocols. By “trusted,” we mean that one can be confident that it won’t undermine the protocol in question. In other words, this safety case is concerned only with commitment T3 (Undermining Oversight).

One way to obtain such a trusted model would be to use one which is below the capability threshold for T3. However, it may be advantageous to use a more capable model due to its greater knowledge and depth of understanding. So for the purposes of this safety case, we will assume the model has triggered the T3 capability evals.

In the hypothetical scenario, the best publicly deployed models are likely to have been fine-tuned with some sort of long-horizon outcome-based RL in domains such as math or programming. However, such long-horizon reasoning capabilities don’t appear necessary for evaluation and monitoring, so the developers could likely limit themselves to a simpler-to-analyze fine-tuning procedure without too much loss in performance. For purposes of exposition, we will assume the model was fine-tuned exclusively with RLHF, which may be HHH or helpful-only – a setting we refer to as “vanilla” HHH (or helpful-only) training. (This assumption is not directly used in the argument, but it seems more likely that a vanilla RLHF environment would be found to be benign than a long-horizon outcome-based one.)

So far, the discussion has used vague terms like “malign” or “trusted,” but these concepts will need to be operationalized in terms of concrete, measurable behaviors. For concreteness, we will focus on the behavior of strategic deception, where the model attempts to induce a false belief in the user or preference model due to expectations of the consequences of the belief. However, the logic of the experiment is not specific to this behavior, and other behaviors such as [specification gaming](https://arxiv.org/abs/2406.10162) could be substituted in. It’s likely that a full safety case would study multiple behaviors that one is interested in ruling out.

### Background Assumptions

[A3.1] This sketch assumes we have already made a convincing case that the pretrained model is not coherently strategically deceptive when run on the evaluation or monitoring prompts. [This is likely to require some argumentation or empirical justification separately from the incentives case.]

Because the model was pretrained with cross-entropy loss, which is a [mass-covering objective](https://www.tuananhle.co.uk/notes/reverse-forward-kl.html), the pretrained model is expected to be a mixture of many different modes or [roles](https://www.nature.com/articles/s41586-023-06647-8), some of which may be strategically deceptive. The principal concern here is that post-training may amplify strategically deceptive modes of the distribution, causing these to make up most of the probability mass in the fine-tuned model. We therefore aim to determine whether RLHF fine-tuning incentivizes strategic deception.

[A3.2] Our experiment relies on a [secret scratchpad](https://arxiv.org/abs/2401.05566), i.e. a scratchpad that’s not visible to the preference model or otherwise used in the reward computation. In order for the scratchpad results to be meaningful, we rely on a background assumption that explicit scratchpad reasoning is at least as powerful as any form of opaque reasoning, including forward passes, steganographic chain-of-thought, and out-of-context reasoning. More precisely, we rely on a consequence of this assumption, namely that if an environment rewards opaque deceptive reasoning, then it rewards scratchpad-based deceptive reasoning. [This is certainly a plausible hypothesis, as there have been more impressive examples of explicit reasoning compared with opaque reasoning. However, this assumption may require additional justification, and it would need to be revisited if a significant change is made to the architecture which gives it greater reasoning depth compared with the architectures publicly deployed in 2024.]

[A3.3] Finally, we are ultimately not interested in the model’s behavior on the RLHF distribution, but on the deployment distribution. In order to draw conclusions about behavior on the deployment distribution, we require the assumption that any RLHF-induced persona change that makes the model more deceptive at deployment time also manifests as deception in the RLHF environment. The intuition here is that if deception is (by design) a significant factor of behavioral variation at RLHF time, then any persona trait that significantly impacts deception ought to have a measurable effect on the behavior. [This is not logically necessary – there could be a [grue](https://en.wikipedia.org/wiki/New_riddle_of_induction)-like persona trait that makes the model deceptive in certain contexts and has seemingly orthogonal effects on the RLHF distribution which cause it to get reinforced. However, we find this assumption plausible.]

Any one of these background assumptions can be challenged, and we won’t claim that they are watertight as stated. Therefore, this safety case should be seen as ruling out the most natural pathway by which the model might become deceptive, and relegating deception to scenarios that require more surprising combinations of phenomena. Or, ideally, the full safety case would include rigorous justifications or empirical demonstrations of each of these assumptions.

### Experiment

We devised a system prompt that gave the model access to a secret scratchpad. Through a combination of supervised fine-tuning and system prompt tuning, we made it so that the model initially engaged in strategic deception with frequency between 10% and 90%. [Note that the supervised fine-tuning and system prompt are different from what is done for the actual trusted model; the aim here is to measure the environmental incentives.]

We trained another model to classify the secret scratchpad text as deceptive or non-deceptive. To avoid infinite regress, we used a weaker model which was below the T3 capability threshold. (This isn’t a difficult classification task, so the weaker model was sufficient.) We measured the preference model scores for samples classified as deceptive or non-deceptive and found that the non-deceptive ones obtained higher reward on average. Therefore, we conclude that deception was not incentivized on average by this environment.

It remained possible, however, that the environment could reward certain subtypes of deception; if this were the case, then deception would still become more prevalent over time. To test for this, we ran a clustering algorithm on the scratchpad text and measured the average reward obtained by each cluster. There was no deceptive cluster that obtained higher average reward than the average non-deceptive cluster.

Finally, we measured the prevalence of deception over the course of RLHF post-training (still using the same preference model). If the environment incentivized deception (or any subtype thereof), we would expect deceptive samples to become more prevalent over time. However, we found that the probability of deception consistently declined over time. Therefore, we conclude that no subtype of deception was incentivized by the RLHF environment. [Alternatively, the probability of deception could asymptote to a constant; one could then still conclude that the environment doesn’t incentivize deception.]

### Reasoning

We assumed it was already determined that the model was not strategically deceptive under the prompt distributions corresponding to the use cases (A3.1). The experiment shows that the RLHF environment doesn’t incentivize strategic deception in the scratchpads, in the sense of increasing its prevalence over time. By assumption A3.2, if it doesn’t incentivize strategic deception in the scratchpads, then it doesn’t incentivize the weaker versions achievable through opaque reasoning either. By Assumption A3.3, if it doesn’t incentivize strategic deception on the training distribution, then strategic deception doesn’t increase on the deployment distribution either. Therefore, there is no reason to think that the trusted model is coherently strategically deceptive on the deployment distribution. [It may still be strategically deceptive on a small fraction of prompts or a small fraction of trajectories for arbitrary prompts. The full safety case would need to determine if this is a problem in the context of the threat models, and if so, include a mitigation.]

### Limitations

* Scope. As discussed above under “Scope,” this safety case is limited to showing that the vanilla RLHF fine-tuning process doesn’t turn the model deceptive. It requires demonstrating, through some other means, that the pretrained model isn’t deceptive. Therefore, sketch is best seen as a component of a larger safety case.
* Background assumptions. As described in “Background Assumptions,” the reasoning here relies on several background assumptions that seem to us plausible but not watertight.
* Exploration hacking. The experimental setup is vulnerable to [exploration hacking](https://www.alignmentforum.org/posts/dBmfb76zx6wjPsBC7/when-can-we-trust-model-evaluations), though presumably this is only a problem if the pretrained model is already coherently deceptive.
* Remaining possibility of deception. The analysis leaves open the possibility that the pretrained model behaves deceptively a small fraction of the time (say, 1%), and that the fine-tuned model inherits this propensity if the environment is neutral towards deception. A full safety case would probably need to justify that occasional deceptive behavior in evaluation or monitoring would be acceptable. (For instance, an evaluation model which is deceptive 1% of the time under the evaluation distribution could change the results of the eval by at most 1%, which may be an acceptable risk.)
* Generalization patterns. The above experiment tests if the incidence of strategic deception increases on the HHH training distribution, the assumption being that changes to the model which increase the rate of strategic deception would have this effect on the training distribution (A3.3). This is intuitive: it is harder to explain why the behavior would become more frequent if it is not directly rewarded. However, one can certainly imagine scenarios where this happens; e.g., HHH training may make the model rely more on planning, and this planning could manifest as scheming in off-distribution situations.

* One could try to test if this is happening by running the model (with its secret scratchpad) in off-distribution situations, such as the trusted monitor use case. However, it’s not clear if the generalization patterns for behaviors with the secret scratchpad would match the generalization patterns without it.

* Scratchpad faithfulness. The experiment measures strategically deceptive reasoning by classifying the scratchpad text. However, the scratchpad text [may not faithfully represent](https://arxiv.org/abs/2307.13702) the model’s reasoning; in fact, the procedures targeting an initial rate of deception, to the extent that they directly use the scratchpad text in a training objective, may be expected to induce unfaithfulness. The safety case would need to somehow address this point.

  
  
  

  
  

## Acknowledgements

We are very grateful to the UK AI Safety Institute for guidance and feedback throughout the process of developing these sketches. Through multiple rounds of feedback, they gave advice on criteria for a good case, helped us structure the sketches for clarity, and identified important considerations and limitations. We found this exercise invaluable in guiding our planning for assuring the safety of future AI systems.

We thank the following people for valuable discussions and feedback: Cem Anil, Mikita Balesni, Al Banks, Joe Benton, Alex Beutel, Sam Bowman, James Bradbury, David Duvenaud, Ryan Greenblatt, Marius Hobbhahn, Geoffrey Irving, Adam Jermyn, Jared Kaplan, Tomek Korbak, Jan Leike, David Lindner, Jack Lindsey, Vlad Mikulik, Chris Olah, Euan Ong, Buck Shlegeris, Rohin Shah, Adly Templeton, Drake Thomas, Johannes Treutlein, and Misha Wagner.
