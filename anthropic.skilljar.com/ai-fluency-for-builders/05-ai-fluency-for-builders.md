<!-- https://anthropic.skilljar.com/ai-fluency-for-builders/486160 -->

## What you'll learn

*Estimated time: 45 minutes*

By the end of this lesson you'll be able to:

* *Translate a user need to precise AI instruction using the Description Chain*
* *Spot when a description failure cascades and trace it back to the link that broke*
* *Express intent through tests that tell AI exactly what success looks like*

## Describing what users need

*(5 minutes)*

Most AI training teaches you to write better prompts. That’s necessary but not sufficient for building great products. This lesson maps the full Description Chain: the path from a messy human need to a precise instruction AI can act on, with the builder as the translator at every step.

#### Key takeaways

* The **Description Chain** connects user voice to requirement to technical spec to AI instruction. Prompt engineering is only one link.
* **The builder is the translator** at every step. AI cannot hear what the user did not say.
* **Code that works but the product doesn’t** is a description failure. Find which link broke upstream.
* **Tests are the most precise form of description.** A passing test with an unhappy user means you described the wrong intent.
* Every step involves **judgment calls** the previous phase did not make for you.

## Exercise

### The Clinic Wait Time Project, Part 2

You’re picking up exactly where the last lesson left off. Pull out your problem brief, your delegation plan, and your acceptance tests.

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

## Lesson reflection

* Which translation in the Description Chain feels most natural? Which do you tend to rush through?
* In your Clinic demo, where was the biggest gap between what you intended and what your partner experienced?

## What's next

In the next lesson, we move from description to discernment. You’ve built something and the code runs — now the question is whether it’s actually good.

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

<!-- youtube: wotzFHTKQ9Q -->

## 자막 (영상 전사)

[snorts] [music] >> So in the last module, you spent real time understanding the problem before touching any tools. You wrote the problem brief. You wrote acceptance tests. You decided what you keep and then what you delegate to AI. But now, you have to turn all of that into something. Something that AI can actually act on. Most AI training treats description as prompt engineering. We're going to approach this task differently by considering all the aspects of description that will help you solve the problem you've clearly defined. Description is a high-level competency that will remain relevant, outlasting tips and tricks that may change from model to model. Recall the six capabilities in the builder's toolkit. Before implementation, we have to define the user need. Here's the full picture. Four steps directly tied to the capabilities in your toolkit, with the builder as the translator and the heart of each step. Let's use the project you're already working on. First step is user voice. This is what a real person actually says. For example, I want to see wait times before I go to the clinic. Notice the tone, the emotion. It carries context the speaker didn't say out loud that it's been 2 hours already. They have a kid in the car and they're deciding between this clinic and urgent care across town. Use your own empathy to connect and observe with what goes unsaid by the user. User voice is just raw material. It's true and it's not yet buildable. So the second part is product requirement. This is where you take that raw user need and you scope it into something measurable. Patients, for example, can view estimated wait times via a mobile-friendly webpage, perhaps updated every 5 minutes. You see what you did there? You made decisions. Mobile-friendly, not an app. Estimated, not exact. Every 5 minutes, not real-time. Each is a key judgment call that you made based on what you learned in your own empathy work. Ensuring that there are very clear concrete criteria helps the AI do its job better when it gets to the implementation step. The third piece is the technical spec. Now you're getting into the real building. A web app, for example, that pulls a clinic API for weight data and displays it with a responsive UI refreshing on a 5-minute interval. That is implementable. An engineer could actually read that and start building. So could an AI. But notice it still leaves room. Which stack? How errors get handled? What happens when the AI goes down? The fourth step is AI instruction. Specific, contextualized with constraints and edge cases clearly defined. The stack you're using and the shape of the data. What to do when there's no data? The test that it has to pass. It's critical that you give the AI specific things it can verify. This helps it work more effectively and for longer. So here's why this matters. Builders who think about carefully describing all aspects of the problem get the best results with AI. The more thoughtful the description, the better the output. AI can't hear what the user didn't say. AI can't decide that estimated is the right requirement because exact times would make the clinic staff anxious about being held to them. It can't know that responsiveness matters because patients are checking wait times while they're in route. You know those things. Your job is to carry them intact as you describe what you need to the AI. Sometimes the translation breaks. And when it does, you get a specific type of failure. Code that works, but the product doesn't. The tests might pass, but the user is still frustrated. That's not a bug, that's a description failure, and it usually lives upstream of the prompt. So a big part of your job as a builder is actually forensic. When the thing you built misses the mark, you trace it back. Was it a user understanding failure where you never really heard what they needed in the first place? Was it a requirement failure where you heard them, but then you it wrong? Was it a spec failure where the requirement was actually right but the technical translation lost something? Or a prompt failure where everything upstream was solid and you just instructed the AI poorly? So one more idea before we build. Your acceptance tests from the last module are a form of description, too. Maybe the most powerful kind. A well-written test is a description of intent that can't be misread because it either passes or it doesn't. When you hand AI a set of tests alongside your prompt, you're not just telling it what to build. You're telling it how you'll know if it succeeded. That changes what you get back. So in this module, you're going to write detailed descriptions for AI with your clinic project. Product requirements, technical specs, tests, prompts, and then for the first time in this course, we're going to build. You'll demo what you build to someone playing a clinic patient and you'll ask two questions. First, did the test pass? And second, is the user satisfied? If the answer to the first is yes and the second is no, that's not a failure. That's the most useful thing that can happen to you in this module. It means your test described the wrong thing and now you know exactly where in the chain to look. Let's get to it. >> [music]
