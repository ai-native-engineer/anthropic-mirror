<!-- source: https://academy.claude.com/courses/introduction-to-evals/when-to-use-what-model -->

Lesson 1 of 4 · Introduction to evalsWhen to use what model

3. /[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

# When to use what model

Lesson 110 min

When to use what model

Claude's models differ in capability, speed, and cost, and you don't have to
guess which one suits your task, because you can measure it. This lesson
shows how, following Meridian, a fictional engineering consultancy that uses
one prompt to pull three fields out of 50 project reports.

*The demo in this video was recorded in August 2026. It ran on Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5. Results will differ on newer models. Each lesson's demo is a separate eval run, so its scores and costs won't match those in other lessons.*

When you pick a Claude model for a task, you probably go on instinct, or on a colleague's word. Claude's models really do differ in [capability, speed, and cost(opens in new tab)](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model), but no published comparison has ever seen your specific prompt, so none of them can tell you how a model will do on your task. **The way to choose is to measure how often each model gets your task right, and only then to look at what each one costs.**

It's a lot like buying a ladder to reach the top of a wall. Before you look at prices, you find out how high the wall is, because a ladder that's too short is useless at any price. Guessing won't tell you which ladders reach, so you measure them, and of those that reach, you buy the cheapest. A taller wall needs a longer ladder, and that's the right one to buy even though it costs more.

With models, that measuring is done by an eval, which is a set of cases you run every model on. Each case is one input your prompt will see and the answer you expect back, and a person writes that answer from the input before any model runs. Each run then gets a score for how many cases the model got right.

This lesson follows Meridian. Each month it gets 50 project reports in Markdown, and one prompt pulls three fields out of each: the project ID, the schedule status, and the top risk. Its cases are one month's 50 reports, and what it doesn't know yet is which model should run that prompt.

Meridian works it out in five steps, which you can follow with your own prompt:

1. Decide how accurate a model must be
2. Score each model on the same cases
3. Work out what one call costs
4. Compare models by what each completed task costs
5. Pick the model with the accuracy you need at the lowest cost

## Decide how accurate a model must be[](#decide-how-accurate-a-model-must-be)

This is the height of the wall, and you settle it before you look at what anything costs. Your accuracy floor is the share of cases a model has to get right before you'd ship it. **To set the floor, work out what one wrong answer costs you, because the more it costs, the higher your floor should be.**

For Meridian, a wrong answer means someone has to check that report by hand, which takes about 5 minutes. Its engineers can absorb 5 of those checks a month, and since 5 of 50 is 10%, Meridian's floor is 90%.

A different task can push the floor much higher. Say one wrong answer costs $1,000, perhaps because it reached a client. Then the floor goes to 100%, and what the model costs hardly matters.

## Score each model on the same cases[](#score-each-model-on-the-same-cases)

A floor is just a number until you measure models against it. **Run every model on the same cases with the same prompt, so that the model is the only thing that changes from one run to the next.** Meridian ran its 50 reports through one prompt on three models: Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5.

A script of Meridian's checks each field against the expected answer. The project ID and the schedule status must match exactly, but the top risk is a sentence, so the script compares it more loosely and allows slight changes in wording. Each case is one task, which for Meridian means one report to pull three fields from. A model completes the task only when it gets all three fields right.

Of the 50 cases, 30 are typical reports, 10 cover several projects at once, and 10 have no risk section. The table breaks each model's score down by those three kinds.

| Model | Typical | Multi-project | Missing risk | Overall |
| --- | --- | --- | --- | --- |
| Haiku 4.5 | 90% | 100% | 50% | 84% |
| Sonnet 5 | 100% | 100% | 100% | 100% |
| Opus 5 | 100% | 100% | 100% | 100% |

*Share of cases each model got right, by kind of report, with the same prompt and a floor of 90%*

Sonnet 5 and Opus 5 both got all 50 right. Haiku 4.5 got 42 of 50, which is 84%, so on this task and with this prompt it doesn't clear the floor.

## Work out what one call costs[](#work-out-what-one-call-costs)

Now that two models have cleared the floor, cost comes in. You're billed by the token, a piece of the text that models process, and every response from the Messages API includes a `usage` block that holds the exact token counts you're billed for. The example below is an illustration, a Sonnet 5 call about the size of one of Meridian's, with 780 input tokens and 41 output tokens.

json

```
"usage": {
  "input_tokens": 780,
  "output_tokens": 41
}
```

Read those counts from `usage` for each model rather than estimating them from your text. A model's tokenizer is the part that splits text into tokens, and not every model uses the same one. So the same text can come to a different number of tokens on different models. Sonnet 5 and Opus 5 use [a newer tokenizer that produces approximately 30% more tokens for the same text(opens in new tab)](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing), and Haiku 4.5 uses the previous one.

Input tokens and output tokens have separate rates, each given per million tokens. The table shows the three models' rates as listed in August 2026, which is when Meridian ran the eval, and [Claude's pricing page(opens in new tab)](https://claude.com/pricing) has the rates that apply today.

| Model | Input | Output |
| --- | --- | --- |
| Haiku 4.5 | $1 | $5 |
| Sonnet 5 | $2 | $10 |
| Opus 5 | $5 | $25 |

*Each model's rate per million input and output tokens, as listed in August 2026*

**A call's cost is its input tokens times the input rate, plus its output tokens times the output rate.** The example is a Sonnet 5 call, so it uses Sonnet 5's rates from that table.

text

```
780 input tokens  × $2 per million  = $0.0016
 41 output tokens × $10 per million = $0.0004
                              total = $0.0020
```

## Compare models by what each completed task costs[](#compare-models-by-what-each-completed-task-costs)

Add up what every call in a run costs, and the total is called the run cost. **Divide the run cost by the number of tasks the model completed, and you get the cost per completed task, which is the figure you [compare models on(opens in new tab)](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task).**

You divide by completed tasks, not by calls. That's because every call is billed, even one that gets the task wrong. So a model's wrong answers add to the cost of each task that same model does complete.

| Model | Completed | Run cost | Cost per completed task |
| --- | --- | --- | --- |
| Haiku 4.5 | 42 of 50 | $0.0380 | $0.0009 |
| Sonnet 5 | 50 of 50 | $0.0984 | $0.0020 |
| Opus 5 | 50 of 50 | $0.2323 | $0.0046 |

*Run cost and cost per completed task for the 50 cases, at the rates listed in August 2026*

## Pick the model with the accuracy you need at the lowest cost[](#pick-the-model-with-the-accuracy-you-need-at-the-lowest-cost)

**Your floor settles which models are candidates, and of those you pick the one whose cost per completed task is lowest.** Sonnet 5 and Opus 5 both got 50 of 50, at $0.0020 and $0.0046 per completed task, so on this task Meridian picks Sonnet 5. Haiku 4.5's $0.0009 is the lowest figure in the table, but it isn't a candidate, because it doesn't clear the floor.

On a harder task, the most capable model might be the only one that clears the floor, and then it's the right choice. Each result is also tied to the prompt and the cases the eval used. Change the prompt or the cases, and the right model can change too, so run the eval again whenever you change either one.

This eval doesn't measure latency. If your users wait for the answers, time the responses on your own cases, just as you scored them here.

## Lower the cost of running the eval[](#lower-the-cost-of-running-the-eval)

Those five steps give you a model, and there's one more way to lower what the eval itself costs. Nobody waits on an eval's answers, so you can send it through the [Batch API(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing), which processes requests asynchronously. **The Batch API runs the same models at [half the price on input and output tokens(opens in new tab)](https://platform.claude.com/docs/en/about-claude/pricing#batch-processing).**

When you compare models, don't mix batch rates and standard rates in one comparison. Work out every model's cost at batch rates, or every model's cost at standard rates.

## The bottom line[](#the-bottom-line)

1. Set your accuracy floor first, from what a wrong answer would cost you.
2. Give every model the same cases, and drop any model that doesn't clear the floor.
3. Take each call's cost from its `usage` block, then divide the run cost by the number of tasks the model completed.
4. Of the candidates that clear the floor, pick the one whose cost per completed task is lowest.

[Next lessonBuild a minimum viable eval](https://academy.claude.com/courses/introduction-to-evals/build-a-minimum-viable-eval)

Lesson 1 of 4 · Introduction to evalsWhen to use what model

Before launch

* [When to use what model](https://academy.claude.com/courses/introduction-to-evals/when-to-use-what-model)
* [Build a minimum viable eval](https://academy.claude.com/courses/introduction-to-evals/build-a-minimum-viable-eval)
* [Iterate the prompt before you upgrade the model](https://academy.claude.com/courses/introduction-to-evals/iterate-the-prompt-before-you-upgrade-the-model)

After launch

* [Evals in production: CI, batch, and drift](https://academy.claude.com/courses/introduction-to-evals/evals-in-production)

Quiz and next steps

* [Course quizQuiz](https://academy.claude.com/courses/introduction-to-evals/course-quiz)

* [Completion badge](https://academy.claude.com/courses/introduction-to-evals/badge)

* [Decide how accurate a model must be](#decide-how-accurate-a-model-must-be)
* [Score each model on the same cases](#score-each-model-on-the-same-cases)
* [Work out what one call costs](#work-out-what-one-call-costs)
* [Compare models by what each completed task costs](#compare-models-by-what-each-completed-task-costs)
* [Pick the model with the accuracy you need at the lowest cost](#pick-the-model-with-the-accuracy-you-need-at-the-lowest-cost)
* [Lower the cost of running the eval](#lower-the-cost-of-running-the-eval)
* [The bottom line](#the-bottom-line)
