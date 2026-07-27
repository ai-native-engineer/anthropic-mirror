<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486161 -->

## What you'll learn

*Estimated time: 30 minutes*

By the end of this lesson you'll be able to:

* *Evaluate AI-generated work across five lenses: correctness, quality, fit, experience, and responsibility*
* *Raise your quality bar beyond "it works" by learning failure modes specific to AI-built products*
* *Catch AI's predictable technical blind spots before they reach production*

## Discernment for code

*(5 minutes)*

When AI can spin up a working product in minutes, “working” stops being the bar. You’ll learn where AI-built products typically fail, the technical blind spots that surface in production but not in development, and how to build the taste that AI doesn’t have.

The Five Lenses of Discernment

Lens 1 is easy to test — run it and see. By Lens 5, you’re making judgment calls AI can’t make for you.

Lens 1Functional Integrity
Lens 2Production Readiness
Lens 3Problem Fit
Lens 4Experience Quality
Lens 5Responsible Impact

Lens 1

Functional Integrity

Does it work?

✓Produces correct output for real inputs, not just test data

Common AI failure

Code that passes unit tests but breaks on real data the prompt never covered

Lens 2

Production Readiness

Does it work well?

✓Handles concurrent users without race conditions

Common AI failure

Smooth in dev, broken under load or behind a real infrastructure stack

Lens 3

Problem Fit

Is it the right thing?

✓Solves the user’s actual need, not just the literal spec you wrote

Common AI failure

Technically complete feature that addresses the prompt but misses the underlying need

Lens 4

Experience Quality

Is it good?

✓Users can complete the core task without help or instruction

Common AI failure

Generic UI patterns that technically work but feel uninvested — confused or frustrated users

Lens 5

Responsible Impact

Is it responsible?

✓Transparent about AI’s role — doesn’t present generated content as verified fact

Common AI failure

AI-generated content presented as authoritative, or a demographic left out by default

#### Key takeaways

* **Code that runs can still fail.** The default AI output is technically complete but often misses the point.
* **AI has predictable blind spots** in concurrency, security, and anything that only breaks at scale.
* **Taste is a builder skill.** AI delivers functional. Making it worth using is on you.

## Exercise

### User testing the Clinic project

Put your build in front of a partner playing a patient or clinic admin — don’t explain, don’t help. Watch where they get confused, what they ignore, and what they wanted that you never built. Write down three things you’d change and which lens each falls under.

## Lesson reflection

* Which of the five lenses do you naturally apply, and which do you have to remind yourself to check?
* When AI produces something that isn’t good enough, what’s your instinct: fix it yourself, or describe it better?

## What's next

You’ve stress-tested the Clinic Wait Time Checker through the lenses you tend to skip. Next, you’ll look at the same tool through a different lens: how does it actually feel to use?

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform?usp=header).

#### Acknowledgments and license

*Copyright 2026 Anthropic. This course was developed in partnership with CodePath, building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*
<!-- youtube: YWVDXsUf8NY -->

# AI Fluency for Builders

[![AI Fluency for Builders](https://img.youtube.com/vi/YWVDXsUf8NY/hqdefault.jpg)](https://www.youtube.com/watch?v=YWVDXsUf8NY)

<details>
<summary>자막: AI Fluency for Builders</summary>

Hi, I'm Michael, the CEO of CodePath. And I'm Kristen from the education team at Anthropic. Welcome to the AI Fluency for builders course. If you have ever shipped software, you already know that writing code is only a small part of the job. You have to figure out what problem is actually worth solving. You have to make hundreds of small decisions about how it should work, and then you have to get it into people's hands and learn from what happens next. That full process, from understanding a customer problem to shipping a solution that reaches them, is what we mean by being a builder. And AI is changing almost every part of that process right now. Most of what gets called AI training focuses on one narrow slice: writing better prompts to get better code out of a language model. That's useful, but it's not enough to develop lasting AI Fluency. You need to know what to build in the first place. And you need to evaluate whether the thing AI produced is actually right, not just technically functional, but solving the real problem, working with real users, and not creating unexpected new problems. AI Fluency is the ability to work with AI systems in ways that are effective, efficient, ethical, and safe. AI Fluency isn't a prompt library. It's a set of interconnected competencies that empower you to make great decisions regardless of the model or feature at your disposal. At the center of this course is the 4D Framework, developed by professors Joseph Feller and Rick Dakan in collaboration with Anthropic. It consists of four competencies,  delegation, description, discernment, and diligence. Think of them as the operating system underneath every collaboration you have with AI. Delegation is about decomposing a problem into parts and deciding what role AI plays at each stage. Delegating implementation to AI is usually fine. Delegating judgment, the call about whether something is actually good and ready, is usually not advised. The best builders know the difference. Description is a builder's ability to ensure that every input, from user voice to product requirements to technical specs, make it into the implementation. Most AI training hyper-focuses on ensuring code is built where the test passes. That's important, but insufficient. Any missing input or context cascades downstream. A user complains that the tool doesn't work for them. You trace it back and discover the issue wasn't in the code. It was in how you understood and described the user problem. Builders must own every aspect of description. Discernment is how you evaluate what AI gives you. Not just does it run, but does it run well? Does it solve the right problem? Is it actually good to use and is it responsible? AI has real blind spots. It can produce code that's locally correct, but breaks under load. It can generate UX that's functional, but confusing. Discernment is the skill of catching those gaps before your users do. Diligence is full ownership of the outcome, not just the output. Shipping is a skill with its own technical realities that AI rarely surfaces proactively. Migrations, rate limiting, monitoring. What happens when something breaks at 2 a.m. and you're the one who built it? Prototype freely. Ship selectively. And be willing to veto something you built when the evidence says it isn't right. Think of AI as a capable but very literal collaborator. It's fast, it's knowledgeable, it doesn't get tired, but it needs clear tasks, real context about why you're building something and specific feedback when it gets something wrong. Managing that collaborator well, knowing when to step in, when to let it run, how to give it the right brief is the core skill this course develops. By the end of this course, you'll approach AI with confidence and intentionality. You'll know how to leverage it to move faster without losing the judgment that makes what you build actually good. And you'll own the full building process, not just the coding slice in the middle. Let's get started. Visit anthropic.com/learn

</details>

<!-- youtube: 7J2-HzHs4c8 -->

## 자막 (영상 전사)

[snorts] [music] >> You've now built something with AI. It runs, the test pass, but so what? Think about the project we've been building. Did it handle a scenario where a patient's estimated wait time suddenly jumps from 10 minutes to 90? Did it account and solve for different patient needs? Did it build in historical biases from the existing data? A working product and a good product are not always the same thing. And when AI can produce a working product in minutes, your ability to tell the difference becomes the most valuable skill in the room. This module gives you a structure for that judgment. Five lenses and five questions to ask of anything that AI builds. The first lens is functional integrity. Does it actually work? Bugs, errors, security holes. This is where most code review stops. It's necessary, but it's not close to sufficient. In our project example, AI built sound logic to display wait times, but did it account for patient priority? What about conflicting data points in determining which one to display? When building, consider the full gamut of functional tests, unit tests, integration tests, regression tests, edge cases, end-to-end. And here's a habit that matters. AI should be building tests alongside the code, not after it. When you prompt, ask it to write test cases in the very same pass. Then build in regular checkpoints. A test suite that hasn't been run is not a safety net, it's just a false sense of security. The second lens is production readiness. Does it actually work well? Performance, scalability, reliability. What happens under load? What happens when hundreds of people try to refresh at the same time? AI has specific blind spots here. So, how do you verify this in your building process? A few concrete moves. Ask AI to stress test its own output. Have it generate production scenarios and check how the code handles them. Ask it explicitly, what production assumptions does this code make? You'll surface things that were missed in the first pass. In your project, did the code account for when the API call takes 5 seconds too long? Does the display freeze, show stale data, or fail gracefully? AI doesn't think about that. That's with you. The third lens is problem fit. Is it the right thing? Does it solve the user's actual problem, or the problem the user thinks they have? Those can diverge as you saw in the last lesson. The patient asked about wait times, and at face value AI can build an estimated wait time display. But what the patient really needed to know was if there was a pediatrician available in the next 20 minutes so they could assess if their child's fever is critical or not. AI solved the stated problem, but you need to check whether that's the real problem. The fourth lens is experience quality. Is it actually good? Is the experience clear, intuitive, accessible? AI doesn't have taste, it has patterns. It will give you a competent interface that no one enjoys using. For a clinical wait time tool, that's not just an aesthetic problem, it's a patient safety issue. It's your job as the builder to notice this and translate it into something concrete and fixable. We'll talk more about experience discernment in the next lesson. The fifth lens is responsible impact. Is it responsible? Bias, privacy, unintended consequences. Who could this harm? What does it assume about the user that might not be true? Let's look back at the clinical wait time tool. Is the algorithm estimating wait times trained on historical data? If that data reflects existing bias, systemic inequities contributing to longer wait times for certain demographics, the model may reproduce that same pattern. It won't flag it, it will just display a number. Build guardrails. Ask AI to name its bias as it builds. And most importantly, question all assumptions. Most engineering education stops at the first two lenses, but builders need all five. And here's what you'll find when you start applying them. The biggest problems are almost never at lens one. AI is good at producing code that runs. It needs your oversight to produce a product that matters. One more thing. When you find something that isn't good enough, notice your own instinct. Do you reach in and fix it yourself, or do you go back and describe better what you needed? Neither is wrong, but the pattern tells you something about how you're working with AI, and whether you're building discernment or just building. All right, it's time to apply these lenses. Let's go.
