<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/generating-test-datasets -->

Lesson 12 of 65 · Claude with Amazon BedrockGenerating test datasets

Building a custom prompt evaluation workflow starts with creating a clear goal and generating test data. In this case, we're building a prompt that helps users write AWS-specific code - either Python functions, JSON configurations, or regular expressions - with no extra explanations or formatting.

## Setting Up the Goal

The prompt should take a user's task description and return one of three output types:

* Python code
* JSON configuration
* Regular expressions

The key requirement is that responses should contain only the requested code without headers, footers, or explanations.

![](https://academy.claude.com/assets/media/b90f92e3b63fb425b59dc9502e316ab8be95c504567d5d380d8e458ccce18114.png)

Starting with a simple first version keeps things manageable. The initial prompt template is straightforward: "Please provide a solution to the following task: {task}"

## Creating Evaluation Datasets

An evaluation dataset contains input examples that you'll feed into your prompt. Each test case gets combined with your prompt and sent to Claude, letting you see how well the prompt performs across different scenarios.

![](https://academy.claude.com/assets/media/c241835434eb37b364613c1db43a14d7d6b4afbd8a5505b2d6d1b95dbe3dc3b7.png)

You can create datasets in two ways:

* Manually write test cases by hand
* Generate them automatically using Claude

For automatic generation, using a faster model like Haiku makes sense since you're generating multiple test cases.

## Generating Test Data with Code

The dataset generation function uses Claude to create realistic test scenarios. Here's the basic structure:

python

```
def generate_dataset():
    prompt = """
    Generate 3 AWS-related tasks that require Python, JSON, or Regex solutions.

    Focus on tasks that can be solved by writing a single Python function,
    a single JSON object, or tasks that do not require writing much code.

    Example output:
    [
        {
            "task": "Description of task"
        },
        ...additional
    ]

    Please generate 3 objects.
    """

    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

```` This approach uses the pre-filled assistant message technique with stop sequences to extract clean JSON responses. The assistant message starts with "```json" and stops at the closing "```", ensuring you get properly formatted data. ## Saving Your Dataset Once generated, save the dataset to avoid regenerating it constantly: ``` dataset = generate_dataset() with open("dataset.json", "w") as f: json.dump(dataset, f, indent=2) ``` ` The generated dataset creates realistic AWS tasks like extracting account IDs from ARNs, writing JSON schemas for EC2 configurations, and creating regex patterns for S3 bucket names. While three test cases work for initial development, production evaluation would need significantly more examples with greater variety. This foundation gives you a repeatable process for creating evaluation datasets that match your specific use case, setting up the next steps of running evaluations and measuring prompt performance. ` ````
