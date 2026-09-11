<!-- source: https://academy.claude.com/tutorials/discernment-toolkit -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Anthropic Education Report: How people check Claude's work

We asked 129 Claude Academy participants what discernment looks like when they work with Claude. Checking Claude's work usually means verifying it against something external, lack of domain expertise is the biggest barrier, and errors caught too late spur new discernment habits.

10 min

![](https://academy.claude.com/assets/v1/thumbnail.light-cu6wjiio.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-omuj02iu.png)

For many, learning to use AI starts with learning the tool itself. People often begin with questions like: *How do I describe what I need to Claude? How do I safely give Claude the files and data it needs to do a good job?* But as Claude is used for bigger and more complex tasks, a harder question surfaces: **how do I know if Claude is right?**

Discernment, or the accuracy and relevance of AI's outputs, is one of the most critical aspects of AI fluency. Yet it's harder to study directly because it can happen beyond the confines of an AI tool.

And so, with the help of [Anthropic Interviewer(opens in new tab)](https://www.anthropic.com/research/anthropic-interviewer), we asked 129 Claude Academy participants: **what does discernment look like when you’re working with Claude?** People shared their stories about recent work they did with Claude, including how they vetted Claude’s quality and accuracy.1

We learned a lot, but three big themes emerged. First, "checking Claude’s work" most often meant verification against something external to the conversation—sources, documents, tests, other people, or another AI. Second, the biggest barrier to discernment was not time pressure but lack of domain expertise. And, third, when Claude’s errors were caught too late, it often prompted people to adopt new and creative discernment behaviors.

These stories help us understand the habits that power users have developed so we can build our own discernment toolkits. Most respondents in this study use Claude daily for six months or longer.2 This is well above the general population, which is useful for cataloging good practice and a limitation for anything else. We make no prevalence claims beyond this sample.

## Key insights[](#key-insights)

Across all of the interviews, we found three notable patterns:

* Checking Claude’s outputs usually involves validation against external sources
* Expertise is the biggest barrier to discernment
* Errors that slip through the cracks can spur the adoption of creative, new discernment behaviors

### Checking Claude’s work against an external source of truth was the most commonly reported discernment practice[](#checking-claudes-work-against-an-external-source-of-truth-was-the-most-commonly-reported-discernment-practice)

We expected "checking Claude’s work" to mostly be described as a read-through for obvious errors. However, 51% of the participants we interviewed described verifying Claude's output against something external: source documents, official docs, their own data, another person, or even another AI. 10% of the checkers went even further, combining several independent checks together. A read-through without any external validation was the minority practice, especially if the task was technical.

What "external source of truth" meant depended on the work. When the task involved code, tests were usually involved. Research and analysis tasks leaned on cross-checks against sources and second opinions. 10 accounts described using a second AI to check the first's work for nuanced knowledge work tasks. Writing tasks leaned on domain knowledge and a careful read by a peer for fit. Different work required different methods.

### Expertise was the biggest barrier to discernment[](#expertise-was-the-biggest-barrier-to-discernment)

AI empowers people to expand their capabilities, which means they're often doing work outside their direct area of expertise. That's where these participants found discernment challenging: it's difficult to judge an answer when you’re not sure what good looks like.

Sixty-two participants named a barrier to discernment. Lack of subject matter expertise topped the list. Some non-technical participants described Claude leading them through solutions involving software-development, where they couldn't tell good code or architecture decisions from bad ones. One learner even turned to online gardening videos to build up just enough domain knowledge to evaluate Claude's recommendations.

We had expected time pressure to top this list. For this group, the bottleneck was having enough subject matter expertise to evaluate the quality of the output.

![Horizontal bar chart titled 'What makes judging AI output hard' showing the barriers to discernment participants named, with the share and count of participants naming each, the top bar drawn in a darker highlight color: lack of domain/technical expertise 23% (14); AI resource/usage limits (context windows, truncation, caps) 19% (12); context and prompting gaps 13% (8); lack of verification resources 11% (7); own volume/time pressure 10% (6); confident tone masking quality 10% (6); trust in the AI's process 10% (6); subtle errors and ambiguous correctness 8% (5); subjective tone and style fit 6% (4).](https://academy.claude.com/assets/v1/7946eb8fd7ff-exfaw8em.png)

### Letting an error slip through changed how people work[](#letting-an-error-slip-through-changed-how-people-work)

Across all interviews, there were 18 meaningful accounts of missing an error Claude had made. Half of the people who shared such a story also told us it changed how they work today. Seeing the mistake taught them how to look for future ones.

Some of the new practices these participants adopted included:

* Requiring Claude to quote its source text first, before offering a recommendation or analysis
* Creating approval gates at each step of a multi-step task, rather than reviewing only at the end
* Using multiple AI agents at once: one produces the work, others check different parts of it

For these participants, they didn’t “check their work harder” or become experts in a new field overnight. Instead, they restructured their workflows and refined their discernment toolkit.

## Building your discernment toolkit[](#building-your-discernment-toolkit)

The most confident discerners in this study had one thing in common: a good toolkit. As you start to use AI for more difficult and complex tasks, we highly recommend identifying a set of practices and workflows you can use to validate Claude’s work. Here are five tools to get you started.

1. **Build tests to validate the work products you create most often.** If you're not a software developer, you probably don't have "tests" for each piece of work you do. But the idea transfers to any field. If you’re a content writer, create rubrics for voice, tone, and format. If you’re a lawyer, define policies and rules you can use to check generated contract language. Try this prompt to iterate with Claude and create your own validation “test” as a reusable skill that can be shared with colleagues:

I want to make a reusable check for one kind of work I produce, so I can catch problems before it goes out. Think of it as my own QA checklist.

Before you write anything, ask me four or five short questions in one round: what the work product is and who reads it; what a great version does that an okay one doesn't; how these usually go wrong, including feedback I've received or mistakes I caught late; and what I'd be most embarrassed to get wrong. If I give you an example of a good one, read it before drafting.

Then turn my answers into a check of five to eight questions I can ask of any future draft, whether I wrote it, you wrote it, or we wrote it together. Put the most important question first. Make every question specific to my work rather than general writing advice, and make sure the check helps me catch wrong facts or numbers, reasoning or claims I couldn't defend if challenged, context the reader needs that isn't on the page, and a tone that won't land with this audience. Don't add numbers, thresholds, or rules I didn't give you.

Deliver the check as a skill, not as text in the chat. The skill should accept a draft as pasted text, a file, or a doc link, run every question in order, and quote the exact lines in the draft that decide each one.

The skill's output should be a visual scorecard published as an artifact, not a text report: a verdict at the top naming the single most important fix, a one-row strip showing every question's status at a glance (pass, fail, flagged), and then one row per question with the status, the quoted line, and one concrete fix. The chat reply after a run should be two lines, the verdict and the counts. Show me the skill for review, then run it once on my example so I can see the scorecard.

Open in Claude

2. **Let Claude help you identify opportunities for discernment before you leave the chat.** Anthropic has published a discernment skill that detects complex tasks and prompts Claude to offer nudges for further validation. After testing this skill with a few enterprises, directional evidence suggests inserting pauses into your workflow increases discernment. Here's an example of what the skill put into chat after the user asked for a report on workers in the City of Philadelphia:

![Screenshot of a 'Pause and reflect' card that the discernment-nudge skill added to a Claude chat, listing three follow-up questions about a report on workers in the City of Philadelphia: how the 45% knowledge-worker share would change if office and sales roles were included and which definition to use; where mixing city ACS counts with metro BLS wages and growth could mislead a reader; and how different the picture would look using place-of-work data, since ACS counts residents, not jobs.](https://academy.claude.com/assets/v1/d4892c8e13f3-dypzmxl9.png)

*(An example of the discernment-nudge skill triggering after completing a report on workers in the City of Philadelphia)*

You can install the discernment-nudge skill by asking Claude here:

Please install this .md file as a skill:

[https://raw.githubusercontent.com/anthropics/skills/refs/heads/main/skills/discernment-nudge/SKILL.md(opens in new tab)](https://raw.githubusercontent.com/anthropics/skills/refs/heads/main/skills/discernment-nudge/SKILL.md)

Open in Claude

3. **Use adversarial review in Claude Code.** Claude Code offers a [built-in adversarial review(opens in new tab)](https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step) step. This means that Claude is able to spin up a fresh subagent to review your code or work product from a new perspective. Using an agent that hasn’t been involved in constructing the output means it's more likely to catch errors or dangerous assumptions.

Use a subagent to review the rate limiter diff against PLAN.md. Check that
every requirement is implemented, the listed edge cases have tests, and
nothing outside the task's scope changed. Report gaps, not style preferences.

Open in Claude Code

4. **Build a panel of experts.** The biggest named barrier to discernment was lacking expertise in the subject at hand. Identifying people you can call for a secondary check expands your options. Knowing who you'd call for a second read in the domains outside your expertise, and reach out before you ship. Then, of course, return the favor. When a colleague brings you something in your area of expertise, your five minutes is what makes their discernment possible.

Try this prompt to iterate with Claude about who might help you discern your outputs, based on your recent email exchanges:

I want to set up a "phone a friend" check. Before I rely on a piece of work, you'll help me find the right people in my own network to judge it. Walk me through this one step at a time, and wait for my answer before moving on.

Step 1: Check whether my email is connected. If it isn't, give me step-by-step instructions to connect it, then wait until I tell you it's done. Don't guess at names.

Step 2: Ask me for the piece of work. I can upload it, paste the text, or paste a link to it. If I say it came from an earlier chat with you, search my past chats for it; if you can't, tell me how to turn on "Search and reference chats" in my settings, or ask me to paste it instead.

Step 3: Tell me in one line what it's about and what kind of expertise it would take to judge whether it's good.

Step 4: Search my email for people with that expertise: people I've gone back and forth with on this topic, people who get copied on it, people who've answered my questions about it, or who own the decision it feeds into.

Step 5: Suggest 2–4 people. For each, give a one-line reason based on what you found in my email, and a short message I could send asking them to look at it.

Prefer people who know the subject and will push back over people I simply email a lot. Don't contact anyone for me, and don't quote my emails in the suggested notes; I'll reach out myself.

Open in Claude

5. **Ask Claude for source grounding.** Checking Claude’s work against an external source was a go-to practice. You can have Claude make this work easier for you by having Claude cite the sources for each claim in the response. With those sources in hand, you can quickly check what holds up and what might require additional research on your part.

Try this prompt in your conversation after you’ve generated an output with Claude:

For each factual claim in your answer, tell me where it came from. Quote the exact passage from the source and include the link or page number. If a claim comes from your general knowledge, label it "unsourced" so I know what to check first.

Open in Claude

## Limitations[](#limitations)

These insights come with important caveats:

* **Sample limitations:** Academy registrants are self-selected, motivated participants who opted into getting better at working with AI; their practices likely sit above a general-population baseline. The sample (129 interviews, 94 complete) skews experienced and technical, so newer users' discernment challenges are underrepresented. These accounts should be understood as a catalog of practice in this population, not a universal benchmark, and we make no prevalence claims about AI users broadly.
* **Self-report:** All data is self-report. We prioritized the "walk me through it" accounts of real work and treated structured ratings as descriptive context. Recall of "a time something slipped through" is subject to availability bias: dramatic failures are likely over-represented versus more forgettable ones.
* **Coding limitations:** Thematic coding was LLM-assisted. We mitigated this with exact per-theme transcript lists retained for audit, deterministic (rule-based) cross-validation of the structured module, a human review of at least 10% of every theme, and a full re-code of every affected dimension after rubric revision.

## Looking ahead[](#looking-ahead)

This study captured stories and themes from motivated power users about how they check Claude’s work. Our intent was to expand our understanding of how discernment develops and what tactics work well in practice.

In future work, we plan to extend this through intervention studies measuring the impact of the discernment skill on organizations and growing the "tests for your field" idea into a shared, role-specific library of checks that everyone can adopt and contribute to.

We expect discernment to evolve as models produce increasingly polished output. With this and future studies, we aim to make that evolution visible and provide educational tools for everyone to use.

## Bibtex[](#bibtex)

If you'd like to cite this post, you can use the following Bibtex key:

text

```
@online{swanson2026aidiscernment,
author = {Kristen Swanson and Maggie Vo and Zoe Ludwig and Jeff Olson and Matt Gallivan and Erik Olesund and Rick Dakan and Joe Feller},
title = {Anthropic Education Report: How people check Claude's work},
date = {2026-09-10},
year = {2026},
url = {https://academy.claude.com/tutorials/discernment-toolkit},
}
```

## Acknowledgements[](#acknowledgements)

Kristen Swanson designed the research, led the analysis, and wrote this report with feedback from Matt Gallivan, Jeff Olson, and Erik Olesund. Maggie Vo and Zoe Ludwig contributed to framework alignment, messaging, and review. The 4D Framework for AI Fluency was developed by Rick Dakan and Joe Feller in partnership with Anthropic. Mo Julapalli and Ankit Siva provided technical support. Ryan Donegan and Molly Vorwerck provided communications review and guidance.

## Footnotes[](#footnotes)

1. When researching how people describe their AI use, protecting participant privacy is paramount. Interviews were conducted by [Anthropic Interviewer(opens in new tab)](https://www.anthropic.com/research/anthropic-interviewer), a qualitative interviewer powered by Claude, under its standard consent flow; responses were not linked to a user’s Claude Academy account, course progress, or Claude.ai conversation data. No personally identifiable information appears in this analysis. Everyone who registered for an AI Fluency course in Claude Academy during the fielding window received a note in their registration email offering an optional research conversation. Participation was uncompensated and separate from course enrollment. Of the 129 participants who started an interview, 94 fully completed it, including the survey module. Open-ended accounts were analyzed from all 129 transcripts, since partial interviews frequently contained a meaningful work story, while survey figures are based on the subset who reached the survey (n=95–98 depending on item). Thematic coding ran as follows: an LLM coded the full corpus against the research questions, with the exact list of transcripts behind every theme retained for audit. The survey module was parsed deterministically. Then, a human evaluator then reviewed at least 10% of every theme to identify coding inconsistencies. The coding rubric was edited based on that review and every affected dimension was re-coded in full against the revised rubric. All new coded data sets were again reviewed and analyzed by a human. This paper was fully written by a human and revised with the help of AI.
2. From the survey module (n=95): 63 of 95 respondents reported daily use, and 62 of 95 reported six or more months of experience with AI tools. Respondents' self-rated confidence was highest for knowing when to verify (mean 3.9 on a 5-point scale) and lowest for judging completeness (3.5), with judging correctness in between (3.7). This is consistent with the findings about discernment barriers: participants broadly know verification is called for and the hard part is doing it outside their expertise.

* [Key insights](#key-insights)
* [Building your discernment toolkit](#building-your-discernment-toolkit)
* [Limitations](#limitations)
* [Looking ahead](#looking-ahead)
* [Bibtex](#bibtex)
* [Acknowledgements](#acknowledgements)
* [Footnotes](#footnotes)
