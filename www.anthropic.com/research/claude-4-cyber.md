<!-- source: https://www.anthropic.com/research/claude-4-cyber -->

# Detailed cyber evaluations of Claude 4

Jul 15, 2025

*Anthropic (with [Pattern Labs](https://patternlabs.co/))*

We believe we are at a crucial period for cybersecurity and AI, with models advancing toward human-level cyber offense capabilities in some scenarios. As part of our commitment to safety at the frontier, we conduct rigorous testing of our models' cyber offense capabilities. For Claude Opus 4 and Claude Sonnet 4, we partnered with Pattern Labs to conduct an in-depth [evaluation](https://patternlabs.co/blog/from-scripts-to-strategy-claude-4s-advanced-approach-to-offensive-security) ranging from standalone capture the flag(CTF) challenges to complex network environment simulations. The results reveal significant progress: Opus demonstrated markedly improved ability to think flexibly and adapt its approach to challenges instead of persisting with failed, unchanging approaches. Moreover, the model demonstrated significant improvement in vulnerability identification and executing complex multi-step attack chains, consistently succeeding where previous models failed. However, important limitations remain, particularly with maintaining coherent, long-horizon plans and goals if presented with unexpected obstacles. Our partners at Pattern Labs have posted the [full evaluation report](https://patternlabs.co/blog/from-scripts-to-strategy-claude-4s-advanced-approach-to-offensive-security), which reveals both these exciting advances and critical limitations that inform our ongoing safety work.

####

### Discovering cryptographic weaknesses with Claude

cryptographic algorithms. The first attack significantly weakens HAWK, a digital signature scheme that was built for a future world where quantum computers are able to break existing standards. The second identifies a new way to attack round-reduced AES, the most widely used symmetric cipher.

[Read more](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

### Project Pilot: Can AI control a drone?

Working with Andon Labs, we’ve developed a new series of evaluations that assess AI models’ ability to use a flying drone, culminating in a new benchmark: Drone-Bench.

[Read more](https://www.anthropic.com/research/project-pilot)

### How Canada uses Claude: Findings from the Anthropic Economic Index

[Read more](https://www.anthropic.com/research/how-canada-uses-claude)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

Cyber evaluations of Claude 4 \ Anthropic
