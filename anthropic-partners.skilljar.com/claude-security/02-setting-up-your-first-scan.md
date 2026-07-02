<!-- https://anthropic-partners.skilljar.com/claude-security/486143 -->

Lesson 2 of 4 · Course: Claude Security

# From an empty product to *your first finding*

A scan takes six clicks. Two of those clicks are configuration calls worth thinking about, and the rest are mechanical. By the end of this lesson, you'll know which calls to make and why.

1Access

## Open the security tab from your Claude.ai sidebar.

Claude Security lives in the same workspace as Claude Code. Look for the lock icon in the left sidebar at **claude.ai/security**. The first time you open it, you land on an empty state with a "Start a scan" prompt, ready to receive a project.

2Connect GitHub

## Install the Anthropic GitHub app. Then point it at the right repo.

Claude Security works on GitHub-hosted code, both github.com and GitHub Enterprise. Your customer needs to install the Anthropic GitHub app and grant access to the repositories they want to scan. This is a one-time step per organization.

Supported

github.com and GitHub Enterprise

Both flavours work the same way. Self-hosted Git that isn't GitHub is not supported today.

Permissions

Read access to selected repos

Customers control which repos are visible to the app. Scope it tightly during a pilot, expand later.

3Choose scope

## The first real decision is scope. Where will Claude read?

Scope controls what Claude reads. Narrower scope keeps the agent focused and the findings sharp. Point it at a wide monorepo and it has more surface to wander; the results get harder to interpret.

Decision · Scenario

Your customer has a **monorepo with eight services**. They want to demo the product to their CISO next week. Where do you point the first scan?

A · Whole monorepo

"More coverage means a better demo." Scan everything in one shot.

B · The most security-critical service

Pick the one the CISO already worries about. Run a tight scan there.

C · A random service to keep the run short

"Just need something to show in the meeting."

**B is right.** Narrow scope keeps the agent focused and the findings legible. Picking the service the CISO already cares about means the conversation in the room is about real risk, not exploration. Wide monorepos are not wrong; they're just a harder first run to interpret.

4Model and effort

## Two configuration calls. Both default to the right answer.

The scan dialog asks for a model and an effort level. Recommend Opus 4.7 unless your customer has a specific reason to use something else; that's where the depth of reasoning lives. Effort controls how hard the agent works. The dialog itself is short: repository, branch, scope, model, effort.

Decision · Scenario

Customer is paying close attention to AI spend. They want a **first scan that's defensible cost-wise**, on a non-critical service. Standard or Extended effort?

A · Standard

Reasonable depth, lower token spend. Good first impression.

B · Extended

Deeper reasoning, more findings, higher cost. Reach further.

**Standard is the right call here.** Extended runs longer and uses more tokens; you trade higher cost for additional findings. On a first scan with cost scrutiny, Standard demonstrates value without forcing a budget conversation. Save Extended for the security-critical service where the customer wants the deepest pass possible.

5Run and watch

## The agent narrates as it works. It's worth showing customers.

A live activity feed shows what the agent is doing in plain language: connecting, fetching, surveying structure, mapping entry points. Each status update is the agent's reasoning surfaced in plain language. That kind of transparency lands differently with sceptical engineers than a results slide ever would.

It's worth pausing on this in a customer demo. Most security teams have never watched an AI reason through their code. When you pause on the activity feed and narrate what the agent is doing, you'll often see the conversation in the room shift, even with sceptical engineers.

Setup principles · the short version

## Three rules that keep your first scan useful.

Rule one

Narrow before broad

Tighter scope, sharper signal. Expand the scan after the first run lands.

Rule two

Opus 4.7 unless told otherwise

It is the depth of reasoning the product was designed around. Anything else is an edge case.

Rule three

Show the scan, not just the result

The activity feed is itself the demo. The findings are the deliverable that follows.

In practice, your first customer scans will look like this: pick the service the security team already loses sleep over, point the agent there, run on Opus 4.7 at Standard effort, and show the room the activity feed while it works. That sequence builds trust and gets you to a real conversation about findings.

<!-- youtube: F_KDolVNnFs -->

[![From an empty product to *your first finding*](https://img.youtube.com/vi/F_KDolVNnFs/hqdefault.jpg)](https://www.youtube.com/watch?v=F_KDolVNnFs)

<details>
<summary>자막: From an empty product to *your first finding*</summary>

So then when I click start scan, that's what happens. You start the scan. And what it kicks off the scanner in the background. You can see some status updates in in the user user experience here, right? We have checking out the the GitHub repository, analyzing the code base. And then you'll see some things that are specific to the code base. It's figuring out where the entry points are. In this case, in my open source project, there's a little bit of network handling. And so it's it figured that out. The agent said, "Oh look, here is some network is exposed. I probably need to run down that." It's a C based code base, so it also is interested in memory safety. And so it's doing some investigations there.

</details>
