<!-- source: https://platform.claude.com/docs/en/test-and-evaluate/eval-tool -->

# Using the Evaluation Tool
The [Claude Console](https://platform.claude.com/dashboard) features an **Evaluation tool** that allows you to test your prompts under various scenarios.
Accessing the Evaluate Feature
To get started with the Evaluation tool:
  1. Open the Claude Console and navigate to the prompt editor.
  2. After composing your prompt, look for the 'Evaluate' tab at the top of the screen.

![Accessing Evaluate Feature](https://platform.claude.com/docs/images/access_evaluate.png)

Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: {{variable}}. This is required for creating eval test sets.
Generating Prompts
The Console offers a built-in [prompt generator](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools) powered by Claude Sonnet 4.5:
  1. 1
Click 'Generate Prompt'
Clicking the 'Generate Prompt' helper tool will open a modal that allows you to enter your task information.
  2. 2
Describe your task
Describe your desired task (e.g., "Triage inbound customer support requests") with as much or as little detail as you desire. The more context you include, the more Claude can tailor its generated prompt to your specific needs.
  3. 3
Generate your prompt
Clicking the orange 'Generate Prompt' button at the bottom will have Claude generate a high quality prompt for you. You can then further improve those prompts using the Evaluation screen in the Console.

This feature makes it easier to create prompts with the appropriate variable syntax for evaluation.
![Prompt Generator](https://platform.claude.com/docs/images/promptgenerator.png)
Creating Test Cases
When you access the Evaluation screen, you have several options to create test cases:
  1. Click the '+ Add Row' button at the bottom left to manually add a case.
  2. Use the 'Generate Test Case' feature to have Claude automatically generate test cases for you.
  3. Import test cases from a CSV file.

To use the 'Generate Test Case' feature:
  1. 1
Click on 'Generate Test Case'
Claude will generate test cases for you, one row at a time for each time you click the button.
  2. 2
Edit generation logic (optional)
You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the 'Generate Test Case' button, then on 'Show generation logic' at the top of the Variables window that pops up. You may have to click `Generate' on the top right of this window to populate initial generation logic.
Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.

Here's an example of a populated Evaluation screen with several test cases:
![Populated Evaluation Screen](https://platform.claude.com/docs/images/eval_populated.png)
If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.
Tips for Effective Evaluation
### Prompt Structure for Evaluation

Use the 'Generate a prompt' helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.
Understanding and comparing results
The Evaluation tool offers several features to help you refine your prompts:
  1. **Side-by-side comparison** : Compare the outputs of two or more prompts to quickly see the impact of your changes.
  2. **Quality grading** : Grade response quality on a 5-point scale to track improvements in response quality per prompt.
  3. **Prompt versioning** : Create new versions of your prompt and re-run the test suite to quickly iterate and improve results.

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments to your prompt more efficiently.
Start evaluating your prompts today to build more robust AI applications with Claude!
  * [Accessing the Evaluate Feature](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool#accessing-the-evaluate-feature)
  * [Generating Prompts](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool#generating-prompts)
  * [Creating Test Cases](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool#creating-test-cases)
  * [Tips for Effective Evaluation](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool#tips-for-effective-evaluation)
  * [Understanding and comparing results](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool#understanding-and-comparing-results)

Best practices/Test and evaluate
# Using the Evaluation Tool
The [Claude Console](https://platform.claude.com/dashboard) features an **Evaluation tool** that allows you to test your prompts under various scenarios.
Accessing the Evaluate Feature
To get started with the Evaluation tool:
  1. Open the Claude Console and navigate to the prompt editor.
  2. After composing your prompt, look for the 'Evaluate' tab at the top of the screen.

![Accessing Evaluate Feature](https://platform.claude.com/docs/images/access_evaluate.png)

Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: {{variable}}. This is required for creating eval test sets.
Generating Prompts
The Console offers a built-in [prompt generator](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools) powered by Claude Sonnet 4.5:
  1. 1
Click 'Generate Prompt'
Clicking the 'Generate Prompt' helper tool will open a modal that allows you to enter your task information.
  2. 2
Describe your task
Describe your desired task (e.g., "Triage inbound customer support requests") with as much or as little detail as you desire. The more context you include, the more Claude can tailor its generated prompt to your specific needs.
  3. 3
Generate your prompt
Clicking the orange 'Generate Prompt' button at the bottom will have Claude generate a high quality prompt for you. You can then further improve those prompts using the Evaluation screen in the Console.

This feature makes it easier to create prompts with the appropriate variable syntax for evaluation.
![Prompt Generator](https://platform.claude.com/docs/images/promptgenerator.png)
Creating Test Cases
When you access the Evaluation screen, you have several options to create test cases:
  1. Click the '+ Add Row' button at the bottom left to manually add a case.
  2. Use the 'Generate Test Case' feature to have Claude automatically generate test cases for you.
  3. Import test cases from a CSV file.

To use the 'Generate Test Case' feature:
  1. 1
Click on 'Generate Test Case'
Claude will generate test cases for you, one row at a time for each time you click the button.
  2. 2
Edit generation logic (optional)
You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the 'Generate Test Case' button, then on 'Show generation logic' at the top of the Variables window that pops up. You may have to click `Generate' on the top right of this window to populate initial generation logic.
Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.

Here's an example of a populated Evaluation screen with several test cases:
![Populated Evaluation Screen](https://platform.claude.com/docs/images/eval_populated.png)
If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.
Tips for Effective Evaluation
### Prompt Structure for Evaluation

Use the 'Generate a prompt' helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.
Understanding and comparing results
The Evaluation tool offers several features to help you refine your prompts:
  1. **Side-by-side comparison** : Compare the outputs of two or more prompts to quickly see the impact of your changes.
  2. **Quality grading** : Grade response quality on a 5-point scale to track improvements in response quality per prompt.
  3. **Prompt versioning** : Create new versions of your prompt and re-run the test suite to quickly iterate and improve results.

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments to your prompt more efficiently.
Start evaluating your prompts today to build more robust AI applications with Claude!
