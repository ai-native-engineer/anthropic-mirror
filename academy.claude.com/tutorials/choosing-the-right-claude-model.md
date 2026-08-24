<!-- source: https://academy.claude.com/tutorials/choosing-the-right-claude-model -->

Claude comes in four models: Haiku, Sonnet, Opus, and Fable. Each is built for different kinds of work, and each uses your rate limit differently. Using Opus on a task Haiku could handle costs you tokens for no gain and slows you down in the process. In this guide you'll learn how to pick the Claude model that can most efficiently accomplish your task *and* keep you more comfortably within your rate limits.

Which models you have and how high your limit is both depend on your [Claude account plan(opens in new tab)](https://claude.com/pricing). Free includes Haiku and Sonnet; [Pro(opens in new tab)](https://claude.com/pricing) and [Max(opens in new tab)](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) add Opus, Fable, and more headroom.

## Meet the four models

Claude comes in four versions. Think of them as different tools designed for different jobs.

| Model | Rate limit use | Best for |
| --- | --- | --- |
| Haiku | Lightest | Quick answers, summaries, and simple extraction — anything you want done instantly |
| Sonnet | Moderate | Coding, writing, analysis, and multi-step workflows — your versatile default |
| Opus | Heavy | Deep research and complex reasoning that genuinely needs sustained thinking |
| Fable | Heaviest | Your largest, most critical projects: long, complex tasks Claude works through with fewer check-ins |

**Haiku** is fast and lightweight. Haiku 4.5 is built for everyday requests, and it rivals the reasoning capabilities of our Sonnet 4.0 model. When you need quick answers to simple questions, basic summaries, or synthesis, Haiku gets it done instantly. It's also the most efficient with your rate limit.

**Sonnet** is the daily driver. Sonnet 5 brings strong reasoning to the kind of work you do every day: coding, writing, analysis, research, and complex problem-solving. It's responsive enough for real-time collaboration and capable enough that most problems won't outgrow it. It also handles computer use, vision tasks, and document and spreadsheet creation well, making it a versatile default across a wide range of work. If you're not sure which model to pick, start here.

**Opus** is a large reasoning specialist. Opus 5 is exceptional for specialized complex tasks requiring advanced reasoning. It's built for problems that genuinely need deep thinking over time. It uses more of your rate limit, so you want to reserve it for tasks that really need it. Opus is available on [Pro plans(opens in new tab)](https://claude.com/pricing) and above.

**Fable** is the go-to for your largest, most important projects. Fable 5 is our newest and most capable model, built for long, complex tasks. It can work through tasks more autonomously with fewer mid-task check-ins: describe the outcome you want, and it plans the steps and checks its own work along the way. It takes time to think through problems before answering, so responses take longer, and it uses the most of your rate limit. Fable is available on paid plans. You can select it from the model picker when a task needs it.

## Understanding rate limits

Your rate limit caps how many tokens you can use in a given time window. The models consume tokens at different rates: Haiku is the lightest, Sonnet is moderate, Opus is heavy, and Fable uses the most.

Models like Haiku and Sonnet are more "efficient" with your limit: you can ask more with fewer tokens. Models like Opus and Fable use more tokens because they do more reasoning. But if you use Opus or Fable on a task that Sonnet or Haiku could handle, you may be using more of your limit unnecessarily.

One thing that helps: setting [thinking and effort(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) controls in order to customize the depth of reasoning Claude applies to a problem. The Effort setting in the model picker adjusts this directly: the default level is the right balance for most work; lower it for quicker answers that use less of your limit; save the highest setting for your hardest problems, since deeper thinking takes more time and uses more of your limit.

## When to use each model

To balance rate limits with efficiency, it's best to consider what kind of output you're looking for from Claude and choose your model accordingly. It helps to know what a useful answer would look like before you send the prompt, and to check the result in proportion to what's riding on it: a quick lookup needs only a glance, while analysis that will shape a decision deserves a closer review.

### Use Haiku for:

* Simple, straightforward questions with short answers
* Tasks where you just need a quick lookup or categorization
* Extracting specific information from text
* Simple summarization or synthesis
* Anything you want done instantly without complex reasoning

### Use Sonnet for:

* Writing and content creation
* Coding tasks — debugging, writing new code, refactoring
* Analysis that needs reasoning but isn't extremely complex
* Customer support chatbots with context and nuance
* Multi-step problems and workflows
* Most "general purpose" work where you're not sure which model to use

### Use Opus for:

* Deep research and analysis you'll question, redirect, and build on as you go
* Complex work you're doing in a live, back-and-forth session, where you want each answer sooner
* Biology and security work: Claude answers these topics with Opus even if you've picked Fable, so starting with Opus is simpler. To learn more, visit our [help center(opens in new tab)](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5).
* Problems where you've tested with Sonnet and it struggled

### Use Fable for:

* Specialized tasks where accuracy is critical
* Long horizon tasks with many connected steps
* Outputs from dense source material: long documents, charts, technical diagrams
* Work where you'd rather describe the outcome and let Claude plan the steps
* Problems you've tested with Opus and it struggled

## What this looks like in practice

Let's see how this plays out with a few common tasks.

| Task | Pick | Why |
| --- | --- | --- |
| Summarizing articles | Haiku | Straightforward content extraction without complex reasoning |
| Debugging code | Sonnet | Exceptional coding capabilities, fast feedback, and clear bug identification |
| Analyzing complex research papers | Opus | Deep analysis across long specialized documents, including methodology critique and forward-looking insights |
| Building a working project from a rough idea | Fable | Plans the steps, checks its own work, and keeps working on long tasks with fewer mid-task check-ins |

## Try the same task on two models

Pick a task you already know well, like summarizing a report you've read yourself. Run this prompt with Haiku first, then start a new chat with Sonnet and run it again:

Summarize the attached report in five bullet points, then flag the one claim in it you'd most want a second source for.



Open in Claude

**Compare where the answers differ, not how long they are.** You've read the report, so you can judge: if Haiku's summary covers everything you would have flagged yourself, the task is Haiku-shaped. Save Sonnet, Opus, and Fable for the work where the lighter answer misses things that matter.

## Choosing models over time

Claude is always evolving, and so are the types of problems you can hand it. Each new model brings its own strengths, so the tasks worth giving Claude grow and shift with every release. When a new model comes out, try out more ambitious tasks that may have hit a ceiling in the past.

Spend a few minutes running your go-to tasks across models. If you're on the free plan, [upgrading(opens in new tab)](https://claude.com/pricing) gives you access to all models and a higher rate limit. When a new model is released, you have more room to try everything.
