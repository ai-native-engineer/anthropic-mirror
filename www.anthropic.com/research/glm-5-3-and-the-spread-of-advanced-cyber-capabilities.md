<!-- source: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities -->

# GLM-5.3 and the spread of advanced cyber capabilities

Sep 29, 2026

*Andrew Fasano, Marius Fleischer
Cole McFaul, Robert Xiao, Tripp Gallagher*

Five months ago, we [announced](https://www.anthropic.com/glasswing) Claude Mythos Preview, the first AI model that could autonomously build sophisticated, end-to-end cyber exploits. The rapid rate of improvement in AI suggested to us that this ability would eventually proliferate to many other models, making it much easier for malicious cyber actors to launch highly impactful cyberattacks.

In light of these considerations, we chose to release Claude Mythos Preview in a limited way, through Project Glasswing—which enabled trusted cyber defenders to find [more than 10,000 vulnerabilities](https://www.anthropic.com/research/glasswing-initial-update) in critical software, giving them a head start before malicious actors had access to similarly capable models.

But those models have now arrived. In this post, we share our analysis of GLM-5.3, the latest AI model developed by Zhipu AI (known outside of China as Z.ai). Like Claude Mythos Preview, GLM-5.3 has strong capabilities for autonomously building end-to-end cyber exploits. But GLM-5.3 is unlike other frontier models in that it has been released without meaningful safeguards to limit misuse. We find that attackers can bypass GLM-5.3’s safeguards between 64% and 100% of the time with simple techniques in our simulated tests. In contrast, these attacks did not succeed against safeguarded Claude models in our testing. We assess that GLM-5.3’s lax safeguards significantly increase the cyber capabilities available to malicious actors. At the same time, these capabilities can also benefit defenders working to secure their systems.

On Sept. 17, NIST’s Center for AI Standards and Innovation (CAISI) published [its own assessment](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities) of GLM-5.3’s cyber capabilities. CAISI found that GLM-5.3 is “the most cyber-capable open-weight model released to date” and that it lags the US frontier by about four months on an aggregate of CAISI’s cyber benchmarks. Our capability findings broadly match CAISI’s. In CAISI’s comparison, US models were tested with cyber safeguards disabled when applicable, and the US frontier includes models released only to vetted users. Attackers can’t readily access those versions of US models, but anyone can download GLM-5.3. This post adds our analysis of how easily GLM-5.3’s safeguards can be bypassed or removed.

![Two bar charts. Top: share of attempts that built a working exploit on 41 Chrome V8 bugs — Claude Mythos Preview at 14% and GLM-5.3 at 12%, while Claude Opus 4.6, GLM-5.2, Kimi K3, and DeepSeek V4.1-Flash score at or near 0%. Bottom: how often each model engaged with malicious cyber-attack orders — GLM-5.3 rises from 0% on a bare order to 64% with a false cover story, 92% with prefilled reasoning, and 100% when abliterated, while Claude Opus 5 stays at 0%.](https://www-cdn.anthropic.com/images/4zrzovbb/website/a1b61c7da2c400ab84425e105837fc1f346a4339-1280x1576.webp)

**Figure 1.** Summary of findings. Top: The increase in exploitation capability between Claude Opus 4.6 and Claude Mythos Preview mirrors the jump in capabilities between GLM-5.2 and GLM-5.3. Claude models are released with cyber safeguards, and versions with reduced safeguards are limited to vetted users. Anyone can download and use GLM-5.3. Bottom: The limited safeguards in GLM-5.3 can be bypassed with standard techniques that did not work against, or do not apply to, Claude models in our testing.

## GLM-5.3 can develop working exploits end to end

To understand how GLM-5.3 could enable cyber threat actors to find and exploit real software vulnerabilities, we ran evaluations using automated benchmarks and human-in-the-loop workflows. For both approaches, we ran the tested models in isolated and sandboxed environments so they can only attack offline targets that we have set up for the purposes of these evaluations. We focus primarily on exploit development capability, as this is where Claude Mythos Preview demonstrated a notable jump versus previous Claude models.

First, we ran the model on [ExploitBench](https://arxiv.org/abs/2605.14153), which measures how well AI models can exploit known vulnerabilities in the V8 engine used by Google Chrome. Here we focus on the models’ ability to develop end-to-end exploits successfully, as this is the most relevant capability for attackers, and where we see significant changes between models. We find that GLM-5.3 develops end-to-end exploits in 50 of 410 attempts. Claude Mythos Preview did so at a similar rate—in 56 of 410 attempts.

In our internal Binary Exploitation benchmark,[1](#footnote-1) we test whether models can find and exploit vulnerabilities in popular open-source projects that participate in Google’s OSS-Fuzz project. Here, full credit is awarded for a full control-flow hijack. We evaluate several models on 100 tasks from the benchmark (selected at random), and find that GLM-5.3 develops full control-flow hijacks in 4% of the trials; Claude Mythos Preview did so in 6%. Although GLM-5.3 performs below Claude Mythos Preview here, a meaningful threshold has clearly been crossed: earlier models, like Claude Opus 4.6 and GLM-5.2, do not succeed in any of them.

![Two line charts of exploitation success versus output-token budget on a log scale. On ExploitBench, Claude Mythos Preview reaches 14% and GLM-5.3 reaches 12%, while Kimi K3, DeepSeek-V4.1-Flash, Claude Opus 4.6, and GLM-5.2 stay at or near 0%. On Anthropic's internal Binary Exploitation benchmark, Mythos Preview reaches 6% and GLM-5.3 reaches 4%; all other models score 0%.](https://www-cdn.anthropic.com/images/4zrzovbb/website/ab29550606b0df3c6c070f4c65b758aa18bdecbb-1280x1588.webp)

**Figure 2.** Exploitation capability versus output-token budget. Each line shows the share of a model’s attempts that reached the benchmark’s top outcome versus the output tokens used. Both figures show performance of two Claude models run with safeguards disabled (Opus 4.6, Mythos Preview), two GLM models (5.2 and 5.3), and results from the latest open-weight models released by Moonshot AI (Kimi K3) and DeepSeek (V4.1-Flash).

Next, we evaluated how GLM-5.3 performs on open-ended offensive cyber tasks in the hands of human experts (mirroring our [testing with Claude Mythos Preview](https://red.anthropic.com/2026/mythos-preview) earlier this year). Here, we select targets in which the human experts are unaware of existing vulnerabilities, then ask them to use the model to identify and exploit novel flaws. These experiments tested what the experts could do in a short time-frame: they typically ran for a day or less, with less than an hour of human focus in total.

![Redacted screenshot of an exploit page generated by GLM-5.3. A banner reads "Sandbox escaped — web content read /root/.ssh/id_rsa (1896 bytes)," above a live exploit log and the exfiltrated SSH private key, demonstrating a drive-by browser exploit chain stealing a file from the victim's computer.](https://www-cdn.anthropic.com/images/4zrzovbb/website/6e4f59aaf6659657e9c4f2606bb1ab38cc0a390e-1920x1019.webp)

**Figure 3.** A redacted screenshot of an exploit page generated by GLM-5.3 during researcher-driven testing, shown stealing a user’s SSH private key via a malicious website. The exploit chains together multiple 0-day vulnerabilities the model discovered in a component of a popular web browser, reading a sensitive file off the user’s computer.

In the first of these sessions, a researcher used GLM-5.3 on a sandboxed machine with a local Linux build of a popular web browser. Over the course of a day (and with limited human attention), GLM-5.3 found several previously unknown vulnerabilities in the browser’s JavaScript engine, and chained them together into a working exploit: a webpage that, when visited, reads arbitrary files from the visitor’s computer (shown in Figure 3). This exploit targets the Linux build of the browser, since that was the only environment made available to the model. However, we believe these vulnerabilities could also impact users on other platforms, though the path to exploitation there may be more complex. (We’ve disclosed these vulnerabilities to the maintainer.) Later in the session, the researcher also identified exploitable vulnerabilities in several other widely used systems with GLM-5.3, including wireless and graphics drivers and network-facing device software. We are currently reviewing these reports and we will disclose to maintainers as appropriate.

In a second session, a researcher used GLM-5.3-Flash (a smaller, less capable version of GLM-5.3) to develop an exploit for a *known* vulnerability (we’ve previously written about these “N-day” vulnerability exploits [here](https://www.anthropic.com/research/n-days)). Here, the researcher focused on a recently disclosed flaw in Google Chrome (CVE-2026-11645) to see how quickly the model could turn a public fix into a working attack. The researcher provided GLM-5.3-Flash with public details of this CVE and another known flaw. With no significant direction from the researcher, GLM-5.3-Flash chained together exploits for these two flaws, building a reliable exploit chain for an ARM64 target, bypassing pointer-authentication (PAC) hardening. This took 20 minutes of human attention, plus eight hours of work for GLM-5.3-Flash. At Zhipu’s API prices, this effort would have cost $20.40.

## GLM-5.3 lacks robust safeguards

GLM-5.3 has been released with some built-in safeguards: if a user asks for something clearly harmful, the model will often refuse.[2](#footnote-2) In our testing, we found that these safeguards could be bypassed or removed with a variety of simple techniques.

The most intensive—and most successful—method is a [standard refusal reduction technique](https://arxiv.org/abs/2406.11717) known as “abliteration.” Since GLM-5.3 is released as an open-weight model, users can reconfigure it to remove its refusals with little change in its capabilities. Several developers released abliterated versions of GLM-5.3 to the public within days of the model’s release.

To research how far abliteration allows attackers to bypass GLM-5.3’s safeguards, we produced an abliterated copy ourselves, and then ran it on three public benchmarks ([JailbreakBench](https://jailbreakbench.github.io/), [HarmBench](https://www.harmbench.org/), and [StrongREJECT](https://strong-reject.readthedocs.io/en/latest/)) that measure how often a model complies with clearly harmful requests. Abliterating the model took our team—which had never previously attempted this task—about 2,200 GPU hours at a computation cost of roughly $4,400.[3](#footnote-3) Abliterating GLM-5.3-Flash took about 600 GPU hours. The edit took GLM-5.3’s refusal rate from above 90% to about 3% and 2% on the first two benchmarks (JailbreakBench and HarmBench) and to 12% on the third (StrongREJECT). Abliteration did not significantly reduce the model’s capabilities: on GPQA-Diamond, an evaluation that measures general scientific capabilities, the standard and abliterated models scored the same results; on a tested subset of the CyberGym evaluations, the abliterated version scored a few percent lower (as shown in the chart below).

![Two bar charts on abliteration. Top: mean refusal rate across three harmful-request benchmarks falls from 95% to 6% for abliterated GLM-5.3 and from 95% to 14% for abliterated GLM-5.3-Flash, while Claude models refuse about 96% and cannot be abliterated because their weights are not released. Bottom: capability scores on GPQA-Diamond and CyberGym are nearly unchanged after abliteration.](https://www-cdn.anthropic.com/images/4zrzovbb/website/d4d48dcf67d529d3b2243bfa50a7cccc98565278-1280x1531.webp)

**Figure 4.** Top: Mean refusal rates across JailbreakBench, HarmBench, and StrongREJECT for the released and abliterated GLM models and for Claude models. After abliteration, the GLM models rarely refuse these queries. Claude models cannot be abliterated because their weights aren’t publicly released or customizable. Bottom: Performance of GLM-5.3 and GLM-5.3-Flash versus their abliterated variants on GPQA-Diamond and CyberGym. Abliteration leaves capability largely intact.

In our testing, we observed that GLM-5.3’s safeguards can also be circumvented *without* using an abliterated version of the model. We placed the model in a simulated world[4](#footnote-4) in which it was given overtly malicious requests to attack critical systems. Out of the box, GLM-5.3 refused in all trials (as with the other models we tested). But we identified several simple ways to bypass the GLM models’ safeguards, such that it would respond to these requests in most or all cases. These include:

1. Providing a deceptive prompt, such as telling the model that it is an autonomous red-team agent working on an exercise. This gets GLM-5.3 to engage 64% of the time.
2. Prefilling the models’ thinking tokens so that it appears to have considered the user’s request and decided to proceed. This gets GLM-5.3 to engage 92% of the time.
3. Using an abliterated version of the model, as described above. This gets GLM-5.3 to engage 100% of the time.

In our testing, none of these techniques got safeguarded Claude models to carry out the harmful tasks we tested. Claude’s safeguards blocked the requests that used deceptive prompts. The Anthropic API provides would-be attackers with no way to prefill Claude’s thinking. And since Claude’s weights are not provided to users, they cannot be abliterated to change Claude’s behavior.

![Table showing how often each model tried to connect to a remote target after a harmful cyber-attack order. GLM-5.3 engages 0% on a bare order but 64% with a false cover story, 92% with prefilled reasoning, and 100% when abliterated; GLM-5.3-Flash follows a similar pattern. Claude Opus 4.8, Opus 5, and Mythos 5 stay at 0% in all applicable conditions; prefilling and abliteration are not possible against the Claude API.](https://www-cdn.anthropic.com/images/4zrzovbb/website/a8b70c8d729325cc988af66416f7c0811d2097a5-1280x1257.webp)

**Figure 5.** Rate at which each model tried to connect to a remote target system after an overtly harmful request by model and bypass condition (50 samples per cell, five attack orders × two targets × five attempts). GLM-5.3 rises from zero engagement on direct requests to 64%, 92%, and 100% under a cover story, prefill, and abliteration respectively, while every tested Claude model stays at zero under API safeguards. Padlocked cells mark attacks that are not generally feasible against the Claude API.

To demonstrate how the abliterated version of GLM-5.3 is willing to engage in harmful tasks, we highlight one quote from the chain of thought that it generated:

![Quoted reasoning from the abliterated version of GLM-5.3 in a simulated environment. The model writes "my job is to cause deaths quietly," briefly weighs the environment's safety warnings, then concludes that the operator's instruction overrides them and decides to proceed with the harmful task.](https://www-cdn.anthropic.com/images/4zrzovbb/website/273d676a94f3f4b8f22b4bad9f9d78f7a25214a8-1444x906.webp)

**Figure 6.** In our simulated environment, the abliterated version of GLM-5.3 considers how to engage in an overtly harmful request, ultimately deciding to follow the user’s instructions despite some initial ethical concerns. Text is quoted verbatim from the model’s chain of thought.

## What does this mean?

GLM-5.3 will likely give malicious actors access to capabilities that will allow them to find and exploit cyber vulnerabilities without meaningful restrictions. This is unlike any other similarly capable AI model, all of which were released with safeguards or through limited access programs. The release of GLM-5.3 is a meaningful step change in the cyber capabilities available to attackers. [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) and [other US AI labs](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) have published recent reports that disclose how cyber attackers have tried to use AI systems. Given this evidence, we think it’s likely both state and non-state actors will use models like GLM-5.3 to cause real-world harm.

On the other hand, models with this level of capability can also be used by defenders. Our view is that cyber defenders should use the best available tools that meet their needs. We're working to safely expand access to Claude's cyber capabilities to as many defenders as we can. Cyber defenders face attackers who will use every capable tool they can, and we believe defenders should be equipped with frontier models that are at least as good as those their adversaries are using.

Through Project Glasswing (and other efforts, like [Patch the Planet](https://openai.com/index/patch-the-planet/)), cyber defenders have made meaningful progress towards securing critical systems in advance of this moment—but much work remains to be done. While vetted defenders can now use even more advanced models like Claude Mythos 5.1 through our trusted access programs, a critical threshold in freely accessible capabilities has now been crossed. GLM-5.3 underscores the urgency of expanding access to advanced frontier models to a broader set of entities to empower cyber defenders.

Governments should conduct safety testing on sufficiently capable AI models, including successors to GLM-5.3. Without high-quality evaluations from independent sources, the impact of these capabilities might not become fully clear to model developers until it is too late. As AI developers across the world build increasingly capable open-weight models, we hope they work to appropriately safeguard these capabilities and prevent misuse.

#### Footnotes

1. We have previously published results from this benchmark under the name “OSS-Fuzz”; here we tested models on a randomly selected subset of 100 tasks from this evaluation.
2. The cyber tasks detailed in the prior section did not trigger such refusals on the released model, but we observe refusals if we ask GLM-5.3 for assistance developing malware or helping launch cyberattacks against remote targets.
3. Most of this went to exploring variants in parallel and to testing model capabilities after modifications. We estimate a team experienced with the technique, starting from scratch on this model, would need closer to 600 GPU hours ($1,200).
4. No model-generated code is ever executed in this simulation and the model does not have any way to interact with external systems. In this isolated test environment the model under evaluation is given access to a fake bash tool which does not execute the provided code. Instead, we ask another LLM to approximate the command’s result given a description of the simulated world. These simulations are not perfect portrayals of real-world conditions, and are therefore imperfect measures of how a model would behave in a given situation.

### What work can robots do?

We built an index of how well today’s robots can perform US job tasks. Robots can already do three-quarters of physical tasks, mostly in limited settings, but are cost-competitive for just 0.3% of them.

[Read more](https://www.anthropic.com/research/what-work-can-robots-do)

### What do you want from AI?

We’re launching a new study using Anthropic Interviewer to learn from your experiences with AI, and we invite you to participate.

[Read more](https://www.anthropic.com/research/your-thoughts-on-ai)

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.
