<!-- source: https://academy.claude.com/courses/introduction-to-evals/evals-in-production -->

Lesson 4 of 4 · Introduction to evalsEvals in production: CI, batch, and drift

3. /[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

# Evals in production: CI, batch, and drift

Lesson 410 min

Evals in production: CI, batch, and drift

An eval still has work to do after launch. On every pull request, it catches
a prompt change that breaks cases before a customer gets a wrong answer. It
also grades live traffic to catch drift, a slow drop in accuracy that comes
as real inputs change.

*The demo in this video was recorded in August 2026. It ran on Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5. Results will differ on newer models. Each lesson's demo is a separate eval run, so its scores and costs won't match those in other lessons.*

**Your eval still runs after launch, because two things keep changing.** Your team will edit the prompt, and an edit can break answers that were right. Real inputs change too, until they stop looking like the ones you tested. So the eval runs on every edit before it ships, and on live traffic after.

This lesson follows Meridian, a fictional engineering consultancy whose prompt reads each monthly project report and returns three fields: the project ID, the schedule status, and the top risk. Meridian's eval has 50 cases. Each case is a report plus the answer you expect for it, and all 50 together make up the full suite.

These four steps keep Meridian's eval working after launch:

1. Run a few cases on every pull request.
2. Keep a pull request from merging until it passes.
3. Run the full suite as one batch.
4. Grade a sample of live traffic every night.

## Run a few cases on every pull request[](#run-a-few-cases-on-every-pull-request)

**Add a workflow to CI, short for continuous integration, and have it run on each pull request.** The workflow runs a smoke eval, which takes few enough of the full suite's cases to finish while you wait. Its score passes or fails a check on the pull request. Meridian picks 10 of its 50 cases to cover every kind of report, and runs them on Claude Haiku 4.5 in about a minute.

The threshold is the lowest passing score, and Meridian's is 88%, so nine of the ten cases have to succeed. The workflow does four tasks, in this order:

1. Run the eval script and save what it returns as JSON.
2. Score those results against the threshold.
3. Comment on the pull request with the results.
4. Fail the check if the score is below the threshold.

Meridian uses GitHub Actions for this, but any CI system able to run your eval script can do the same four tasks. The file itself is in the box below.

## Keep a pull request from merging until it passes[](#keep-a-pull-request-from-merging-until-it-passes)

**Turn on a branch protection rule that makes the smoke eval a [required check(opens in new tab)](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging), one that must pass before a pull request can merge.** The rule belongs to the branch, not the workflow file, and without it a red X is just a warning.

At Meridian, an engineer opens a pull request called "Simplify extraction prompt" that drops two rules. One told Claude to return `null` when a report gives no top risk, and the other had Claude quote the line the risk comes from before answering.

The run scores 80%, below the 88% threshold. Both failures are missing-risk cases, reports that have no risk section, so each should have come back `null`, but Claude named a risk anyway.

![A github-actions comment on the pull request: Prompt eval at 80%, 8 of 10 cases passed, below the 88% threshold, with the two failing missing-risk cases listed](https://academy.claude.com/assets/media/cc87d057f262bf70c4e3f51f8d80d16416e38bb7324350a5d5376e432ca2989e.png)

*The smoke eval scores 80% and falls short of the 88% threshold, because in two missing-risk cases Claude named a risk the report never gives.*

The red check keeps the merge button grey, and its comment shows the engineer which cases broke: r041 and r042. Once the prompt is fixed and pushed, the check goes green and the merge can go ahead, so no customer ever saw the broken prompt.

![The same pull request after the fix: Prompt eval at 100%, all checks have passed, and the merge button is enabled](https://academy.claude.com/assets/media/fa95b27cd7b5a83a851d1168a091525b04d73bc624e5489c87d57267d9610ced.png)

*After the fix every case passes at 100%, so the merge is no longer blocked.*

## Run the full suite as one batch[](#run-the-full-suite-as-one-batch)

**Run the full suite [whenever you change the prompt or the model(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#how-evals-fit-with-other-methods-for-a-holistic-understanding-of-agents), and send it through the [Batch API(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing).** Meridian's eval compares Haiku 4.5, Claude Sonnet 5, and Claude Opus 5, so its batch holds 150 requests, all 50 cases for each. The Batch API runs them all for [half the usual price for input and output tokens(opens in new tab)](https://platform.claude.com/docs/en/about-claude/pricing#batch-processing), and you collect the answers later, [usually within the hour(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#message-batches-api).

| Model | Standard price | Batch API price |
| --- | --- | --- |
| Haiku 4.5 | $0.0468 | $0.0234 |
| Sonnet 5 | $0.1301 | $0.0650 |
| Opus 5 | $0.3432 | $0.1716 |

*Standard and Batch API prices for one pass through Meridian's 50 cases on each model, as of August 2026. [Today's prices(opens in new tab)](https://claude.com/pricing).*

[Batch the requests no one waits on, and use standard ones where someone does(opens in new tab)](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#batch-work-that-can-wait). Only the smoke eval, which a merge waits on, stays on `client.messages.create(...)`.

The eval script needs two changes.

**Label each request with a `custom_id`.** [Results can arrive in any order(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#best-practices-for-effective-batching), so you match them by this label, and it has to be unique in the batch. Each case goes to three models, so join the case ID to the model, as in `r041_claude-haiku-4-5`.

python

```
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": f"{case['id']}_{model}",
            "params": {
                "model": model,
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": case["prompt"]}],
            },
        }
        for model in MODELS
        for case in CASES
    ]
)
```

**Read `request_counts` before you score.** It counts how many requests ended each way, which shows when a run came back short. [A batch not done within 24 hours expires(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#batch-limitations), and [an expired request costs nothing but has no answer(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#retrieving-batch-results).

python

```
batch = client.messages.batches.retrieve(batch.id)
print(batch.request_counts)

answers = {}
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        answers[result.custom_id] = result.result.message
```

## Grade a sample of live traffic every night[](#grade-a-sample-of-live-traffic-every-night)

**Grade a small sample of live traffic, the real requests your app handles, every night.** The full suite only knows the reports you had when you built it, so if a new client starts sending reports in a format none of your cases covers, your CI stays green as the answers get worse. That slow loss of accuracy is drift.

Here's how:

1. **Sample.** Pick out between 1 and 5% of live traffic.
2. **Grade the sample with an [LLM judge(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#grade-your-evaluations).** That's a second model that scores each answer against a rubric of written rules, using only the report, Claude's answer, and the rubric, so it doesn't need expected answers, which live traffic lacks. Still, [read a few answers yourself now and then(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#how-evals-fit-with-other-methods-for-a-holistic-understanding-of-agents), because a judge needs checking by a person too.
3. **Alert only on a real drop.** That's a night's score more than two standard deviations below the trailing baseline, the average of recent nights. Two standard deviations is a bigger change than a normal night brings.
4. **Make a case of each answer the judge marks incorrect.** Write its expected answer, then add the case to the full suite, because [cases from real failures(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#collect-tasks-for-the-initial-eval-dataset) keep the suite close to real use.

Live traffic shows you what the full suite misses, and each failure you add narrows that gap. Treat the 1 to 5% and the two standard deviations as starting points to tune for your own traffic.

## The bottom line[](#the-bottom-line)

1. Have a smoke eval run on each pull request, and let its score pass or fail the check.
2. Make that check required, so a low score really does stop the merge.
3. Run the full suite as a batch, which costs half as much, because no one is waiting for it.
4. Grade a nightly sample of live traffic, alert when the score drops further than usual, and turn every failure into a new case in the full suite.

[Previous lessonIterate the prompt before you upgrade the model](https://academy.claude.com/courses/introduction-to-evals/iterate-the-prompt-before-you-upgrade-the-model)[Next lessonCourse quiz](https://academy.claude.com/courses/introduction-to-evals/course-quiz)

Lesson 4 of 4 · Introduction to evalsEvals in production: CI, batch, and drift

Before launch

* [When to use what model](https://academy.claude.com/courses/introduction-to-evals/when-to-use-what-model)
* [Build a minimum viable eval](https://academy.claude.com/courses/introduction-to-evals/build-a-minimum-viable-eval)
* [Iterate the prompt before you upgrade the model](https://academy.claude.com/courses/introduction-to-evals/iterate-the-prompt-before-you-upgrade-the-model)

After launch

* [Evals in production: CI, batch, and drift](https://academy.claude.com/courses/introduction-to-evals/evals-in-production)

Quiz and next steps

* [Course quizQuiz](https://academy.claude.com/courses/introduction-to-evals/course-quiz)

* [Completion badge](https://academy.claude.com/courses/introduction-to-evals/badge)

* [Run a few cases on every pull request](#run-a-few-cases-on-every-pull-request)
* [Keep a pull request from merging until it passes](#keep-a-pull-request-from-merging-until-it-passes)
* [Run the full suite as one batch](#run-the-full-suite-as-one-batch)
* [Grade a sample of live traffic every night](#grade-a-sample-of-live-traffic-every-night)
* [The bottom line](#the-bottom-line)
