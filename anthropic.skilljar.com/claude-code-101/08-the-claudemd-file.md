<!-- https://anthropic.skilljar.com/claude-code-101/469795 -->

### Video



### The CLAUDE.md File

One of the most useful features in Claude Code is the CLAUDE.md file. It gives Claude Code persistent memory about your project.

## The Problem It Solves

When you open Claude Code without a CLAUDE.md file, it starts fresh every time. It has to re-explore your codebase, figure out what dependencies are needed, and understand what features are already implemented. Sometimes it makes assumptions, which makes it harder to steer Claude in the right direction.

CLAUDE.md solves this. It's a Markdown file you add to the root of your project, and Claude Code reads it automatically every time you start a session. Think of it as an onboarding script for your codebase. The contents of the CLAUDE.md file are appended to your prompt.

## An Example

Here's what a typical CLAUDE.md file looks like:

```
# Project

This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style
- Use 2-space indentation
- Prefer named exports
- All API routes go in app/api/
- Use server actions instead of API routes where possible
```

It's straightforward. Now if you ask Claude Code to create a React component, it already knows to use Tailwind for styling and to follow your code conventions.

![A CLAUDE.md file open in VS Code showing project info, commands, and code style rules](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686400%2Fvideo8claudemdexample.1775686400069.jpg)

## CLAUDE.md is for Teams

You can (and should) commit your CLAUDE.md to version control so your team benefits from it. There's actually a hierarchy of memory files depending on who they're for:

* **Project-level CLAUDE.md** lives in the root directory of your project. Shared with the team.

* **User-level CLAUDE.md** lives in your configuration folder. This one is just for you and applies across all your projects. Put your personal preferences here.

  

## Tips

**Save corrections to memory.** If you find yourself correcting Claude repeatedly — like telling it to always use server actions instead of API routes — explicitly ask Claude to save that rule to memory. Next time you open the project, it'll know.

![Asking Claude to save a rule to the CLAUDE.md file — always use server actions instead of API routes](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686399%2Fvideo8Askingclaudetoputinmemory.1775686399417.jpg)

**Reference project docs.** If you have documentation in your project that you want Claude to reference, use the `@` symbol with the file path:

```
## README.md

Please read if you need more info: @README.md
```

  

**Start without one.** We recommend starting a project without a CLAUDE.md file so you can see where you constantly have to course-correct the model. This keeps your CLAUDE.md compact and focused on only the necessary information. When you're ready, run `/init` to have Claude generate one for you.

  

## Recap

The difference between a frustrating Claude Code session and a productive one often comes down to context — and the CLAUDE.md file is how you provide that context. Start with your stack, your preferences, and your commands, then build from there as you go.
<!-- youtube: O0FGCxkHM-U -->

# The CLAUDE.md file

[![The CLAUDE.md file](https://img.youtube.com/vi/O0FGCxkHM-U/hqdefault.jpg)](https://www.youtube.com/watch?v=O0FGCxkHM-U)

<details>
<summary>자막: The CLAUDE.md file</summary>

One of the most useful parts of Claude Code is the claw.md file.
>> [music]
>> It gives Claude Code persistent memory
about your project.
>> [music]
>> When you open up Claude Code without a
claw.md file, it's like it has to start fresh every single time. It has to re-explore your code base, understand what dependencies are needed, and the features that are already implemented. Sometimes it has to make assumptions, which makes it harder for us to steer Claude in the right direction. But, that's where claw.md comes in. It's a markdown file that you add to the root of your project, and Claude Code reads it automatically every time you start a session. It's like an onboarding script for your code base. Simply put, the contents of claw.md file are appended to your own prompt. You can run the {slash} init command, which will make Claude generate one based off of your code base. So, let's have a look at one. This is a Next.js 15 app using the app router, Tailwind, and Drizzle ORM. Command, dev server, run tests, lint, code style, use two-space indentation, prefer named exports, all API routes go in app/{slash}api, use server actions instead of API routes where possible. And it's pretty straightforward. Now, if I ask Claude Code to create a React component, it knows how to style it with Tailwind or any other CSS framework that I'm using. We can see that Claude does a better job at doing his job right off the bat versus having to understand where everything is at first. And before you ask, the answer is yes. You share this in your version control for your team to use, but there's actually a hierarchy of memory files depending on who it's for. So, first you have your project-level claw.md that lives in the root directory of your project. You have a user-level claw.md that lives in your configuration folder. This one is just for you and goes across all your projects. So, put your preferences here, like how you write code comments. First, if you have to correct Claude to do something like always use server actions instead of API routes, then explicitly ask Claude to save this to memory, so that when you come back to this project, it will know every single time. Second, if you have docs in your project that you want Claude to reference, just use the @ symbol with the file path. And third is we recommend you start off a project without a Claude.md file, you can see where you have to constantly course correct the model. This keeps your Claude.md file compact and contain only the necessary information that Claude can work with. The difference between a frustrating Claude code session and a productive one comes down to the context and the Claude.md file is how you provide that context. Start with your stack, your preferences, and then commands, and
>> [music]
>> just build from there as you go.

</details>
