<!-- source: https://academy.claude.com/courses/tool-use-with-the-messages-api/streaming-tool-calls -->

Lesson 4 of 9 · Tool use with the Messages APIStreaming tool calls: No more frozen spinners

3. /[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

# Streaming tool calls: No more frozen spinners

Lesson 48 min

Streaming tool calls: No more frozen spinners

SummaryTranscript

A streamed tool call arrives with the tool's name first and its input in pieces, so the screen can say what is happening. The video shows two versions of the screen at Meridian, a fictional engineering consultancy, side by side. One has no streaming and the other has streaming. The demo is simulated and runs at one-third speed.

*This video was recorded in September 2026, and its code uses Claude Sonnet 5 (`claude-sonnet-5`). Your results may differ on newer models.*

Say your user watches a spinner for eight seconds. That happens because your tool loop sends each request, waits, and gets back a finished response.

In that time Claude picks a tool and writes its input, your code runs the tool, and Claude writes the answer. Your code sees each response only once it is finished, so your UI has nothing to show while Claude writes.

Meridian has this problem today. Its support agent is written in Python and answers employees' questions about projects. When an employee asks "What's the status of the pump station job?" the screen says "thinking..." until the answer comes.

Streaming changes what that employee sees. **With streaming, your code gets the response piece by piece, before it is finished.** So Meridian's screen can say "Looking up project..." as soon as Claude picks the tool.

## What a streamed tool call looks like[](#what-a-streamed-tool-call-looks-like)

Where your tool loop sends its request, replace `client.messages.create(...)` with [`client.messages.stream(...)`(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/streaming#streaming-with-sdks). The response then arrives as a series of [server-sent events(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/streaming), small JSON messages that each have a `type`.

A response is made of content blocks, or blocks for short, with one block for each stretch of Claude's text and one for each tool call. A tool call's block has the type `tool_use`. Current models can also add thinking blocks, which this lesson's code ignores.

Picture a friend reading you a phone number over the phone. First they tell you whose number it is: "Here's the plumber's number." Then they read it out a few digits at a time, stopping wherever they like. Finally they say "That's it."

**A tool call's block arrives the way the phone number did.** One event opens it, one or more events fill it, and one event closes it. Here are the events of Meridian's tool call.

text

```
{"type": "content_block_start", "index": 0,
 "content_block": {"type": "tool_use", "id": "toolu_01",
                   "name": "lookup_project_status", "input": {}}}
{"type": "content_block_delta", "index": 0,
 "delta": {"type": "input_json_delta", "partial_json": "{\"project_"}}
{"type": "content_block_delta", "index": 0,
 "delta": {"type": "input_json_delta", "partial_json": "id\": \"MEG-2"}}
{"type": "content_block_delta", "index": 0,
 "delta": {"type": "input_json_delta", "partial_json": "026-0142\"}"}}
{"type": "content_block_stop", "index": 0}
```

## Show the chosen tool as soon as its block opens[](#show-the-chosen-tool-as-soon-as-its-block-opens)

**The tool's name is in `content_block_start`, the block's first event.** When that event arrives, your code can update the status line, the one line of text your UI shows while your user waits.

Meridian keeps a small dict, `STATUS`, that maps each tool's name to words for the user, so `lookup_project_status` becomes "Looking up project..." on the screen.

## Put the streaming request together[](#put-the-streaming-request-together)

**When the stream ends, call `stream.get_final_message()` to get the finished response, the same kind of object that `client.messages.create(...)` returns.** So the rest of your tool loop stays as it was.

Here is Meridian's streaming request. `on_status` is a function you write that shows a string as the status line.

## Key takeaways[](#key-takeaways)

* A streamed tool call arrives with the tool's name first, then its input in pieces.
* As soon as `content_block_start` arrives, show the chosen tool in words your user understands.
* `stream.get_final_message()` returns the finished response, so the rest of your tool loop doesn't change.

[Previous lessonParallel tool calling: Cut the latency](https://academy.claude.com/courses/tool-use-with-the-messages-api/parallel-tool-calling)[Next lessonCode execution: Claude runs the code it writes](https://academy.claude.com/courses/tool-use-with-the-messages-api/code-execution)

Lesson 4 of 9 · Tool use with the Messages APIStreaming tool calls: No more frozen spinners

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

* [What a streamed tool call looks like](#what-a-streamed-tool-call-looks-like)
* [Show the chosen tool as soon as its block opens](#show-the-chosen-tool-as-soon-as-its-block-opens)
* [Put the streaming request together](#put-the-streaming-request-together)
* [Key takeaways](#key-takeaways)
