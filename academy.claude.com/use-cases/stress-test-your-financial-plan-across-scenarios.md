<!-- source: https://academy.claude.com/use-cases/stress-test-your-financial-plan-across-scenarios -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Stress-test your financial plan across scenarios

Claude Opus 4.6 tests a financial plan against a full range of possible outcomes, traces how each risk cascades through the rest, and builds a working model you can adjust yourself.

15 minPersonalClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-othme1zy.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-fi3pgdb7.png)

![Stress-test your financial plan across scenarios result](https://academy.claude.com/assets/v1/stress-test-your-financial-plan-across-scenarios-jf5kslme.png)[Open artifact](https://claude.ai/public/artifacts/1ca44b81-2605-4516-935f-25e35b24f955)

## 1. Describe the task

Opus 4.6 synthesizes across your full set of financial documents before building anything. It connects variables that most calculators treat independently — tax brackets, withdrawal sequences, Social Security timing — and reasons through how they cascade over decades.

Describe your situation and what you want to understand. Your financial documents, covered in the next section, provide the detail. Opus 4.6 determines the approach, runs the analysis, and produces working spreadsheets and scenario explorers. From there, you can keep working in [Claude in Excel(opens in new tab)](https://claude.com/claude-for-excel).

I’m 52, hoping to retire at 62. My partner and I have about $1.2M across a 401(k), Roth IRA, and taxable brokerage. I make $185K, he makes $95K, we spend about $8,500/month. Mortgage is paid off in 2031. Not sure if we should be doing Roth conversions now while we’re in a lower bracket.

I’ve uploaded our tax returns, investment statements, Social Security estimates, and budget. Where does this plan break and what are the highest-leverage moves?

Open in Claude

## 2. Give Claude context

The more complete your uploads, the more connections Claude can find across your tax situation, investment accounts, and benefit estimates.

### Required context

Upload your financial documents: tax returns, investment account statements, Social Security benefit estimates, and a monthly expense breakdown.

Tax ReturnPDF

Account StatementPDF

Tax ReturnPDF

### Optional context

[Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) lets Claude scale how deeply it reasons based on task complexity. Turning it on gives Claude more room to reason through complex, interdependent variables before producing results.

[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

## 3. What Claude creates

Opus 4.6 produces a working financial model with probability distributions across a range of modeled scenarios, an interactive scenario explorer, and a clear action plan. Keep in mind, Claude produces outputs based on the documents you provide. You should review any strategies with a qualified financial professional before acting on them. Here’s the kind of analysis you’ll get:

I’ve read through all your documents. Before building anything, I want to flag something: your mortgage payoff in 2031, your peak earnings window, and the Roth conversion opportunity all overlap. That’s actually a timing advantage most calculators would miss. Here’s what I found.

**Financial snapshot:** Combined income, savings by account type, monthly spending, savings rate, and estimated Social Security benefits.

**Monte Carlo results:** Estimated success rate to age 92 based on historical return distributions, median portfolio at key ages, and the 10th-percentile downside. These results shift meaningfully when you change the underlying assumptions, which the scenario explorer lets you do.

**Potential vulnerabilities in the model:** Sequence-of-returns risk. A bear market in your first two retirement years drops estimated success rates significantly. The same downturn a decade later barely registers.

**Three strategies with the largest impact on estimated success rate:** Roth conversion ladder, delaying Social Security to 70, and a two-year cash buffer, each with a modeled impact on the probability distribution.

**Interactive scenario explorer:** Toggle strategies on and off and watch the probability distribution shift. Adjust returns, inflation, and spending assumptions.

**Downloadable spreadsheet:** Adjustable inputs, Monte Carlo results, Roth conversion schedule, withdrawal sequence, and year-by-year tax projections.

***Important:** This analysis models scenarios based on the inputs you provided and general financial principles. It does not account for your full financial picture, tax situation, or personal circumstances the way a licensed advisor would. Review any strategies with a fee-only financial planner or CPA before making changes to your plan.*

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Stress-test a life change

Opus 4.6 stays with the full complexity when you throw a wrench in the plan. Describe a scenario and it re-runs the entire analysis, tracing how one variable ripples through income, taxes, withdrawal sequences, and long-term success rate without simplifying away the interactions.

What if I lose my job at 57 and can only find work at $120K? How does that change the Roth conversion window?

Open in Claude

### Take the model into Excel

Opus 4.6 produces downloadable spreadsheets you can open in [Claude in Excel(opens in new tab)](https://claude.com/claude-for-excel) to keep adjusting. Change an assumption, test a new scenario, or extend the projections without rebuilding anything from scratch.

I want to play with the inflation assumptions. What happens to the withdrawal sequence if we get a 5% inflation year in 2029?

Open in Claude

### Ask what you’re missing

Opus 4.6 reasons across finance and tax at domain-expert level and will surface things you didn’t think to ask about, like a narrow window for conversions created by a tax bracket transition or a withdrawal order that saves you money over decades. Push it further.

What would a financial planner flag about this plan that I haven’t asked about?

Open in Claude

## 5. Tricks, tips, and troubleshooting

### Start with your situation

If you aren't sure about the approach you'd like to take, describe your financial situation and what you want to understand. Opus 4.6 identifies an analytical approach from your context on its own.

### Upload everything at once

Opus 4.6 synthesizes across your full document set before building anything, finding interactions between your tax returns, investment statements, and Social Security estimates that cascade through each other. The more complete the picture, the stronger the analysis.

### Run longer analyses through Cowork

If your financial documents are already on your computer, Cowork in [Claude Desktop(opens in new tab)](https://claude.com/download) can read them directly from a folder rather than uploading individually. For complex plans with many accounts, tax considerations, and interdependent variables, Cowork handles longer-running analysis without hitting context limits, spinning up sub-agents to model different scenarios in parallel before synthesizing the results.

### Start another task while this one runs

Financial modeling runs across many variables and scenarios. Open a new session from the sidebar for other work. You'll see a grey dot in the sidebar when this one needs attention.

## 6. Ready to try for yourself?

Try Opus 4.6 with your financial plan and see how changing one input ripples through the entire model.

I’m 52, hoping to retire at 62. My partner and I have about $1.2M across a 401(k), Roth IRA, and taxable brokerage. I make $185K, he makes $95K, we spend about $8,500/month. Mortgage is paid off in 2031. Not sure if we should be doing Roth conversions now while we’re in a lower bracket.

I’ve uploaded our tax returns, investment statements, Social Security estimates, and budget. Where does this plan break and what are the highest-leverage moves?

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
