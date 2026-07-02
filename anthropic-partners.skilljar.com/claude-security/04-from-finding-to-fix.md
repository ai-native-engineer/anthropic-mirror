<!-- https://anthropic-partners.skilljar.com/claude-security/486145 -->

Lesson 4 of 4 · Course: Claude Security

# From a finding to a *pull request.*

One click hands the finding to a Claude Code session that already knows the file and the vulnerability. The session drafts the patch; you review the diff and open a PR to GitHub. The security team still owns the review.

The full path

## Five steps. One click each.

This is the path Claude Security was designed around. Every interaction the customer has with a finding ends here, in a pull request the security team can review and merge. The shape of the flow is the product.

1

Open a finding

From the findings list, click into the one you're ready to fix. You see mechanism, impact, location, and reproduction.

2

Click *Create Fix*

Top-right of the finding view. The full finding context gets handed to a new Claude Code session, no copy-paste.

3

Claude Code drafts the patch

The session opens with the file already loaded and the vulnerability already understood. It reads the context and proposes the change.

4

You iterate

Read the diff. Adjust if needed. Ask follow-ups. The session is interactive, the same way any Claude Code session works.

5

Click *Create PR*

A pull request lands in the customer's GitHub repo. The team reviews and merges on their own schedule.

What gets handed over

## No copy-paste. No re-explaining. The session opens already in context.

When you click Create Fix, Claude Code receives the finding's full case file: file path, line, severity, category, the mechanism description, and the impact. The session can read the file before saying a word. This is often where the demo lands.

Claude Code, opened from a finding. The vulnerability details are already in the prompt.

The principle that runs through all of this

## Claude jumpstarts the work. Your customer still ships it.

The quickest way to lose a security customer is to position this as automation that bypasses their review. Claude Security speeds up the path from finding to fix without removing the security team from the loop. Framing it that way is what makes the conversation land.

A framing for the conversation

"Claude finds the bug, validates it, and proposes the patch. **Your team reviews the diff and merges.** You move from a backlog you can't action to fixes you can ship."

Activity · Customer conversation

## The head of security pushes back. What's your move?

Your customer's security lead has just heard you describe Claude Security. She's worried this is automation that bypasses her review. Pick the response that lands.

Decision · Scenario

She asks: **"Are you saying Claude can just push fixes to our codebase?"**

A · "Yes, Claude finds the bug, validates it, and ships the patch. Your team gets back the time it used to spend triaging."

Lead with speed. Position automation as the win.

B · "Not push. Claude drafts the patch and opens a pull request. Your team reviews the diff and merges."

Name the workflow exactly. Hand the review authority back to her team.

C · "Claude only finds the vulnerabilities. Your team writes the fixes from there."

Keep it conservative. Don't oversell the product.

**B is the answer.** It names the workflow accurately, hands the security team the review authority she's protecting, and reframes the productivity story without overpromising. **The traps:** A over-claims and loses sceptical security leads who hear "automation that bypasses review." C under-claims and erases the differentiation that justifies the engagement (Claude does draft the patch and open the PR). The principle that runs through both: Claude jumpstarts the work, your customer ships it.

What changes for the security team

## The shift isn't "more findings." It's fewer untouched ones.

When you walk a customer through their first month with Claude Security, the number that matters isn't the finding count. It's how many got fixed.

Before

Backlog full of "needs investigation"

* Findings stack up in a tracker
* Most don't get touched in a quarter
* Real risk lives inside the noise
* Engineering blames Security; Security blames the tools

After

Backlog of patches in review

* Each finding lands as a draft PR
* Review is fast because the diff is small and the context is rich
* Severity tags become workflow priorities, not aspirations
* Engineering and Security ship together

Your first move

## The fastest way to learn this product is to run a scan on something you own.

Pick a small repo your team has access to. Run a scan today. Click Create Fix on the first finding that surfaces. You'll have something concrete to show in the next customer conversation, and you'll have answered the questions you can't anticipate yet.

When you're talking to a customer, the credible move is the same: ask if they have a repo you can scan together in the meeting. Twenty minutes of live activity feed and a real PR is more convincing than any deck.

<!-- youtube: vmxfuiACRRk -->

[![From a finding to a *pull request.*](https://img.youtube.com/vi/vmxfuiACRRk/hqdefault.jpg)](https://www.youtube.com/watch?v=vmxfuiACRRk)

<details>
<summary>자막: From a finding to a *pull request.*</summary>

But what we think is even easier is that create fix button up at the top right. And if we click that, we pivot over into a cloud code on the web session with the vulnerability details, and it will go start fixing it for you right there. It's a cloud code session though, so you can interact with it here in the in the prompt. Hey, this didn't quite do what I want. You're not following our coding style, etc. And at the end of the day, you can click create PR, and you're right on the way to fixing it.

</details>
