<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/model-based-grading -->

Lesson 14 of 66 · Claude with Google Cloud's Vertex AIModel based grading

When building prompt evaluation workflows, grading systems provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1 and 10, where 10 represents high quality and 1 represents poor quality.

## Types of Graders

![](https://academy.claude.com/assets/media/4ddd6988ba49fadfcd2e95aeb3da98a4d9537d0bf0918d0223eaf0d97ce1bc50.png)

There are three main approaches to grading model outputs:

* **Code graders** - Programmatically evaluate outputs using custom code
* **Model graders** - Use another AI model to assess the quality
* **Human graders** - Have people manually review and score outputs

### Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

* Checking output length
* Verifying output does or doesn't contain certain words
* Syntax validation for JSON, Python, or regex
* Readability scores to ensure appropriate reading levels

### Model Graders

Model graders offer tremendous flexibility by using an additional API call to evaluate outputs. They're useful for assessing:

* Response quality
* Quality of instruction following
* Completeness
* Helpfulness
* Safety

### Human Graders

Human graders provide the most flexibility but come with significant downsides. While humans can evaluate responses for any criteria imaginable, the process is time-consuming and tedious.

## Defining Evaluation Criteria

![](https://academy.claude.com/assets/media/73dbc7e22915d1004fcfe651c18a37312bbf0d5ed7e2973048ff77364e1ada21.png)

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

* **Format** - Should return only Python, JSON, or Regex without explanation
* **Valid Syntax** - Produced code should have valid syntax
* **Task Following** - Response should directly address the user's task with accurate code

![](https://academy.claude.com/assets/media/f105fac52c912c56853b65e239d1d3836e77b466273e5f0432528e6ed7098e61.png)

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

## Implementing a Model Grader

Model graders are often the easiest to implement. Here's a basic structure:

python

```
def grade_by_model(test_case, output):
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

![](https://academy.claude.com/assets/media/d155671c3adeac0adb05a09cf0fc9c4652494fd25aa2b2a0a571f6d792086c15.png)

The grading prompt should be comprehensive and include:

* Clear role definition for the grader
* The original task
* The AI-generated solution to evaluate
* Specific output format requirements

Ask for more than just a score. Request strengths, weaknesses, and reasoning alongside the numerical score. This prevents the model from defaulting to middling scores like 6 and forces more thoughtful evaluation.

## Integrating Graders into Your Workflow

Once you have a grader function, integrate it into your test case runner:

python

```
def run_test_case(test_case):
    output = run_prompt(test_case)

    # Call the model grader
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]

    return {
        "output": output,
        "test_case": test_case,
        "score": score,
        "reasoning": reasoning
    }
```

After running all test cases, calculate an average score to get an objective metric for your prompt's performance:

python

```
from statistics import mean

def run_eval(dataset):
    results = []
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")

    return results
```

This gives you a concrete number to focus on improving. While model graders can be somewhat capricious and might benefit from better guidance, they provide a starting point for objective evaluation that you can iterate on and improve.
