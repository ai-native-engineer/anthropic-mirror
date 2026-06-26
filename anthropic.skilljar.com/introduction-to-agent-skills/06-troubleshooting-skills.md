<!-- https://anthropic.skilljar.com/introduction-to-agent-skills/434530 -->

**What you'll learn**

*Estimated time: 15 minutes*

By the end of this lesson you'll be able to:

* Use the skills validator to catch structural issues before debugging
* Diagnose and fix common skill triggering and loading problems
* Resolve skill priority conflicts between enterprise, personal, project, and plugin skills
* Debug runtime errors including missing dependencies, permissions, and path issues

## Troubleshooting skills

*(4 minutes)*

When skills don't work as expected, the problem usually falls into a few predictable categories. This video walks through each one — from skills that don't trigger to priority conflicts to runtime failures — and gives you a systematic troubleshooting approach. You'll also learn about the skills validator tool and how to use `claude --debug` to diagnose loading issues.

#### Key takeaways

* Start with the **skills validator tool** — it catches structural problems before you spend time debugging other things
* If a skill **doesn't trigger**, the cause is almost always the description — add trigger phrases that match how you actually phrase requests
* If a skill **doesn't load**, check that `SKILL.md` is inside a named directory (not at the skills root) and the file name is exactly `SKILL.md`
* If the **wrong skill gets used**, your descriptions are too similar — make them more distinct
* For **runtime errors**, check dependencies, file permissions (`chmod +x`), and path separators (use forward slashes everywhere)

When skills don't work, the problem usually falls into one of a few categories: the skill doesn't trigger, doesn't load, has conflicts, or fails at runtime. The good news is that most fixes are pretty straightforward.

## Use the Skills Validator

The first thing to try is the agent skills verifier command. Installation steps vary by operating system, but using `uv` is the easiest way to get it set up quickly.

Once installed, either navigate to your skill directory or run the command from anywhere. The validator will catch structural problems before you spend time debugging other things.

## Skill Doesn't Trigger

Your skill exists and passes validation, but Claude isn't using it when you expect. The cause is almost always the description.

Claude uses semantic matching, so your request needs to overlap with the description's meaning. If there's not enough overlap, no match. Here's what to do:

* Check your description against how you're actually phrasing requests
* Add trigger phrases users would actually say
* Test with variations like "help me profile this," "why is this slow?", "make this faster"
* If any variation fails to trigger, add those keywords to your description

## Skill Doesn't Load

If your skill doesn't appear when you ask Claude "what skills are available," check these structural requirements:

* The `SKILL.md` file must be inside a named directory, not at the skills root
* The file name must be exactly `SKILL.md` — all caps on "SKILL", lowercase "md"

Run `claude --debug` to see loading errors. Look for messages mentioning your skill name. Sometimes this alone will point you straight to the problem.

## Wrong Skill Gets Used

If Claude uses the wrong skill or seems confused between skills, your descriptions are probably too similar. Make them distinct. Being as specific as possible doesn't just help Claude decide when to use your skill — it also prevents conflicts with other similar-sounding skills.

## Skill Priority Conflicts

If your personal skill is being ignored, an enterprise or higher-priority skill might have the same name.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1771527274%2FSkills6_12.1771527274623.png)

For example, if there's an enterprise "code-review" skill and you also have a personal "code-review" skill, the enterprise one wins every time. Your options:

1. Rename your skill to something more distinct (this is usually the easier path) 2. Talk to your admin about the enterprise skill

## Plugin Skills Not Appearing

Installed a plugin but can't see its skills? Clear the cache, restart Claude Code, and reinstall.

If skills still don't appear after that, the plugin structure might be wrong. This is when the validator tool really earns its keep.

## Runtime Errors

The skill loads but fails during execution. A few common causes:

* **Missing dependencies:** If your skill uses external packages, they must be installed. Add dependency info to your skill description so Claude knows what's needed.
* **Permission issues:** Scripts need execute permission. Run `chmod +x` on any scripts your skill references.
* **Path separators:** Use forward slashes everywhere, even on Windows.

## Quick Troubleshooting Checklist

* **Not triggering?** Improve your description and add trigger phrases.
* **Not loading?** Check your path, file name, and YAML syntax.
* **Wrong skill used?** Make descriptions more distinct from each other.
* **Being shadowed?** Check the priority hierarchy and rename if needed.
* **Plugin skills missing?** Clear cache and reinstall.
* **Runtime failure?** Check dependencies, permissions, and paths.

## Lesson reflection

* Have you encountered any of these troubleshooting scenarios in your own work? Which fix would have saved you the most time?
* How would you set up a process to validate skills before sharing them with your team?

## Course wrap-up

Congratulations on completing Introduction to Agent Skills! You've learned how to create, configure, share, and troubleshoot skills in Claude Code. As you start building skills for your own workflows, remember that the best skills come from real pain points — start with the instructions you find yourself repeating most often.

#### Feedback

We'd love to hear how you're using skills in your work, plus any feedback about this course. Share your feedback [here](https://forms.gle/RvHPBwQt9ZmcDc1P9).

<!-- youtube: YBa1cwaG7is -->

## 자막 (영상 전사)

When skills don't work, the problem usually falls into one of a few categories. The skill doesn't trigger, doesn't load, has conflicts, or fails at runtime. But [music] good news, most fixes are pretty straightforward. Here are some of them. First thing we can do is try the agent skills verifier command. Depending on your operating system, installation steps will differ, but we recommend using UV as it's the easiest way to get it installed fast. Once installed, either navigate to your skill directory or run this command from anywhere. Your skill exists, it passes the validator, but Claude isn't using it when expected. H well, the cause is almost always the description. Cloud uses semantic matching, so your request needs to overlap with the description's meaning. If there's not enough overlap, no match. Check your description against how you're phrasing requests. Add trigger phrases users would actually say, test with variations. Help me profile this. Why is this slow? Make this faster. If any fail to trigger, add those keywords to your description. If your skill doesn't appear when you ask Claude what skills are available, well, check these things. Skills must be in the right location with the right structure. The skill.md file must be inside of a name directory, not at a skills root. The file name must be exactly skill.md. All caps on the skill lowerase MD. Just crossing things off the list here. Okay, just crossing them off. Run claude-debug to see loading errors. Look for messages mentioning your skill name. Sometimes this will just solve the problem for you. If Claude uses the wrong skill or seems confused, your descriptions are probably too similar. Make them distinct. Remember, being as specific as possible doesn't just help with Claude deciding when to use your skill, but not conflicting with other similar sounding skills. If your personal skill is being ignored, an enterprise or higher priority skill might have the same name. So investigate that. If you see an enterprise code review and you also have a personal code review, well the enterprise one will win every time. So your solutions is to rename your skill to something a little bit more distinct. Talk to your admin about the enterprise skill, but you'll have a better chance with number one. Probably install the plugin but can't see it. Skills? Well, clear the cache. Restart claw code and reinstall. If skills still don't appear, the plug-in structure just might be wrong. This is when the validator tool makes sense. The skill loads but fails during execution. If your skill uses external packages, they must be installed. Add this info to your description. Scripts need execute permission. Use for slashes everywhere, even on Windows. So, here's a quick checklist. Not triggering? Well, improve your description and trigger phrases. Not loading? Check your path, file name, YAML syntax. Wrong skill [music] used? Make your descriptions a little bit more distinct. Are you being shadowed? Check the priority and rename if needed. Plugins are missing. Clear your cache and reinstall. Runtime failure? Check dependencies, permissions, and pass.
