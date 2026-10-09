<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/middle-office-risk-management -->

Chapter 093 min read

# Middle office: Risk management

3 min read

27 min remaining

Risk teams are building agents that keep context from one day to the next. A typical agent works with the risk managers on the firm’s data and helps them explain each day’s changes in risk across asset classes.

## Main use cases

### Drafting daily risk commentary

Each morning, an agent reads positions, sensitivities, and market data, along with the results of the firm’s coded checks against its risk limits, investment guidelines, and concentration limits. It explains what changed by desk and asset class, flags positions close to a limit, and drafts the sign-off commentary. It answers risk managers’ follow-up questions with the context of prior days, and it logs the reasoning behind everything it produces.

### Investigating limit breaches

A program checks the firm’s positions against each risk limit and flags any breach or near-breach. For each flag, Claude identifies the trades that caused it, gives a first view of how serious it is, and drafts the escalation for the risk manager to review.

### Designing and testing new stress scenarios

Agents propose new coherent scenarios, run each one through the firm’s risk engine, and explain which positions drive the P&L. Risk committees review these scenarios next to the standard set that replays past market events.

### Validating models and monitoring counterparties

Claude Code, with read-only access, reproduces model results and compares the documentation against the code for validation reports. Scheduled agents watch ratings, spreads, and news on prime brokers, exchanges, custodians, and other counterparties through credit-data connectors.

#### Outcome: Risk managers review drafted commentary before they sign off, and can trace each explanation to the data as it stood that morning.
