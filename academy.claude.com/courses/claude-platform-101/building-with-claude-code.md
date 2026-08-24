<!-- source: https://academy.claude.com/courses/claude-platform-101/building-with-claude-code -->

Lesson 13 of 13 · Claude Platform 101Building with Claude Code

Loading

Building with Claude Code

Writing code that calls the Claude API by hand works fine, but there's an
even faster path: have Claude write it for you. In this lesson, we'll use
**Claude Code** to fill in an API integration from a stubbed-out
file — using the same primitives you've learned throughout this course.

## Starting from a stub

The project is simple: a TypeScript file that gets weather. It contains two stubs:

* **getWeather** — accepts a city and returns the temperature and conditions.
* **run** — a function that should use the **tool runner** and the Claude TypeScript SDK.

The tool runner is the piece that handles tool calling and the agent loop for you, so you don't have to wire that up manually.

## The Claude API skill

Claude Code comes with a built-in skill called **Claude API**. You can invoke it directly with `/claude-api`, or Claude Code will invoke it automatically when it detects that you're using the TypeScript SDK.

## One prompt, working code

Open the project folder in your terminal and launch Claude Code.

From there, it takes a single prompt. A good prompt does three things:

* It **names the file** you want changed.
* It **names the pattern** you want used.
* It **names the end state** you expect.

Claude Code then fills in `getWeather` and `run` against the types, appends a call at the bottom of the file, executes the script, and reports the output. If something errors out, it reads the error message and patches the code in place.

![Claude Code in the terminal reading weather.ts and the tool runner file after receiving the prompt](https://academy.claude.com/assets/media/2a4537bcd3845e6c8cf2d160eebd10f487f57729d007fc1ceec56bf67b515bf0.png)

## What Claude Code produced

In this run, Claude Code created a **Zod tool** that parsed the input and returned the output based on the city type. It also created the tool runner and the `run` function we asked for, and printed the final results of the agent loop.

![Claude Code generating the weather code in the terminal, with the betaZodTool import and hardcoded city data visible](https://academy.claude.com/assets/media/d78d1f952202fef1bf8ed8d77662dd31f66b6dc6dc15e894c2b58fe57214e6c6.png)

## The pattern to remember

Most of what you write against the Claude API has a familiar shape:

1. Define a tool.
2. Hand it to a runner.
3. Return the result.

You don't need to type that from memory every single time. Instead, stub the file, hand it to Claude Code, and just review the diff.

## Recap

* **Claude Code** is an agent that edits files and runs commands inside your terminal.
* The built-in **Claude API** skill loads automatically when Claude Code detects the TypeScript SDK, or you can invoke it with `/claude-api`.
* Give it a prompt that names the file, the pattern, and the end state — it writes the code, runs it, and fixes errors in place.
* Claude API code follows a familiar shape: define a tool, hand it to a runner, return the result. Stub it, delegate it, review the diff.
