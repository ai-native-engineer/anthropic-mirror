<!-- https://anthropic-partners.skilljar.com/whats-new-with-opus-47/486153 -->

Lesson 3 of 5 · Course: What's New with Opus 4.7

# Sonnet asks Opus for help. *Inside one API call.*

Advisor Strategy is the cleanest cost lever in 4.7. Sonnet or Haiku handle most of a request and quietly call up to Opus when the work needs frontier intelligence. One API call. No router to write. The customer gets Opus quality where it matters and Sonnet pricing everywhere else.

What it is

## A drop-in feature that lets a smaller model borrow a larger one.

Most workloads don't need Opus end-to-end. Most have moments inside them, occasional sub-problems, where Opus would help and Sonnet wouldn't. Advisor Strategy is the mechanism for handling exactly that: Sonnet leads the request, recognises when a sub-problem is beyond its depth, and calls Opus for guidance. The result comes back, Sonnet finishes the work, and the user gets a single response.

From the launch call: **"You don't have to change your call. Just provide this tool to your Sonnet or Haiku calls and it will call up to Opus when it needs that extra intelligence."** One API request handles multiple model handoffs internally. No routers, no orchestration, no infra to build.

How you enable it

## One added tool on the call. The rest is automatic.

The integration is a single tool entry on your existing Sonnet or Haiku call. No code path changes, no fallback logic, no separate API endpoints. The model decides when to consult; you get one response back.

```
from anthropic import Anthropic
client = Anthropic()
# Standard Sonnet call. The advisor_strategy tool lets the model
# consult Opus mid-request when it decides the work needs it.
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    tools=[{
        "type": "advisor_strategy",
        "advisor_model": "claude-opus-4-7"
    }],
    messages=[{
        "role": "user",
        "content": "Prove that for any prime p > 3, p² - 1 is divisible by 24."
    }]
)
# One API request. Sonnet handles routine work; Opus gets called only
# when Sonnet recognises a sub-problem beyond its depth.
```

Pseudocode. Verify the exact tool signature against current Anthropic docs before shipping.

When it fires

## Three math problems show the pattern.

The launch demo runs three problems past Sonnet with Advisor Strategy enabled. Same call, same configuration, three different outcomes. The shape of the model's decision-making is the lesson.

Easy

"Compound interest on $10,000 at 4% annual, compounded quarterly, over 5 years. What's the final balance?"

**Sonnet solves alone.** 1,200 tokens in, 400 out, ~5 seconds. No Opus call.

Medium

"A stick is broken at two random points. What's the probability the three pieces form a triangle?"

**Calls Opus mid-request.** Sonnet starts the problem, recognises geometric-probability reasoning is heavier than routine, asks Opus.

Hard

"Prove that for any prime p > 3, p² - 1 is divisible by 24."

**Uses Advisor Strategy fully.** Number-theoretic proof requires Opus-level reasoning; the call to Opus happens inside the same API request.

Why it matters

## Opus quality, where it counts. Sonnet pricing, everywhere else.

This is the cost lever your customers will actually care about. Most workloads have moments inside them — occasional sub-problems — where Opus would help and Sonnet wouldn't. Pre-4.7 the choices were: run everything on Opus and pay for capability you don't need, or run everything on Sonnet and miss the hard cases. Advisor Strategy splits the difference inside one call.

The pitch your customer will respond to

No router to write, no orchestration layer to maintain, no model-fallback logic in your application code. **One tool entry on the call** and the routing happens inside the model. The customer's engineering team writes less. The bill goes down on the routine work. The hard problems still get Opus.

Activity · Workload fit

## A customer has three workloads. Which one benefits most from Advisor Strategy?

Advisor Strategy is most valuable when the workload has variance: mostly routine work, occasional hard sub-problems. Workloads that are uniformly hard or uniformly easy don't benefit much.

Decision · Scenario

Same customer, three different workloads. **Which one is the highest-value place to enable Advisor Strategy?**

A · Customer support chatbot with mostly routine queries

High volume, simple questions, occasional human escalation.

B · Multi-step financial reasoning with occasional complex sub-problems

Most steps are spreadsheet-tier arithmetic; occasionally a step needs deeper reasoning about edge cases or unusual instruments.

C · Long-horizon scientific research agent that always needs frontier reasoning

Every step is novel reasoning. No shortcut to Sonnet without quality loss.

**B is the answer.** The variance is what makes Advisor Strategy valuable: routine reasoning runs on Sonnet, the occasional hard sub-problem promotes to Opus, and the customer pays accordingly. A is uniformly routine; just run Haiku or Sonnet and skip the strategy entirely. C is uniformly hard; if every step needs Opus, run Opus end-to-end instead of paying the coordination overhead. Advisor Strategy earns its place precisely on workloads with mixed difficulty.

<!-- youtube: SbupSX3w4wQ -->

[![when Sonnet recognises a sub-problem beyond its depth.](https://img.youtube.com/vi/SbupSX3w4wQ/hqdefault.jpg)](https://www.youtube.com/watch?v=SbupSX3w4wQ)

<details>
<summary>자막: when Sonnet recognises a sub-problem beyond its depth.</summary>

Let's take a quick look at the advisor strategy in action. So, I have a code sample here that I built that's going to demonstrate the advisor strategy. I'm going to go ahead and kick it off, and then we can talk about it. So, what the code does here is this pretty simple solution. Uh it's going to ask a couple of of different uh math problems here. You can see the problem. If you had $10,000 of annual interest rate of 4% compounded quarterly, how much do you have after 5 years? Round to the nearest cent. And so, what we've done here is um use the advisor strategy pattern here where it will call out to Opus if it needs that extra intelligence, right? It's unable to solve the problem itself. And so, you can see here just the output of the formula. And in this particular problem, it was pretty easy to solve. It did not require calling out to Opus. It was able to uh do it all within Sonnet. And so, you can see here the token count at the bottom here um uh 1,200 in, 400 out. It took about 5 seconds. But, I have some other problems. Let's try a more complicated one. This one here is uh a stick of length one is broken at two points chosen independently along with which one of the way? What is the probability that the three resulting pieces can form a triangle? Justify your answer. And so, it's thinking right now. And as it's thinking, let's take a look at the code here. So, if you see here um uh lines 55, 56, 57, here I'm just defining the model that I'm using, Sonnet Opus. And then here's the new piece here um line 57 where we specify the new advisor tool because it's just considered a tool call um within the agent itself. All right, let's look back at the example and see what it's done here. All right. Um Um, a lot going on here. Um so, again, the problem was a stick of length one is broken at two points chosen independently and uniformly along its length. What is the probability that the three resulting pieces can form a triangle? Justify the answer. So, unlike the first problem, this one does need that extra uh intelligence from Opus. You can see here it called it called both the Opus and the Sonnet. And so, um you can see here the the results that it gave back, which isn't the important part for now. But, if we scroll down here, we can see um under the tool call here, I know it's a little small here, um the tool the tokens in and out for both Sonnet and Opus. So, again, we we chose Sonnet for the model to use, but gave it the tool the advisor tool to call up to Opus when it needs that extra extra intelligence. So, if I scroll down here to um right here around line 123 here, you can see the message request that calls out. You can see us loading in that advisor tool. Um and you can see that the model was uh the executor model, which we said was was um was Sonnet. So, again, let's try let's try one more. I have a third problem. We'll see what happens here. Um prove that every prime P greater than three and the number of P squared minus one is divisible by 24. Okay, that's a pretty seems like a pretty complicated math problem to me. I definitely don't know it. And so, let's see if this one calls out to uh to Opus. All right. So, here's our answer. Um and again, this one did use the advisor. You can see here um if I highlight up here, it says server tool use advisor. Um Anthropic for the full transcript to Claude Opus 47 server side. Right? So, again, this is all one um one call out. Um we don't need to make multiple calls out. One uh one client request in response. Um and you can see here the portion that were both Sonnet related as well as portions that were Opus related and so you can see here it gave us the mathematical proof for this this problem. And if we scroll down towards the bottom much like before we can see both the iterations of the Sonnet call or the the Sonnet processing I should say it's all the same call as well as the number of iterations is just one here for the Opus and you can see that the tokens in and out that were used along with the the time. So again it's pretty neat really kind of changes the way we design right and the good thing about this that it's it's a drop-in feature right you don't have to change your call you can just provide this tool to your Sonnet or Haiku calls and it will call up to Opus when it needs that extra intelligence.

</details>
