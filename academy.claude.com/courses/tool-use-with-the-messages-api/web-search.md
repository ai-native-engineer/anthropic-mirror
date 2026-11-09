<!-- source: https://academy.claude.com/courses/tool-use-with-the-messages-api/web-search -->

Lesson 6 of 9 · Tool use with the Messages APIWeb search: Answers from the sites you trust

3. /[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

# Web search: Answers from the sites you trust

Lesson 67 min

Web search: Answers from the sites you trust

SummaryTranscript

The web search tool lets Claude search the web while it works on your
request. Dynamic filtering keeps only the relevant parts of the search
results, so you use fewer tokens on search-heavy requests. Meridian, a
fictional engineering consultancy, cites engineering standards in its
proposals.

*The demo in this video was recorded in September 2026. It ran on Claude Sonnet 5 (`claude-sonnet-5`). Results may differ on newer models.*

Claude answers from what it learned in training, so it doesn't know about anything newer than that, or anything that was never in it. When a question needs those facts, someone has to look them up, and that legwork falls to you.

**With the web search tool, Claude does that legwork itself, searching the web while it works on your request and answering from what it finds.**

One of Meridian's proposals cites four Canadian engineering standards by clause, and Meridian carries professional liability if any reference is wrong. So before the proposal goes out, Meridian wants each reference checked against official sources.

## Add the tool to your request[](#add-the-tool-to-your-request)

Web search is a server tool. It runs on Anthropic's infrastructure, so you don't write a handler for it or send back a `tool_result`.

**Adding it takes one entry in your `tools` list.** The entry's `type` picks the version of the tool, and Meridian sets it to `web_search_20260209`. Its `name` is always `web_search`. The [tool reference(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#anthropic-provided-tools) lists the current versions, so copy the `type` value from there.

On Claude 4.6 and later models, `web_search_20260209` and later versions use dynamic filtering by default. Claude runs code that filters the search results, so only relevant content reaches the context window.

Claude usually does all its searching during one request. Your code sends that request and gets back the finished answer.

The API can pause a long-running turn and return a `stop_reason` of `pause_turn`. When it does, send the response's content back as an assistant message, with the same `tools`, and Claude continues.

[Each search is billed(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#usage-and-pricing) on top of what you pay for tokens. [Not every cloud platform offers web search(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock#features-not-supported).

## Name the sites Claude may use[](#name-the-sites-claude-may-use)

So far, nothing in the request limits which sites Claude can search, and that's a problem for Meridian. The open web is full of forum posts and reseller sites, but Meridian can stand behind only official sources.

So you tell the search where it may look. **`allowed_domains` is another field in the tool's entry, and it limits search results to the sites you name.** Meridian names four sites. Two belong to the bodies that publish these standards and certify to them, `csagroup.org` and `cwbgroup.org`. Two belong to governments, `ontario.ca` and `canada.ca`.

`allowed_domains` takes a list. Write each item as a bare domain with no `https://`, and its subdomains are included.

## Read the answer and its sources[](#read-the-answer-and-its-sources)

Claude's answer can arrive in several `text` blocks, with the searches in between. **So join every `text` block to get the whole answer.**

Each search also adds a `web_search_tool_result` block to the response. It holds the list of results the search returned, and each result has a `title` and a `url`.

Of Meridian's four references, Claude found that two check out, a third checks out except for its subclause number, and the fourth is wrong.

## Put the program together[](#put-the-program-together)

Meridian's program puts these steps together. In the program, `excerpt` holds the passage from the proposal, and `QUESTION` holds Meridian's question.

## Key takeaways[](#key-takeaways)

* Web search is a server tool, so you add one entry to `tools` and don't write a handler. Claude usually does all its searching during one request.
* `allowed_domains` limits search results to the sites you name.
* On Claude 4.6 and later models, dynamic filtering is on by default in `web_search_20260209` and later versions, so only relevant content reaches the context window.

[Previous lessonCode execution: Claude runs the code it writes](https://academy.claude.com/courses/tool-use-with-the-messages-api/code-execution)[Next lessonComputer use: Automate desktop software with no API](https://academy.claude.com/courses/tool-use-with-the-messages-api/computer-use)

Lesson 6 of 9 · Tool use with the Messages APIWeb search: Answers from the sites you trust

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
* [Name the sites Claude may use](#name-the-sites-claude-may-use)
* [Read the answer and its sources](#read-the-answer-and-its-sources)
* [Put the program together](#put-the-program-together)
* [Key takeaways](#key-takeaways)
