<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/code-execution-and-the-files-api -->

Lesson 46 of 67 · Building with the Claude APICode execution and the Files API

The Anthropic API offers two powerful features that work exceptionally well together: the Files API and Code Execution. While they might seem separate at first, combining them opens up some really interesting possibilities for delegating complex tasks to Claude.

## Files API

The Files API provides an alternative way to handle file uploads. Instead of encoding images or PDFs directly in your messages as base64 data, you can upload files ahead of time and reference them later.

![](https://academy.claude.com/assets/media/ee042cc9aaaaf3d0ce0177dd43d9c26aca27190fbac45d51f37c4318f7b22e07.jpg)

Here's how it works:

* Upload your file (image, PDF, text, etc.) to Claude using a separate API call
* Receive a file metadata object containing a unique file ID
* Reference that file ID in future messages instead of including raw file data

![](https://academy.claude.com/assets/media/96059a1704f4b5ec3f88bcd6519f2bf178558676fcabf3fdd4e5dc2d66912f6b.jpg)

This approach is particularly useful when you want to reference the same file multiple times or when working with larger files that would be cumbersome to include in every request.

## Code Execution Tool

Code execution is a server-based tool that doesn't require you to provide an implementation. You simply include a predefined tool schema in your request, and Claude can optionally execute Python code in an isolated Docker container.

![](https://academy.claude.com/assets/media/1d10a3e11cdf7df719894139c9797e7aaa5d19634fbdf4ff35f36937fd8a1cde.jpg)

Key characteristics of the code execution environment:

* Runs in an isolated Docker container
* No network access (can't make external API calls)
* Claude can execute code multiple times during a single conversation
* Results are captured and interpreted by Claude for the final response

## Combining Files API and Code Execution

The real power comes from using these features together. Since the Docker containers have no network access, the Files API becomes the primary way to get data in and out of the execution environment.

![](https://academy.claude.com/assets/media/f680a4ba00bc0efa3ab86156263d34ed95e0fb7d7181341677e9b386a246ee33.jpg)

Here's a typical workflow:

1. Upload your data file (like a CSV) using the Files API
2. Include a container upload block in your message with the file ID
3. Ask Claude to analyze the data
4. Claude writes and executes code to process your file
5. Claude can generate outputs (like plots) that you can download

## Practical Example

Let's look at a real example using streaming service data. The CSV file contains user information including subscription tiers, viewing habits, and whether they've churned (canceled their subscription).

![](https://academy.claude.com/assets/media/37896049b6036071a0c10181dfa7468260b1c071ebd49e15223861d9918581b0.jpg)

First, upload the file using a helper function:

python

```
file_metadata = upload('streaming.csv')
```

Then create a message that includes both the uploaded file and a request for analysis:

python

```
messages = []
add_user_message(
    messages,
    [
        {
            "type": "text",
            "text": """Run a detailed analysis to determine major drivers of churn.
            Your final output should include at least one detailed plot summarizing your findings."""
        },
        {"type": "container_upload", "file_id": file_metadata.id},
    ],
)

chat(
    messages,
    tools=[{"type": "code_execution_20250522", "name": "code_execution"}]
)
```

## Understanding the Response

When Claude uses code execution, the response contains multiple types of blocks:

* **Text blocks** - Claude's analysis and explanations
* **Server tool use blocks** - The actual code Claude decided to run
* **Code execution tool result blocks** - Output from running the code

![](https://academy.claude.com/assets/media/532b74fcf5245797a3f537305a22a033db55c59faf5995bca4834ad517066a4d.jpg)

Claude might execute code multiple times during a single response, iteratively building up its analysis. Each execution cycle includes the code and its results.

## Downloading Generated Files

One of the most powerful features is Claude's ability to generate files (like plots or reports) and make them available for download. When Claude creates a visualization, it gets stored in the container and you can download it using the Files API.

Look for blocks with `type: "code_execution_output"` in the response - these contain file IDs for generated content:

python

```
download_file("file_id_from_response")
```

![](https://academy.claude.com/assets/media/8c86d9737bcc9bcf07c7a91c64fe2311e8878e713e0c5fab8471de65cc71907b.jpg)

The result is a comprehensive analysis with professional visualizations that would have taken significant manual coding to produce.

## Beyond Data Analysis

While data analysis is a natural fit, the combination of Files API and code execution opens up many possibilities:

* Image processing and manipulation
* Document parsing and transformation
* Mathematical computations and modeling
* Report generation with custom formatting

The key is that you can delegate complex, computational tasks to Claude while maintaining control over the inputs and outputs through the Files API. This creates a powerful workflow where Claude becomes your coding assistant that can actually execute and iterate on solutions.
