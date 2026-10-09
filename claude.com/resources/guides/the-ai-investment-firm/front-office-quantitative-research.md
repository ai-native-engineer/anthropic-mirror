<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/front-office-quantitative-research -->

Chapter 063 min read

# Front office: Quantitative research

3 min read

36 min remaining

Quantitative research is a natural fit for Claude Code because most of a researcher’s work is writing and running code, data is structured, and the feedback loop is a backtest on historical data. Researchers work with Claude Code against internal libraries and backtesters, hand it papers to replicate, and increasingly run fleets of agents that generate, implement, and score signals.

## Main use cases

### Exploring and backtesting signals in the firm’s data and tools

Claude Code runs inside the research codebase with a standing brief that describes the data catalog, the backtester, and the coding conventions. At the start of a session, Claude checks a new dataset for gaps, survivorship, and point-in-time integrity. Then it explores feature-engineering ideas, codes the signal, writes the data-quality checks, runs the backtest, and reports Sharpe, drawdown, and turnover in the tear sheet. Researchers often run several sessions in parallel, asking Claude Code for quick answers, as well as for long, careful analysis.

### Replicating papers on internal data

When researchers give Claude Code a paper as a PDF, it reconstructs the methodology against internal data, tries to reproduce the result, runs out-of-sample and robustness checks, and writes a verdict with the code ready for review. Researchers used to put off replication until they had bandwidth to take it on; with Claude Code, they receive a first pass the same day they hand over the paper.

### Running the research loop with agents

A planner agent proposes hypotheses and researcher agents write and test signal code in isolated copies of the codebase. An evaluator agent scores each signal against the firm’s criteria, using multiple-testing controls and a holdout set that the agents can’t access. The researchers review the scored signals and decide which to pursue.

### Querying an analyst assistant in plain English

Some firms have built in-house analyst assistants on Claude. Analysts ask questions in plain English, and the assistant writes the Python, builds the charts, and iterates on the analysis. Systematic managers pair it with batch pipelines that turn their archives of filings, transcripts, and news into features.

#### Outcome: Researchers spend more of their time judging which ideas deserve capital, because Claude handles more of the data exploration, feature engineering, and testing. Every trial is logged, so the reported statistics are adjusted for the number of tests run.
