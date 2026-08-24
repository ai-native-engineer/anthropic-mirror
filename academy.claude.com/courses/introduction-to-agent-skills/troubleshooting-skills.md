<!-- source: https://academy.claude.com/courses/introduction-to-agent-skills/troubleshooting-skills -->

Lesson 6 of 6 · Introduction to agent skillsTroubleshooting skills

## Troubleshooting skills

Loading

Troubleshooting skills · 4 min

When skills don't work as expected, the problem usually falls into a few
predictable categories. This video walks through each one — from skills
that don't trigger to priority conflicts to runtime failures — and gives
you a systematic troubleshooting approach. You'll also learn about the
skills validator tool and how to use `claude --debug` to diagnose loading
issues.

## Key takeaways

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

![The skill priority hierarchy — Enterprise highlighted above Personal, Project, and Plugins — alongside the managed-settings.json file name](https://academy.claude.com/assets/media/75bd17ace918ad6549313137a838e24a2767a349914def59ee6edf0be1bf5972.png)

For example, if there's an enterprise "code-review" skill and you also have a personal "code-review" skill, the enterprise one wins every time. Your options:

1. Rename your skill to something more distinct (this is usually the easier path)
2. Talk to your admin about the enterprise skill

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
