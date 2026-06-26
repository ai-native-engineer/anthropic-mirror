<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool -->

# Computer use tool
Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction. On [WebArena](https://webarena.dev/), a benchmark for autonomous web navigation across real websites, Claude achieves state-of-the-art results among single-agent systems, demonstrating strong ability to complete multi-step browser tasks end to end.
Computer use is in beta and requires a [beta header](https://platform.claude.com/docs/en/api/beta-headers):
  * `"computer-use-2025-11-24"` for Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5
  * `"computer-use-2025-01-24"` for Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.1 ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations)), Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations)), and Claude Opus 4 ([retired, except on Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))

Reach out through the [feedback form](https://forms.gle/H6UFuXaaLywri9hz6) to share your feedback on this feature.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Overview
Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides:
  * **Screenshot capture:** See what's currently displayed on screen
  * **Mouse control:** Click, drag, and move the cursor
  * **Keyboard input:** Type text and use keyboard shortcuts
  * **Desktop automation:** Interact with any application or interface

While computer use can be augmented with other tools such as bash and text editor for more comprehensive automation workflows, computer use specifically refers to the computer use tool's capability to see and control desktop environments.
For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
Security considerations
Computer use is a beta feature with unique risks distinct from standard API features. These risks are heightened when interacting with the internet.

To minimize risks, consider taking precautions such as:
  1. Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
  2. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft.
  3. Limiting internet access to an allowlist of domains to reduce exposure to malicious content.
  4. Asking a human to confirm decisions that might result in meaningful real-world consequences and any tasks requiring affirmative consent, such as accepting cookies, completing financial transactions, or agreeing to terms of service.

In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images might override instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.
Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the computer use tools, classifiers will automatically run on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, [contact support](https://support.claude.com/en/).
These precautions remain important even with the classifier defense layer in place.
Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.
[  Computer use reference implementation  Get started with the computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop. ](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
Quick start
Here's how to get started with computer use:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",  # or another compatible model
    max_tokens=1024,
    tools=[
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
        {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
        {"type": "bash_20250124", "name": "bash"},
    ],
    messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
    betas=["computer-use-2025-11-24"],
)
print(response)

A beta header is only required for the computer use tool.
The preceding example shows all three tools being used together, which requires the beta header because it includes the computer use tool.
* * *
How computer use works
  1. 1
Provide Claude with the computer use tool and a user prompt
     * Add the computer use tool (and optionally other tools) to your API request.
     * Include a user prompt that requires desktop interaction, for example, "Save a picture of a cat to my desktop."
  2. 2
Claude selects the computer use tool
     * Claude assesses if the computer use tool can help with the user's query.
     * If yes, Claude constructs a properly formatted tool use request.
     * The API response has a `stop_reason` of `tool_use`, signaling a tool use request.
  3. 3
Extract tool input, evaluate the tool on a computer, and return results
     * On your end, extract the tool name and input from Claude's request.
     * Use the tool on a container or virtual machine.
     * Continue the conversation with a new `user` message containing a `tool_result` content block.
  4. 4
Claude continues calling computer use tools until it's completed the task
     * Claude analyzes the tool results to determine if more tool use is needed or the task has been completed.
     * If Claude determines another tool is needed, it responds with another `tool_use` `stop_reason` and you should return to step 3.
     * Otherwise, it crafts a text response to the user.

The repetition of steps 3 and 4 without user input is referred to as the "agent loop" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request).
### 
The computing environment
Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:
  1. **Virtual display:** A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.
  2. **Desktop environment:** A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.
  3. **Applications:** Pre-installed Linux applications such as Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.
  4. **Tool implementations:** Integration code that translates Claude's abstract tool requests (such as "move mouse" or "take screenshot") into actual operations in the virtual environment.
  5. **Agent loop:** A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:
  1. Receives Claude's tool use requests
  2. Translates them into actions in your computing environment
  3. Captures the results (such as screenshots and command outputs)
  4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.
* * *
How to implement computer use
### 
Start with the reference implementation
A [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is available that includes everything you need to get started with computer use:
  * A [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use with Claude
  * Implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools)
  * An [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that interacts with the Claude API and runs the computer use tools
  * A web interface to interact with the container, agent loop, and tools.

### 
Understanding the agentic loop
The core of computer use is the "agent loop": a cycle where Claude requests tool actions, your application runs them, and returns results to Claude. Here's a simplified example:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def sampling_loop(model, messages, max_iterations=10):
    """
    Run the computer-use agent loop until Claude stops requesting tools
    or the iteration limit is reached.
    """
    for _ in range(max_iterations):
        response = client.beta.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages,
            tools=TOOLS,
            betas=["computer-use-2025-11-24"],
        )

        # Add Claude's response to the conversation history
        messages.append({"role": "assistant", "content": response.content})

        # Run any tools Claude requested and collect results
        tool_results = process_tool_calls(response)
        if not tool_results:
            return messages  # No more tool use; task complete

        # Send tool results back to Claude for the next iteration
        messages.append({"role": "user", "content": tool_results})

    return messages

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.
Try the reference implementation out before reading the rest of this documentation.
### 
Optimize model performance with prompting
Here are some tips on how to get the best quality outputs:
  1. Specify simple, well-defined tasks and provide explicit instructions for each step.
  2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
  3. Some UI elements (such as dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
  4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
  5. If you need the model to log in, provide it with the username and password in your prompt inside XML tags such as `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Review [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.
  6. When constructing a user turn's `content` array, place the instruction text _before_ the screenshot image. Providing the target description before the image is processed improves click accuracy.
  7. When using `computer_20251124` with `enable_zoom: true` set, Claude zooms in on a region when asked about small text or specific UI elements that aren't legible at the screenshot's default resolution, such as file names in a sidebar, tab titles, status-bar text, line numbers, or button labels. If Claude isn't zooming when you expect, ask about a specific region or element rather than the screen as a whole.


If you repeatedly encounter a clear set of issues or know in advance the tasks Claude will need to complete, use the system prompt to provide Claude with explicit tips or instructions on how to do the tasks successfully.

For agents that span multiple sessions, run end-to-end verification at the start of each session, not only after implementation. Browser-based checks catch regressions from prior sessions that code-level review alone misses. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) for details.
### 
System prompts
When one of the Anthropic-schema tools is requested through the Claude API, a computer use-specific system prompt is generated. It's similar to the [tool use system prompt](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#tool-use-system-prompt) but starts with:
> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.
As with regular tool use, the user-provided `system_prompt` field is still respected and used in the construction of the combined system prompt.
### 
Available actions
The computer use tool supports these actions:
**Basic actions (all versions)**
  * **screenshot:** Capture the current display
  * **left_click:** Click at coordinates `[x, y]`
  * **type:** Type text string
  * **key:** Press key or key combination (for example, "ctrl+s")
  * **mouse_move:** Move cursor to coordinates

**Enhanced actions (`computer_20250124`)** Available on all models that support computer use:
  * **scroll:** Scroll in any direction with amount control
  * **left_click_drag:** Click and drag between coordinates
  * **right_click** , **middle_click:** Additional mouse buttons
  * **double_click** , **triple_click:** Multiple clicks
  * **left_mouse_down** , **left_mouse_up:** Fine-grained click control
  * **hold_key:** Hold down a key for a specified duration (in seconds)
  * **wait:** Pause between actions

**Enhanced actions (`computer_20251124`)** Available in Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5:
  * All actions from `computer_20250124`
  * **zoom:** View a specific region of the screen at full resolution. Requires `enable_zoom: true` in tool definition. Takes a `region` parameter with coordinates `[x1, y1, x2, y2]` defining top-left and bottom-right corners of the area to inspect.

### Example actions
### Modifier keys with click and scroll actions
### 
Tool parameters  
| Parameter  | Required  | Description  |  
| --- | --- | --- |  
| `type`  | Yes  | Tool version (`computer_20251124` or `computer_20250124`)  |  
| `name`  | Yes  | Must be "computer"  |  
| `display_width_px`  | Yes  | Display width in pixels  |  
| `display_height_px`  | Yes  | Display height in pixels  |  
| `display_number`  | No  | Display number for X11 environments  |  
| `enable_zoom`  | No  | Enable zoom action (`computer_20251124` only). Set to `true` to allow Claude to zoom into specific screen regions. Default: `false`  |  
**Important:** Your application must explicitly run the computer use tool; Claude cannot run it directly. You are responsible for implementing the screenshot capture, mouse movements, keyboard inputs, and other actions based on Claude's requests.
### 
Combining with extended thinking
For combining computer use with extended thinking, see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).

For computer use specifically, internal benchmarking suggests these `effort` settings:
  * **Claude Opus 4.7:** use `high` as the default; use `low` for high-throughput or cost-sensitive workloads.
  * **Claude Sonnet 4.6 and Claude Opus 4.6:** use `medium` as the default (best accuracy-to-cost ratio). Avoid `max`, which adds token cost without improving accuracy on UI tasks. On these models, `low` uses _fewer_ output tokens than disabling thinking entirely (fewer mistakes mean fewer retries), making it a strong option for cost-sensitive loops.

### 
Augmenting computer use with other tools
To add other tools alongside computer use, include them in the same `tools` array. The [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#quick-start) section shows this pattern with the [bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) and [text editor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool). You can add your own [custom tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) the same way.
### 
Build a custom computer use environment
The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed to have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:
  * A virtualized or containerized environment suitable for computer use with Claude
  * An implementation of at least one of the Anthropic-schema computer use tools
  * An agent loop that interacts with the Claude API and runs the `tool_use` results using your tool implementations
  * An API or UI that allows user input to start the agent loop

#### 
Implement the computer use tool
The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.
  1. 1
Set up your computing environment
Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.
  2. 2
Implement action handlers
Create functions to handle each action type that Claude might request:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def capture_screenshot():
    return "<screenshot data>"

def click_at(x, y):
    return f"clicked at ({x}, {y})"

def type_text(text):
    return f"typed: {text}"

def handle_computer_action(action_type, params):
    if action_type == "screenshot":
        return capture_screenshot()
    elif action_type == "left_click":
        x, y = params["coordinate"]
        return click_at(x, y)
    elif action_type == "type":
        return type_text(params["text"])
    # Handle other actions as needed
    return f"unhandled action: {action_type}"

  3. 3
Process Claude's tool calls
Extract and run tool calls from Claude's responses:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def process_tool_calls(response):
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            action = block.input["action"]
            result = handle_computer_action(action, block.input)
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
            )
    return tool_results

  4. 4
Implement the agent loop
Create a loop that continues until Claude completes the task:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def sampling_loop(model, messages, max_iterations=10):
    """
    Run the computer-use agent loop until Claude stops requesting tools
    or the iteration limit is reached.
    """
    for _ in range(max_iterations):
        response = client.beta.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages,
            tools=TOOLS,
            betas=["computer-use-2025-11-24"],
        )

        # Add Claude's response to the conversation history
        messages.append({"role": "assistant", "content": response.content})

        # Run any tools Claude requested and collect results
        tool_results = process_tool_calls(response)
        if not tool_results:
            return messages  # No more tool use; task complete

        # Send tool results back to Claude for the next iteration
        messages.append({"role": "user", "content": tool_results})

    return messages

#### 
Handle errors
When implementing the computer use tool, various errors might occur. Here's how to handle them:
### Screenshot capture failure
### Invalid coordinates
### Action execution failure
#### 
Size screenshots to fit image limits
Screenshots sent to the computer tool must already fit within Claude's image size limits (see [image size limits](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size)). The API does not resize oversized images; a screenshot that exceeds the limit is rejected with an HTTP 400 validation error.
Limits vary by model. Claude Opus 4.8 and Claude Opus 4.7 accept up to 2576 pixels on the long edge; earlier models accept up to 1568 pixels on the long edge and approximately 1.15 megapixels total. The following example uses the earlier-model 1568 px / 1.15 MP limits; substitute your model's limit.
If your screen is larger than the limit, resize the screenshot before sending it, set `display_width_px`/`display_height_px` to the resized dimensions, and scale Claude's returned coordinates back to the original screen space:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

import math

def get_scale_factor(width, height):
    """Calculate scale factor to meet API constraints."""
    long_edge = max(width, height)
    total_pixels = width * height

    long_edge_scale = 1568 / long_edge
    total_pixels_scale = math.sqrt(1_150_000 / total_pixels)

    return min(1.0, long_edge_scale, total_pixels_scale)

# When capturing screenshot
scale = get_scale_factor(screen_width, screen_height)
scaled_width = int(screen_width * scale)
scaled_height = int(screen_height * scale)

# Resize image to scaled dimensions before sending to Claude
screenshot = capture_and_resize(scaled_width, scaled_height)

# When handling Claude's coordinates, scale them back up
def execute_click(x, y):
    screen_x = x / scale
    screen_y = y / scale
    perform_click(screen_x, screen_y)

**macOS Retina displays** capture screenshots at a device pixel ratio of 2, so the image is twice the resolution of the logical screen coordinates. Either downscale the screenshot by 2x before sending, or halve the coordinates Claude returns before issuing the click.
#### 
Diagnose click issues
If clicks miss their targets, the cause is usually one of the following:  
| Symptom  | Likely cause  | Try  |  
| --- | --- | --- |  
| Clicks consistently offset in one direction  |  `display_width_px`/`display_height_px` don't match the image dimensions actually sent  | Ensure display dimensions exactly match the screenshot you send  |  
| Clicks land in the right area but miss the target  | Target is very small, detail was lost downscaling a 4K+ source, or aspect ratio was distorted  | Set `enable_zoom: true`; capture at lower DPI or crop to the relevant region; preserve aspect ratio when resizing  |  
| Claude clicks the wrong element entirely  | Ambiguous instruction, or visually similar elements nearby  | Use positional prompts ("the blue Submit button in the bottom-right"); break the interaction into smaller steps  |  
| Accuracy is consistently poor  | Resolution too low  | Try 1280x720 as a baseline  |  

**Model choice affects click precision.** Claude Sonnet 4.6 is more mechanically precise at clicking than Claude Opus 4.6 and is more robust when screenshots require heavy downscaling. Claude Opus 4.7 narrows that gap: its click precision is roughly comparable to Sonnet 4.6, and its higher resolution limit means less downscaling is needed.
#### 
Follow implementation best practices
### Use appropriate display resolution
### Implement proper screenshot handling
### Manage screenshot history for prompt caching
### Add action delays
### Validate actions before running them
### Log actions for debugging
* * *
Understand computer use limitations
The computer use functionality is in beta. While Claude's capabilities are state of the art, developers should be aware of its limitations:
  1. **Latency:** The current computer use latency for human-AI interactions might be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments.
  2. **Computer vision accuracy and reliability:** Claude might make mistakes or hallucinate when outputting specific coordinates while generating actions. Extended thinking can help you understand the model's reasoning and identify potential issues.
  3. **Tool selection accuracy and reliability:** Claude might make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability might be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks.
  4. **Scrolling reliability:** The scroll action supports direction control (up, down, left, right) and a specified amount. In applications where scrolling doesn't take effect, keyboard alternatives such as Page Down can help.
  5. **Spreadsheet interaction:** Use the fine-grained mouse control actions (`left_mouse_down`, `left_mouse_up`) and modifier-key combinations to select individual cells. Complex spreadsheet operations might still require multiple attempts.
  6. **Account creation and content generation on social and communications platforms:** While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability might be updated in the future.
  7. **Vulnerabilities:** Vulnerabilities such as jailbreaking or prompt injection might persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images might override instructions or cause Claude to make mistakes. Consider the following: a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges b. Avoiding giving computer use access to sensitive accounts or data without strict oversight c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications
  8. **Inappropriate or illegal actions:** Under Anthropic's Terms of Service, you must not employ computer use to violate any laws or the Acceptable Use Policy.

Always carefully review and verify Claude's computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.
Data retention
Computer use is a client-side tool. All screenshots, mouse actions, keyboard inputs, and any files involved in a session are captured and stored in your environment, not by Anthropic. Anthropic processes the screenshot images and action requests in real time as part of the API call but does not retain them after the response is returned.
Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Pricing
Computer use follows the standard [tool use pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:
**System prompt overhead** : The computer use beta adds 466-499 tokens to the system prompt
**Computer use tool token usage** :  
| Model  | Input tokens per tool definition  |  
| --- | --- |  
| Claude 4.x models  | 735 tokens  |  
**Additional token consumption** :
  * Screenshot images (see [Vision pricing](https://platform.claude.com/docs/en/build-with-claude/vision))
  * Tool execution results returned to Claude

If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
Next steps
[  Text editor tool Continue to the next tool: view, create, and edit files with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)[ Reference implementation  Get started with the complete Docker-based implementation ](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)[  Tool documentation Learn more about tool use and creating custom tools ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Best practices in detail  Benchmarked recommendations for resolution, thinking effort, and context management ](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude)
  * [Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#overview)
  * [Security considerations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#security-considerations)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#quick-start)
  * [How computer use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#how-computer-use-works)
  * [The computing environment](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#the-computing-environment)
  * [How to implement computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#how-to-implement-computer-use)
  * [Start with the reference implementation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#start-with-the-reference-implementation)
  * [Understanding the agentic loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#understanding-the-agentic-loop)
  * [Optimize model performance with prompting](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#optimize-model-performance-with-prompting)
  * [System prompts](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#system-prompts)
  * [Available actions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#available-actions)
  * [Tool parameters](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#tool-parameters)
  * [Combining with extended thinking](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#combining-with-extended-thinking)
  * [Augmenting computer use with other tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#augmenting-computer-use-with-other-tools)
  * [Build a custom computer use environment](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#build-a-custom-computer-use-environment)
  * [Understand computer use limitations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#understand-computer-use-limitations)
  * [Data retention](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#data-retention)
  * [Pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#pricing)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#next-steps)

Messages/Tools
# Computer use tool
Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction. On [WebArena](https://webarena.dev/), a benchmark for autonomous web navigation across real websites, Claude achieves state-of-the-art results among single-agent systems, demonstrating strong ability to complete multi-step browser tasks end to end.
Computer use is in beta and requires a [beta header](https://platform.claude.com/docs/en/api/beta-headers):
  * `"computer-use-2025-11-24"` for Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5
  * `"computer-use-2025-01-24"` for Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.1 ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations)), Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations)), and Claude Opus 4 ([retired, except on Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))

Reach out through the [feedback form](https://forms.gle/H6UFuXaaLywri9hz6) to share your feedback on this feature.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Overview
Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides:
  * **Screenshot capture:** See what's currently displayed on screen
  * **Mouse control:** Click, drag, and move the cursor
  * **Keyboard input:** Type text and use keyboard shortcuts
  * **Desktop automation:** Interact with any application or interface

While computer use can be augmented with other tools such as bash and text editor for more comprehensive automation workflows, computer use specifically refers to the computer use tool's capability to see and control desktop environments.
For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
Security considerations
Computer use is a beta feature with unique risks distinct from standard API features. These risks are heightened when interacting with the internet.

To minimize risks, consider taking precautions such as:
  1. Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
  2. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft.
  3. Limiting internet access to an allowlist of domains to reduce exposure to malicious content.
  4. Asking a human to confirm decisions that might result in meaningful real-world consequences and any tasks requiring affirmative consent, such as accepting cookies, completing financial transactions, or agreeing to terms of service.

In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images might override instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.
Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the computer use tools, classifiers will automatically run on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, [contact support](https://support.claude.com/en/).
These precautions remain important even with the classifier defense layer in place.
Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.
[  Computer use reference implementation  Get started with the computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop. ](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
Quick start
Here's how to get started with computer use:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",  # or another compatible model
    max_tokens=1024,
    tools=[
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
        {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
        {"type": "bash_20250124", "name": "bash"},
    ],
    messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
    betas=["computer-use-2025-11-24"],
)
print(response)

A beta header is only required for the computer use tool.
The preceding example shows all three tools being used together, which requires the beta header because it includes the computer use tool.
* * *
How computer use works
  1. 1
Provide Claude with the computer use tool and a user prompt
     * Add the computer use tool (and optionally other tools) to your API request.
     * Include a user prompt that requires desktop interaction, for example, "Save a picture of a cat to my desktop."
  2. 2
Claude selects the computer use tool
     * Claude assesses if the computer use tool can help with the user's query.
     * If yes, Claude constructs a properly formatted tool use request.
     * The API response has a `stop_reason` of `tool_use`, signaling a tool use request.
  3. 3
Extract tool input, evaluate the tool on a computer, and return results
     * On your end, extract the tool name and input from Claude's request.
     * Use the tool on a container or virtual machine.
     * Continue the conversation with a new `user` message containing a `tool_result` content block.
  4. 4
Claude continues calling computer use tools until it's completed the task
     * Claude analyzes the tool results to determine if more tool use is needed or the task has been completed.
     * If Claude determines another tool is needed, it responds with another `tool_use` `stop_reason` and you should return to step 3.
     * Otherwise, it crafts a text response to the user.

The repetition of steps 3 and 4 without user input is referred to as the "agent loop" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request).
### 
The computing environment
Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:
  1. **Virtual display:** A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.
  2. **Desktop environment:** A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.
  3. **Applications:** Pre-installed Linux applications such as Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.
  4. **Tool implementations:** Integration code that translates Claude's abstract tool requests (such as "move mouse" or "take screenshot") into actual operations in the virtual environment.
  5. **Agent loop:** A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:
  1. Receives Claude's tool use requests
  2. Translates them into actions in your computing environment
  3. Captures the results (such as screenshots and command outputs)
  4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.
* * *
How to implement computer use
### 
Start with the reference implementation
A [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is available that includes everything you need to get started with computer use:
  * A [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use with Claude
  * Implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools)
  * An [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that interacts with the Claude API and runs the computer use tools
  * A web interface to interact with the container, agent loop, and tools.

### 
Understanding the agentic loop
The core of computer use is the "agent loop": a cycle where Claude requests tool actions, your application runs them, and returns results to Claude. Here's a simplified example:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def sampling_loop(model, messages, max_iterations=10):
    """
    Run the computer-use agent loop until Claude stops requesting tools
    or the iteration limit is reached.
    """
    for _ in range(max_iterations):
        response = client.beta.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages,
            tools=TOOLS,
            betas=["computer-use-2025-11-24"],
        )

        # Add Claude's response to the conversation history
        messages.append({"role": "assistant", "content": response.content})

        # Run any tools Claude requested and collect results
        tool_results = process_tool_calls(response)
        if not tool_results:
            return messages  # No more tool use; task complete

        # Send tool results back to Claude for the next iteration
        messages.append({"role": "user", "content": tool_results})

    return messages

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.
Try the reference implementation out before reading the rest of this documentation.
### 
Optimize model performance with prompting
Here are some tips on how to get the best quality outputs:
  1. Specify simple, well-defined tasks and provide explicit instructions for each step.
  2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
  3. Some UI elements (such as dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
  4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
  5. If you need the model to log in, provide it with the username and password in your prompt inside XML tags such as `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Review [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.
  6. When constructing a user turn's `content` array, place the instruction text _before_ the screenshot image. Providing the target description before the image is processed improves click accuracy.
  7. When using `computer_20251124` with `enable_zoom: true` set, Claude zooms in on a region when asked about small text or specific UI elements that aren't legible at the screenshot's default resolution, such as file names in a sidebar, tab titles, status-bar text, line numbers, or button labels. If Claude isn't zooming when you expect, ask about a specific region or element rather than the screen as a whole.


If you repeatedly encounter a clear set of issues or know in advance the tasks Claude will need to complete, use the system prompt to provide Claude with explicit tips or instructions on how to do the tasks successfully.

For agents that span multiple sessions, run end-to-end verification at the start of each session, not only after implementation. Browser-based checks catch regressions from prior sessions that code-level review alone misses. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) for details.
### 
System prompts
When one of the Anthropic-schema tools is requested through the Claude API, a computer use-specific system prompt is generated. It's similar to the [tool use system prompt](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#tool-use-system-prompt) but starts with:
> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.
As with regular tool use, the user-provided `system_prompt` field is still respected and used in the construction of the combined system prompt.
### 
Available actions
The computer use tool supports these actions:
**Basic actions (all versions)**
  * **screenshot:** Capture the current display
  * **left_click:** Click at coordinates `[x, y]`
  * **type:** Type text string
  * **key:** Press key or key combination (for example, "ctrl+s")
  * **mouse_move:** Move cursor to coordinates

**Enhanced actions (`computer_20250124`)** Available on all models that support computer use:
  * **scroll:** Scroll in any direction with amount control
  * **left_click_drag:** Click and drag between coordinates
  * **right_click** , **middle_click:** Additional mouse buttons
  * **double_click** , **triple_click:** Multiple clicks
  * **left_mouse_down** , **left_mouse_up:** Fine-grained click control
  * **hold_key:** Hold down a key for a specified duration (in seconds)
  * **wait:** Pause between actions

**Enhanced actions (`computer_20251124`)** Available in Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5:
  * All actions from `computer_20250124`
  * **zoom:** View a specific region of the screen at full resolution. Requires `enable_zoom: true` in tool definition. Takes a `region` parameter with coordinates `[x1, y1, x2, y2]` defining top-left and bottom-right corners of the area to inspect.

### Example actions
### Modifier keys with click and scroll actions
### 
Tool parameters  
| Parameter  | Required  | Description  |  
| --- | --- | --- |  
| `type`  | Yes  | Tool version (`computer_20251124` or `computer_20250124`)  |  
| `name`  | Yes  | Must be "computer"  |  
| `display_width_px`  | Yes  | Display width in pixels  |  
| `display_height_px`  | Yes  | Display height in pixels  |  
| `display_number`  | No  | Display number for X11 environments  |  
| `enable_zoom`  | No  | Enable zoom action (`computer_20251124` only). Set to `true` to allow Claude to zoom into specific screen regions. Default: `false`  |  
**Important:** Your application must explicitly run the computer use tool; Claude cannot run it directly. You are responsible for implementing the screenshot capture, mouse movements, keyboard inputs, and other actions based on Claude's requests.
### 
Combining with extended thinking
For combining computer use with extended thinking, see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).

For computer use specifically, internal benchmarking suggests these `effort` settings:
  * **Claude Opus 4.7:** use `high` as the default; use `low` for high-throughput or cost-sensitive workloads.
  * **Claude Sonnet 4.6 and Claude Opus 4.6:** use `medium` as the default (best accuracy-to-cost ratio). Avoid `max`, which adds token cost without improving accuracy on UI tasks. On these models, `low` uses _fewer_ output tokens than disabling thinking entirely (fewer mistakes mean fewer retries), making it a strong option for cost-sensitive loops.

### 
Augmenting computer use with other tools
To add other tools alongside computer use, include them in the same `tools` array. The [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#quick-start) section shows this pattern with the [bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) and [text editor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool). You can add your own [custom tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) the same way.
### 
Build a custom computer use environment
The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed to have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:
  * A virtualized or containerized environment suitable for computer use with Claude
  * An implementation of at least one of the Anthropic-schema computer use tools
  * An agent loop that interacts with the Claude API and runs the `tool_use` results using your tool implementations
  * An API or UI that allows user input to start the agent loop

#### 
Implement the computer use tool
The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.
  1. 1
Set up your computing environment
Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.
  2. 2
Implement action handlers
Create functions to handle each action type that Claude might request:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def capture_screenshot():
    return "<screenshot data>"

def click_at(x, y):
    return f"clicked at ({x}, {y})"

def type_text(text):
    return f"typed: {text}"

def handle_computer_action(action_type, params):
    if action_type == "screenshot":
        return capture_screenshot()
    elif action_type == "left_click":
        x, y = params["coordinate"]
        return click_at(x, y)
    elif action_type == "type":
        return type_text(params["text"])
    # Handle other actions as needed
    return f"unhandled action: {action_type}"

  3. 3
Process Claude's tool calls
Extract and run tool calls from Claude's responses:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def process_tool_calls(response):
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            action = block.input["action"]
            result = handle_computer_action(action, block.input)
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
            )
    return tool_results

  4. 4
Implement the agent loop
Create a loop that continues until Claude completes the task:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

def sampling_loop(model, messages, max_iterations=10):
    """
    Run the computer-use agent loop until Claude stops requesting tools
    or the iteration limit is reached.
    """
    for _ in range(max_iterations):
        response = client.beta.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages,
            tools=TOOLS,
            betas=["computer-use-2025-11-24"],
        )

        # Add Claude's response to the conversation history
        messages.append({"role": "assistant", "content": response.content})

        # Run any tools Claude requested and collect results
        tool_results = process_tool_calls(response)
        if not tool_results:
            return messages  # No more tool use; task complete

        # Send tool results back to Claude for the next iteration
        messages.append({"role": "user", "content": tool_results})

    return messages

#### 
Handle errors
When implementing the computer use tool, various errors might occur. Here's how to handle them:
### Screenshot capture failure
### Invalid coordinates
### Action execution failure
#### 
Size screenshots to fit image limits
Screenshots sent to the computer tool must already fit within Claude's image size limits (see [image size limits](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size)). The API does not resize oversized images; a screenshot that exceeds the limit is rejected with an HTTP 400 validation error.
Limits vary by model. Claude Opus 4.8 and Claude Opus 4.7 accept up to 2576 pixels on the long edge; earlier models accept up to 1568 pixels on the long edge and approximately 1.15 megapixels total. The following example uses the earlier-model 1568 px / 1.15 MP limits; substitute your model's limit.
If your screen is larger than the limit, resize the screenshot before sending it, set `display_width_px`/`display_height_px` to the resized dimensions, and scale Claude's returned coordinates back to the original screen space:
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

import math

def get_scale_factor(width, height):
    """Calculate scale factor to meet API constraints."""
    long_edge = max(width, height)
    total_pixels = width * height

    long_edge_scale = 1568 / long_edge
    total_pixels_scale = math.sqrt(1_150_000 / total_pixels)

    return min(1.0, long_edge_scale, total_pixels_scale)

# When capturing screenshot
scale = get_scale_factor(screen_width, screen_height)
scaled_width = int(screen_width * scale)
scaled_height = int(screen_height * scale)

# Resize image to scaled dimensions before sending to Claude
screenshot = capture_and_resize(scaled_width, scaled_height)

# When handling Claude's coordinates, scale them back up
def execute_click(x, y):
    screen_x = x / scale
    screen_y = y / scale
    perform_click(screen_x, screen_y)

**macOS Retina displays** capture screenshots at a device pixel ratio of 2, so the image is twice the resolution of the logical screen coordinates. Either downscale the screenshot by 2x before sending, or halve the coordinates Claude returns before issuing the click.
#### 
Diagnose click issues
If clicks miss their targets, the cause is usually one of the following:  
| Symptom  | Likely cause  | Try  |  
| --- | --- | --- |  
| Clicks consistently offset in one direction  |  `display_width_px`/`display_height_px` don't match the image dimensions actually sent  | Ensure display dimensions exactly match the screenshot you send  |  
| Clicks land in the right area but miss the target  | Target is very small, detail was lost downscaling a 4K+ source, or aspect ratio was distorted  | Set `enable_zoom: true`; capture at lower DPI or crop to the relevant region; preserve aspect ratio when resizing  |  
| Claude clicks the wrong element entirely  | Ambiguous instruction, or visually similar elements nearby  | Use positional prompts ("the blue Submit button in the bottom-right"); break the interaction into smaller steps  |  
| Accuracy is consistently poor  | Resolution too low  | Try 1280x720 as a baseline  |  

**Model choice affects click precision.** Claude Sonnet 4.6 is more mechanically precise at clicking than Claude Opus 4.6 and is more robust when screenshots require heavy downscaling. Claude Opus 4.7 narrows that gap: its click precision is roughly comparable to Sonnet 4.6, and its higher resolution limit means less downscaling is needed.
#### 
Follow implementation best practices
### Use appropriate display resolution
### Implement proper screenshot handling
### Manage screenshot history for prompt caching
### Add action delays
### Validate actions before running them
### Log actions for debugging
* * *
Understand computer use limitations
The computer use functionality is in beta. While Claude's capabilities are state of the art, developers should be aware of its limitations:
  1. **Latency:** The current computer use latency for human-AI interactions might be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments.
  2. **Computer vision accuracy and reliability:** Claude might make mistakes or hallucinate when outputting specific coordinates while generating actions. Extended thinking can help you understand the model's reasoning and identify potential issues.
  3. **Tool selection accuracy and reliability:** Claude might make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability might be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks.
  4. **Scrolling reliability:** The scroll action supports direction control (up, down, left, right) and a specified amount. In applications where scrolling doesn't take effect, keyboard alternatives such as Page Down can help.
  5. **Spreadsheet interaction:** Use the fine-grained mouse control actions (`left_mouse_down`, `left_mouse_up`) and modifier-key combinations to select individual cells. Complex spreadsheet operations might still require multiple attempts.
  6. **Account creation and content generation on social and communications platforms:** While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability might be updated in the future.
  7. **Vulnerabilities:** Vulnerabilities such as jailbreaking or prompt injection might persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images might override instructions or cause Claude to make mistakes. Consider the following: a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges b. Avoiding giving computer use access to sensitive accounts or data without strict oversight c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications
  8. **Inappropriate or illegal actions:** Under Anthropic's Terms of Service, you must not employ computer use to violate any laws or the Acceptable Use Policy.

Always carefully review and verify Claude's computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.
Data retention
Computer use is a client-side tool. All screenshots, mouse actions, keyboard inputs, and any files involved in a session are captured and stored in your environment, not by Anthropic. Anthropic processes the screenshot images and action requests in real time as part of the API call but does not retain them after the response is returned.
Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Pricing
Computer use follows the standard [tool use pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:
**System prompt overhead** : The computer use beta adds 466-499 tokens to the system prompt
**Computer use tool token usage** :  
| Model  | Input tokens per tool definition  |  
| --- | --- |  
| Claude 4.x models  | 735 tokens  |  
**Additional token consumption** :
  * Screenshot images (see [Vision pricing](https://platform.claude.com/docs/en/build-with-claude/vision))
  * Tool execution results returned to Claude

If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
Next steps
[  Text editor tool Continue to the next tool: view, create, and edit files with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)[ Reference implementation  Get started with the complete Docker-based implementation ](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)[  Tool documentation Learn more about tool use and creating custom tools ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Best practices in detail  Benchmarked recommendations for resolution, thinking effort, and context management ](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude)
