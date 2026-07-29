<!-- https://anthropic.skilljar.com/introduction-to-subagents/450701 -->

You know how to create subagents and design them well. Now the question is: when do they actually help, and when do they get in the way? The difference comes down to one thing -- whether the intermediate work matters to your main thread.

## When subagents shine

Subagents work best when the exploration is separate from the execution. If each step in a task depends on what the previous step discovered, you want that work in your main thread. But if you just need an answer and don't care about the journey, delegate it.

Subagents excel at tasks where:

* You need a result, not a play-by-play of how it was found
* The exploratory work would clutter your main thread's context
* The task benefits from a fresh perspective or a custom system prompt

## Research tasks

Research is the classic subagent use case. Consider investigating how authentication works in an unfamiliar codebase. Your main thread needs to know *where* the JWT is validated, but it doesn't need to see every file that was searched along the way.

A research subagent can read dozens of files, trace through function calls, and explore different code paths. All that exploration stays in the subagent's context. Your main thread receives a clean summary like:

```
JWT validation happens in middleware/auth.js line 42, called from the Express router in route/api.js
```

The subagent did the heavy lifting. Your main thread gets exactly what it needs to move forward.

## Code Reviews

Claude reviews code more effectively when the code is presented as being authored by someone else. If you built a feature over many turns with your main thread, asking that same thread to review it often produces weak feedback. Claude was involved in creating it, so it has trouble seeing it with fresh eyes.

A reviewer subagent sees the changes in a separate context. It runs `git diff`, reads the modified files, and applies its specialized review criteria without the history of how the code was written. This separation also lets you encode project-specific review standards in the subagent's system prompt, ensuring consistent review criteria across the team.

## Custom System Prompts

Claude Code's default system prompt emphasizes concise, code-focused responses. That works great for coding, but not for everything.

Here are two cases where a custom system prompt makes the subagent genuinely better than the main thread:

* **Copywriting subagent** -- Give it instructions about tone, audience, and style. Claude Code's default prompt tends toward concise technical writing, which really isn't what you want for a landing page or email campaign. A copywriting subagent can have completely different instructions about voice and structure.
* **Styling subagent** -- Point it at your design system files. When the subagent runs, those files load into its context automatically, so it knows your color variables, spacing conventions, and component patterns before it even starts writing any CSS.

## When Subagents Hurt

The overhead of launching a subagent -- losing visibility into its work and compressing its findings into a summary -- only makes sense when the subagent does something the main thread can't. There are three common anti-patterns to watch out for.

### Expert Claims

Subagents that claim expertise rarely help. Prompts like "you are a Python expert" or "you are a Kubernetes specialist" add no value because Claude already has that knowledge. There's nothing a so-called expert subagent can do that your main thread can't do directly.

### Sequential Pipelines

Sequential subagent pipelines create problems. Consider a three-agent flow: one to reproduce a bug, one to debug it, and one to fix it. Pipelines work when tasks are truly independent. They fail when each step depends on discoveries from the previous step -- and bug fixing almost always does. Information gets lost in the handoff between agents.

### Test Runners

Test runner subagents tend to hide information you need. When tests fail, you want the full output to diagnose issues. A subagent that returns "tests failed" forces you to create additional debug scripts to get details that would have been visible in direct output. Testing has shown that the test runner pattern performed worse among all configurations.

## The Decision Rule

When you're deciding whether to use a subagent, ask yourself one question: **does the intermediate work matter?**

If the answer is no -- you just need the final result -- delegate it to a subagent. If the answer is yes -- you need to see and react to what's happening along the way -- keep it in your main thread.

Use subagents for:

* Research and exploration
* Code reviews
* Tasks that need a custom system prompt

Avoid subagents for:

* "Expert" personas that don't add real capability
* Multi-step pipelines where each step depends on the last
* Running tests where you need full output for debugging

<!-- youtube: n5LoKZ8Oa-A -->

[![Using Subagents Effectively](https://img.youtube.com/vi/n5LoKZ8Oa-A/hqdefault.jpg)](https://www.youtube.com/watch?v=n5LoKZ8Oa-A)

<details>
<summary>자막: Using Subagents Effectively</summary>

You know how to create sub agents and design them well. Now, let's cover when they actually help and when they get in the way. Simply put, the difference comes down to whether the intermediate work matters to your main thread. When exploration is separate from execution, sub agents shine. When each step depends on what the previous step discovered, well, information gets lost in the handoff process. Sub agents excel at research tasks where you just need an answer, not the journey. Consider investigating how authentication works in an unfamiliar code base. Well, the main thread might need to know where is the JWT validated, but doesn't need to see every file that was searched. A research sub agent can read dozens of files, trace through function calls, and explore different code paths. All that exploration stays in the sub agent's context. Your main thread receives JWT validation happens in middleware/auth.js at line 42, called from the Express router and route/api.js, or something like that. Claude reviews work more effectively when the code is presented as being authored by someone else. If you build a feature over many turns with your main thread, asking the main thread to then review it often doesn't give the best feedback. Claude was involved in creating it, so it has trouble seeing it with fresh eyes. A reviewer sub agent sees the changes in a separate context. It runs get diff, reads the modified files, and applies its specialized review criteria without the history of how the code was written. And this separation also lets you encode project-specific review standards in the sub agent system prompt, ensuring consistent review criteria across the team. Claude Code's default system prompt emphasizes concise, code-focused response. And this works great for coding, but not for everything. So, one is a copywriting sub-agent with instructions about tone, audience, and style. This will produce better marketing text than the main thread would. Claude Code's default prompt tends towards concise, technical writing, which really isn't what you want for a landing page or email campaign, unless you want to put your customers to sleep. A copywriting sub-agent can have completely different instructions about voice and structure. A styling sub-agent that at mentions your design system files will apply consistent CSS patterns. When the sub-agent runs, those files load into the context automatically, so it knows your color variables, spacing conventions, and component patterns before it even starts writing any CSS. Sub-agents that claim expertise rarely help. Prompts like, "You are a Python expert." or "You are a Kubernetes specialist." add no value because Claude already has that knowledge. The overhead of launching a sub-agent, losing visibility into its work, and compressing its findings into a summary only makes sense when the sub-agent does something that the main thread can't. Like applying a custom system prompt or keeping exploratory work isolated. Sequential sub-agent pipelines create problems. Consider a three-agent flow. One to reproduce a bug, one to debug it, and one to fix it. Pipelines work when tasks are truly independent. They fail when each step depends on discoveries from the previous step. Test runner sub-agents tend to hide information you need. When tests fail, you want the full output to diagnose issues. A sub-agent that returns a test failed forces you to create additional debug scripts to get details that would have been visible in direct output. Testing has showed that the test runner pattern performed worse among all configurations. Across the series, we covered how sub-agents work as isolated threads that return summaries. How to create them with the /agents command, and how to design them with structured outputs and specific descriptions. Use them for research, reviews, and tasks needing custom system prompts. But, avoid them for expert claims, multi-step pipelines, and test runners. The key question, does the intermediate work matter? If not, then delegate it.

</details>
