<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/how-the-work-is-controlled -->

Chapter 153 min read

# How the work is controlled

3 min read

9 min remaining

### Access follows existing permissions

Connectors that each person signs in to use that person's existing permissions, so Claude reaches only what that person can. Each agent gets only the access its task needs, set by team and business unit. At multi-manager firms, skills and memory are kept separate for each pod.

### Exact calculations run as code

Limit checks, fee calculations, and reconciliations run as deterministic code that can be tested and audited. Claude writes the code and the tests, and explains what the code flags.

### Agents stay out of production paths

Agents that investigate execution problems work with read-only access and stay out of the latency-critical path. Fixes are proposed as pull requests for an engineer to review.

### A person signs off

Claude doesn't provide investment, legal, tax, or compliance advice, and each firm remains responsible for its decisions and regulatory obligations. A person reviews and approves the work before it goes to a client, gets filed, or is acted on. Evals show when a process is ready for the next stage, and when a new model can take over.

### Everything is recorded

Prompts and responses go to the firm’s compliance archive through its cloud logging or Anthropic’s Compliance API (on Enterprise plans). Agents log the reasoning behind what they produce, and Claude Code runs with per-user attribution and sandboxing.

## Where to start

### Pick one process.

Choose one the team already measures. Reconciliation, the month-end close, and the earnings-night model update are common first choices.

### Record the baseline.

Write down how long the work takes today and how often it’s right.

### Build the eval and write the skill.

Build the test set from the team’s real work, and have the people who do the work best write down how they do it.

### Connect the systems and name the owners.

Give Claude access to the systems the process touches, and name an owner for the skill, the eval, and the results.

### Move up a stage when the evals say so.

Then pick the next process.
