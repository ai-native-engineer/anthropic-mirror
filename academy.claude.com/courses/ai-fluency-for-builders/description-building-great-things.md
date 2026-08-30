<!-- source: https://academy.claude.com/courses/ai-fluency-for-builders/description-building-great-things -->

Lesson 5 of 9 · AI Fluency for BuildersDescription & building great things

3. /[AI Fluency for Builders](https://academy.claude.com/courses/ai-fluency-for-builders)

[AI Fluency for Builders](https://academy.claude.com/courses/ai-fluency-for-builders)

# Description & building great things

Lesson 515 min

In this lessonBy the end, you’ll be able to

* Translate a user need to precise AI instruction using the Description Chain
* Spot when a description failure cascades and trace it back to the link that broke
* Express intent through tests that tell AI exactly what success looks like

## Describing what users need[](#describing-what-users-need)

Describing what users need · 5 min

Most AI training teaches you to write better prompts. That’s necessary but
not sufficient for building great products. This lesson maps the full
Description Chain: the path from a messy human need to a precise instruction
AI can act on, with the builder as the translator at every step.

## Key takeaways[](#key-takeaways)

* The **Description Chain** connects user voice to requirement to technical spec to AI instruction. Prompt engineering is only one link.
* **The builder is the translator** at every step. AI cannot hear what the user did not say.
* **Code that works but the product doesn’t** is a description failure. Find which link broke upstream.
* **Tests are the most precise form of description.** A passing test with an unhappy user means you described the wrong intent.
* Every step involves **judgment calls** the previous phase did not make for you.

## Exercise[](#exercise)

### The Clinic Wait Time Project, Part 2

You're picking up exactly where the last lesson left off. Pull out your problem brief, your delegation plan, and your acceptance tests.

### Step 1: Write the product requirement

One paragraph. Take the user need from your problem brief and scope it into something measurable. Every adjective should be a decision you can defend. If you write “fast,” write how fast. If you write “simple,” describe what simple means for a patient checking from a phone in a parking lot.

### Step 2: Write the technical spec

Half a page. Describe what gets built and how it’s structured. Name the pieces. Name how they talk to each other. Use AI in augmentation mode here: share your product requirement, ask it to propose a technical approach, then push back on anything that doesn’t fit your constraints.

### Step 3: Tighten your tests

Revisit your acceptance tests from the previous lesson. Rewrite them so each one is something code could pass or fail. Add at least two edge cases: what happens when the clinic is closed, when there’s no data, when the wait time is zero.

### Step 4: Write your AI prompts and build

Write the instructions that turn your spec into working code. Include your constraints, your stack choices, and your tests. Build the first version.

### Step 5: Demo it

Find a partner. They play a clinic patient — they’ve got a sick kid and ten minutes. Hand them your build and watch them use it. Don’t explain anything. Don’t help.

Did the tests pass? Is the patient satisfied? If those answers don’t match, which link in the chain would you go back to?

## Lesson reflection[](#lesson-reflection)

* Which translation in the Description Chain feels most natural? Which do you tend to rush through?
* In your Clinic demo, where was the biggest gap between what you intended and what your partner experienced?

## What's next[](#whats-next)

In the next lesson, we move from description to discernment. You’ve built something and the code runs — now the question is whether it’s actually good.

[Previous lessonDelegation & the builder's toolkit](https://academy.claude.com/courses/ai-fluency-for-builders/delegation-the-builder-s-toolkit)[Next lessonDiscernment for code](https://academy.claude.com/courses/ai-fluency-for-builders/discernment-for-code)

Lesson 5 of 9 · AI Fluency for BuildersDescription & building great things

Introduction and AI Fluency framework

* [Welcome to AI Fluency for builders](https://academy.claude.com/courses/ai-fluency-for-builders/ai-fluency-for-builders)
* [The 4D Framework](https://academy.claude.com/courses/ai-fluency-for-builders/the-4d-framework)

How AI works

* [AI capabilities & limitations](https://academy.claude.com/courses/ai-fluency-for-builders/ai-capabilities-and-limitations)

The 4D framework for builders

* [Delegation & the builder's toolkit](https://academy.claude.com/courses/ai-fluency-for-builders/delegation-the-builder-s-toolkit)
* [Description & building great things](https://academy.claude.com/courses/ai-fluency-for-builders/description-building-great-things)

Discernment for builders

* [Discernment for code](https://academy.claude.com/courses/ai-fluency-for-builders/discernment-for-code)
* [Discernment for user experience](https://academy.claude.com/courses/ai-fluency-for-builders/discernment-for-user-experience)

Tying it all together

* [Stand behind what you build](https://academy.claude.com/courses/ai-fluency-for-builders/stand-behind-what-you-build)

Wrapping up

* [Closure & looking forward](https://academy.claude.com/courses/ai-fluency-for-builders/closure-looking-forward)
* [Course quizQuiz](https://academy.claude.com/courses/ai-fluency-for-builders/course-quiz)

* [Completion badge](https://academy.claude.com/courses/ai-fluency-for-builders/badge)

* [Describing what users need](#describing-what-users-need)
* [Key takeaways](#key-takeaways)
* [Exercise](#exercise)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
