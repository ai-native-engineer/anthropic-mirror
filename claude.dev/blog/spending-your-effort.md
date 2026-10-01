<!-- source: https://claude.dev/blog/spending-your-effort/ -->

# Using Claude Code: Spending your effort

What effort really is and when to use which level in Claude Code, from my own tests of three builds and a deep dive into Terminal-Bench 3.0 on Opus 5.5 and Fable 5.1.

Sep 25, 2026

8 min

Using Claude Code: Spending your effort

[└What is effort?](#what-is-effort)[└Effort curves](#effort-curves)[└Building with effort](#building-with-effort)[└How effort levels impact output on difficult tasks](#how-effort-levels-impact-output-on-difficult-tasks)

[X.com](https://twitter.com/intent/tweet?text=Using%20Claude%20Code%3A%20Spending%20your%20effort%20%2F%20claude.dev%20Blog&url=https%3A%2F%2Fclaude.dev%2Fblog%2Fspending-your-effort%2F)[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclaude.dev%2Fblog%2Fspending-your-effort%2F)[Email](mailto:?subject=Using%20Claude%20Code%3A%20Spending%20your%20effort%20%2F%20claude.dev%20Blog&body=https%3A%2F%2Fclaude.dev%2Fblog%2Fspending-your-effort%2F)Copy URL[Copy markdown](https://claude.dev/blog/spending-your-effort.md)

One of the best parts of our newest Claude models is how they respond to effort without breaking the prompt cache in Claude Code, but I’ve received a lot of questions on this from users. [What is effort](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) really, and when do you use which effort level? Why do we need effort at all?

To answer this, I decided to do a deep dive into the evals and do my own tests of effort across normal work.

At a high level, I found that effort was a great way of modulating how much verification and edgecase testing Claude did and how much of its own judgement it used. Extra effort gave better results in domains where verification and edgecase testing was more useful like hardware, code review, and security.

For normal software engineering, I’m running a loop of getting the model to interview me then implementing on low effort, reviewing what it built, and then running verification on high effort.

## WHAT IS EFFORT?

At a high level, effort gives the model an approximation of how much compute you want it to spend on the task. It’s somewhat related to your modeling of the difficulty of the task.

Think of it this way, if someone asked you to do something in 12 hours straight, you might assume they just want you to do it and try very hard. If someone asked you to do the same task in 1 hour, you’d try to get them the best version that meets their task and then expect to iterate from there.

Or, you might push back and say the task requires at *least* 3 hours and then work for 3 hours to deliver it.

You should think of effort in the same way. Claude will always try and do your task reasonably, but higher effort will involve Claude taking more independent action for judgement and verification.

## EFFORT CURVES

Fable 5.1 and Opus 5.5’s effort curves are our best yet: at each level, there is an uptick in benchmark scores and tokens consumed.

Terminal-Bench 3.0

Pass rate against tokens spent, by effort setting

**FIG A**Terminal-Bench 3.0, the same 70 tasks for every model (the 4 GPU tasks are left out). Opus 5.5 ran about three weeks later, with responses capped at 128k tokens and no GitHub or PyPI access; Opus 5’s max is its effort-120 run.

But what does this mean in practice? To evaluate this, I tried several tasks at different effort levels and pored over the benchmarks.

## BUILDING WITH EFFORT

The best way to understand how models work is to run experiments. I tried doing the same tasks at several different effort levels on Opus 5.5 to understand the work it would do. I did this on a wide variety of work, but am illustrating this with a few toy examples.

### Underspecified build task

If I ask Claude to “build a personal fitness and workout tracker app,” effort changes dramatically how fleshed out the app is, but also results in Claude making more choices along the way. At low effort, the fitness app is just a log and a simple graph. At higher effort levels the app is more complex with additional detail. At max effort there’s a heat chart.

low(1.5 min)medium(4 min)high(11 min)max(67 min)

If I wanted a simple base to iterate from, low effort would get it done. Max effort would be if I wanted Claude’s best one shot.

### Lightly specified design task

What if I have a task that is fairly specified already but I want some exploration with Claude? As an example I tried to ask it to redesign the `/config` menu in Claude Code. Every pass had roughly the same idea, to use submenus and better search.

At low effort (which took 1 minute), I got an interactive sketch that conveyed the idea but didn’t look very much like Claude Code.

At max effort (which took 28 minutes), I got a mockup that looked very much like Claude Code, along with a bunch of walkthroughs for different flows.

If my goal was to iterate and give feedback, low effort would get there much faster. But max effort gives me something much more polished right off the bat. For this particular task, I think I prefer using low effort to understand Claude’s vision.

lowmediumhighmax

### Highly specified build task

What if I gave Claude lots of details? I tried asking Claude to interview me in-depth about the fitness app and then gave that spec to be implemented by different models at different effort levels.

I found that given this spec, the models behaved much more similarly. I got designs that looked fairly similar and had similar implementations but with different details, at max effort Claude took some time to simplify a few of the details.

low(16 min)medium(22 min)high(33 min)max(79 min)

PreviousNextPause

### Takeaways

For regular software engineering, particularly new feature work, the effort level depends a lot on how in the loop I want to be. Low effort allows Claude to respond quickly with a starting point, higher effort levels will get more work done but Claude will also make more assumptions on my behalf.

A particularly fruitful loop for feature development I’ve been using is:

* Give Claude a spec and ask it to interview me about any details I’m missing
* Implement it on low effort
* Review to make sure it got the gist of it correct, iterate on low effort as needed
* Verify and test on high effort

## HOW EFFORT LEVELS IMPACT OUTPUT ON DIFFICULT TASKS

But these are obviously toy examples, where Claude is well able to complete them. What about when the difference is between Claude completing the task or not completing the task?

To find these difficult problems, you have to go to the benchmarks so I dove into one I like: Terminal-Bench 3.0, a community-sourced benchmark.

Terminal-Bench 3.0 problems can broadly be separated into categories like security, hardware, ML, science, software, operations and media. You can see all of the problems here: <https://github.com/harbor-framework/terminal-bench/releases/tag/v3.0.0>. They’re sourced from the community, so anyone can contribute.

It’s worth reading to get a sense of the type of problems these models face. I found I was surprised by the scope and ambition of a lot of these tasks. They are much more complicated than the average task I’d face.

For example, some of the tasks included:

* **Hardware** (`retro-console-soc`): build an 8-bit game console in Verilog that fits a small FPGA and renders a test ROM.
* **Science** (`takens-embedding-lean`): formally prove Takens’ embedding theorem in Lean 4.
* **ML** (`mp-checkpoint-consolidation`): merge 16 shards of a mixture-of-experts checkpoint into one file that reproduces the reference logits.
* **Operations** (`intrastat-meldung`): run a company’s month-end EU trade-statistics filing end to end.
* **Media** (`layout-config-recreation`): rebuild a poster image as an editable layout file.

### Higher effort levels help when there are many edge cases

My main takeaway from reading the Terminal-Bench 3.0 results was that **higher effort is best for tasks with lots of hidden edge cases.**

A clean example is `html-js-filter`, a Terminal-Bench 3.0 task that asks for an HTML sanitizer that strips every way of smuggling JavaScript into a page. Fable 5.1 went from 1/5 at low to 5/5 at xhigh.¹

A typical attempt at low effort takes about 2 minutes. Each of these attempts wrote a filter in roughly one pass, then tested it against a single hand-written page.

A high-effort run finishes in about 33 minutes. In the run I traced, it adversarially reviewed its first draft, then read the installed parser’s source to check for bugs, ran many clean test cases until they gave the same output as the input, ran a standard XSS test suite, and finally, wrote a random-document fuzzer.

For something as edge-cased as a HTML sanitizer, this extra effort is well worth it. Spending more tokens for thoroughness also makes sense for complex tasks with high production requirements such as performance optimization or security review.

But you don’t need this level of effort for every task.

The diagram below shows every Terminal-Bench 3.0 result and how it failed, across different models and effort levels. Overall, increasing effort tends to reduce failures due to missing edgecases (purple blocks), but does not fix when the model has the wrong approach (blue blocks).

Fable 5.1Opus 5Fable 5

Effort

lowmediumxhighmax

Replay

Fable 5.1 at low: 140 passed, 2 works on my machine, 7 overfit to the examples, 10 close, but not exact, 40 a bug its tests missed, 45 misread a requirement, 31 wrong or incomplete fix, 32 got the domain rule wrong, 25 picked the wrong reading, 38 other failures, of 370 attempts. Fable 5.1 at max: 214 passed, 1 works on my machine, 3 overfit to the examples, 6 close, but not exact, 14 a bug its tests missed, 26 misread a requirement, 10 wrong or incomplete fix, 24 got the domain rule wrong, 47 picked the wrong reading, 25 other failures, of 370 attempts.

**FIG B**Each square is one attempt. Failure kinds come from a model judge and are approximate.

### Problem areas where effort helps

One of the most interesting takeaways for me from evaluating these models on Terminal-Bench 3.0 was that there were some problem areas that benefited from effort more than others. You can see a breakdown in the following diagram:

Fable 5.1Opus 5Fable 5

Replay

Fable 5.1, pass rate at low effort → top effort: Security 64% → 87%, Hardware 34% → 75%, ML 54% → 73%, Science 41% → 61%, Software 43% → 56%, Media 18% → 30%, Operations 12% → 22%.

**FIG C**Pass rate. Low effort pools each model's two lowest settings, top effort its three highest, since categories are small.

To illustrate this, I chose a few problems from different areas from Terminal-Bench 3.0 where Opus 5.5 failed at low effort but succeeded at high effort — mostly because it tested and accounted for edge cases:

**`mvcc-lsm-compaction`**: a Terminal-Bench 3.0 task that asks for a fix to a storage-engine bug from its crash report, without breaking compaction. Opus 5.5 went from 0/5 at low to 4/5 at xhigh.

At low (about a minute per attempt), Claude would edit the code before building it or running the reproducer, and did not check that its new test would have caught the original bug.

At xhigh (about 11 minutes), Claude reproduced the crash first, wrote a randomized test against a reference that never compacts, and checked that its tests failed on half-finished fixes.

**`cli-2ph-simplex`**: a Terminal-Bench 3.0 task that asks for a CLI linear-program solver written in Python. Opus 5.5 went from 0/5 at low to 5/5 at high.

The low attempts wrote a solver in one pass, checked it with a few small problems and stopped around 10k tokens. In the final message, Claude warned it might be slow on big problems, but did not check.

During the high attempts, Claude tested its solver on random problems against a separate brute-force solver, then timed bigger ones, hit cases that ran far too long or crashed, and reworked its search.

**`gsea-proteomics`**: a Terminal-Bench 3.0 task that asks for a gene set enrichment analysis (GSEA) on proteomics data to find which of eight treatments resemble a target tissue. Opus 5.5 went from 0/5 at low to 4/5 at high.

At low effort, Claude picked a reasonable-sounding way to prep the data, ran the analysis that one way, and reported the result.

At high, Claude tried two ways of prepping the data, noticed that the list of significant treatments changed, and dug into why before choosing the correct one.

If a user were in the loop, Claude may have asked the user about the way to set up the problem, but without a user in the loop, high effort does better.

### When to use different effort levels in Claude Code

Here’s my rule of thumb on when to use which effort level:

* **Low**: for when I want quick responses that are in the loop, e.g. brainstorming, sketching, easy changes
* **Medium**: for most of my regular software engineering work, e.g. new feature implementation.
* **High**: for work where verification is important or there are edge cases, e.g. fixing a bug in a brownfield codebase.
* **Max**: When I want Claude to operate fully autonomously to solve difficult problems, e.g. end to end building and verification of an app, finding security vulnerabilities in critical software.

Try varying effort for Opus 5.5 and Fable 5.1 based on your task or even mid-conversation by using `/effort` in Claude Code and let me know if this matches your intuition.

*¹ A note on the numbers: these come from our own internal runs, 5 attempts per task, with our production safety interventions off for Fable 5.1; in Claude products, Fable 5.1’s safeguards hand some security requests to Opus. The security tasks also ran without internet access, so the per-task counts here won’t line up with the public leaderboard or the launch post. The worked examples come from individual runs, some at intermediate effort settings.*

[Sep 28, 2026Automating eval design and hillclimbing with Claude12 min](https://claude.dev/blog/automating-eval-design-and-hillclimbing/)[Sep 28, 2026Building with Claude Sonnet 5.59 min](https://claude.dev/blog/building-with-claude-sonnet-5-5/)[Sep 25, 2026What a task costs on Opus 5.521 min](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/)[Sep 23, 2026How we made claude.ai 3x faster in two weeks15 min](https://claude.dev/blog/how-we-made-claude-ai-faster/)[Sep 22, 2026Getting the most out of Opus 5.5 in Claude and Claude Code9 min](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)
