<!-- source: https://academy.claude.com/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Evaluate a company from the science to the balance sheet

Claude Opus 4.6 runs due diligence across SEC filings, clinical trial data, and patent documents at once, evaluating the science, modeling the financials, and catching where one contradicts the other.

15 minFinanceClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-nopkb6rc.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-is78zafq.png)

![Evaluate a company from the science to the balance sheet result](https://academy.claude.com/assets/v1/evaluate-a-company-from-the-science-to-the-balance-sheet-56l1xsie.png)[Open artifact](https://claude.ai/public/artifacts/6b7948e9-f7fd-4c48-960a-b0b490b99b16)

## 1. Describe the task[](#1-describe-the-task)

Opus 4.6 reads across SEC filings, trial protocols, and patent documents simultaneously, reasoning through the dependencies between them. It catches where one document contradicts another — a risk factor in the 10-K that doesn't match revenue assumptions in the 10-Q, or an undisclosed regulatory requirement that changes the timeline.

State the decision your analysis feeds, name the documents Claude will work from, and spell out the deliverables you expect back. The prompt below does all three, then adds a boundary: it anchors on the Phase III readout, lists the five filings, asks for a research memo and a downloadable model, and tells Claude to stay inside the uploaded documents rather than estimating around them.

I'm evaluating Meridian Therapeutics (~$4B mid-cap biotech) ahead of their Phase III readout. I've uploaded the 10-K, 10-Q, proxy, trial protocol, and patent filings.

Evaluate the science and trial design. Build a risk-adjusted pipeline valuation. Flag anything in the filings that contradicts management's guidance or earnings narrative. Model the downside scenarios I should be stress-testing. Work only from the documents I've uploaded; where the filings don't support a number, say so instead of estimating.

Produce a research memo and a downloadable model. Tell me what I should be worried about that I haven't asked about.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

Upload all five documents together: the 10-K, 10-Q, proxy, trial protocol, and patent filings. What Claude gives you back is mostly determined by what you give it to read, so spend your effort assembling the complete filing set rather than polishing the wording of the ask. The buried finding in the memo below only surfaces because the 10-K and the 10-Q are in context at the same time.

### Required context[](#required-context)

SEC filings (10-K, 10-Q, proxy)PDF

Clinical trial protocolPDF

Patent filingsPDF

### Optional context[](#optional-context)

If your filings are already on your computer, Cowork in [Claude Desktop(opens in new tab)](https://claude.com/download) can read them directly from a folder rather than uploading individually.

[Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) lets Claude scale how deeply it reasons based on task complexity. For multi-document financial analysis, it's worth turning on.

[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

## 3. What Claude creates[](#3-what-claude-creates)

Claude produces an integrated research memo, a downloadable financial model, an interactive scenario dashboard, and a patent cliff timeline. Opus 4.6 reads across all five documents simultaneously, and one finding it surfaced on its own is the kind of detail that could change the risk assessment.

### Research memo: Meridian Therapeutics

**1. Mechanism and Phase II signal**

MRD-4420 is a selective JAK1 inhibitor targeting the IL-6/STAT3 axis in rheumatoid arthritis. The selectivity matters — first-generation JAK inhibitors hit multiple isoforms, triggering the 2021 FDA boxed warning. Phase II showed ACR50 response rates of 48% vs. 32% for adalimumab (n=340), clinically meaningful but not powered for cardiovascular safety.

**2. Phase III risk**

The superiority design (n=1200) requires wider margins than non-inferiority. At the Phase II effect size, power is ~88%. If the effect attenuates 25% (common in Phase II-to-III transitions), power drops to ~62%.

**3. Buried regulatory finding**

Page 187 of the 10-K discloses an FDA request for a 52-week cardiovascular safety assessment — not in the original protocol. Cross-referencing the 10-Q, R&D guidance increased $45M without explanation. This likely means an additional safety extension study: 12–18 months added to timeline, $40–50M in costs, pushing earliest revenue to late 2028 vs. management's mid-2027 guidance. At $68M quarterly burn, cash runway narrows from 14 months post-filing to roughly 8.

**4. Scenario summary**

The model maps three scenarios based on the assumptions above:

Clean data, on-timeline: highest valuation range. Ambiguous data with 6-month delay and dilutive raise: mid-range. Failed superiority with pivot to non-inferiority: lowest range.

Per-share estimates depend on your discount rate, probability weights, and dilution assumptions. Adjust these in the downloadable model below.

### Interactive scenario dashboard

*[View the scenario dashboard]*

Toggle between scenarios and adjust key variables (probability of success, peak sales, discount rate, timeline delay) and watch the valuation recalculate in real time.

### Patent cliff and cash runway timeline

*[View the timeline]*

Core composition-of-matter patent expiration in 2036, method-of-use extension to 2039, mapped against cash runway and projected revenue ramp under each scenario.

*[Download: meridian-therapeutics-pipeline-model.xlsx]*

Adjustable inputs for all key variables. Changing any assumption recalculates pipeline NPV and dilution scenarios automatically.

***Important:** Claude is a research tool, not a financial advisor. This analysis surfaces findings and structures scenarios based on the documents and assumptions you provide. All projections reflect those inputs and may not match actual outcomes. Consult a qualified financial professional before making investment decisions.*

## 4. Follow up prompts[](#4-follow-up-prompts)

The memo is a starting point, not the deliverable. Each follow-up below pushes on something the first pass produced: the evidence behind the buried regulatory finding, the downside decision tree, and the assumptions driving the valuation.

### Pull the evidence behind the buried finding[](#pull-the-evidence-behind-the-buried-finding)

The safety-study finding is an inference Claude built from two separate disclosures. Make it show its work before that finding moves your position.

*Show me the exact disclosure on page 187 of the 10-K and the R&D guidance change in the 10-Q that the safety-study finding rests on. Quote both passages, then walk through the inference step by step so I can check it against the filings.*

Open in Claude

### Push the analysis further[](#push-the-analysis-further)

Opus 4.6 holds both the science and the financials in context at once, which means it can reason through multi-step problems where a change in one domain cascades into another.

*Model what happens if Phase III misses the superiority endpoint by a narrow margin. Walk through the decision tree: does management pivot to non-inferiority? How does that cascade through the timeline, cash runway, and valuation?*

Open in Claude

### Stress-test the model's assumptions[](#stress-test-the-models-assumptions)

The scenario ranges move with your discount rate, probability weights, and dilution assumptions. Push on the inputs you would defend differently before the model shapes your number.

*Rerun the scenario summary with a higher discount rate and a lower probability of success. Which scenario boundaries move the most, and at what inputs does the mid-range case stop holding?*

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Front-load your context[](#front-load-your-context)

A missing filing doesn't announce itself. If the trial protocol is left out, the memo's trial-design analysis has nothing behind it; if the 10-Q is missing, nothing can contradict the 10-K's guidance. Attach the complete five-document set in one message before you send the prompt.

### Verify the finding before it moves your thesis[](#verify-the-finding-before-it-moves-your-thesis)

Match your verification effort to the cost of being wrong: a variable name in the model can pass on a skim, but a claim that changes your valuation needs to be traced back to its source. Before you act on the safety-study finding, open the 10-K to the cited page and the 10-Q's R&D guidance line and confirm the disclosures say what the memo says they say. The added study, its cost, and the timeline slip are Claude's inference from those two passages, not quoted facts.

### Let Claude flag what you missed[](#let-claude-flag-what-you-missed)

Opus 4.6 works through more of the analysis before asking for direction, and it reads across documents in ways that catch what a surface read won't. An instruction like "flag anything that changes the investment thesis" often surfaces findings you didn't know to look for.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Point the same structure at the company you're evaluating: the decision it feeds, the full filing set, the deliverables you expect. The documents change; the cross-checks don't.

I'm evaluating Meridian Therapeutics (~$4B mid-cap biotech) ahead of their Phase III readout. I've uploaded the 10-K, 10-Q, proxy, trial protocol, and patent filings.

Evaluate the science and trial design. Build a risk-adjusted pipeline valuation. Flag anything in the filings that contradicts management's guidance or earnings narrative. Model the downside scenarios I should be stress-testing. Work only from the documents I've uploaded; where the filings don't support a number, say so instead of estimating.

Produce a research memo and a downloadable model. Tell me what I should be worried about that I haven't asked about.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
