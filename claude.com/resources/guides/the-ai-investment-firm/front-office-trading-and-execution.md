<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/front-office-trading-and-execution -->

Chapter 083 min read

# Front office: Trading and execution

3 min read

30 min remaining

On the desk, traders run their standard analyses through skills in a sandbox, agents with read-only access investigate execution anomalies, and parsers turn dealer chatter into structured data.

## Main use cases

### Running trader analyses in a sandbox

Traders get Claude Code or a lightweight agent app inside a sandbox, with skills for the desk’s standard analyses, such as transaction cost analysis (TCA), markouts, P&L explain, event studies, and venue comparison. Claude produces the notebook and the charts.

### Investigating execution problems

When fills, latencies, or P&L look wrong, an agent with read-only access to logs, tick data, and configuration gathers the evidence and ranks likely causes. It then proposes a fix as a pull request for an engineer to review.

### Answering cross-asset questions through market-data connectors

Traders can ask Claude cross-asset questions in plain language. Claude pulls prices through market-data connectors, runs the calculations in code with the pricing tools, and writes up the result for the trader. For example, a fixed-income desk can ask for bond relative value under a rate shock, a digital-asset desk can ask about funding rates and on-chain liquidity, and an event-contract desk can compare pricing across venues.

### Parsing dealer runs, broker email, and chat into structured quotes

Smaller Claude models parse dealer runs, axes, chat, and broker emails into structured quotes and market color, which feed research and the desk’s quote history.

#### Outcome: Traders get same-day answers to cross-asset questions. When fills or latencies look wrong, agents gather evidence from logs, tick data, and configuration, and rank the likely causes, so engineers can diagnose incidents faster.
