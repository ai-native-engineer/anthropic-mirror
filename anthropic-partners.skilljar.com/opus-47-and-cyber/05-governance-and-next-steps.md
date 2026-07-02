<!-- https://anthropic-partners.skilljar.com/opus-47-and-cyber/486150 -->

Lesson 5 of 5 · Course: Opus 4.7 and Cyber

# The most important conversation isn't *technical.*

Customers will ask why Mythos isn't available. Security teams will ask how the safeguards hold up under real workloads. Partner leaders will ask what Anthropic stands behind. This lesson is how to answer all three, and where to take the work from here.

Why Mythos is held back

## Autonomous exploitation is where Anthropic drew the line.

Mythos can take a vulnerability and turn it into a fully working exploit: remote code execution, local code execution, cryptographic breaks, authentication bypasses. Releasing that capability broadly is a different category of decision than releasing a scanner that finds bugs.

The risk is asymmetric. The same capability that helps defenders simulate attacks also helps attackers compress the time between a public patch and a working exploit. Anthropic's read is that the risk profile of broadly releasing Mythos is currently higher than the customer value it would unlock. So Mythos sits in research preview, and Opus 4.7 ships.

From the researcher

## Nicholas Carlini on why Anthropic drew the line where it did.

The previous section covers what Anthropic decided. This clip is Nicholas Carlini explaining why. He covers the risk calculus behind holding Mythos back, how Opus 4.7 behaves when a request crosses the line, and the principle the whole governance model rests on. Worth hearing directly from the researcher, not just reading a summary of his reasoning.

When that principle comes up in a customer governance conversation, being able to attribute it to the researcher rather than a slide makes a difference. Partners working in regulated industries have found it's the line that tends to land.

The operational model

## Opus 4.7 plus a human reviewer is the deployable shape.

For nearly every real engagement, the question isn't "find me Mythos." It's how to get useful work from a model that ships today, with the review process customers need anyway.

Opus 4.7 finds the bugs, a human reviews them, and patches move through a normal pull-request flow. This is the way changes already move in your customer's engineering org. The safeguards aren't a constraint on the system; they're the part that makes it deployable in regulated industries where "autonomous" is not an acceptable adjective.

The precedent worth naming

Anthropic is signalling that **safe first applies even when it costs revenue.** Mythos sitting in preview isn't a temporary delay until someone fixes the price. It's the company stating publicly that some capabilities don't get to ship widely yet, even when there is willing demand. Customers in regulated industries notice this, and it tends to land well in the rooms where partners are doing the work that matters.

Activity · The governance question

## A customer asks the question. Pick your response.

This is the question every partner ends up answering, sometimes within the first ten minutes of a customer conversation. There's a confident answer and there are two hedges that lose the room.

Decision · Scenario

A CISO asks: **"If Mythos's methodology can autonomously generate exploits, why isn't Anthropic just letting us use the more capable model?"**

A · Mythos is governance-restricted. Opus 4.7 plus human review gives you the same operational outcome with safeguards in place.

Name the precedent (safe first, even when it costs revenue), name the operational model, move on.

B · It's mostly a commercial decision. Anthropic plans to release Mythos when they can charge more.

Frame it as pricing. Imply the restriction is temporary.

C · Depends on your industry. You may be able to request access through a special program.

Hedge. Suggest there's a workaround.

**A is the answer.** It names the precedent (safe first, even when it costs revenue), explains the operational model that's actually deployable (Opus 4.7 plus human review), and doesn't apologise for the safeguard. B frames a serious governance decision as a pricing manoeuvre, which is both inaccurate and the kind of answer that loses CISOs in regulated industries. C hedges in a way that suggests there's a workaround, which there isn't, and you'll have to walk it back later. The confidence in A is the part that lands.

What Anthropic provides

## Four resources to lean on.

Anthropic ships more than the model. Partners building offerings in this space have direct access to the four resources below. Use them. They're how you get from a workable prototype to something a customer signs off on.

Resource one

Best practices guides and blogs

Anthropic's published guidance on security applications and LLM-based defences. The starting point for engineers new to this work.

Resource two

Cookbook for custom vulnerability finding

A working library of patterns for partners new to LLM security. Prompt templates, sandbox configurations, output handling. Designed to be lifted into your own engagements.

Resource three

Runbook and the Glass Wing harness

Reference pipelines, prompting guides, and security skills derived from the Mythos research line. The closest thing partners have to Anthropic's own internal scaffolding.

Resource four

Applied AI engineering time

Dedicated scoping and engineering time with the Applied AI team. Use it for harness work, model-refusal investigations, safeguard tuning, anywhere the model is doing something you don't expect.

Where you stand now

## Five things you can do, post-course.

A quick inventory. Each of these is something the course was designed to make you capable of by the end. If any of them feels shaky, the section it came from is worth re-reading before your next customer conversation.

1

You can position **Claude Security** in a customer conversation and name where it fits in the existing stack.

2

You can recommend **Opus 4.7** with confidence when a customer asks why not Mythos.

3

You can sketch the **five-step methodology** and explain what one hint changes about coverage.

4

You can match a customer ask to the **right offering bucket**: code security at scale, custom builds, or pre-acquisition review.

5

You can answer the **governance question** without hedging.

<!-- youtube: -WlLPPv1DwI -->

[![The most important conversation isn't *technical.*](https://img.youtube.com/vi/-WlLPPv1DwI/hqdefault.jpg)](https://www.youtube.com/watch?v=-WlLPPv1DwI)

<details>
<summary>자막: The most important conversation isn't *technical.*</summary>

Given the acknowledgement that Mythos class models are being held back because of exploit generation capability, what governance or guardrail model do you envision for safely deploying Opus class vulnerability discovery at enterprise scale? Yeah, so the thing we want to make sure of is not that no one has access to these capabilities, but that for Mythos class capabilities, we want to make sure that we're not going to enter a world where, you know, someone who's disgruntled because some company wronged them, instead of writing a bad review on Yelp or something, goes like, I'm going to go and take down their their database and delete as much stuff as they can. And like, with their normal capabilities, they would have no hope of even knowing how to start. But with a model that can autonomously find and then exploit vulnerabilities, this is the kind of thing that we imagine might be possible. And so we really want to do is to make sure that these capabilities are not something can be that can be used by people who just like want to see the world burn. Um and so we really just want to make sure that the capabilities are behind sufficient safeguards that we feel safe putting the model out there. And, you know, we we imagine that this is something that other people will have in the future. Um we in our blog post that announced Mythos said, you know, even open weight models may in the future be able to do something like this. So we're we're not imagining a world where this can never be released. We definitely believe that this is a thing that will that will happen. Um what we want to do is to make sure that um as the first company who has something like this, we are setting precedent that like it's okay to forego some amount of revenue and, you know, potential goodwill of having people use always the best model because we think it's the safe thing to do in this case.

</details>
