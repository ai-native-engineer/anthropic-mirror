<!-- https://anthropic-partners.skilljar.com/whats-new-with-opus-47/486154 -->

Lesson 4 of 5 · Course: What's New with Opus 4.7

# Set the ceiling. *The model respects it.*

Task Budgets is the second cost lever in 4.7. Set a token limit for an entire agentic loop, not just a single request. Claude sees the remaining budget and adjusts its work toward a clean finish. Spend gets predictable.

What changed

## From "max tokens per request" to *"budget for the whole loop."*

Before 4.7, the only spending control was max\_tokens on a single request. For agentic workloads that make many requests, that left customers exposed: any one run could chain into something expensive, and the only way to find out was to look at the bill. Task Budgets moves the ceiling to the right level.

Before

Per-request limits only

Set max\_tokens for each individual API call. An agentic loop with twenty calls could still spend twenty times the per-call ceiling, with no aggregate control.

Now

A budget for the entire agentic loop

Set one token limit for the whole task. Claude tracks remaining budget live and adapts its work. Spend becomes a knob your customer turns rather than a number they discover at the end of the month.

How it works

## Claude sees a live countdown and uses it.

The behaviour change is the part worth explaining to customers. The budget isn't a hard cutoff that severs the run at the worst possible moment. It's a soft limit the model is aware of, and the model adjusts to it.

01

Track

Claude sees the remaining budget as it works. The countdown is live across the whole loop, not just within one request.

02

Prioritize

When budget is tight, Claude weights the high-value work first. The agentic plan adjusts in real time to fit the ceiling.

03

Wrap up gracefully

As the budget runs down, Claude moves to closing the work cleanly rather than getting cut off mid-step. Soft limit, not a hard kill.

The launch demo

## Carbon capture research, with and without a budget.

Same prompt, two runs. The prompt: research carbon capture and storage, identify three leading companies, produce a 500-word brief. The only variable is whether Task Budgets is enabled. The token consumption tells the story.

Run 1 · No budget

44K tokens

Same prompt, no ceiling set.

Claude explored broadly, took the path it wanted, produced the brief. No spending discipline, no signal from the runtime that the work needed to converge. Output quality was strong; cost was higher than it needed to be.

Run 2 · 25K budget

11K tokens

Same prompt, 25,000 token budget set.

Claude stayed well under the ceiling. The budget signal prompted earlier convergence, fewer exploratory steps, and a cleaner path to the brief. Output remained on-spec; cost dropped to roughly a quarter of the unconstrained run.

  

The line your customer's finance team will repeat

The same workload finished for roughly **a quarter of the unconstrained spend**, and the output stayed on-spec. The bottleneck wasn't capability; it was the absence of a signal telling the model to converge. A budget is that signal.

When to use it

## Validate the trade-off with an eval harness.

Budgets are a real lever, and the trade-off is real too. Tighter budgets mean lower spend; they can also mean less exploration. The honest version is "test the budget against your eval suite and see what you can afford to lose."

For production workloads, that means running both conditions, scoring output quality against your customer's actual evaluation criteria, and picking the budget level where quality stays acceptable. The carbon-capture demo is a starting point, not an answer. Your customer's workload may absorb a much tighter budget; it may need a looser one. The harness is what tells you.

Activity · The right spending control

## A customer is hitting cost ceilings. Which control do you recommend?

Different cost problems call for different controls. The trap here is reaching for the most familiar lever even when it isn't the one that fits.

Decision · Scenario

A customer runs an agentic research workflow. Each task can chain through **fifteen to twenty model calls**, and aggregate spend per task is variable and hard to predict. What do you recommend?

A · Lower max\_tokens on each individual request and retry on truncation

Tighten per-call limits and absorb the retries.

B · Set a Task Budget for the entire agentic loop

Single ceiling across all the calls in the task. The model adapts its work to fit.

C · Run the task on Haiku to cap the per-call cost

Downshift the model to control unit economics.

**B is the answer.** The customer's pain is aggregate spend across many calls in a single task; a per-call lever (A) doesn't address it and adds retry complexity. C trades cost for capability and may not produce the research quality the workload needs. Task Budgets is the lever for this shape of problem: one ceiling at the task level, the model handles the prioritization inside it, the customer gets a predictable bill. Validate the budget level against an eval suite before shipping.

<!-- youtube: 7vZcrr5QIoM -->

[![Set the ceiling. *The model respects it.*](https://img.youtube.com/vi/7vZcrr5QIoM/hqdefault.jpg)](https://www.youtube.com/watch?v=7vZcrr5QIoM)

<details>
<summary>자막: Set the ceiling. *The model respects it.*</summary>

All right, so I have another demo here. Let me switch tabs. This one is similar. Um you can see here we'll look at the we'll go ahead and fire it off and we can look at the code. On three. All right, so in this example here um I give it a prompt here. You can see the prompt here it says a little bigger. Uh research the current state of carbon capture and storage, commercial deployment, identify three companies leading the field covering the core technology, most recent findings, partnership, take off agreement. And it says produce a 500 word comparative brief. Okay, so jumping over to the code here you can see um here's the function call or the the API call out. Um and we gave it a a max token size here that we set here. This one was set to What did we set this one to? Uh find that value. It was 25,000. Oh, yeah, 25,000 is the uh Sorry, uh yeah, the the budget. All right, so it's still thinking here. Um it's going to write twice. The first time with no task budget and the second time with a task budget. We can compare those those two results. Again here the response looks very similar um to the one before, but in our tool call area um we're not calling the advisor tool again. We're just using the web search tool. Um all right, looks like it's done here. So we can see um the first run without a task budget consumes 44,000-ish tokens and then um the second run with our budget of 25,000 consumed um only 11,000 of of that budget. So, it was well under budget. >> [snorts] >> Um and then you can see here a a side-by-side comparison. Um and then here are the two outputs. I didn't display the whole outputs and you're probably thinking, "Hey, well, like what if one output's better than the other?" Um and that's where your eval would come in, right? So, after we would do set a budget, we would then hook this up to a a harness eval and then use that to compare the results using some other um grounded truth or using LLM as a judge to evaluate the results for both with and without the budget. So, again, um task budgets are a good way to keep control of of your genic workflows in the amount of tokens that um those workflows are are consuming.

</details>
