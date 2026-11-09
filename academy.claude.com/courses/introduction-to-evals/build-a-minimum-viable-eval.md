<!-- source: https://academy.claude.com/courses/introduction-to-evals/build-a-minimum-viable-eval -->

Lesson 2 of 4 · Introduction to evalsBuild a minimum viable eval

3. /[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

[Introduction to evals](https://academy.claude.com/courses/introduction-to-evals)

# Build a minimum viable eval

Lesson 215 min

Build a minimum viable eval

Ask five engineers which Claude model handles a task best, and you'll get
five opinions. An eval gives you a number instead, and a useful one can
start small. This lesson builds a small eval for Meridian, a fictional
engineering consultancy.

*The demo in this video was recorded in August 2026. It ran on Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5. Results will differ on newer models. Each lesson's demo is a separate eval run, so its scores and costs won't match those in other lessons.*

**An eval is a test that models take.** It has three parts: realistic inputs, the answer you expect for each, and a way to grade what each model returns. Each model runs your prompt on every input. An input together with its expected answer makes a case, and grading every case gives you a score.

Meridian's extraction prompt pulls three fields out of each monthly project report: the project ID and the schedule status, which are short values, and the top risk, which is a sentence.

Building an eval is like giving an exam, with you as the teacher and the models as the students.

| The exam | The eval |
| --- | --- |
| The teacher writes the exam and its answer key before anyone takes it. | You write the expected answers before any model runs. |
| A scoring machine grades the multiple-choice section from the key. | Code compares a field with its expected answer. |
| The essay question goes to a teaching assistant with a grading guide. | A sentence goes to an LLM judge with a rubric. |
| The teacher grades a few essays before trusting the assistant with the rest. | You hand-grade a sample. |

An LLM judge is a second model that checks an answer and decides whether it's right. Anything that grades an answer is called a grader, whether it's code, a model, or a person. You'll build Meridian's eval in six steps:

1. Choose a grader for each field
2. Design the set of cases
3. Write down the expected answers
4. Set up the LLM judge for the top risk
5. Run the models and grade their answers
6. Hand-grade a sample before you trust the judge

## Choose a grader for each field[](#choose-a-grader-for-each-field)

There are three ways to grade an answer. The rule is to [pick the quickest method that's also reliable and scales(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#grade-your-evaluations).

1. **Code-based grading.** Your code checks that an answer matches its expected answer exactly, or that it contains a key phrase. It's the quickest and most reliable way, and it scales to any number of cases.
2. **LLM judge.** The judge fits answers where two different sentences can both be right. It's also quick, flexible, and scalable.
3. **Human grading.** A person reads each answer, which gives the best quality but is slow and costly, so it comes last. People are still the right graders for specialized, high-stakes work and for answers that come down to judgment.

**Use code for every field it can check exactly, and give the judge only what's left.** Here's how that plays out for Meridian's three fields on one of its cases, report r032.

| Field | Expected answer in r032 | Grader, and why |
| --- | --- | --- |
| `project_id` | MER-2524 | Code, with an exact match, because an ID is either right or wrong |
| `schedule_status` | delayed | Code, with an exact match, because the field can only be `on_track`, `at_risk`, or `delayed` |
| `top_risk` | Utility relocation by the gas company is running four weeks behind their committed schedule. | The judge, because there are many ways to put the same risk into words |

When a report names no risk, though, the expected `top_risk` answer is `null`, JSON's empty value. Code can check that with an exact match.

## Design the set of cases[](#design-the-set-of-cases)

Four rules shape the whole set of cases. They build on the [eval design principles(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#eval-design-principles) in the docs.

1. **Make cases task-specific.** Build them from your own real reports, because sample data only shows how a model does on samples.
2. **Automate the grading.** You'll run the set again and again, so the everyday grading has to work without a person.
3. **Favor volume over polish.** For the same effort, many cases graded automatically tell you more than a few graded carefully by hand.
4. **Stratify your edge cases.** An edge case is an unusual input that production still sends, such as a scanned report. Give each kind about the share of cases it has in production, so if scanned reports are 5% of what arrives, make them about 5% of the set.

**Above all, the mix of cases should look like what production sends you.** Teams often take volume to mean hundreds of cases, but [a set of 20 to 50 simple ones is a great start(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

Meridian settled on 50 cases. Thirty are typical reports, 10 cover several projects, and 10 are missing-risk cases, which means reports with no risk section. Both unusual kinds reach Meridian often enough that it wants them covered.

## Write down the expected answers[](#write-down-the-expected-answers)

Cases whose expected answers a person has written down are called a labeled set. **Write each expected answer yourself, from the report, before any model runs.** The code grader compares the models' answers against them.

Meridian keeps its labeled set in one file, `golden.json`, with one record for each case. A record holds the case's `id`, its `category`, and the expected answer for each field. The `category` is `typical`, `multi_project`, or `missing_risk`.

## Set up the LLM judge for the top risk[](#set-up-the-llm-judge-for-the-top-risk)

The `top_risk` field holds a sentence. Code can't tell whether two different sentences name the same risk, so this field goes to the judge. It's the essay question, and like the teaching assistant, the judge needs a grading guide.

That guide is a rubric, a written set of rules for what counts as correct and what counts as incorrect. [It should be detailed and clear(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#tips-for-llm-based-grading).

The judge's prompt holds the report, the answer, and the rubric. [Each goes in its own XML tags(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags), so the judge is less likely to mix them up. Your expected answer isn't in the prompt, because the judge decides from the report itself. That way an answer doesn't lose credit just for wording the risk differently from you. Keep your expected answer anyway, since it's your record of the right answer when you grade a sample by hand.

The judge's decision on one answer is called its verdict. **A verdict is only useful if it comes back in a shape your code can count.** [Structured outputs(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) give you that. You send a JSON schema with the request, and the response has to match it. A JSON schema describes which fields the JSON may hold and what can go in each one.

Meridian's schema has two fields, `explanation` and `verdict`. The verdict must be `correct`, `incorrect`, or `unknown`. The explanation is a short account of why the judge decided as it did, so it's what you read when you want to know what went wrong with an answer.

The value that matters most is `unknown`. It gives the judge [a way out(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), an option to say it can't tell. Without it, the judge has to guess between the other two whenever it isn't sure.

## Run the models and grade their answers[](#run-the-models-and-grade-their-answers)

Before anything can be graded, you need answers. Run your prompt on every case with each model you're testing, and save every answer to a file. Meridian ran its extraction prompt on all 50 cases with Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5.

**Test the judge once, on cases code can also grade, to see whether the two graders agree.** Meridian's first judge run took only the 10 missing-risk cases, which came to 30 answers across the three models. Their expected answer is `null`, so code could grade them too. Save each verdict next to its answer, so you can check the judge by hand later.

| Model | Correct | Incorrect | Unknown | Agrees with code grader |
| --- | --- | --- | --- | --- |
| Haiku 4.5 | 5 | 5 | 0 | 10/10 |
| Sonnet 5 | 10 | 0 | 0 | 10/10 |
| Opus 5 | 10 | 0 | 0 | 10/10 |

*The judge's first run, on the 10 missing-risk cases, where code could grade too.*

For reports with no risk section, Meridian now has a number for each model where it used to have opinions.

Haiku 4.5's five incorrect answers are all the same kind of mistake, and case r045 shows one.

| In case r045 | Text |
| --- | --- |
| What the report says about a county permit renewal | "the team does not anticipate any issues with the renewal." |
| Haiku 4.5's answer | "County permit renewal window opens next quarter and could impact project continuity if not completed timely." |
| The judge's explanation | "The answer converts this explicitly-reassuring routine note into a top risk, which the rubric says is incorrect. The correct answer would have been null." |

The judge's explanation names the kind of mistake the answer made. That mistake comes from the extraction prompt, which never says what to do when a report names no risk.

## Hand-grade a sample before you trust the judge[](#hand-grade-a-sample-before-you-trust-the-judge)

The judge agreed with code on all 30 answers, but code could check those anyway. The judge's real job is grading free text, where code can't help. **Before you give it that job, [test that it's reliable(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#grade-your-evaluations).** Two practices help.

1. **Grade a sample yourself.** Grade a handful of saved answers by hand and compare your grades with the judge's verdicts, because [a judge should agree closely with human experts(opens in new tab)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Where you and the judge disagree, make the rubric clearer and run it again.
2. **Use a judge that didn't write the answers.** It's [generally best to grade with a different model from the one that wrote the output(opens in new tab)](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#example-evals).

## The bottom line[](#the-bottom-line)

1. Grade with code where an exact check works, with a judge where two different sentences can both be right, and with people where it comes down to judgment.
2. Write the expected answers down before any model runs, and build a set of cases that looks like production.
3. Give the judge a rubric, a schema its verdict has to match, and the option to say `unknown`.
4. Grade a sample of the judge's work by hand before you trust it.

[Previous lessonWhen to use what model](https://academy.claude.com/courses/introduction-to-evals/when-to-use-what-model)[Next lessonIterate the prompt before you upgrade the model](https://academy.claude.com/courses/introduction-to-evals/iterate-the-prompt-before-you-upgrade-the-model)

Lesson 2 of 4 · Introduction to evalsBuild a minimum viable eval

Before launch

* [When to use what model](https://academy.claude.com/courses/introduction-to-evals/when-to-use-what-model)
* [Build a minimum viable eval](https://academy.claude.com/courses/introduction-to-evals/build-a-minimum-viable-eval)
* [Iterate the prompt before you upgrade the model](https://academy.claude.com/courses/introduction-to-evals/iterate-the-prompt-before-you-upgrade-the-model)

After launch

* [Evals in production: CI, batch, and drift](https://academy.claude.com/courses/introduction-to-evals/evals-in-production)

Quiz and next steps

* [Course quizQuiz](https://academy.claude.com/courses/introduction-to-evals/course-quiz)

* [Completion badge](https://academy.claude.com/courses/introduction-to-evals/badge)

* [Choose a grader for each field](#choose-a-grader-for-each-field)
* [Design the set of cases](#design-the-set-of-cases)
* [Write down the expected answers](#write-down-the-expected-answers)
* [Set up the LLM judge for the top risk](#set-up-the-llm-judge-for-the-top-risk)
* [Run the models and grade their answers](#run-the-models-and-grade-their-answers)
* [Hand-grade a sample before you trust the judge](#hand-grade-a-sample-before-you-trust-the-judge)
* [The bottom line](#the-bottom-line)
