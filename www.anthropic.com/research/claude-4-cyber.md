<!-- source: https://www.anthropic.com/research/claude-4-cyber -->

# Detailed cyber evaluations of Claude 4

Jul 15, 2025

*Anthropic (with [Pattern Labs](https://patternlabs.co/))*

We believe we are at a crucial period for cybersecurity and AI, with models advancing toward human-level cyber offense capabilities in some scenarios. As part of our commitment to safety at the frontier, we conduct rigorous testing of our models' cyber offense capabilities. For Claude Opus 4 and Claude Sonnet 4, we partnered with Pattern Labs to conduct an in-depth [evaluation](https://patternlabs.co/blog/from-scripts-to-strategy-claude-4s-advanced-approach-to-offensive-security) ranging from standalone capture the flag(CTF) challenges to complex network environment simulations. The results reveal significant progress: Opus demonstrated markedly improved ability to think flexibly and adapt its approach to challenges instead of persisting with failed, unchanging approaches. Moreover, the model demonstrated significant improvement in vulnerability identification and executing complex multi-step attack chains, consistently succeeding where previous models failed. However, important limitations remain, particularly with maintaining coherent, long-horizon plans and goals if presented with unexpected obstacles. Our partners at Pattern Labs have posted the [full evaluation report](https://patternlabs.co/blog/from-scripts-to-strategy-claude-4s-advanced-approach-to-offensive-security), which reveals both these exciting advances and critical limitations that inform our ongoing safety work.

####

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)

### Enabling independent research on how people use Claude

Earlier this year, we ran a pilot giving external researchers access to aggregate, real-world Claude usage data. Three research groups designed their own studies for Anthropic Insights, our privacy-preserving analysis tool. In this post, we share high-level results from those studies and what we learned running this pilot.

[Read more](https://www.anthropic.com/research/enabling-independent-research)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.
