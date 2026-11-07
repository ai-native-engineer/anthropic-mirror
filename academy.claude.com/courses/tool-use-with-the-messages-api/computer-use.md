<!-- source: https://academy.claude.com/courses/tool-use-with-the-messages-api/computer-use -->

Lesson 7 of 9 · Tool use with the Messages APIComputer use: Automate desktop software with no API

3. /[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

# Computer use: Automate desktop software with no API

Lesson 79 min

Most companies have at least one app with no API at all. The tools from the earlier lessons can't reach it, because there's nothing for them to call.

Meridian, a fictional engineering consultancy, has one of these apps. It's an old drawing manager called PlotDesk, also fictional. Every Friday, one person spends the day clicking through the same screens to export PDF plot sets. PlotDesk has no API and no command line. It has only windows and buttons.

**Computer use lets Claude operate PlotDesk through those windows and buttons, just as a person would, by looking at screenshots and deciding what to click and which text to type.**

Meridian wants Claude to export today's PDF plot set for project MEG-2026-0142.

## See who carries out each action[](#see-who-carries-out-each-action)

Through the API, Claude never connects to the desktop. All Claude produces is a response with tool calls in it. Your program is the Python program that calls the Messages API. It carries out each action on the desktop and sends back the result.

Here's the loop. Claude asks for a screenshot. Your program takes one and sends it back as an image. Claude looks at it and sends the next action, such as a click at given coordinates or some text to type. Your program carries out the action, and the loop repeats until the task is done. **It's the tool loop you already have, except that some of the results are screenshots.**

Meridian's whole export took seven actions.

| Claude's action | What happened |
| --- | --- |
| `screenshot` | Claude finds the PlotDesk window |
| `left_click` | On the Project number field |
| `type` | MEG-2026-0142 |
| `left_click` | On Open |
| `screenshot` | PlotDesk shows the project: Pump Station Replacement, 22 sheets |
| `left_click` | On Export PDF |
| `screenshot` | The status bar reads "Exported MEG-2026-0142\_plots.pdf" |

## Run the desktop in a dedicated container[](#run-the-desktop-in-a-dedicated-container)

Claude acts on whatever is on the screen. Text in a web page or an image can override your instructions or lead Claude into mistakes. **To limit how much harm one wrong action can do, give the desktop a dedicated container or virtual machine that holds only what the task needs.** Set it up this way:

* Each session gets a dedicated container.
* The container holds no credentials and no directories mounted from the host.
* The container can reach only the network hosts the task uses.

Your program and your API key stay outside the container.

## Write the actions, and let the SDK run the loop[](#write-the-actions-and-let-the-sdk-run-the-loop)

The Python and TypeScript SDKs have a class called the computer toolset. You subclass it and write one method for each action the task needs. The class builds the toolset's `tools` entry for you and is in beta. In Python, it needs version 1.12.0 or later of the SDK.

Meridian implements three of the toolset's actions: `screenshot`, `left_click`, and `type`. Any action you don't implement is sent to the API as disabled.

Each method is one line that hands the work to `backend`. That's your own wrapper around whatever controls the desktop, such as a VNC client or `xdotool`. This [minimal VNC example in Python and TypeScript(opens in new tab)](https://github.com/anthropics/claude-quickstarts/tree/main/computer-toolset) is a good place to start, but it isn't meant for production.

Pass an instance of your class in `tools`, along with the prompt. **Tool Runner, an SDK helper, runs the loop for you until Claude replies without a tool call.**

As of October 2026, [this toolset(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) is available on the Claude API and on Claude Models on Google Cloud (Google managed). Amazon Bedrock, Microsoft Foundry, and Claude Platform on AWS have the earlier beta tool versions. Those take a different `tools` entry and a beta header, a request header that turns on a beta feature.

## Have a person approve clicks and typing[](#have-a-person-approve-clicks-and-typing)

When you create the instance, pass a function called `confirm`. The SDK calls it before every action. If it returns `True`, the action runs. Anything else refuses the action, and Claude is told that a person turned it down.

`confirm` sees the action and its input, but not the screen. A person watching the desktop can see what sits at the point Claude wants to click. **So Meridian approves screenshots automatically and sends every click and every `type` action to its operator, the person watching the desktop.**

Here's Meridian's program. Three names in it come from Meridian's own code, not the SDK: `backend`, `ask_operator`, and `TASK`. `ask_operator` shows the operator the action and returns their answer, and `TASK` holds the prompt.

## Decide when computer use fits[](#decide-when-computer-use-fits)

Every screenshot stays in the conversation, so each step costs more than the one before. So when the software has an MCP server (a service that offers its functions to Claude as tools), an API, or a command line, use that instead. **Computer use is for software that has none of these, like PlotDesk.**

If the task stays inside web pages, the [browser use tool(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool) is the closer fit. It reads and acts on the page itself and needs no full desktop.

## Key takeaways[](#key-takeaways)

* Claude asks for actions, and your program carries them out.
* The desktop runs in a dedicated container for each session.
* You implement only the actions the task needs.
* Meridian's `confirm` function sends every click and every `type` action to a person to approve.
* Use a direct interface when one exists, and computer use when none does.

[Previous lessonWeb search: Answers from the sites you trust](https://academy.claude.com/courses/tool-use-with-the-messages-api/web-search)[Next lessonCut the cost of tool-heavy workflows](https://academy.claude.com/courses/tool-use-with-the-messages-api/cut-the-cost-of-tool-heavy-workflows)

Lesson 7 of 9 · Tool use with the Messages APIComputer use: Automate desktop software with no API

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

* [See who carries out each action](#see-who-carries-out-each-action)
* [Run the desktop in a dedicated container](#run-the-desktop-in-a-dedicated-container)
* [Write the actions, and let the SDK run the loop](#write-the-actions-and-let-the-sdk-run-the-loop)
* [Have a person approve clicks and typing](#have-a-person-approve-clicks-and-typing)
* [Decide when computer use fits](#decide-when-computer-use-fits)
* [Key takeaways](#key-takeaways)
