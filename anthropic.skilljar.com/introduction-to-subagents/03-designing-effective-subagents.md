<!-- https://anthropic.skilljar.com/introduction-to-subagents/450700 -->

Now that you know how to create subagents, let's look at the patterns that make them actually effective. A subagent that's poorly configured will wander, run too long, or produce output the main agent can't use. The fixes come down to four things: writing good descriptions, defining an output format, reporting obstacles, and limiting tool access.

## How Subagent Config Data Gets Used

When you send a message to the main context window agent, the name and description of every available subagent are included in the system prompt. This is how the main agent decides which subagent to launch and when. If you want better control over when a subagent gets triggered automatically, the name and description are what you should tweak.

The description also plays a second role. When the main agent launches a subagent, it writes an input prompt to kick off the task. It uses the description as guidance for writing that prompt. So the description doesn't just control *when* a subagent runs -- it shapes *what the subagent is told to do*.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773975083%2Fvid3redone-v2_02.1773975083694.png)  

## Writing Descriptions That Shape Input Prompts

Consider a code review subagent. With a generic description, the main agent might write an input prompt like "use get diff to find the current changes." That's vague. The subagent has to figure out which files matter on its own.

If you update the description to include something like "You must tell the agent precisely which files you want it to review," the main agent will now write a much more specific input prompt that lists the actual files to review.

This same technique works across different types of subagents. For example, adding "return sources that can be cited" to a web search subagent's description causes the main agent to include that instruction when delegating the task.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773975124%2Fvid3redone-v2_03.1773975124367.png)  

## Defining an Output Format

The single most important improvement you can make to a subagent is defining an output format in its system prompt. This does two things:

* It creates natural stopping points -- the subagent knows it's done when it has filled in each section of the format.
* It prevents the subagent from running too long. Without a defined output, subagents struggle to decide when enough research has been done and tend to run much longer than necessary.

Here's an example of a structured output format for a code review subagent:

```
Provide your review in a structured format:

1. Summary: Brief overview of what you reviewed and overall assessment 2. Critical Issues: Any security vulnerabilities, data integrity risks, or logic errors that must be fixed immediately 3. Major Issues: Quality problems, architecture misalignment, or significant performance concerns 4. Minor Issues: Style inconsistencies, documentation gaps, or minor optimizations 5. Recommendations: Suggestions for improvement, refactoring opportunities, or best practices to apply 6. Approval Status: Clear statement of whether the code is ready to merge/deploy or requires changes
```

This format gives the subagent a clear checklist to work through. Once every section is filled in, the subagent knows it can stop.

## Reporting Obstacles

When a subagent discovers a workaround during its work -- like solving a dependency issue or finding that a certain command needs particular flags -- those details need to appear in the summary it returns. If they don't, the main thread has to rediscover the same solutions on its own, which wastes time and tokens.

The kinds of things you want surfaced include:

* Setup issues or environment quirks
* Workarounds discovered during the task
* Commands that needed special flags or configuration
* Dependencies or imports that caused problems

The way to get this information is to explicitly ask for it in the output format. Adding an "Obstacles Encountered" section to your output template surfaces this information reliably.

```
7. Obstacles Encountered: Report any obstacles encountered during the review process. This can be: setup issues, workarounds discovered or environment quirks. Report commands that needed a special flag or configuration. Report dependencies or imports that caused problems.
```

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773975160%2Fvid3redone-v2_11.1773975160096.png)  

## Limiting Tool Access

Not every subagent needs access to every tool. Think about what a subagent actually needs to do, and only give it the tools required for that job. This does two things: it prevents unintended side effects, and it makes each subagent's role clearer when you have several of them.

Here's how to think about tool access for common subagent types:

* **Research / read-only subagent** -- Only needs `Glob`, `Grep`, and `Read`. Cannot accidentally modify files.
* **Code reviewer** -- Needs `Bash` access to run `git diff` and see what changed, but still doesn't need `Edit` or `Write`.
* **Styling / code modification agent** -- This is where you give `Edit` and `Write` access, because the subagent's job is to actually change your code.

## Putting It All Together

Effective subagents share four characteristics:

1. **Specific descriptions** -- The description controls when the subagent is launched and what instructions it receives. Write it to steer both. 2. **Structured output** -- Define an output format in the system prompt so the subagent knows when it's done and returns information the main thread can use. 3. **Obstacle reporting** -- Include a section in the output format for workarounds, quirks, and problems so the main thread doesn't have to rediscover them. 4. **Limited tool access** -- Only give a subagent the tools it actually needs. Read-only for research, bash for reviewers, edit/write only for agents that should change code.

Each of these patterns is simple on its own, but together they turn a subagent from something that vaguely tries to help into a focused, predictable worker that finishes on time and reports back clearly.

<!-- youtube: WPxWKT_OaU4 -->

[![Designing Effective Subagents](https://img.youtube.com/vi/WPxWKT_OaU4/hqdefault.jpg)](https://www.youtube.com/watch?v=WPxWKT_OaU4)

<details>
<summary>자막: Designing Effective Subagents</summary>

Now that you know how to create sub agents, let's look at patterns that lead to effective sub agents. First, let's get a better idea of how some of the data in the sub agent config file is used. Whenever you send a message to the main context window agent, the name and description of each sub agent is included in the system prompt. So, if you want to better control when the main agent launches a sub agent automatically, you should modify the name description. Next, remember that when a sub agent is launched, the main agent writes an input prompt. When writing this input prompt, it uses the description as guidance. So, if you want to better control when the main agent launches a sub agent automatically, you should modify the name and description. Let's consider our review sub agent again. Right now, when the main agent runs the sub agent, the sub agent is given an input prompt telling it to use get diff to find the current changes. If we wanted the main agent to more reliably tell the sub agent exactly which files to review, we would update the description. You must tell the agent precisely which files you want it to review. Now, if we ask Claude to run the code reviewer agent, we'll see a different input. You can also influence what the main thread tells a sub agent through the description. So, adding return sources that can be cited to a web search sub agent's description causes the main thread to include that instruction when delegating the task. The most important improvement that you can make is defining an output format in the system prompt. This creates natural stopping points for the sub agent. Without a defined output format, sub agents struggle to decide when enough research has been done and they tend to run much much longer than sub agents that are given an output format. When a sub agent discovers a workaround to some issue like solving a dependency issue or finding that a certain command needs particular flags, these details should appear in the summary. Otherwise, the main thread has to rediscover the same solutions. Obstacles encountered, any setup issues, workarounds discovered, or environment quirks, commands that needed special flags or configuration, dependencies or imports that cause problems. Explicitly asking for obstacle reporting in the output format surfaces this information. A read-only sub agent using just glob, grep, read cannot accidentally modify files. This constraint clarifies that the sub agent's role and prevents unintended side effects. So, think about what sub agents actually needs to do. If it's just researching, it only needs to read files, so keep it read-only. That way it can't accidentally modify anything while exploring. A reviewer needs to run get diff to see what changed, so give it bash access, but it still doesn't need to edit files. Only give edit and write to sub agents that should actually change your code like a styling agent applying CSS updates. This also helps clarify what each sub agent is for when you have several of them. So, effective sub agents use structured output, report obstacles, have specific descriptions, and limit tool access.

</details>
