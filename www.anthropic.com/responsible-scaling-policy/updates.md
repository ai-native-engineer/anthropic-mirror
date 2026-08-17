<!-- source: https://www.anthropic.com/responsible-scaling-policy/updates -->

# Previous goals

An archive of the former goals of our Frontier Safety Roadmap. We move goals to this page once we've completed or meaningfully modified them. A record of all changes we’ve made to our goals can be found on our Roadmap (under the ‘Updates’ heading).

[View updates](https://www.anthropic.com/responsible-scaling-policy/roadmap#overview)

## Principles for data retention

***Status:** Completed May 5, 2026 and removed from the Roadmap on the same date.*

#### Version of this goal as set on: February 19, 2026

Target date: April 1, 2026

We offer many customers “zero data retention” policies so they can be confident that sensitive information is safe. Doing this for all customers, however, would greatly hamper our efforts to detect misuse attempts and continually learn from real-world usage of our systems. We would like better principles for which customers are offered which retention policies, and how we can ensure that “zero data retention” usage remains safe even as AI capabilities improve. We will complete an internal in-depth analysis of key factors and set new Frontier Safety Roadmap goals based on it.

Details: We will write a comprehensive internal report to identify how our Safeguards could be improved by updating our data retention policies. Within 6 weeks of report completion, we will publish a new goal related to this or announce that we aren’t doing so.

We are highly confident that we will complete this report, and will use it as a jumping-off point to set further goals.

**Update**

On March 29, 2026, we completed a comprehensive internal report to identify how our Safeguards could be improved by updating our data retention policies. By May 11, 2026, we will publish a new goal related to this or announce that we aren’t doing so.

**Update**

On May 5th 2026, we removed this content from the page after deciding not to set a new goal on this front. Based in part on the analysis we completed as a prior roadmap goal, we are undertaking a major project to improve our data retention practices for certain future models from a safety point of view, and we will be putting out public content explaining our thinking. We don’t feel that setting a separate date-bound goal in this context would be helpful as a forcing function for the goal, we feel that other internal processes will provide adequate forcing functions.

## Launching moonshot R&D projects

***Status:** Initial goal completed April 2, 2026 and a revised version remains on the Roadmap.*

#### Version of this goal as set on: April 2, 2026

Security is an ongoing and immediate priority for us, but it is also a long-term challenge where we’ll need to be creative and explore promising and incomplete ideas. This is because we may, at some point in the future, be targets of the world’s best-resourced attackers. Our moonshot R&D projects are exploring ambitious, possibly unconventional ways to achieve unprecedented levels of security.

Current ongoing projects:

* We are exploring a potential prototype of what our key workflows and infrastructure would look like (and what the productivity impact would be) if they were subject to extreme security practices. This would include simulating (at very small scale) isolated networks, “green lines” for limited remote connections, as well as commensurate physical security controls. We will complete Phase 1 - an inventory of needed components and preliminary analysis of costs and timelines - by May 15, 2026 and decide on next steps within 2 weeks of doing so. (It’s possible that we will de-prioritize this project in favor of other work, depending on what we determine in Phase 1.)
* We will develop a prototype by September 30, 2026 of provable inference, a technique for reliably, provably “signing” AI model outputs in a way that makes them attributable to a specific set of model weights. In the future, it’s possible that very sophisticated attackers will seek to infiltrate our systems and modify our models after we’ve trained them - whether to sabotage our work or co-opt our models into serving their own goals. If we could reliably and systematically verify that model outputs were coming from a specific set of model weights, we believe this threat would be significantly reduced.

**Update**

On May 5th 2026, we changed our target date for Phase 1 from May 15, 2026 to September 30, 2026 because we decided to focus the relevant resources on accelerating our “Leveling up across the board” goal for the time being. While we still don’t expect to *fully complete* the latter goal in the next few months, we believe we will make significant progress on it, and that the safety benefits of doing so are greater than what we’d realize with our original prioritization. As for the latter goal, our initial discussions have left us skeptical that isolated networks are a feasible path forward inside the next 1-2 years, when [powerful AI may be developed](https://www.darioamodei.com/essay/the-adolescence-of-technology). We still plan to complete Phase 1, which will hopefully leave us with a more confident and grounded view.

#### Version of this goal as set on: February 19, 2026

Security is an ongoing and immediate priority for us, but it is also a long-term challenge where we’ll need to be creative and explore promising and incomplete ideas. This is because we may, at some point in the future, be targets of the world’s best-resourced attackers. Our moonshot R&D projects will explore ambitious, possibly unconventional ways to achieve unprecedented levels of security.

Possible moonshot projects range from a small-scale “mock secure research environment” (simulating what our key workflows and infrastructure could look like under extreme security) to exploring applications of advanced AI to security.

**Details of this goal**

Candidate projects include:

* An operational Mock Secure Research Environment, aiming to simulate at a very small scale what our key workflows and infrastructure would look like (and what the productivity impact would be) if they were subject to extreme security practices. This would include simulating isolated networks,“green lines” for limited remote connections, as well as commensurate physical security controls.
* An analysis of the feasibility of full adoption of confidential compute during the entire lifecycle of model R&D.
* An initial assessment of what AI-assisted security tooling (vulnerability discovery, automated patching, anomaly detection) is feasible today.
* A pilot of a continuous personnel security vetting program for high-risk roles with defined screening criteria, monitoring, and reporting requirements.
* A pilot of a system in which all interaction with our models (including internal research and training) uses APIs rather than interaction with raw model weights.
* An attempt to create adaptive behavioral models for flagging anomalous activity by users and services on our systems (flagged anomalies should adapt as our workflows and usage patterns change).
* An attempt to identify our most valuable algorithmic IP and a path to giving it additional protections.

By April 1, 2026, we will have selected and begun 1-3 project(s), including but not limited to those above, and established concrete further goals and timelines for each. Each should lead to a working answer to the key open questions within 6 months.

We are highly confident that we can complete this initial step, and will use it as a jumping-off point to set further goals.

**Update**

By April 2nd 2026, we had completed this goal by selecting and beginning work on two projects, detailed above.

## A roadmap for policymakers

***Status:** As of July 8, 2026, we consider our [Advanced AI Framework](https://www-cdn.anthropic.com/files/4zrzovbb/website/0a58d567024a8b448ff15158ebc3625328dfcc1f.pdf) to fulfill this goal. We plan to publish a new policy goal to replace it. We did not make any significant changes before completing this goal.*

#### Version of this goal as set on: February 19, 2026

We will develop and share a set of ambitious policy proposals to effectively manage industry AI risks globally without unnecessarily limiting the benefits from AI development or slowing the AI development of democracies relative to that of autocracies.

We believe the right framework is a **regulatory ladder:** requirements that scale with risk. Today's frontier models require transparency and basic oversight. Yet as capabilities increase, we are moving towards a need for more rigorous external testing, stronger incident reporting, and deeper government oversight. At the most advanced capability levels and risks, the appropriate governance analogy may be closer to nuclear energy or financial regulation than to today's approach to software.

As with our advocacy for transparency [frameworks](https://www.anthropic.com/news/the-need-for-transparency-in-frontier-ai) as a starting point, we will develop and advocate for more advanced and risk-appropriate proposals in collaboration with a wide array of stakeholders.

**Update**

By July 8th 2026, we had completed this goal and are planning to set another policy goal to replace it.
