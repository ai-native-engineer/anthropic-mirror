<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-overview -->

Lesson 22 of 66 · Claude with Google Cloud's Vertex AIProject overview

We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

![](https://academy.claude.com/assets/media/0b1a7a20c9a0a4d57723e9c95065d706990ddccabbba00944372d861507b1785.png)

The goal is to have a conversation like this: you tell Claude "Set a reminder for my doctor's appointment. It's a week from Thursday," and Claude responds "OK, I will remind you." To make this work, we need to understand why this is actually harder than it looks.

## Why This Is Challenging

Claude has some built-in knowledge about dates and times, but it also has some significant limitations:

* Claude might know the current date, but not the exact time
* Claude doesn't always handle time-based addition well, especially if looking many days into the future
* Claude doesn't know how to set a reminder!

![](https://academy.claude.com/assets/media/5794a6fc8bd5562b3626d7108435489fd6c4eba4a3a300715c958b9ae766abae.png)

These limitations mean that even a simple request like "set a reminder for 24 hours from now" becomes problematic. Claude doesn't know what "24 hours from now" actually means without knowing the current time. And even if it could calculate the right date, it has no mechanism to actually create a reminder.

## Tools We Need

To solve these problems, we'll create three custom tools that work together:

![](https://academy.claude.com/assets/media/d1042ce4670eec51e35842b37d919f53d8285a0da854a7661546e4e3b3ef62eb.png)

## Get the Current Date Time

This is our starting tool - it gives Claude access to both the current date and the exact time. This solves the problem of Claude not knowing when "now" actually is.

## Add Duration to Date Time

This tool handles the math of adding time periods to dates. Instead of relying on Claude to correctly calculate "what date is 379 days from January 13th, 1973," we give it a reliable tool that can handle these calculations accurately.

## Set a Reminder

Finally, we need a way for Claude to actually create reminders. This tool will provide the mechanism that Claude lacks for setting up future notifications.

We'll implement these tools one at a time, starting with the datetime tool to understand how tool calling works, then building up to the more complex functionality. By the end, Claude will be able to handle natural language requests about setting reminders and convert them into actual scheduled notifications.
