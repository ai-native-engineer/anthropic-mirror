<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/tool-functions -->

Lesson 22 of 65 · Claude with Amazon BedrockTool functions

Building tools for Claude requires solving several challenges that aren't immediately obvious. When you want Claude to set reminders for future dates, you quickly discover that while Claude knows the current date, it doesn't always know the exact time, struggles with complex date arithmetic, and has no built-in way to actually set reminders.

![](https://academy.claude.com/assets/media/59f1421b35b91a9e12d77fe6fc39b9aa25f631d512952ff9d558642a0644650e.png)

The solution is to create custom tools that handle these specific tasks. For a reminder system, you'll need three separate tools: one to get the current date and time, another to add durations to dates, and a third to actually set the reminder.

## Why This Is Challenging

Claude has some limitations when it comes to time-based tasks:

* Claude might know the current date, but not the exact time
* Claude doesn't always handle time-based addition well, especially when looking many days into the future
* Claude doesn't know how to set a reminder

![](https://academy.claude.com/assets/media/a7c479969f35c554cc2bbba8f8e3908cabc2f621e13b4068267e5c971b20692b.png)

## The Tools You Need

To solve these problems, you'll create three dedicated tools:

* **Get the current date time** - Claude needs to know the current date and time
* **Add duration to date time** - Claude isn't perfect with date time addition
* **Set a reminder** - Need a way to set a reminder

![](https://academy.claude.com/assets/media/ab568fe7efa0dc2e7418393d5d926dbca2ccc2840fa0ea0e396b4c786d2699c6.png)

## How Tool Functions Work

The tool system follows a specific flow between your server and Claude. You write functions that Claude can call when it needs additional information, and Claude receives the results to help formulate its response.

![](https://academy.claude.com/assets/media/5b0bb0502e2b58bf4e767efced7d0f7f7c385c57501d457c61769d5ede05a2a1.png)

The process involves several steps: writing the tool function, creating a JSON schema specification, calling Claude with that schema, running the tool when Claude requests it, and providing the results back to Claude.

![](https://academy.claude.com/assets/media/493213de9630b90abce40533716123bee8656cde00774668558a6aedcf045085.png)

## Writing Tool Functions

Tool functions are plain Python functions that get executed when Claude decides it needs additional information to help the user. Here's how to write them effectively:

### Best Practices

* Use well-named, descriptive arguments (this becomes important later)
* Validate the inputs, raising an error if they fail validation
* Return meaningful errors - Claude will try to call your function a second time if it gets an error

![](https://academy.claude.com/assets/media/ab8e2ed3a5d133c180b9fb859d6d53a4c122fea7cef28570e948c20faa8dcd33.png)

## Creating Your First Tool

Let's start with the simplest tool - getting the current date and time. This function takes a date format parameter and returns the current timestamp:

python

```
from datetime import datetime, timedelta

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(date_format)
```

This function is straightforward but follows the key principles: it has a descriptive name, takes a well-named parameter with a sensible default, and returns exactly what it promises.

## JSON Schema Specification

Once you have your function, you need to write a JSON Schema that describes it to Claude. This schema tells Claude what arguments the function requires and helps it understand when and how to use the tool.

![](https://academy.claude.com/assets/media/6ea349aba9b64c132b3081158284d2e6eecfc9fcba6b1b8a88aaec781d262097.png)

The JSON Schema serves two purposes: it helps Claude understand what arguments your function requires, and it's not just an LLM concept - JSON Schema is commonly used for data validation across many programming contexts. There are plenty of online tools to help you generate schemas.

### Schema Best Practices

* Explain what the tool does, when to use it, and what it returns
* Aim for 3 to 4 sentences in your descriptions
* Provide detailed descriptions for parameters

With your tool function written and schema defined, you're ready to integrate it with Claude and start building more sophisticated AI interactions that can handle real-world tasks like setting reminders.
