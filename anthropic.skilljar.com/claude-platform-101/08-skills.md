<!-- https://anthropic.skilljar.com/claude-platform-101/486259 -->
<!-- youtube: 3fGaS8mcD9Q -->

# Skills

[![Skills](https://img.youtube.com/vi/3fGaS8mcD9Q/hqdefault.jpg)](https://www.youtube.com/watch?v=3fGaS8mcD9Q)

<details>
<summary>자막: Skills</summary>

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. And incorporating these skills in your agent loop is easy. A skill is a package set of instructions, a skill.md file, optionally with helper files, that you upload once and then attach to any messages.create call. You're teaching Claude how you do something. Your status report format, your review checklist, your release notes. Claude reads the skill, follows the procedure, and produces output in your shape. But it's worth knowing a skill versus a tool. Tools connect Claude to data and actions. Look up this code section, send this email. Claude calls it and something else runs. Skills teach Claude a procedure. Generate the daily status report following this template. It's a playbook Claude reads and follows, which sometimes means running bundle scripts itself. Tools are about what Claude can do, while skills are about how you want it done. And taking into consideration that skills also don't load all into context on startup. It only does the name and description, so that when your agent decides when to use the skill, it will then load it into context. Skills are uploaded once to your workspace, then referenced by ID. You can either upload this directly on the Claude platform, or you can do it programmatically. Like I did here. Now, I want a status report generator. The rules for what makes a good status report, sections, tone, how to summarize, blockers, live in a skill-like package ahead of time. The activity log itself is just a string that I'm passing in. A few things worth pointing out is that we're calling the client.beta.messages.create, not the standard one, and passing the skills into the beta's header. As of this video, skills are still a beta feature. Container.skills is where the skill attaches, a list, so you can layer multiple skills onto one call. And I've also turned on code execution here. Skills often pair well with code execution because the skill procedures can do real work like in your terminal. So, let's run it. The output is a status report formatted exactly the way the skill said to format it. Sections, tone, blogger handlings, all coming from the skill.md file that you uploaded. The user prompt is one line, the procedure lives in the skill. And so, in a production app, this is how a team would standardize output across an entire feature. So, with this daily status report endpoint, every PM gets the same structure, the same tone, the same sections, and the same order without anyone copy-pasting a template into a prompt.
>> [music]
>> Skills package your procedures.
Upload once with the client.beta.skills.create endpoint, attach with container.skills on any messages.create call, and then use them when the how matters as much as the what.

</details>
