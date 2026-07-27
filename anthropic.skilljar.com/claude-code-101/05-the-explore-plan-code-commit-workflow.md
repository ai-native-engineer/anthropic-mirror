<!-- https://anthropic.skilljar.com/claude-code-101/469792 -->

### Video



### The Explore → Plan → Code → Commit Workflow

If you take one thing away from this course, let it be this workflow: **Explore, Plan, Code, and Commit**. Without it, most people jump straight to asking Claude to write code — which means more course-correcting later on.

## Explore and Plan

The fastest way to handle these first two steps is with **Plan Mode**. In plan mode, Claude can't edit files — it just reads files to gather information about how it will tackle the implementation.

To enter plan mode, press `Shift + Tab` until you see "Plan Mode" under the text input. Then write a prompt like:

![Claude Code status bar showing plan mode on with shift+tab to cycle](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686390%2Fvideo5planmodeshifttab.1775686390450.jpg)

```
I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it.
```

  

Claude will read relevant files, run some web searches, and give you a plan of action. Review it and decide if it meets your criteria. If not, ask it to revise specific areas.

![Claude Code presenting the plan with options to approve, revise areas, or ask questions](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686389%2Fvideo5planmodereviseareas.1775686389692.jpg)

This is the best place to course-correct because it's before any code is written. You can also run the explore subagent without being in plan mode if you just want a general summary of your codebase without intending to make changes afterward.

## Code

Once the plan looks good, select "approve" to accept it and let Claude work through the list items. You can choose whether Claude auto-accepts file edits or asks you each time.

Claude will do its best to troubleshoot before considering the plan "finished," but at times you'll need to step in. This is the benefit of working with Plan Mode — after execution, you also have the context of how you got to the results, which helps guide Claude's next decisions.

A few tips to make the coding phase smoother:

* **Define a success criteria.** For Claude to be confident in its results, it needs to be clear on what "correct" looks like. Make this explicit when writing your plan.
* **Add tools.** Tools that help Claude complete its goals remove a lot of back and forth. For example, if you're building web UIs, install the Claude in Chrome extension so Claude Code can control a browser tab and test the UI directly.   
    
  ![The Claude in Chrome extension page in the Chrome Web Store](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686387%2Fvideo5claudeinchromeextension.1775686387012.jpg)
* **Include a test suite.** Give Claude a test suite it can continuously validate against. Claude can even write tests for you. Before handing this off, make sure the tests are a reliable source of truth to avoid false positives.

**Quick tip:** If you find Claude keeps running into the same issues, ask it to save the solution to its CLAUDE.md file.

## Commit

Once you've tested the changes yourself and are happy with the results, it's time to push your code. Before you commit, run a **subagent code reviewer** to look at your work. A subagent gets a fresh pair of eyes on the codebase — it doesn't carry the bias the main agent might have from the session.

![A code-reviewer subagent running in Claude Code, reading files and reviewing recent changes](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686388%2Fvideo5claudesubagentcodereviewer.1775686387773.jpg)

Then get Claude to generate a commit message in your style. Rinse and repeat.

## Recap

To be effective with Claude Code, follow the Explore, Plan, Code, and Commit workflow:

* **Explore** gives Claude the relevant context it needs for your project.
* **Plan** creates a plan of action that Claude uses to measure success.
* **Code** is the back and forth between you and Claude before settling on the final outcome.
* **Commit** helps you review and push your code so you can start on your next feature.
<!-- youtube: xJQuF02NAK8 -->

# The explore → plan → code → commit workflow

[![The explore → plan → code → commit workflow](https://img.youtube.com/vi/xJQuF02NAK8/hqdefault.jpg)](https://www.youtube.com/watch?v=xJQuF02NAK8)

<details>
<summary>자막: The explore → plan → code → commit workflow</summary>

If you take one thing away from Claude code, let it be this workflow: explore, plan, code, and commit. Without this, most people jump straight to pasting in Claude to write code, which means more course correcting later on. The fastest way to handle step one and two is with plan mode. With plan mode, Claude can't edit files. It just reads files to gather research on how to tackle this implementation. To enter plan mode, hit shift and tab until you see the plan mode under the text input. I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it. And Claude will read relevant files, do some web searches, and give you a plan of action. Make sure you review it and determine if it meets your criteria. Otherwise, I can ask it to add on or revise some areas. Perfect. And this right here is the best place to course correct because it's before any code is written. You can also use explore without being in plan mode by just asking Claude to explore your code base. Now, once the plan looks good, you can select approve to accept the plan and let Claude toggle all of the list items it provided. You can determine if you want Claude to auto accept the file edits or ask every single time. Claude will do its best to troubleshoot your code base before considering the plan finished. But at times, you'll need to course correct. This is the benefit of working with plan mode because after the plan is finished, we also have the context of how it got to the results to help it guide its next decision. In order for Claude to be confident in its results, it has to be clear on what it deems correct. When writing your plan, make this explicit. Adding tools that will help Claude complete its goals will remove a lot of back and forth. For example, if you're building web UIs, make sure you have the Claude and Chrome extension so that Claude code can control a tab and test out the UI before deeming it finished. In your project, include a test suite that Claude can continuously validate on. Claude can even write tests for you. Before passing this off to Claude, make sure that the tests are a source of truth for you and your team to avoid any false positives. Quick tip, if you find Claude keeps running into the same issues, ask Claude to save the solution to his Claude MD file. Now, once you have tested for yourself and are happy with the results, it's time to push your code. A tip before you commit, run a sub agent code reviewer to look at your code. Then you get Claude to generate a commit message for you in your style. Rinse and repeat.
>> [music]
>> If you want to be effective with Claude
code, follow the explore, plan, code, and commit workflow. Exploration will give the relevant context Claude needs for your project. Plan will create a plan of action that Claude will use to determine if they are successful. Code is the back and forth that you and Claude do before settling on the final outcomes of the plan. Commit helps you review and push your code so you can start on your next feature.

</details>
