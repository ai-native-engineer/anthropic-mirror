<!-- https://anthropic.skilljar.com/claude-code-101/469795 -->
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
