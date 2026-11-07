<!-- source: https://academy.claude.com/courses/tool-use-with-the-messages-api/code-execution -->

Lesson 5 of 9 · Tool use with the Messages APICode execution: Claude runs the code it writes

3. /[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

# Code execution: Claude runs the code it writes

Lesson 58 min

Code execution: Claude runs the code it writes

SummaryTranscript

Code execution lets Claude write Python, run it on Anthropic's side, and
answer from what it prints.

*The demo in this video was recorded in September 2026. It ran on Claude Sonnet 5 (`claude-sonnet-5`). Results may differ on newer models.*

Some questions need math across many files. That's a job for code.

Take Meridian, a fictional engineering consultancy. It has 12 CSV files, one for each pump station, and each file holds a year of flow readings. It wants to know whether any station ever went over its design capacity, and if so, when.

Code execution is how Claude does that job. **Claude gets a container where it can run the Python it writes and answer from what the code prints.**

## Add the tool to your request[](#add-the-tool-to-your-request)

Code execution is a server tool, a tool that runs on Anthropic's infrastructure. You write no handler for it, and your code sends back no `tool_result`.

**Adding code execution takes one entry in your `tools` list.** The date at the end of the entry's `type` is the tool's version, and Meridian uses `code_execution_20260120`. The current versions are [listed in the Tool reference(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#anthropic-provided-tools), so copy the `type` value from there.

Meridian keeps the list in a constant named `TOOLS`, and its request passes it as `tools=TOOLS`:

python

```
TOOLS = [{"type": "code_execution_20260120", "name": "code_execution"}]
```

As of October 2026, [code execution(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#availability-feature-support) runs on the Claude API, Claude Platform on AWS, the Claude models on Google Cloud that Anthropic manages, and Microsoft Foundry deployments hosted on Anthropic.

## Put your files in the container[](#put-your-files-in-the-container)

Claude's code runs in a container on Anthropic's side. Your files are still on your machine, so the container doesn't have them yet. Meridian's program gets them into the container in two steps:

1. Upload each file with the [Files API(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/files), which gives you back a file ID.
2. Put that file ID in your message, in a `container_upload` block.

**Meridian's program adds one `container_upload` block for each file, in the same message as its question.** The files are then loaded onto the container, where Claude's code can open them.

## Read Claude's answer[](#read-claudes-answer)

**Your code sends one request and usually gets back the finished answer.**

The API can pause a long-running turn and return a `stop_reason` of `pause_turn`. When it does, send the response's content back as an assistant message, with the same `tools`, and Claude continues.

Claude's answer for Meridian is that Station 7 went over its design capacity of 600 L/s twice, in April and May 2025. In the response, the answer comes after the commands Claude ran.

## Put the program together[](#put-the-program-together)

Meridian's program below adds the tool, puts the files in the container, and reads the answer. In the program, `paths` holds the 12 CSV files as `pathlib.Path` objects, and `QUESTION` holds Meridian's question.

## Key takeaways[](#key-takeaways)

* Code execution is a server tool. You add one entry to `tools`, and Claude's code runs in a container on Anthropic's side.
* You upload each file with the Files API, then put its file ID in a `container_upload` block.

[Previous lessonStreaming tool calls: No more frozen spinners](https://academy.claude.com/courses/tool-use-with-the-messages-api/streaming-tool-calls)[Next lessonWeb search: Answers from the sites you trust](https://academy.claude.com/courses/tool-use-with-the-messages-api/web-search)

Lesson 5 of 9 · Tool use with the Messages APICode execution: Claude runs the code it writes

Reliable calls

* [Creating tools that Claude picks](https://academy.claude.com/courses/tool-use-with-the-messages-api/creating-tools-that-claude-picks)
* [Strict tool use: Stop rejecting your own calls](https://academy.claude.com/courses/tool-use-with-the-messages-api/strict-tool-use)

Parallel and streamed tool calls

* [Parallel tool calling: Cut the latency](https://academy.claude.com/courses/tool-use-with-the-messages-api/parallel-tool-calling)
* [Streaming tool calls: No more frozen spinners](https://academy.claude.com/courses/tool-use-with-the-messages-api/streaming-tool-calls)

Tools Anthropic provides

* [Code execution: Claude runs the code it writes](https://academy.claude.com/courses/tool-use-with-the-messages-api/code-execution)
* [Web search: Answers from the sites you trust](https://academy.claude.com/courses/tool-use-with-the-messages-api/web-search)
* [Computer use: Automate desktop software with no API](https://academy.claude.com/courses/tool-use-with-the-messages-api/computer-use)

Costs of tool-heavy requests

* [Cut the cost of tool-heavy workflows](https://academy.claude.com/courses/tool-use-with-the-messages-api/cut-the-cost-of-tool-heavy-workflows)

Quiz and next steps

* [Course quizQuiz](https://academy.claude.com/courses/tool-use-with-the-messages-api/course-quiz)
* [Start fixing your own tools](https://academy.claude.com/courses/tool-use-with-the-messages-api/next-steps)

* [Completion badge](https://academy.claude.com/courses/tool-use-with-the-messages-api/badge)

* [Add the tool to your request](#add-the-tool-to-your-request)
* [Put your files in the container](#put-your-files-in-the-container)
* [Read Claude's answer](#read-claudes-answer)
* [Put the program together](#put-the-program-together)
* [Key takeaways](#key-takeaways)
