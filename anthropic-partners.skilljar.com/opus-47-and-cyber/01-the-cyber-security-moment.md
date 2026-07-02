<!-- https://anthropic-partners.skilljar.com/opus-47-and-cyber/486146 -->

Lesson 1 of 5 · Course: Opus 4.7 and Cyber

# AI is changing *how bugs get found.*

Traditional scanners and fuzzers have served the industry for decades. They're still useful, and they're hitting their limits at the same time. This lesson is about what AI is now surfacing in real production code, and what that means for the customers you work with.

Why now

## Traditional tools have a ceiling.

Regex-based scanners and SAST tools are good at the bugs they were designed to catch. They look for known patterns: SQL injection shapes, common buffer-handling mistakes, unsafe API calls. The work is mechanical and repeatable, and it leaves a real gap.

The bugs they miss are the ones that need reasoning. Bugs that depend on how a function is called, on the state of memory across a sequence of operations, on the interaction between subsystems that no individual rule was written to inspect. These bugs are still in production code, often for decades, and they don't show up until somebody reads the file with intent.

Real bugs, found by reading code

## Six numbers worth knowing.

These are vulnerabilities Nicholas Carlini, a Research Scientist at Anthropic, his team, and partners have surfaced with Claude in production codebases. None of them are theoretical. Several of them sat in widely-deployed code for years, in some cases decades, before AI read the file and noticed.

27yr

remote-crash bug

OpenBSD

Unnoticed in the source tree since 1998. Found by reading the code.

16yr

bug missed by fuzzers

FFmpeg

Existing fuzzers had hit the surrounding code more than five million times without catching it.

10

full priv-esc attacks

Linux kernel

Multiple distinct bugs chained end-to-end into a working privilege escalation.

5

billion devices affected

wolfSSL

One critical and eight high-severity vulnerabilities in a cryptography library shipped across an estimated five billion devices.

4

complete auth bypasses

Crypto libraries

Across all major libraries. Includes complete certificate bypasses and weaknesses in authenticated encryption.

2hr

patch to exploit

Closed-source OS

Time to turn a publicly released patch into a fully working exploit, autonomously, with no human in the loop.

Source: Nicholas Carlini's research and partner engagements with Claude.

What's actually different now

## AI reads code with the context that scanners can't carry.

A scanner sees a pattern. Claude sees a function in the context of how it's used, what data flows through it, what assumptions the surrounding code relies on, and what an attacker would have to do to reach it. That's the shift that makes the numbers above possible.

The practical version

Traditional tools catch bugs that fit known shapes. Claude surfaces the ones that need reasoning: bugs that depend on context, call sequence, or cross-subsystem state. The two run together and most customers end up using both, and the question for partners is how to help them get from "we've found new things" to "we've shipped the fix."

Where you fit in

## This is a moment partners are well-placed to help with.

Security teams are watching this shift happen and asking the same set of questions. How does the model actually work? How do we set it up? What does the output look like when it lands in our backlog? How do we govern it? These are the questions you're about to answer.

The rest of this course is structured around those questions. Lesson 2 walks through how Claude finds bugs, end to end. Lesson 3 puts Opus 4.7 alongside Mythos so you understand the trade-offs. Lesson 4 shows the custom harness pattern your engineers will actually use. Lesson 5 covers the governance and the partner support that comes with all of it.
