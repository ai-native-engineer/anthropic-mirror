<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486163 -->

## What you'll learn

*Estimated time: 45 minutes*

By the end of this lesson you'll be able to:

* *Articulate what you own when you ship something AI helped build*
* *Identify the technical realities that surface at ship time and build feedback loops that catch them*
* *Make the call: ship it, fix it, or stop it*

## Diligence & sharing your work

*(3 minutes)*

Diligence in the builder model is full ownership: you’re responsible for the product from whether it should exist to whether it’s serving users after launch. This lesson covers what it means to ship, the technical realities AI won’t warn you about, why tests become your safety net the moment something is live, and the underrated skill of deprecating your own work.

#### Key takeaways

* **You own the outcome, not the output.** “AI wrote it” explains nothing and excuses nothing.
* **Shipping has its own technical vocabulary** (migrations, versioning, rate limits, feature flags) that AI will not surface unless you ask.
* **Tests make post-launch iteration safe.** The test-first habit is why you can keep changing things confidently.
* **Prototype freely, ship selectively.** Cheap code creates value only when paired with honest evaluation.
* **Access is a design decision.** Check who your assumptions exclude before you call something shipped.

## Exercise

### Ship the Clinic app

Shipping is where diligence becomes real — before you deploy, answer each of these honestly.

Once you’ve worked through these, deploy your app or host it as a prototype, share it with three real users, and make one iteration based on what you learn, with tests that verify the change.

* **Understanding** — Can you explain what your code does, not just what it should do?
* **Testing** — Do your acceptance tests still pass? Have you tested edge cases — closed clinic, missing data, zero wait time?
* **Access** — Who does your build not serve well?
* **Responsibility** — Could this output be misread or misused? Have you been transparent about AI’s role?
* **Feedback loop** — How will you know if it’s working after it ships?

## Lesson reflection

* How has your thinking about AI integration changed from the beginning of this course?
* What’s one thing you’ll do differently in your work with AI based on what you’ve learned?

## What's next

You’ve built, evaluated, and shipped the Clinic Wait Time Checker. In the final lesson, you’ll bring the full 4D Framework together and leave with a real task already in motion.

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

<!-- youtube: wrgLtG-IHKk -->

## 자막 (영상 전사)

Hi there. My name is Martina and I'm an engineer at Anthropic. Throughout this course you've delegated, described, and discerned. You have a clinic app that works. It's almost time to ship it. In the 4D framework, diligence means taking responsibility for what you build with AI. Essentially, making sure your use of AI is transparent, ethical, and accountable. This includes being transparent about your AI use and disclosing it, taking ownership of the outputs that AI creates, verifying work before you ship, considering the impact of what you built on others, and honoring policies, privacy, and professional standards that govern AI use in your organization or industry. Rather than tell you what to value, I'm going to show you what diligence looks like in my day-to-day as an engineer. With AI, you can end up being the owner of code you didn't write. Diligence is how you catch up to your own code, understand it, stress it, test it, and put the systems in place that catch what you miss. For me, that comes down to three habits. When you're writing code yourself, it becomes apparent as you go that there are things you hadn't thought of. Some edge case, some decision you hadn't realized needed to be made. With AI, sometimes those end up getting decided without ever being surfaced to you. So, I try to recreate that step on purpose. Get those questions out in the open where I can actually weigh in. When an edge case pops into my head, I'll just say to the model, like, "Can you double-check that users can't view other users' files?" After Claude built something substantial, I asked directly, "What assumptions and trade-offs did you make? What security risks should I be aware of?" That ensures that you're looped in on the important decisions. When Claude writes most of a pull request, I make sure to say so in the description. Not as a disclaimer, as information. This is relevant because AI makes a different shape of mistake than humans do. Deprecated APIs used confidently, code that's locally clean but inconsistent with the code base, invented behavior for cases you never specified. A reviewer who knows that can better tailor their review. It's easy to feel out of your depth when AI does the building. You can end up with working code you don't understand, which wasn't really possible before. But it's not that you can't understand it. It's just a separate step now, and AI can help with that, too. Claude is more than happy to sit with you and patiently explain. It takes a bit of time, but that's what puts you back in the loop. Here's the thing. The engineering best practices that existed before AI still apply after. Maybe even more so, because now you're shipping faster and you understand a smaller fraction of what you shipped. Tests are still the easiest way to make sure you don't break something while moving this fast. A solid test suite pins down the behavior you care about, so you can keep iterating without fear. Observability hasn't gone anywhere, either. Some things only show up when real users have it, so you want logs, error tracking, dashboards. You find out from your own data, not from a user email. And feature flags remain useful for when something does slip through. Having these safety nets in place is what lets you move fast safely. Verification, transparency, understanding. Tests on one end, observability on the other. None of this is new to engineering. AI is just a new tool under your belt to get there.
