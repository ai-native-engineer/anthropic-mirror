<!-- source: https://alignment.anthropic.com/2025/introducing-safeguards-research-team/index.html -->

# Introducing Anthropic's Safeguards Research Team

Following the release of [Constitutional Classifiers](https://arxiv.org/abs/2501.18837), we are excited to announce Anthropic’s new Safeguards Research Team. We'll be focusing on topics such as jailbreak robustness, automated red teaming, and developing effective monitoring techniques, both for model misuse and misalignment. The team is currently led by Mrinank Sharma, and current members are Erik Jones, Meg Tong, Jerry Wei, Euan Ong, Alwin Peng, Ted Sumers, Taesung Lee, Giulio Zhou, and Scott Goodfriend.

We will operate in close collaboration with Anthropic's broader Safeguards organization, which is responsible for building deployment infrastructure, implementing safety mechanisms, and maintaining user policies. This integration enables us to directly inform threat models, identify early warning signs of model misalignment, and prioritize pressing challenges. We will also be able to obtain rapid feedback about whether our safety solutions work and gain invaluable experience in deploying safety techniques into production.

We are planning to work on projects in the following areas:

* Defense techniques for misuse and misalignment, such as [Constitutional Classifiers](https://arxiv.org/abs/2501.18837) and [other classifier-based approaches](https://arxiv.org/abs/2412.02159), potentially using [model internals](https://arxiv.org/abs/2407.15549).
* Vulnerability identification, such as our work on [many-shot jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking), [best-of-N jailbreaking](https://arxiv.org/abs/2412.03556), and [understanding image jailbreaks](https://arxiv.org/abs/2407.15211). This also includes projects on automated red teaming.
* Monitoring: Creating efficient monitoring techniques, performing deployment-informed threat modeling to better understand risks, and exploring AI-assisted summarization to surface concerning patterns and anomalies. We want techniques that can analyze real-world usage to uncover previously unforeseen model misuse and misalignment risks, in order to inform our threat-modeling – for instance, using tools such as [Clio](https://www.anthropic.com/research/clio) and anomaly detection.
* Response: Techniques here include [rapid response](https://arxiv.org/abs/2411.07494), [few-shot catastrophe](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed)[prevention](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed), and protocols for [low-stakes](https://arxiv.org/abs/2411.17693)[control](https://arxiv.org/abs/2411.17693). If we detect harm, how can we respond quickly to mitigate it?
* Safety cases: Documenting comprehensive arguments for the safety of AI systems, particularly for model misuse.

We're currently expanding our team and seeking pragmatic research scientists and engineers with strong experimental skills. You can apply to join our team [here](https://boards.greenhouse.io/anthropic/jobs/4459012008).

We also work closely with the [Anthropic Fellows Program](https://alignment.anthropic.com/2024/anthropic-fellows-program/) and will run some projects through [MATS](https://www.matsprogram.org/).
