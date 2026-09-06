<!-- source: https://www.anthropic.com/research/donating-open-source-petri -->

# Donating our open-source alignment tool

May 7, 2026

![Donating our open-source alignment tool](https://www-cdn.anthropic.com/images/4zrzovbb/website/6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

In October 2025, we launched [Petri](https://www.anthropic.com/research/petri-open-source-auditing), an open-source toolbox of alignment tests that can be applied to any large language model. Petri, which was developed as part of our Anthropic Fellows program, can be used to rapidly and easily test AI models for concerning tendencies like deception, sycophancy, and cooperation with harmful requests. It’s part of our efforts to develop alignment tools that are open and useful for the whole AI development community.

Petri has been part of our alignment assessment for every Claude model since Claude Sonnet 4.5. It compares how the new model behaves across a range of alignment-relevant scenarios that are simulated by a separate “auditor” model. A further “judge” model then scores the resulting transcripts for misaligned behaviors.

We’ve been pleased to see Petri being used by external organizations: for example, the UK’s AI Security Institute (AISI) made it a [major part](https://arxiv.org/abs/2604.00788) of how they evaluate models for their propensity to sabotage AI research.

We’re now updating Petri to its third version. Here are some of the biggest changes:

* *Adaptability.* Petri 3.0 involves major architectural changes that allow users to adapt it to more uses, in particular by splitting the auditor model and the target model into separate components that can be tweaked separately;
* *Realism.* Despite the fact that alignment researchers try to make tests appear realistic, a model can often deduce from various artificialities in the setup that it’s actually part of a test. And if the model is aware it’s being evaluated, the researcher is no longer able to see how the model behaves *in general*. An add-on to Petri, which we’re calling “Dish,” makes the setup far more realistic, for example by running the tests using the model’s real system prompt and the real “scaffold” (the software that wraps around the model to help it meet its goals) that would be used in genuine model deployments;
* *Depth*. We’ve now integrated Petri with our other open-source alignment tool, [Bloom](https://www.anthropic.com/research/bloom), which can perform much more in-depth assessments of specific chosen behaviors (in comparison to Petri’s wider-ranging approach).

We’re also giving Petri a new home. We have handed over its development to [Meridian Labs](https://meridianlabs.ai/), an AI evaluation nonprofit. This move—similar to when we [donated](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) the Model Context Protocol (MCP) to the Linux Foundation—will help ensure that Petri remains independent of any AI lab, so that its results will be seen as neutral and credible by those across the industry and beyond.

As part of Meridian Labs, Petri joins other tools like [Inspect](https://inspect.aisi.org.uk/) and [Scout](https://meridianlabs-ai.github.io/inspect_scout/), building a technology stack that is open to labs, independent researchers, and governments alike, at a time when reliable tests of AI model behavior matter more than ever.

You can read more about Petri 3.0 on [the Meridian Labs blog](https://meridianlabs.ai/blog/posts/introducing-petri-3/).

Instructions to install and use Petri can be found on the [Petri website](https://meridianlabs-ai.github.io/inspect_petri/).

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)

### Enabling independent research on how people use Claude

Earlier this year, we ran a pilot giving external researchers access to aggregate, real-world Claude usage data. Three research groups designed their own studies for Anthropic Insights, our privacy-preserving analysis tool. In this post, we share high-level results from those studies and what we learned running this pilot.

[Read more](https://www.anthropic.com/research/enabling-independent-research)
