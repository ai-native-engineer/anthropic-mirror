<!-- source: https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow -->

Lesson 5 of 12 · Claude Code 101The explore → plan → code → commit workflow

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# The explore → plan → code → commit workflow

Lesson 58 min

The explore → plan → code → commit workflow

If you take one thing away from this course, let it be this workflow:
**Explore, Plan, Code, and Commit**. Without it, most people jump straight
to asking Claude to write code — which means more course-correcting later
on.

## Explore and Plan

The fastest way to handle these first two steps is with **Plan Mode**. In plan mode, Claude can't edit files — it just reads files to gather information about how it will tackle the implementation.

To enter plan mode, press `Shift + Tab` until you see "Plan Mode" under the text input. Then write a prompt like:

![Claude Code status bar showing plan mode on with shift+tab to cycle](https://academy.claude.com/assets/media/7cb40799b30ac6dbf30945994053139cc228086849e432947b344381f4edd4df.jpg)

I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it.

Open in Claude Code

Claude will read relevant files, run some web searches, and give you a plan of action. Review it and decide if it meets your criteria. If not, ask it to revise specific areas.

![Claude Code presenting the plan with options to approve, revise areas, or ask questions](https://academy.claude.com/assets/media/8c9aa778ca4deab716094a243d80ef4788460504f215bc3e6f279adc36cab8ae.jpg)

This is the best place to course-correct because it's before any code is written. You can also run the explore subagent without being in plan mode if you just want a general summary of your codebase without intending to make changes afterward.

## Code

Once the plan looks good, select "approve" to accept it and let Claude work through the list items. You can choose whether Claude auto-accepts file edits or asks you each time.

Claude will do its best to troubleshoot before considering the plan "finished," but at times you'll need to step in. This is the benefit of working with Plan Mode — after execution, you also have the context of how you got to the results, which helps guide Claude's next decisions.

A few tips to make the coding phase smoother:

* **Define a success criteria.** For Claude to be confident in its results, it needs to be clear on what "correct" looks like. Make this explicit when writing your plan.
* **Add tools.** Tools that help Claude complete its goals remove a lot of back and forth. For example, if you're building web UIs, install the Claude in Chrome extension so Claude Code can control a browser tab and test the UI directly.

  ![The Claude in Chrome extension page in the Chrome Web Store](https://academy.claude.com/assets/media/bf3b9eb343e3a61fbd3b6a12ad8f99f1ca989cc945977f386cc92771c4c516ff.jpg)
* **Include a test suite.** Give Claude a test suite it can continuously validate against. Claude can even write tests for you. Before handing this off, make sure the tests are a reliable source of truth to avoid false positives.

**Quick tip:** If you find Claude keeps running into the same issues, ask it to save the solution to its CLAUDE.md file.

## Commit

Once you've tested the changes yourself and are happy with the results, it's time to push your code. Before you commit, run a **subagent code reviewer** to look at your work. A subagent gets a fresh pair of eyes on the codebase — it doesn't carry the bias the main agent might have from the session.

![A code-reviewer subagent running in Claude Code, reading files and reviewing recent changes](https://academy.claude.com/assets/media/3d64a0570bf9a62202320b490b2f60414a9f9a52d9897957eabf4bb14edce043.jpg)

Then get Claude to generate a commit message in your style. Rinse and repeat.

## Recap

To be effective with Claude Code, follow the Explore, Plan, Code, and Commit workflow:

* **Explore** gives Claude the relevant context it needs for your project.
* **Plan** creates a plan of action that Claude uses to measure success.
* **Code** is the back and forth between you and Claude before settling on the final outcome.
* **Commit** helps you review and push your code so you can start on your next feature.

[Previous lessonYour first prompt](https://academy.claude.com/courses/claude-code-101/your-first-prompt)[Next lessonContext management](https://academy.claude.com/courses/claude-code-101/context-management)

Lesson 5 of 12 · Claude Code 101The explore → plan → code → commit workflow

What is Claude Code?

* [What is Claude Code?](https://academy.claude.com/courses/claude-code-101/what-is-claude-code)
* [How Claude Code works](https://academy.claude.com/courses/claude-code-101/how-claude-code-works)

Your first prompt

* [Installing Claude Code](https://academy.claude.com/courses/claude-code-101/installing-claude-code)
* [Your first prompt](https://academy.claude.com/courses/claude-code-101/your-first-prompt)

Daily workflows

* [The explore → plan → code → commit workflow](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow)
* [Context management](https://academy.claude.com/courses/claude-code-101/context-management)
* [Code review](https://academy.claude.com/courses/claude-code-101/code-review)

Customizing Claude Code

* [The CLAUDE.md file](https://academy.claude.com/courses/claude-code-101/the-claude-md-file)
* [Subagents](https://academy.claude.com/courses/claude-code-101/subagents)
* [Skills](https://academy.claude.com/courses/claude-code-101/skills)
* [MCP](https://academy.claude.com/courses/claude-code-101/mcp)
* [Hooks](https://academy.claude.com/courses/claude-code-101/hooks)

Quiz

* [Course quizQuiz](https://academy.claude.com/courses/claude-code-101/course-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-code-101/badge)

* [Explore and Plan](#explore-and-plan)
* [Code](#code)
* [Commit](#commit)
* [Recap](#recap)
