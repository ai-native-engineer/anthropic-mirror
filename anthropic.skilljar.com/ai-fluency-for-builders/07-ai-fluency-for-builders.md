<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486162 -->

## What you'll learn

*Estimated time: 45 minutes*

By the end of this lesson you'll be able to:

* *Apply hierarchy, user flows, accessibility, and feedback patterns when specifying what AI should build*
* *Critique AI-generated designs using feedback specific enough to act on*
* *Make intentional tradeoff decisions between speed, polish, and user needs*

## Discernment for user experience

*(2 minutes)*

As AI speeds up implementation, design becomes the differentiator. This lesson covers the UX principles that matter most when working with AI, why “make it look good” produces nothing useful, and how to close the gap between a critique you’d give a colleague and a description AI can execute.

UX Lab: Apply the four principles

Each tab shows a food delivery screen with common UX problems AI generates by default. Hover over any element to discover what’s wrong — then click Show Fix to see how it should be built.

Clarity
Hierarchy
Accessibility
Feedback

Principle 1 of 4

Clarity

Every element should instantly communicate its purpose. Users shouldn’t have to guess what a button does or what a field means.

Show Fix↻ Reset

←No destination label — users can’t tell where “back” goes
AppGeneric title — what screen is this?
⋮Unexplained icon — what does this open?

Burger12.00No currency symbol — is this dollars?

Fries4.50

Total16.50

SubmitVague action — submit what? For how much?

← Back to menu
Order review
Help

Burger$12.00

Fries$4.50

Order total$16.50

Place Order — $16.50

Principle 2 of 4

Hierarchy

Visual weight should match information priority. The most important thing should look the most important.

Show Fix↻ Reset

Order total: $16.50Most critical info buried in a flat list — nothing stands out

Arriving by 1:10 PMSame size as the order number — hard to find fast

Order #1284

123 Main St, Apt 4B

Subtotal $14.00 + Delivery $2.50

$16.50

Arriving by 1:10 PM

Order #1284 · 123 Main St, Apt 4B

Subtotal $14.00 + Delivery $2.50

Principle 3 of 4

Accessibility

About 1 in 5 people has a disability — visual, cognitive, or neurological. AI generates for the median user. Small text, color-only signals, and jargon quietly exclude everyone else.

Show Fix↻ Reset

Order #1284
Color only — no text label. Colorblind users cannot tell if this means confirmed or failed.

Item9px header text — unreadable for low vision users without screen magnification.

qty“qty” is an abbreviation — creates friction for users with cognitive disabilities or limited literacy.
Price

Burger1$12.00

Fries1$4.50

Total$16.50

ETA: 35 min · Cancellation per T&C9px text. “ETA” and “T&C” are jargon — neurodivergent users often need plain language to process confidently.

Order #1284
✓ Order confirmed

Item
QuantityPrice

Burger1$12.00

Fries1$4.50

Order total$16.50

Arrives in approximately 35 minutes · Free cancellation — see details

Principle 4 of 4

Feedback

When something breaks, users need to know what happened, what to do next, and how to get help. A raw error code answers none of those questions.

Show Fix↻ Reset

←
Order Review
⋮

⚠

No explanation — users don’t know if their order went through, failed, or is still pending.

Error 503“503 Service Unavailable” is a server code. It means nothing to a user trying to order lunch.

← Back
Order Review
Help

✕

We couldn’t place your order

Our payment system hit a snag. Your cart is saved — try again in a moment.

Try again →

Still having trouble?

Chat with support →

#### Key takeaways

* **When implementation is fast, experience is the differentiator.** Design literacy is a core builder skill.
* **“Make it look good” is a wish, not a spec.** Describe experience with the same precision as a function.
* **AI does not get accessibility right by default.** Specify it, then audit what you get back.
* A good **critique** and an actionable **AI description** are different artifacts. Learn to translate between them.

## Exercise

### The Clinic Wait Time Project, Part 3

Write a design spec for your clinic app — user flows, information hierarchy, interaction patterns — then rebuild it with AI against that spec. Critique the result: where did AI nail it, and where is it technically correct but experientially flat? Run a quick accessibility audit and document what AI missed.

* **Clarity & Mental Model** — Does the output use language and patterns a clinic admin would recognize?
* **Information Hierarchy** — Is the most important information the first thing users see?
* **Accessibility** — Does it pass color contrast, screen reader, and keyboard navigation checks?
* **Feedback & Error Handling** — Does the interface acknowledge user actions and explain what to do when something goes wrong?

## Lesson reflection

* How much of your design spec describes what the interface does versus how it should feel to use?
* After running the accessibility check, did you build with accessibility in mind from the start, or add it at the end?

## What's next

You’ve looked at your Clinic Wait Time Checker through both a code lens and a UX lens. In the next lesson, you’ll tackle the hardest question: what does it mean to actually stand behind what you build?

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

<!-- youtube: jgcF2d0kW7U -->

## 자막 (영상 전사)

[snorts] [music] >> As implementation gets faster, design and user experience become even more important. You don't need to become a designer, but you do need to recognize good experience, spec for it, and iterate towards it. A few principles here to guide you. One is clarity. If users can't tell what your product does or how to get started, they're gone. Clarity means unifying form and function while respecting people's mental models. Users arrive with expectations shaped by other software and by the world. Keep it simple and map your interface to concepts they recognize. A patient checking wait times expects it to work like every other status checker. Two is hierarchy and progressive disclosure. Make it easy for people to scan and find the information that is needed. Don't overwhelm them. Use text size and weight to create good headers, minify the amount of unneeded elements, and allow people to find the information they need as they need it instead of cramming it all into one space. Three, accessibility is a baseline, not a nice to have. Screen reader compatibility, color contrast, keyboard navigation, you should ask the AI for these explicitly every single time and build test cases to validate. Four, feedback and responsiveness. When the user does something, the interface should acknowledge it, not lead the user to question if something might be broken. Loading states, confirmations, and error messages that explain what to do next, all in simple human language, help build trust. The gap between making it look good and a good experience is enormous. Make it look good is a wish. Put the wait time in the largest text on the page, use a single color to indicate status, and make the refresh time visible so the patient knows how stale the number is is an actionable strong description. This is description and discernment working together. You describe the experience precisely, AI builds it. You evaluate what comes back against what you intended. You describe the gap, repeat. One thing you'll notice in the exercises, the critique that you'd give a colleague and the description AI needs are not the same document. "This feels cluttered" is a fair critique, but it's useless instruction for AI. Part of design literacy is learning how to translate your own taste into something that is executable. Let's put it to work.
