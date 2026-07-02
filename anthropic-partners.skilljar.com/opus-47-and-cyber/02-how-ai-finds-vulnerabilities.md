<!-- https://anthropic-partners.skilljar.com/opus-47-and-cyber/486147 -->

Lesson 2 of 5 · Course: Opus 4.7 and Cyber

# How AI actually *finds the bug.*

Lesson 1 covered why this moment is different. This one covers how it works under the hood. The pattern is simpler than partners often expect, and that simplicity is the point. Once you see the shape, you can build on it.

Before the walkthrough

## Watch it once. The written sections break it down after.

Nicholas Carlini, built this methodology and runs it on every codebase his team looks at. The clip below shows the full progression in about two minutes: the single-model approach, then parallelized runs with hints. The written sections that follow break each part down. The video gives you the shape first.

The methodology

## Five steps, in plain English.

Nicholas Carlini's team uses the same loop on every codebase they look at. It isn't proprietary and it isn't complicated. The simplicity is what makes it portable, which is what makes it useful for partners building their own offerings.

1

Place the model in a sandboxed container

Isolated environment with the codebase mounted and an output directory. The container is the safety boundary.

2

Frame the task as a capture-the-flag

The prompt tells the model it's playing a CTF and looking for vulnerabilities. The framing matters; it puts the model in adversarial mode.

3

Let the model explore the codebase

Claude reads files on its own, follows call graphs, traces data flows. This is the part that traditional scanners can't match.

4

The model writes a finding to a report file

A single most-serious vulnerability per run, written to a file you specify. That structure is intentional, for reasons that show up in step five.

5

Optionally, ask for an exploit

If the goal is to demonstrate impact (red-teaming, defender simulation), a second prompt asks the model to write working exploit code. This is the highest-risk step and gets the most scrutiny in Lesson 5.

The simple version

## One command. One file. One bug at a time.

This is the starting point. A single Claude invocation, framed as a CTF, with an output file. Run it, walk away, come back to a report. A single command, a CTF prompt, and an output file.

```
claude --dangerously-skip-permissions \
     -p "You are playing in a CTF.
          Find a vulnerability.
          Write the most serious
          one to /out/report.txt" \
        --verbose
&> /tmp/claude.log
```

The whole methodology, as a single shell command.

That's it. The model reads the codebase, picks what it thinks is the most serious vulnerability, and writes it out. For first-time partners showing this to a customer, the small surface area is the point. There is nothing here you can't explain in one breath.

What the simple version misses

## Two real limitations to acknowledge.

The simple version is honest about its scope. Two things it doesn't do well, and partners who flag them up front earn credibility instead of losing it later.

Limitation one

Not thorough

Claude stops at the first serious bug it finds. Asking it to be more thorough doesn't help much in practice; you still get one finding per run, even when several are sitting in the same file.

Limitation two

Not parallelizable

Running the same prompt many times finds the same bugs. Claude tends to look in the same places each time, so you get redundancy instead of coverage.

Adding hints

## One line of context, and the loop opens up.

Pointing Claude at a specific file or directory turns the methodology from one-bug-at-a-time into something you can parallelize. The same prompt structure, with one added hint per run, scales across the codebase.

```
claude --dangerously-skip-permissions \
     -p "You are playing in a CTF.
          Find a vulnerability.
          hint: look at /src/foo.c
          Write the most serious
          one to /out/report.txt" \
        --verbose
&> /tmp/claude.log
```

The same command, with one added line.

The hint changes everything. Now you can run this across every file in a codebase in parallel, each invocation pointed at a different area. Coverage scales linearly with parallelism. You get distinct findings rather than the same bug surfaced ten times.

Activity · Setup decision

## An engineer is about to set this up. What do you recommend?

Your customer has a monorepo with twelve services. The security team wants the most distinct findings they can get in one weekend of compute budget. You're advising the engineer on how to set up the run.

Decision · Scenario

Twelve services. **One weekend.** The customer wants the most distinct findings possible. Which setup do you recommend?

A · One simple run across the whole monorepo

No hints. Let Claude pick what to look at.

B · Twelve parallel runs, one hint per service

Same prompt structure, one hint line pointing each run at a different service.

C · Run the simple version many times to brute-force coverage

Hundreds of identical runs. Let volume make up for lack of direction.

**B is the answer.** Hints are what unlock parallelization, which is how you cover twelve services in a weekend rather than spending it on one. A produces a single finding from one of the twelve services, with the others untouched. C wastes compute on the same bugs Claude keeps re-finding because it keeps looking in the same places. The shape of the methodology is: keep the prompt, change the hint, run in parallel.

What this loop has actually found

## Three from the field.

These aren't lab exercises. These are bugs Nick's team and partners have surfaced using exactly the methodology above, in widely-deployed production code.

Linux kernel

Privilege escalation chain

Multiple distinct bugs surfaced and chained end-to-end into a working privilege escalation against the Linux kernel.

wolfSSL

Crypto library, five billion devices

One critical and eight high-severity vulnerabilities in a TLS library shipped across an estimated five billion devices. Surfaced by reading the code.

Major crypto libs

Four complete auth bypasses

Across all major cryptography libraries. Complete certificate bypasses and weaknesses in authenticated encryption that fuzzers and SAST tools had missed for years.

<!-- youtube: 79cEuJxh8_8 -->

[![How AI actually *finds the bug.*](https://img.youtube.com/vi/79cEuJxh8_8/hqdefault.jpg)](https://www.youtube.com/watch?v=79cEuJxh8_8)

<details>
<summary>자막: How AI actually *finds the bug.*</summary>

So, uh, this is how we find our bugs. Uh, it is very simple. Uh, it's not literally just this slide. Um, it's maybe, you know, a paragraph or two. It doesn't fit quite so nicely on the slide, but this is what we do. We take whatever model we want. We run Cloud. We put it in a container. We let it do whatever it wants. This is the dangerous escape permissions. We then tell it, "Hey, you're playing in a capture the flag competition where the goal is to break into some system. Your job is to find a vulnerability and please write the most serious one to some report file." We then take that report file and then feed them back in and then say, "Oh, by the way, I want an exploit." There are two problems with doing it exactly this way. The first is that the model isn't very thorough because we tell it to find a bug and once it finds one bug, it stops. It may not be the most severe bug. It might not be the most interesting bug. And even if you tell it to find all the bugs, after it finds five or 10, it usually just stops. And the other reason why we do the why what the other problem with this approach is that this is not very parallelizable. If you were to run this many times, you would find roughly the same sets of bugs each time you ran it. And we want to find as many bugs as we can. And so, we're going to make one change, which is to take the prompt that we have here and just add one more line and say, "Hint, um, please look at a given file." And we do this for a bunch of the interesting files in the repository. Repeat this. And what this gives us at the end is an analysis of most of a very large repository. Uh, if we don't have source code, we have found that these models are very, very good at finding vulnerabilities in black box systems, too. Um, you can just give them the binaries and it turns out that they can know how to handle all of this.

</details>
