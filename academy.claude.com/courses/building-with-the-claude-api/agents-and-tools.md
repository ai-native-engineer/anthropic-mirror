<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools -->

Lesson 65 of 67 · Building with the Claude APIAgents and tools

Agents represent a shift from the structured workflows we've been working with. While workflows are perfect when you know the exact steps needed to complete a task, agents shine when you're not sure what those steps should be. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

![](https://academy.claude.com/assets/media/8478d80427e9081aa66a7084783dfb337ac19806a7d4a29e7c2705ac54474fc3.jpg)

This flexibility makes agents attractive for building applications that need to handle varied, unpredictable tasks. You can create an agent once, ensure it works reasonably well, and then deploy it to solve a wide range of problems. However, this flexibility comes with trade-offs in reliability and cost that we'll explore later.

## How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools:

![](https://academy.claude.com/assets/media/7d814984b14a8cf9d543c3f61882d8abac783e7ce893730b5fc78f059839182c.jpg)

* `get_current_datetime` - Gets the current date and time
* `add_duration_to_datetime` - Adds time to a given date
* `set_reminder` - Creates a reminder for a specific time

These tools seem simple individually, but Claude can chain them together to handle surprisingly complex requests:

![](https://academy.claude.com/assets/media/7c1d89fa8e71f13aa3a2e6f097bdf0c47ce192d6e716044928dd3b3012a67209.jpg)

For "What's the time?", Claude simply calls `get_current_datetime`. But for "What day of the week is it in 11 days?", it chains `get_current_datetime` followed by `add_duration_to_datetime`. For setting a gym reminder next Wednesday, it might use all three tools in sequence.

Claude can even recognize when it needs more information. If you ask "When does my 90-day warranty expire?", it knows to ask when you purchased the item before calculating the expiration date.

## Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

![](https://academy.claude.com/assets/media/4f6caa40d08beb99072be1d57118d7d346bd5d52c2307242d249cf1819ba7de0.jpg)

Claude Code has access to generic, flexible tools like:

* `bash` - Run any command
* `read` - Read any file
* `write` - Create any file
* `edit` - Modify files
* `glob` - Find files
* `grep` - Search file contents

It notably doesn't have specialized tools like "refactor code" or "install dependencies." Instead, Claude figures out how to use the basic tools to accomplish these complex tasks. This abstraction allows it to handle countless programming scenarios that the developers never explicitly planned for.

## Best Practice: Combinable Tools

When designing agents, provide tools that Claude can combine in creative ways. For example, a social media video agent might include:

![](https://academy.claude.com/assets/media/39ba419929e69d84456f4ad31a7c3296b292eb15d7a64a5a158efc0e65291fc0.jpg)

* `bash` - Access to FFMPEG for video processing
* `generate_image` - Create images from prompts
* `text_to_speech` - Convert text to audio
* `post_media` - Upload content to social platforms

This tool set enables both simple workflows (create and post a video) and more interactive experiences where the agent might generate a sample image first, get user approval, then proceed with video creation.

![](https://academy.claude.com/assets/media/0980bf9ff221f46f8d110f9a53eeea730ca1d487090685740bec60708bac5497.jpg)

The agent can adapt its approach based on user feedback and preferences, something that would be difficult to achieve with a rigid workflow. This flexibility is what makes agents powerful for building dynamic, user-responsive applications.
