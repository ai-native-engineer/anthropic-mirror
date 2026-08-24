<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-tools -->

Lesson 64 of 66 · Claude with Google Cloud's Vertex AIAgents and tools

Agents represent a shift from the structured workflows we've explored earlier. While workflows excel when you know the exact steps needed to complete a task, agents shine when the path forward isn't clear. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

![](https://academy.claude.com/assets/media/16fa498153525b728dcd64b59a13b14a0ed9675789cbef298959ad647a25cd00.png)

This flexibility makes agents attractive for developers. You can build an agent once, ensure it works reasonably well, and then deploy it to handle a wide variety of tasks. However, this approach comes with significant drawbacks around reliability and cost that we'll explore later.

## How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools we covered earlier in the course:

![](https://academy.claude.com/assets/media/7fd7b08522e76b8b19ae619ca26738f461c036eb5a3d728765e44549c5ed0be5.png)

* `get_current_datetime` - Returns the current date and time
* `add_duration_to_datetime` - Adds time to a given date
* `set_reminder` - Creates a reminder for a specific time

Each tool is simple on its own, but Claude can combine them to handle diverse requests:

![](https://academy.claude.com/assets/media/984ba3cc574af7e55b1590c9eec8ea81c87573a6af147f17fdd616f0d13bc2be.png)

For "What's the time?", Claude simply calls `get_current_datetime`. For "What day of the week is it in 11 days?", it chains `get_current_datetime` followed by `add_duration_to_datetime`. More complex requests like "Set a reminder to go to the gym next Wednesday" require all three tools in sequence.

Claude can even recognize when it needs additional information. When asked "When does my 90-day warranty expire?", it first asks the user when they obtained the warranty, then uses that information with `add_duration_to_datetime` to calculate the expiration date.

## Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

![](https://academy.claude.com/assets/media/0870204ddda3d7af4bff0897edb5083e87a93a90b976697e1124eeedbbcf1ef1.png)

Claude Code has access to generic, flexible tools:

* `bash` - Run commands
* `glob` - Find files
* `grep` - Search file contents
* `read` - Read a file
* `write` - Create a file
* `edit` - Edit a file
* `webfetch` - Fetch a URL

Notice what Claude Code doesn't have - specialized tools like "Refactor" or "Run Tests" or "Install Dependencies". Instead, it figures out how to accomplish these tasks by combining the basic tools available. To install dependencies, it reads project files to understand the configuration, then uses bash to run the appropriate installation commands.

## Best Practice: Provide Reasonably Abstract Tools

When building agents, focus on tools that Claude can combine creatively rather than tools that solve one specific problem. Consider a social media video creation agent:

![](https://academy.claude.com/assets/media/315b4d5b327f0a3944c6dec53533b0216e0f0da0e989db4276e58bc46a71befe.png)

Effective tools for this agent might include:

* `bash` - Provides access to FFMPEG for video processing
* `generate_image` - Creates images from text prompts
* `text_to_speech` - Converts text to audio
* `post_media` - Publishes content to social media

This tool set enables both simple and complex interactions. A user might request "Create and post a video on Python programming," and the agent handles everything automatically. Alternatively, the interaction could be more collaborative:

![](https://academy.claude.com/assets/media/246eea9097e99cc6b00ca5178b06762fb06d486175088bf68f353cd556e9431a.png)

The user might say "I want you to make a video on Python, but first I want to pick out an initial image for the video." The agent can generate a sample image, show it to the user for approval, then proceed with video creation once confirmed.

This flexibility emerges naturally from providing the right level of abstraction in your tools. Each tool should be general enough to be useful in multiple contexts, but specific enough to accomplish meaningful work when combined with others.
