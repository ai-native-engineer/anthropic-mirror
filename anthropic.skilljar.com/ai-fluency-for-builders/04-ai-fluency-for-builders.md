<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486159 -->

## What you'll learn

*Estimated time: 45 minutes*

By the end of this lesson you'll be able to:

* *Introduce the builder's toolkit and where AI adds value at each stage*
* *Explain why delegating implementation is safe and delegating judgment is not*
* *Write acceptance tests that define done before a single line of code exists*

## Delegation & the builder's toolkit

*(5 minutes)*

Before you write a single line of code, you make a dozen decisions that shape whether what you build will matter. This lesson reframes delegation: it’s not “should I use AI here?” but “I have a customer problem — how do I break it down, and what role does AI play?”

The Builder’s Toolkit

Click any capability to see where AI fits in your build process.

▼ AI is strongest here

Empathy Design Architecture Implementation Judgment Shipping

Step 1 of 6

Empathy

AI weak

Understanding who you’re building for. AI can surface data and personas — it can’t feel the gap.

Step 2 of 6

Design

AI moderate

Translating user needs into an experience worth having. AI generates patterns quickly; you bring taste and context.

Step 3 of 6

Architecture

AI moderate

Structuring a system that holds up under real conditions. AI knows common patterns; your constraints are yours to specify.

Step 4 of 6

Implementation

AI strong

Write, debug, and iterate on code. This is where AI genuinely excels — delegate freely here.

Step 5 of 6

Judgment

AI weak

Deciding what’s right, good enough, and worth shipping. AI can list options; it can’t own the call.

Step 6 of 6

Shipping

AI moderate

Getting it in front of users and iterating. AI automates steps; responsibility is yours.

← ← ← ← ←

→ → → → →

#### Key takeaways

* **Delegation** means decomposing the problem first, then deciding what AI handles at each step.
* **Write acceptance tests** before code. They give you and AI a shared definition of done.
* As AI accelerates implementation, your value shifts to **framing problems** and **raising the bar**.

## Exercise

### The Clinic Wait Time Project, Part 1

This project threads through the entire course. You’ll return to it in every lesson, and by the end you’ll have built something real. But in this lesson, you write zero code. That’s intentional.

**The scenario:** A community health clinic needs a way for patients to check wait times before coming in. That’s all you’ve been told.

Your job this session is to do the work that comes before building. You’ll produce three deliverables.

### Deliverable 1: A Problem Brief (one page max)

Answer these questions in plain language:

* Who are the users? Be specific. Patients, yes — but which patients? What about staff? Who else touches this?
* What do they actually need? Not “a wait time checker.” What outcome are they hoping for?
* What does a great solution feel like to use? Describe the experience, not the features.
* What are the real constraints? Think budget, technical skill at the clinic, patient access to devices, privacy requirements.

### Deliverable 2: A Delegation Plan

Map the build to the six toolkit capabilities. For each one, decide which AI collaboration mode fits best: **Automation** (AI does it, you check), **Augmentation** (you and AI work it together), or **Agency** (AI operates with latitude inside boundaries you set). Make a simple table — six rows, one per capability.

### Deliverable 3: Acceptance Tests

Write five to seven statements that define “done.” Each must be concrete enough that a stranger could tell you whether the finished product passes or fails.

**Good:** “A patient with a basic smartphone can find the current wait time in under 30 seconds without creating an account.”  
**Bad:** “The system is easy to use.”

## Lesson reflection

* Where did you spend most of your time across the six capabilities on a past project? Where should you have spent more?
* If implementation became effectively free tomorrow, where would your value as a builder come from?

## What's next

In the next lesson, we move from delegation to description. You’ve decided what to build and who’s doing what — now you need to communicate that clearly enough that AI can actually execute it.

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

<!-- youtube: AWSZoy3w_nE -->

## 자막 (영상 전사)

If you spent any time building with AI, you've probably noticed something. The hard part isn't getting AI to write code, the hard part is knowing what code you want an AI to write. Many people think of delegating something to an AI as a simple yes or no question. But for builders, knowing exactly what and how to delegate is much more complex. Your customer comes to you with a problem. How do you decompose it into something that you can actually build? And what role does AI play at each stage of that work? Here's a useful frame. Imagine yourself as the lead on a project and AI is your team. A great lead doesn't just assign tasks, they frame the problem so everyone understands what they're solving. They set goals so the team knows what good looks like. They decide what to tackle first, and critically, they know which decisions to make themselves and which ones to hand off. That's delegation in the builder sense. And it starts well before any code gets written. Every builder carries a toolkit that they may not know that they have. You could boil it down to six capabilities you can reach for at any different moment in a build. AI can help with all six, but it's much stronger at some than others, and knowing the difference is a key part of AI fluency for builders. The first capability is empathy. What does the person we're building for actually need? Not what they said that they want, but what will actually truly help their work. This is where you talk to users and observe what frustrates them. AI can help you organize what you learn here, but it can't sit with a clinic receptionist and notice that she checks her phone 40 times a day because patients keep calling to ask about wait times. That observation is all you. The second is design. What should we build and why? This is where you weigh tradeoffs, make bets, and decide what matters. Should it be a text message or a webpage? Should it show exact wait times or ranges? Those are judgment calls. All AI can do is generate options, but the judgment about which option fits is yours. Third is architecture. How should the thing be structured? What are the pieces and how do they fit together? AI knows patterns. It's seen a thousand systems like the one you're sketching, but it doesn't know your constraints, your team skills, or what you need to change 6 months from now. Human plus AI works really, really well here. Fourth is implementation, writing the actual code. This is where AI is the strongest. Once you know what you're building and how it should be structured, AI can write working code effectively. This is the capability you should delegate most aggressively. If you've entered this stage without clearly defined tests and success checkpoints, you've probably skipped a step. Fifth is judgment. Does it actually work? Is it actually good? Would you put your name on it? AI will tell you the code runs, but it won't tell you if the experience feels right, whether the edge cases matter, or whether you've solved a real problem at hand. Judgment requires your expertise, standards, and perspective. Last is shipping, getting it to real users and learning from what happens. This means communication, measurement, iteration. AI can draft release notes, but it can't read the room when your user hesitates before clicking. Now look at the shape of that list. Implementation sits right in the middle, and that's where AI is the strongest. Empathy, judgment, and shipping sit at the edges, and that's where AI is the weakest. That's the key insight for this course. AI is the strongest in the middle of the toolkit and weakest at the edges. The edges are where the human work lives. The edges are where the value is. So, what does good delegation look like in practice? It looks like spending real time at the beginning of a project getting clear on who you're building for and defining what success means. It looks like inspecting the results skeptically and keeping judgment calls in your own hands. There's a temptation, once you have a tool that can write code instantly, to skip straight to building. To treat empathy and design work as overhead. Resist that feeling. The faster AI makes implementation, the more your value shifts to everything around it. The builders who thrive in this era won't be the ones who prompt the fastest. They will be the ones who frame problems clearly, who know what good looks like before they start, and who can tell the difference between code that runs and code that matters. The work starts now. Let's get into it.
