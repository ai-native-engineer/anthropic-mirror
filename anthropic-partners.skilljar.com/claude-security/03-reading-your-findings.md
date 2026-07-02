<!-- https://anthropic-partners.skilljar.com/claude-security/486144 -->

Lesson 3 of 4 · Course: Claude Security

# Seven findings in front of you. *Which three matter most?*

A scan returns a list. The job is to find the real signal in it and help the customer act on what matters. This lesson is about reading findings the way a security researcher reads them.

The list view

## More than a severity bucket. You get a strategic summary.

Most scanners drop a list of severities and walk away. Claude Security opens with a written summary of what the run found and where to start, then surfaces the findings underneath. The summary tells you the story; the list is the evidence.

![Claude Security - Findings Summary](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F436aeb9rxr1gf0g7r03dl0sle%2Fpublic%2F1779990389%2Fclaude-security_lesson4_img02_findings-summary.1779990389311.png)

Note the summary on top. That's the agent telling you where to focus.

Anatomy of a finding

## Click into one and you get a full case file.

Each finding opens into the same four-part structure. This is what your customer sees, and what their security team needs to make a confident decision.

01

The mechanism

A plain-language description of the bug. What's wrong, in the function, line by line. Start there.

02

Impact

What an attacker can actually do with it. Remote? Authenticated? One byte or full takeover?

03

Reproduction

Concrete steps to trigger the vulnerability. The bridge from finding to validation.

04

Severity, confidence, location

Side panel: where in the file, how confident the agent is, and the category it falls under.

![Claude-Security-Findings-Detail](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F436aeb9rxr1gf0g7r03dl0sle%2Fpublic%2F1779990407%2Fclaude-security_lesson4_img02_finding-details.1779990407580.png)

A real finding detail. The structure is the same for every entry in your list.

Why these findings are worth your time

## Every finding has been argued against before you see it.

Claude Security runs adversarial verification on each finding before it surfaces. A separate pass actively tries to disprove the bug. If the counter-argument holds, the finding gets dropped. What lands in your list has already survived a fight.

Activity · Triage

## Your customer has seven findings. They can patch three this sprint.

All seven are real. Severity alone won't tell you which three to fix. Reachability and what an attacker actually gains matter just as much. Read each finding and pick the three that should ship this sprint.

Pick **three findings** to fix first. After your third pick, you'll see which calls held up and why.

0 / 3 selected

Medium

Memory Corruption

Off-by-one OOB write in UDP control message parser

src/net.c:223 · remote, unauthenticated

Medium

Privilege

Pidfile creation follows symlinks as root

src/pmtr.c:384 · local privilege escalation

Medium

Logic Error / DoS

Missing PID validation enables process group signal spoofing

src/net.c:251 · requires authenticated control channel

Low

Auth

Log forgery via unsanitized executable basename

src/pmtr.c:305 · log integrity, not exploitation

Low

TOCTOU / Privilege

Symlink-following open of job stdout/stderr as root

src/job.c:681 · local privilege, exploitable in default config

Low

Memory

Off-by-one OOB read in supervisor log line splitter

src/log.c:142 · local, leaks one byte adjacent to buffer

Low

Hardening

Missing stack canaries on optional debug build target

build/debug.mk · build hygiene, not deployed

The right three

You picked X of 3 right.

**Fix first:** the UDP OOB write (remote, unauthenticated, hits memory), the pidfile symlink follow as root (local privilege escalation in default deployment), and the job stdout symlink follow (same class of root-symlink risk, also exploitable in default configs).

**The traps:** the missing-PID-validation finding looks Medium but requires an already-authenticated control channel, which most deployments restrict. The log-forgery and OOB-read findings affect integrity and information leak, not exploitation. The stack-canary item is a debug-only build target.

**The principle:** remote-and-unauthenticated beats authenticated-only. Privilege-escalation paths reachable in default deployments beat those requiring unusual setup. Severity tags are a starting point; impact and reachability are the conversation.

Reset and try again

In the customer conversation

## A finding becomes a decision. Your job is to frame the decision.

When you walk a customer through findings, the useful work is translating them. The product gives you the technical detail; the customer needs to know what it means for their risk and what fixing it actually buys them. Both sentences matter.

Try this pattern: read the finding's mechanism, say what an attacker actually gains from it, and name what the fix removes. "This is an off-by-one buffer overwrite reachable from any attacker on the network. Today, anyone who can hit your service can corrupt one byte of memory at will. Patching it closes that primitive entirely." Three sentences, and your customer can decide.

<!-- youtube: WjCNbHKLG9Q -->

[![Seven findings in front of you. *Which three matter most?*](https://img.youtube.com/vi/WjCNbHKLG9Q/hqdefault.jpg)](https://www.youtube.com/watch?v=WjCNbHKLG9Q)

<details>
<summary>자막: Seven findings in front of you. *Which three matter most?*</summary>

What's happening on the back end is quite complicated at this point. Um, even with a very simple prompt, we instruct it to spin up a wide variety of investigators and the model has enough knowledge to understand this is a C code base, this is memory um, that we need to be concerned about and this is has some network uh, exposure. So, I'm going to go spin up some sub agents to go look at those different things and it does that completely autonomously. When it actually finishes, it runs an adversarial verification process and this is super important and a key feature of uh, cloud security and also should be what everyone is using for vault fighting wherever they are. We believe this is a very strong best practice. What that means is we spin up a series of agents that attempt to disprove the finding that we originally found with a very adversarial uh, prompt which says you should assume this is wrong effectively, right? And it goes through and it investigates the code kind of from the other side. So, first we were finding the vault and now we're trying to disprove the vault. And what happens then at the end is that we look for any disprovals and that helps us take out false positives. So, we have a very high true positive rate.

</details>
