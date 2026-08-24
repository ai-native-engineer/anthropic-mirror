<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/structure-with-xml-tags -->

Lesson 19 of 66 · Claude with Google Cloud's Vertex AIStructure with XML tags

When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

## Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

![](https://academy.claude.com/assets/media/31cfcf31ba1bc9fe15a2543c9236fc3509f70793a5414192e4bb642b9ddd5704.png)

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping different content sections in XML tags, you create clear delimiters that help Claude understand the structure of your prompt.

## Using XML Tags for Clarity

XML tags act as containers that separate distinct portions of your prompt. You can create custom tag names that describe the content they contain:

![](https://academy.claude.com/assets/media/36d7ff6d8c95678b923927f86e231dcb43dec2d8cffd63e4c7394e2334c25fd5.png)

In this case, wrapping the sales data in `<sales_records>` tags makes it immediately clear what that content represents. The tag name itself provides context about the data type.

## A Practical Example

Here's a more dramatic example that shows why structure matters. On the left, you have a debugging request with mixed code and documentation:

![](https://academy.claude.com/assets/media/06552fb30df1c3da1b204e2c362c55d78c2aa236d4c6a149b1e55bc594752e58.png)

Without clear boundaries, Claude has to guess which parts are the buggy code and which parts are documentation. The improved version on the right uses XML tags to separate these concerns:

```
<my_code>
from datavortex import Pipeline, DataSource

def process_data(input_file, output_file):
    pipeline = Pipeline()
    source = DataSource.from_csv(input_file)
</my_code>

<docs>
# Creating a data source from data vortex
csv_source = DataSource.from_csv("data.csv")
</docs>
```



Now Claude can easily identify what needs debugging versus what serves as reference material.

## Applying Structure to Your Prompts

Even when your interpolated content isn't massive, XML tags can still improve clarity. For example, when generating meal plans, you might group athlete information together:

```
<athlete_information>
- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
</athlete_information>
```



This makes it explicit that these values represent external input about the athlete, rather than part of your instructions.

## Key Benefits

* Most useful when including large amounts of context or data
* Help serve as clear delimiters for Claude to parse different content types
* Improve Claude's ability to understand the relationship between different parts of your prompt
* Make your prompts more maintainable and easier to debug

XML tags are particularly valuable when you're working with complex prompts that mix instructions, data, examples, and other content types. The clearer you can make the structure, the better Claude can understand and respond to your specific needs.
