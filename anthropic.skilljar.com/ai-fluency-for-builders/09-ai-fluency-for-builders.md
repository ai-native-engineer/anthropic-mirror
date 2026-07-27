<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486165 -->

## What you'll learn

*Estimated time: 15 minutes*

By the end of this lesson you'll be able to:

* *Find resources to continue building your AI fluency after this course*
* *Share what you learned with colleagues who could benefit from the 4D Framework*
* *Collect your certificate of completion*

## Looking forward

*(4 minutes)*

This closing video brings together everything you've learned across the course and challenges you to put it into practice immediately with real work that's already waiting for you.

#### Key takeaways

* **AI is strongest in the middle of the toolkit.** Delegate implementation freely. Keep empathy, judgment, and shipping in your hands.
* **Robust description** means following the full chain: user voice to requirement to spec to AI instruction to tests. A failure at any link cascades downstream.
* **Prototype freely, ship selectively.** Be willing to veto something you built when the evidence says it is not working.
* **Apply discernment before shipping.** AI output often passes “Does it work?” but stumbles on “Is it the right thing?” Those gaps are where your judgment matters most.
* **The 4Ds are dynamic, not a sequence.** Moving fluidly between them as you build is what fluency looks like in practice.

## Exercise

### Your next build

Before completing this course, choose one real task from your current work to tackle with AI support this week. Pick something concrete and already waiting — not a hypothetical.

Good candidates:

* A feature request you've been putting off
* User research or feedback that hasn't been synthesized
* A technical spec that needs to be written before work can begin
* A part of your codebase with no tests that makes you nervous to touch

Work through it using all four competencies:

* **Delegation** — Which stages are safe to delegate? Which require your judgment?
* **Description** — Write the full chain: user need → requirement → spec → AI instruction → tests.
* **Discernment** — Evaluate output through all five lenses.
* **Diligence** — Before shipping: Do I understand what this does? Is there a feedback loop? Would I stand behind it?

## Lesson reflection

* What task are you committing to this week — and which part of the 4D Framework will matter most?
* What did you believe about working with AI at the start of this course that you now see differently?
* Who on your team would benefit from the 4D Framework?

## What's next

Next, take the short assessment to earn your certificate of completion.

#### Feedback

As you progress through the course, we’d love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform?usp=header).

#### Acknowledgments and license

*Copyright 2026 Anthropic. This course was developed in partnership with CodePath, building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*
<!-- youtube: YWVDXsUf8NY -->

# AI Fluency for Builders

[![AI Fluency for Builders](https://img.youtube.com/vi/YWVDXsUf8NY/hqdefault.jpg)](https://www.youtube.com/watch?v=YWVDXsUf8NY)

<details>
<summary>자막: AI Fluency for Builders</summary>

Hi, I'm Michael, the CEO of CodePath. And I'm Kristen from the education team at Anthropic. Welcome to the AI Fluency for builders course. If you have ever shipped software, you already know that writing code is only a small part of the job. You have to figure out what problem is actually worth solving. You have to make hundreds of small decisions about how it should work, and then you have to get it into people's hands and learn from what happens next. That full process, from understanding a customer problem to shipping a solution that reaches them, is what we mean by being a builder. And AI is changing almost every part of that process right now. Most of what gets called AI training focuses on one narrow slice: writing better prompts to get better code out of a language model. That's useful, but it's not enough to develop lasting AI Fluency. You need to know what to build in the first place. And you need to evaluate whether the thing AI produced is actually right, not just technically functional, but solving the real problem, working with real users, and not creating unexpected new problems. AI Fluency is the ability to work with AI systems in ways that are effective, efficient, ethical, and safe. AI Fluency isn't a prompt library. It's a set of interconnected competencies that empower you to make great decisions regardless of the model or feature at your disposal. At the center of this course is the 4D Framework, developed by professors Joseph Feller and Rick Dakan in collaboration with Anthropic. It consists of four competencies,  delegation, description, discernment, and diligence. Think of them as the operating system underneath every collaboration you have with AI. Delegation is about decomposing a problem into parts and deciding what role AI plays at each stage. Delegating implementation to AI is usually fine. Delegating judgment, the call about whether something is actually good and ready, is usually not advised. The best builders know the difference. Description is a builder's ability to ensure that every input, from user voice to product requirements to technical specs, make it into the implementation. Most AI training hyper-focuses on ensuring code is built where the test passes. That's important, but insufficient. Any missing input or context cascades downstream. A user complains that the tool doesn't work for them. You trace it back and discover the issue wasn't in the code. It was in how you understood and described the user problem. Builders must own every aspect of description. Discernment is how you evaluate what AI gives you. Not just does it run, but does it run well? Does it solve the right problem? Is it actually good to use and is it responsible? AI has real blind spots. It can produce code that's locally correct, but breaks under load. It can generate UX that's functional, but confusing. Discernment is the skill of catching those gaps before your users do. Diligence is full ownership of the outcome, not just the output. Shipping is a skill with its own technical realities that AI rarely surfaces proactively. Migrations, rate limiting, monitoring. What happens when something breaks at 2 a.m. and you're the one who built it? Prototype freely. Ship selectively. And be willing to veto something you built when the evidence says it isn't right. Think of AI as a capable but very literal collaborator. It's fast, it's knowledgeable, it doesn't get tired, but it needs clear tasks, real context about why you're building something and specific feedback when it gets something wrong. Managing that collaborator well, knowing when to step in, when to let it run, how to give it the right brief is the core skill this course develops. By the end of this course, you'll approach AI with confidence and intentionality. You'll know how to leverage it to move faster without losing the judgment that makes what you build actually good. And you'll own the full building process, not just the coding slice in the middle. Let's get started. Visit anthropic.com/learn

</details>

<!-- youtube: 7pFhV_i2KDI -->

## 자막 (영상 전사)

[snorts] [music] >> Kristen again from the education team at Anthropic. >> And I'm Chris, the chief product officer at CodePath. You've made it to the final lesson. Now let's talk about what happens next. The ways you can put AI fluency to work when you build. You have real work waiting for you. Maybe it's a feature that users have been requesting for 3 months. Maybe it's a prototype you've been meaning to turn into something real. Or maybe it's that pile of user feedback sitting in a spreadsheet that you haven't had time to synthesize. So here's your final assignment. Pick one of those things and use what you've learned in this course to tackle it with AI support this week. >> Start with delegation. Before you even open your laptop, think about what's actually in front of you. Break the problem down. What parts of this work genuinely benefit from AI? Implementation, scaffolding, boilerplate, first drafts and specs, these are strong candidates. But what parts need you? The judgment calls. The understanding of who your user actually is. And what they might be struggling with. The decision about whether the thing you built is actually the right thing. Those belong to you. Remember the builder's toolkit. You have six instruments. Empathy, design, architecture, implementation, judgment and shipping. AI is strongest in the middle at implementation and parts of architecture. It's weakest at the edges. It can't feel what your user feels. It can't tell whether what you shipped actually made a difference. That's your job. Once you've made your delegation decisions, move into description. This includes so much more than just what to code. It includes everything from user voice to product requirement to technical spec to AI instruction to tests. So before you write a single prompt, be clear about what problem you're solving and for whom. What does done look like? What would a test for success actually measure? When you give AI a well-described task with clear acceptance criteria, you're treating it like a capable junior collaborator with a clear brief. And of course, as you work, apply discernment. Does it work? Does it work well? Is it the right thing? Is it good? Is it responsible? Sometimes AI builds the thing you describe, but not the thing that solves the problem. Or it builds the thing that works, but one that people don't want to use. Find that out. Finally, practice diligence. Prototype freely. That's how you learn. But ship selectively. Before anything goes to users, ask, "Do I understand what this does? Can I explain it? And is there a way to know if it's working?" And of course, be willing to veto something you built when the evidence says it isn't working. Sunk effort is one of the hardest things to walk away from. But the builder's job isn't to defend the software. It's to serve the user. The four D's are dynamic. You'll move from delegation to description, back to discernment, and realize you want to delegate differently. That's your AI fluency developing through practice. >> In the resources section below, you'll find blueprints covering common builder tasks. From writing technical specs to structuring a build-measure-learn cycle with AI assistance. Use these as your starting points. Adapt them to your needs. And then reflect on what you learned. You can also take a short quiz to earn your certificate of completion. Now that's something we're sharing with your other builders in your network to start a conversation about what this kind of fluency looks like on a team. Congratulations on completing this course. The builders who will do the most interesting things with AI in the next few years aren't the ones who automate the most. It's the ones who know when to delegate and when to stay in the loop. These are the ones who care enough about their users to not just ship something because it compiles. That's who you are. Now go build something great.
