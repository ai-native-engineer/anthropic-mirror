<!-- https://anthropic-partners.skilljar.com/opus-47-and-cyber/486148 -->

Lesson 3 of 5 · Course: Opus 4.7 and Cyber

# Two models in the conversation. *Only one ships.*

Customers will ask about both Opus 4.7 and Mythos, often because they've read about the benchmark. This lesson is how to talk about the gap between them, where it matters, and where it doesn't.

Where the numbers land

## 97 versus 90, on the same benchmark.

CyberGym is the standard test for autonomous vulnerability discovery. Mythos Preview clears it at 97%. Opus 4.7, Anthropic's best generally-available model, clears it at 90%. That's the actual gap, and it's worth knowing exactly because customers will quote it back to you.

7%

The gap, in absolute terms

Mythos Preview97%

Opus 4.790%

When the question is "find any crashing input," not a specific one, Mythos Preview reaches nearly 100%. The headline gap is real, but narrower in practice than the absolute numbers suggest.

CyberGym benchmark for autonomous vulnerability discovery.

Where each model earns its place

## Finding is roughly equivalent. Exploiting is where Mythos pulls ahead.

The benchmark is one number. Underneath it, the two models do different jobs at different levels. Worth understanding both before you walk into a customer conversation.

Vulnerability finding

Opus 4.7 is the practical choice

Opus 4.7 finds almost as many vulnerabilities as Mythos. It does so cheaper and faster, with a model your customers can already use. For most cyber engagements, this is the job that matters.

Exploitation

Mythos pulls ahead, when it's needed

Mythos excels at turning a vulnerability into a working exploit: remote code execution, local code execution, cryptographic breaks, authentication bypasses. The gap there is real, and it's the reason Mythos is held back.

What 90% looks like in practice

## Opus 4.6 finding a real SQL injection vulnerability, on a real codebase.

The benchmark number tells you the model is capable. This shows you the capability in motion. A live run against Ghost CMS, one of the most popular content management systems, surfaces a SQL injection vulnerability the way a security researcher would.

That's what 90% looks like when it lands in a customer's environment: a finding with a clear paper trail, written by the model, ready for the engineer who owns the patch.

The practical version

## Both models produce more findings than most customers can patch.

This is the framing partners need most when a CTO quotes the benchmark gap. The bottleneck in real security teams isn't finding more bugs. It's getting through the ones already on the board.

The line that resets the conversation

A scanner that finds 97% of bugs and a scanner that finds 90% of bugs land in the same backlog, and most security teams can only patch a fraction of either. **The question that matters is how fast the team can act on what's already in front of them.** That's where Claude Security earns its place in your customer's stack, and where the model choice stops being academic.

Availability, today

## Opus 4.7 ships. Mythos is held back.

The other thing your customers will ask: can I get my hands on Mythos? The short answer is no, and the reason is governance. The longer answer matters for Lesson 5.

Opus 4.7

Available, today

Generally available with no waitlist, no internal-use restriction, and a commercial license. The model your customers are already running for other workloads.

Mythos Preview

Held back, for governance reasons

Anthropic is deliberately not shipping Mythos broadly. Autonomous exploit generation at Mythos's level is considered too high-risk to release without serious safeguards. Lesson 5 covers what that means in practice.

Activity · Customer question

## The conversation you'll have, almost word-for-word.

A CTO has read about Mythos. They are sceptical of starting with Opus 4.7 when something more capable is on the horizon. Pick the response that lands.

Decision · Scenario

CTO: **"Why should I start with Opus 4.7 instead of waiting for Mythos? The benchmark says it's seven points more capable."**

A · "You're right, the gap matters. It's worth waiting for Mythos."

Concede the point. Slow the customer down until Mythos is available.

B · "Opus 4.7 is what's available, and the gap mostly disappears in practice."

Most teams can't patch every finding either model produces. Mythos is held back for governance reasons that aren't going away soon.

C · "Depends on your use case. Mythos is worth waiting for in some situations."

Hedge. Leave the door open for the customer to wait.

**B is the answer.** It names the practical equivalence (most teams are bottlenecked at remediation, not detection), names the availability reality (Mythos isn't coming soon), and gives the CTO a reason to act now. A and C both concede ground that doesn't need conceding. The seven-point gap is real, but a benchmark score doesn't tell you how many of those bugs the customer's team will actually patch. Recommend Opus 4.7 with confidence.

<!-- youtube: cEvUz1fsLKU -->

[![Two models in the conversation. *Only one ships.*](https://img.youtube.com/vi/cEvUz1fsLKU/hqdefault.jpg)](https://www.youtube.com/watch?v=cEvUz1fsLKU)

<details>
<summary>자막: Two models in the conversation. *Only one ships.*</summary>

There's a very big distinction between exploiting vulnerabilities and finding vulnerabilities. And we have found that Opus 4.7 and the Opus class models are very, very good at finding vulnerabilities, too. They're They're not as good as Mythos, but the kinds of bugs that they find are quite sophisticated and are the kinds of bugs that exist because people aren't not being as careful as they ought to have been when creating the security of some system.

</details>
