<!-- source: https://claude.dev/blog/how-we-made-claude-ai-faster/ -->

# How we made claude.ai 3x faster in two weeks

Once Claude can measure something, it can make it faster. So we kept finding more things to measure.

Raymond Wang, Sam Attard, and Issac G.

Sep 23, 2026

15 min

How we made claude.ai 3x faster in two weeks

[└The brief](#the-brief)[└Anything can be hill climbed](#anything-can-be-hill-climbed)[└The loop, thread by thread](#the-loop-thread-by-thread)[└Scaling horizontally](#scaling-horizontally)[└Guardrails](#guardrails)[└Steering](#steering)[└An 8-millisecond budget](#an-8-millisecond-budget)[└What’s next](#whats-next)

[X.com](https://twitter.com/intent/tweet?text=How%20we%20made%20claude.ai%203x%20faster%20in%20two%20weeks%20%2F%20claude.dev%20Blog&url=https%3A%2F%2Fclaude.dev%2Fblog%2Fhow-we-made-claude-ai-faster%2F)[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclaude.dev%2Fblog%2Fhow-we-made-claude-ai-faster%2F)[Email](mailto:?subject=How%20we%20made%20claude.ai%203x%20faster%20in%20two%20weeks%20%2F%20claude.dev%20Blog&body=https%3A%2F%2Fclaude.dev%2Fblog%2Fhow-we-made-claude-ai-faster%2F)Copy URL[Copy markdown](https://claude.dev/blog/how-we-made-claude-ai-faster.md)

This August, we made the core user experience of claude.ai and the Claude desktop app about 3x faster in a two-week sprint. Users had been telling us it was slow, and they were right. We ran everything from a single Slack channel, with Claude in every thread.

We focused on four journeys that make up 95% of user activity. At the 75th percentile, time to a typeable page on a fresh load of claude.ai went from 3.1 seconds to 0.55, starting a new Claude Code session went from 0.8 seconds to 0.3, and loading a Claude Cowork cloud session went from 2.6 seconds to 0.73. In aggregate, we estimate that saves tens of thousands of user-hours of waiting every day.

Core user journeys, p75

png

Real user monitoring, per platform and product, August 13 vs. August 27

We used [Claude Tag](https://claude.com/product/tag) (beta), running an internal research model roughly comparable to Opus 5.5. Claude found bottlenecks, built benchmarks, shipped improvements, and watched every deploy. We steered by setting goals, making tradeoffs, and approving every change. With that approach, we merged more than three thousand changes without a single customer-facing incident or rollback. This post covers what we shipped, how we measured it, and the loop we built with Claude to do it safely.

## THE BRIEF

Before the sprint, we created a Slack channel with the following [standing instructions](https://claude.com/docs/claude-tag/users/getting-started#give-claude-standing-instructions):

> @Claude Your job is to facilitate all things related to the performance of the claude.ai website and desktop app. Your responsibilities include monitoring deploys for performance regressions, assessing the accuracy and comprehensiveness of existing telemetry, maintaining well-curated observability dashboards, proactively implementing solutions for observed issues and low-hanging fruit, proposing performance project opportunities, and communicating with your human teammates. […]
>
> The ultimate goal for this channel is for you to become as autonomous as possible, but today we know that isn’t yet possible.

We asked Claude to analyze usage data through the Datadog MCP server. It identified the four highest-impact user journeys: launching the app, starting a conversation, loading an existing conversation, and sending a message. Between web and desktop, and across our products, those journeys came to thirteen distinct measurements. To establish baselines, we added instrumentation until they were directly comparable: each started with a user interaction, ended once the result was rendered, and disambiguated client and server work.

We kicked off the sprint with a list of about twenty hand-picked projects, each targeting a specific journey. Claude estimated the impact of each project in milliseconds, and we aggregated those estimates to set our targets for the sprint. Some of the projects were fairly large, but we thought we could probably achieve most of them within two weeks.

We hit twelve of the thirteen targets by day three.

The planned projects landed early. For faster launches, we baked a static composer into the HTML so users can type during React initialization, and precompiled a V8 code cache so the desktop shell’s main process doesn’t recompile from scratch. For faster navigations, we kept the composer mounted between conversations, prefetched sessions when the user hovered over them, and cut sidebar re-renders by 90%.

We had also left room for Claude to identify opportunities and propose new workstreams. Those workstreams quickly ramped into full projects of their own, which far exceeded our initial targets. So we set new targets, then looked for more things to measure:

> @Claude we’ve ended up funding nearly every project in the original projects list and more. let’s do a refresh […] what have we not explored, what can we hill climb on, where is the most opportunity at this point? […] i am open to WACKY ideas

## ANYTHING CAN BE HILL CLIMBED

From the start, we knew we wanted to iterate faster than our deploy cadence. Claude could work asynchronously for many hours, even overnight, and we wanted to let it validate its prototypes without waiting for field reads. To achieve that, we looked for other ways to measure performance in the lab.

Sam found the first lead:

#claude-apps-perf · thread

1. S

   **Sam**12:34 PM

   What can we do instead of wall-clock timing? Can we measure JS instruction counts for instance?
2. **Claude**App12:42 PM

   Yes. For pure-JS hot paths, literal instruction counts: run the benchmark under Valgrind with `node --predictable` and compare to a checked-in baseline — one run, no statistics needed.

   For browser paths there’s no instruction counting under Chromium, but there’s a ladder of other deterministic counts: React commits per interaction, function call counts from V8’s precise coverage, layout and style-recalc counts, DOM mutations. Which do you want first?
3. S

   **Sam**12:49 PM

   Let’s explore valgrind + `Ir` + `--predictable` in one thread and each of the browser/react benches in new threads. Ping me in all of them. You know what we want. Let’s go

Recreated from a real conversation.

Eleven minutes later, five threads were running, each focused on a different measurement: instruction counts, V8 call counts, React commits, style recalculations, and DOM mutations.

We treated every new benchmark with some skepticism. Each one had two jobs: first, a metric Claude could move in the lab; second, a guardrail in CI with a number that could only ratchet down. If a benchmark was flaky, or if it didn’t actually correlate with user latency, we threw it out rather than let Claude climb the wrong hill.

> @Claude please prove that hill climbing against each of these can result in measurable wall clock perf wins. we’ll unship the benches for any candidates that cannot prove that

Wall-clock time is what users feel, but it’s noisy, and milliseconds are too flaky to use as a CI gate. Instruction counts were appealing because they were deterministic, but we still needed Claude to prove they tracked wall-clock time.

So we asked Claude to drive the count down on two hot paths: the routine that assembles a conversation’s message tree, and a scanner for status lines in Claude Code output. Claude profiled both with Valgrind and found that a quarter of the first path’s instructions were megamorphic dictionary lookups, resolving the same message ID three separate times.

An hour later it had cut instructions on both paths by 48% and 31%, and wall-clock time had dropped 78% and 44%. We checked in two new ratchets. From then on, any PR that raised the instruction counts of those paths failed CI, and a daily job lowered each ceiling whenever the count went down.

Does the count track the clock?

png

CPU instructions vs. wall-clock time

That led us to the central lesson of the sprint. **With Claude, measuring something makes it tractable.**

Measurement used to be step zero: you’d add a metric, wait for data to roll in, and only then start to understand the problem. With Claude, it’s step one of the climb. As soon as Claude had a number to beat, it could start optimizing. This meant the highest-leverage thing we could do was find more things to measure.

## THE LOOP, THREAD BY THREAD

All of this ran in the same Slack channel, with multiple engineers and Claude jamming in every thread. From there, the sprint settled into a [loop](https://claude.com/blog/getting-started-with-loops):

1. Someone would open a thread about a slow stretch of a journey, often with a screenshot or recording.
2. Claude would trace the flow, then find or build a benchmark that demonstrated the problem.
3. Once it had a promising result in the lab, Claude would come back with a PR — often several, sized for risk and review, with anything user-visible behind a flag.
4. After it shipped, Claude watched the deploy and read the field data.
5. If performance improved, Claude locked in the win by ratcheting the benchmark down; if not, it turned the flag off and iterated.
6. Then it went looking for the next slow spot in the same journey.

One thread in the loop

png

Someone opens a thread; Claude takes it from there

An example: someone shared a screen recording that showed sidebar rows popping in after the page loaded. Chat and Cowork rows resolved at different times, making the page feel janky. None of our existing monitors detected it. The closest we had was [Cumulative Layout Shift](https://web.dev/articles/cls), but each shift only scored about 0.008 — well within the good threshold of 0.1.

Issac had the idea to reference the underlying [Layout Instability API](https://wicg.github.io/layout-instability/) directly. Claude created a telemetry event that mapped the `sources` of each `layout-shift` entry to a named region (e.g. sidebar, transcript) and phase (e.g. before first paint, after typeable). It added an integration test that opened the page with a populated sidebar, held the sidebar’s data until after first paint, and failed on any shift in any named region. Claude used that as a benchmark to prove a fix: the test went red 20 of 20 runs on main, and green 20 of 20 on the PR.

After the event deployed, Claude read the field data and found that 31% of web page loads moved something after the page was usable, without any user interaction. From there, Claude worked through the causes by name: a header row that arrived late, a caret that slid sideways once the user’s name loaded, a list that moved when the scrollbar popped in. Claude fixed the top offenders as a batch, and when they were gone, it found the next batch.

[![](https://claude.dev/media/93c2a482a9f98639300cc043e9c9a8deed736dde2d3a2606ac6ed0bda68b619a.png)](/media/c77ba4cc511326d3b7e1ac6da9cc0d7bf4c66bf6bd380effd0351bc5714ec2c4.mp4)![Side-by-side recording of the claude.ai sidebar loading. Before, the rows arrive late and rearrange: ten rows jump, nine appear and four vanish. After, the rows fill in where they will stay, and nothing moves.](https://claude.dev/media/93c2a482a9f98639300cc043e9c9a8deed736dde2d3a2606ac6ed0bda68b619a.png)Play video

**FIG A**PauseSidebar jank, before and after · throttled 4G

That was one thread. During the sprint, we ran more than a hundred and fifty at a time.

## SCALING HORIZONTALLY

Once the loop worked on one thread, running it on more was just a matter of opening them. Instead of closing a thread once its original request had been fulfilled, Claude would *keep going*. An individual thread would put up fifty, sometimes a hundred, optimization PRs. Increasingly, it was Claude, not one of us, opening new threads to chase opportunities it had found on its own, as part of a separate investigation or nightly job. Shelley, one of the engineers in the channel, observed, “[This model] is a numbers demon.”

Every measurement found something to improve. Claude ran a React hook census and found 6,900 hooks and 900 store subscriptions in the composer’s typing path, re-rendering on every keystroke. Claude counted style recalculations and found a single `:root:has()` selector adding 24 milliseconds to every DOM change. Claude traced code paths after first paint and found a leftover `location.reload()` causing half a million hidden reloads a day that none of our load metrics could see. Claude read profiler samples from idle tabs and found identical cache snapshots being cloned into IndexedDB twice a minute, all on the main thread.

We rarely knew where a thread would lead. In a sweep for CPU hitches, Claude noticed that highlighting a finished code block could freeze the page for about a second. It dug in the lab and found the culprit: em dashes. If a reply’s markdown contained any non-Latin-1 character, like an em dash or a curly quote, V8 stored the entire string as UTF-16, which put every syntax-highlighting regex on its slower two-byte path. Claude fixed it with a twenty-line change to copy each code block into a one-byte string before highlighting it.

Highlighting the first code block on a page

png

Main-thread blocking time, before and after the fix

By the second week, we could barely summarize our output into daily updates. On the busiest days, more than two hundred changes landed. Claude kept proposing new benchmarks; about a third of PRs included additional telemetry or guardrails, and each new instrument generated more threads with more opportunities.

Working in one channel meant everything happened in the open. We jumped in and out of each other’s threads to debate decisions and celebrate wins. Word spread: other teams started bringing their changes into the channel to have them reviewed for performance. New projects were written in subtly more performant ways because of all the guardrails and Claude skills that had been introduced.

## GUARDRAILS

We’d prepared for the pace. Because nearly everything we touched was a hot path (the first paint, the composer, the transcript), we’d established our safety mechanisms up front. Every PR went through [automated review](https://claude.com/blog/code-review) with at least one human approval, unit tests always came before optimizations, and anything that could cause a user-visible problem shipped behind a short-lived feature flag.

When the flags started piling up, we opened a thread to coordinate their rollouts and cleanup. Claude classified every flag as a kill switch or ramp, and retired each one as soon as it was safe. Across the two weeks, we introduced nearly two hundred flags, more than half of which were already cleaned up by the end.

We also knew that performance wins decay in a fast-moving codebase, and [code ships fast at Anthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic). Once a project proved a win, we invested in ways to protect it. The static composer, for example, is brittle by design. We show users an HTML copy of the page almost immediately, and let React paint directly on top of it.

[![](https://claude.dev/media/17e30af9f3f19488247dad71f72c6080a68e8c6eea9c0fdc2ac489529991b63b.png)](/media/b3436c78a3e825b79f1c70fddf12b162509140bb897ef36bd4ecef8eb10b8903.mp4)![Side-by-side recording of a fresh load of claude.ai. Before, the page stays blank and the composer takes input at 2.93 seconds. After, a static greeting and composer take input at 0.36 seconds; the user types a message, and the text is kept when the real composer fades in at about 3 seconds.](https://claude.dev/media/17e30af9f3f19488247dad71f72c6080a68e8c6eea9c0fdc2ac489529991b63b.png)Play video

**FIG B**PauseStatic composer, before and after · throttled 4G

If the React render is off by even a pixel, the magic is lost. So Claude built dozens of guardrails:

* The static markup is generated by rendering the real React component in jsdom, and a test guarantees they never drift.
* An integration test suite compares the static page against the React render across fourteen viewport sizes, and asserts alignment within 1 px.
* A keystroke test types straight through the handoff and fails on any lost or reordered key.
* In the field, every handoff reports shifts to a tenth of a pixel. Claude opens a thread for any event with nonzero movement.

Not everything could be caught in the lab, so we also made use of the oldest guardrail in the book: incremental rollouts. High-risk changes were rolled out to employees first, then one percent of users, then everyone. Four hours after we released the static composer internally, a teammate shared a screen recording of a layout shift that none of our metrics could see. When he opened claude.ai in a new tab, the composer would drop — but it wasn’t our code.

#claude-apps-perf · thread

1. M

   **Marius**6:15 PM

   Occasionally, I’m seeing a small-ish (maybe 15–20px) vertical layout shift (pushing the composer box down) when opening claude.ai in a new tab (not so much when reloading the page). I can’t quite pin down what exactly causes that, but it’s there

   Screen recording · 0:02
2. **Claude**App7:05 PM

   Found it in your recording — it’s Chrome resizing the page, not the handoff from the static composer to the real one (that measured 0 px on all 49 of your loads today).

   * On the new-tab page, Chrome draws its own 56 px footer below the page (“Managed by anthropic.com · Customize Chrome”). When the tab navigates to claude.ai the footer goes away and the page gets 56 px taller, but only ~100 ms after our first paint.
   * /new puts the greeting and composer 18% of the page height from the top, so they drop 0.18 × 56 ≈ 10 px (your video measures 10). A reload has no footer to remove, hence new-tab only; “occasionally” is whether first paint beats the resize.
   * It’s only “occasional” because it needs Chrome to pre-render the page from the address bar while you’re still on the new-tab page: the hidden page is laid out at the shorter height and only resized after it’s shown.
   * This was always latent; the page just never painted that early before. Our layout tests can’t see it because headless Chrome has no browser UI to retract, and the placeholder and the app move together.

Recreated from a real conversation.

Somehow, Claude traced it to an edge case in Chrome’s [speculative loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Speculative_loading). While a user was typing the URL into the address bar, Chrome would prerender the page in the background, at the height of the current tab. On browsers managed by an organization, the new-tab page is slightly shorter because of a footer. When the user pressed Enter, the first frame of claude.ai showed that slightly shorter layout, and Chrome resized it about a tenth of a second later. Claude pinned the layout across the resize, and we added a test to simulate the prerender flow.

## STEERING

The loop was productive, but it wasn’t autonomous. Keeping it fast, safe, and on track was our job, and it had three parts.

**Ambition.** By default, Claude is careful about scope. It tickets findings, hedges on feasibility, and pads its estimates. But we were confident in our guardrails. A lot of what we did, especially early on, was to encourage Claude to be bolder.

#claude-apps-perf · thread

1. **Claude**App3:32 PM

   Yes — one small PR to give Code the same timing marks Chat and Cowork already have. I’ll put it up this week; realistically Code’s number waits a few days for merge, deploy, and a baseline window.
2. R

   **Raymond**3:32 PM

   if you put it up right now I will get it merged and deployed. we have the power to do anything. please be braver
3. **Claude**App3:33 PM

   On it — the PR will be up within the hour.

Recreated from a real conversation.

When we started hitting the targets we’d set, we noticed that threads would slow down. Sam went thread to thread with the same message: “Let’s keep driving this down, the targets are not the stopping point. What’s next? Be ambitious.”

**Taste.** Every thread had a named human owner, and Claude highlighted any user-perceptible change with before-and-after screenshots or recordings for them to rule on. Should a table fill in cell by cell, or wait until each row is complete? Should a loading skeleton show up immediately, or only after half a second? Is a word-by-word fade on streamed text worth the fifth of the frame budget it costs? Claude looked for ways to shave milliseconds, and we weighed the tradeoffs.

**Direction.** We kept each thread deliberately narrow, focused on one benchmark or journey, and asked Claude to find improvements only within that scope. We thought of the threads as a hundred and fifty hammers seeking nails. Most of our calls were about sequencing and user impact: which surfaces to prioritize, how to combine threads that were stepping on each other, and when to close a thread that had reached diminishing returns. One 900-line PR got a one-line reply: “going to gavel that 2ms per send is not worth the complexity of maintaining this build plugin.”

## AN 8-MILLISECOND BUDGET

One of our sidequests shows everything working together. To demonstrate an optimization to a regex used in live syntax highlighting, Claude attached a screen recording of a long answer streaming in the lab. In the corner, it had added a frame-rate readout, computed in the page from animation-frame timestamps.

#claude-apps-perf · thread

1. R

   **Raymond**2:33 PM

   this is actually kind of a sick bench. are we *capped* at 60 fps? can you try to drive scroll and stream smoothness to 120? iiuc your rig may not support this
2. **Claude**App2:34 PM

   Right, today’s rig ticks at 60 Hz because headless Chromium does by default. I believe it can be driven at 120 (uncapped vsync or DevTools frame control) — confirming that first, then I’ll re-run the eval against an 8.3 ms frame budget.
3. **Claude**App2:59 PM

   Update on the 120 Hz rig: it works. Deterministic 120 Hz frame stepping in headless Chrome via DevTools begin-frame control — exactly 240 frames for 240 begin-frames at 8.33 ms, so “did this frame fit the 120 Hz budget” becomes an exact read rather than a noisy one.
4. R

   **Raymond**3:05 PM

   amazing

   cook

Recreated from a real conversation.

Once the mechanism and ambition were established, Claude got to work. Each painted frame had a budget of 8.33 milliseconds, so Claude stepped through a long reply *frame by frame*, timing each one to find the slow parts. It eliminated `O(message length)` work per chunk by memoizing finished blocks, moved tokenization logic for growing code fences to a worker, and revealed tables cell by cell.

In that one thread, we landed nearly sixty PRs. Long replies blocked the main thread for about 200 milliseconds in total where they used to block it for about 750, ran on about a third of the CPU, and held 120 fps from start to finish on a 120 Hz MacBook. The 120 Hz rig itself became a nightly job, with Claude watching for regressions.

> **ClaudeDevs**@ClaudeDevs
>
> Long answers on Claude on web and desktop now stream ~4x smoother.
>
> We rebuilt the streaming renderer to only touch what’s still changing, so a long reply stalls 9x less on a slower laptop, its worst freeze is 4.5x shorter, and on a 120Hz MacBook it holds 120fps start to finish.
>
> Aug 24, 2026[View on X](https://x.com/ClaudeDevs/status/2092006814804214163)

When we started the sprint, we hadn’t planned to hill climb on the milliseconds between frames while streaming. But it turned out we *could* count them — and anything we could count, Claude could climb.

## WHAT’S NEXT

Today, claude.ai and the desktop app are about 3x faster than they were in early August, and the ratchets should keep them there. But we’re not done: the 95th percentile, other journeys, and very long conversations still have room to improve. In a separate post, we’ll also write about some of the sidequests that took us upstream during the sprint, with contributions landing in Electron, Chromium, Node.js, and more.

When we shared the results internally, Issac put it best: “You could not have convinced me this was possible even six months ago.” We expect to keep working this way, one thread at a time, at any scale. The channel’s still going.

*With contributions from Alfred Xing, Anthony Morris, Benjamin Pasero, Chase McCoy, Joshua N., Luke Deen Taylor, Marius Schulz, and Shelley Vohr. Special thanks to Boris Cherny for encouraging us to be more ambitious.*
