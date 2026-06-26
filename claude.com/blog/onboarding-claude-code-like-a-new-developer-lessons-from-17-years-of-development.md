<!-- source: https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

# Onboarding Claude Code like a new developer: Lessons from 17 years of development

The methodology that onboards new developers to MacCoss Lab's 700,000-line codebase works on Claude Code, too. Here's how Brendan MacLean, a Claude Developer Ambassador whose lab is part of our [Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) program, did it.

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  April 28, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development

[Skyline](https://skyline.ms/home/software/Skyline/wiki-page.view?name=team), the open source protein analysis software maintained by principal developer Brendan MacLean at the University of Washington's MacCoss Lab, has been in active development since 2008. Skyline helps researchers detect and quantify proteins in things like blood plasma and tissue, which is vital for biomarker discovery, disease research, and drug development. The MacCoss Lab codebase contains 700,000+ lines of C#, maintained for 17 years by a small team running 200,000+ automated nightly tests.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef9d6a1af11e710950d666_e16f087b.png)

*A 3D illustration of the Seattle skyline created in Blender, representing the home of the University of Washington's MacCoss Lab, where Brendan MacLean and his team have developed and maintained Skyline since 2008. Claude helped Brendan add the Claude logo in the back. Image courtesy of MacCoss lab.*

For nearly three decades, Brendan has been Skyline’s connective tissue, onboarding dozens of undergrads, grad students, and postdocs to the lab.\*

As developers joined and left, the codebase absorbed their contributions. By 2024, it carried the usual burdens of a long-lived project. Certain areas had grown untouchable as developers turned over.

After decades of training lab members, Brendan knew how to bring researchers up to speed on the lab’s massive codebase. What he didn't expect was that the same methodology, applied to an AI tool, would make Skyline’s codebase manageable again.

## The same onboarding problem, a different kind of developer

Brendan was skeptical modern AI coding tools could understand lines of C# the way a tool purpose-built for exactly this language and environment already did.

Early experiments with Claude.ai in the browser confirmed the pattern. He'd describe a problem, get a response, and copy a whole C# file back into his project, limiting scope to contained problems he could describe without any reference to project code.

"It became very laborious once changes became more incremental," Brendan says.

Every session with Claude.ai felt like starting from scratch as it had no understanding of what Skyline was, how its components related, or what 17 years of development had established.

That was the same experience Brendan faced onboarding new developers, which gave him an idea.

"I could introduce Claude through Claude Code to my large project as I would a trainee developer: by explaining enough to achieve a successful limited project and produce improved context for the next iteration," Brendan says.

He moved all AI context into its own repository, [pwiz-ai](https://github.com/ProteoWizard/pwiz-ai), kept separate from the codebase so it applies across all branches and time points. The `CLAUDE.md` file at the root handles environment setup and points Claude to the relevant documentation: think of it as the ‘lay of the land,’ not the expertise itself.

The expertise lives in [skills,](https://agentskills.io/home) an open format for giving agents capabilities and expertise. His `debugging` skill, for example, is designed to pull Claude out of what he calls "guess and test" mode, pushing it toward root cause analysis before attempting any fix. Skills can be triggered manually or automatically; Brendan tunes his most critical ones with explicit conditions—the `debugging` skill description reads "ALWAYS load when investigating bugs, failures, or unexpected behavior."

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef9d6a1af11e710950d669_24e72102.png)

*The pwiz-ai repository structure, showing how context, skills, and MCP integrations connect to Skyline's codebase. Image courtesy of MacCoss lab.*

With context established, the overhead of teaching Claude the ins and outs of debugging the codebase becomes significantly less steep. Claude already knows what the code does. The interaction starts from understanding rather than from zero.

“What seemed like a major concern—'Claude can't truly learn about my large project'—grows ever clearer: context is just another artifact to maintain and grow,” Brendan says.

## Reducing tech debt and accelerating development

A year-long project to build a Files View panel in Skyline—a new interface showing all document-related files, with file system monitoring and drag-and-drop organization— sat unfinished after the developer who owned it left. Brendan picked it up with Claude Code.

Two weeks later it was done, with all final commits co-authored by Claude.

"Prior efforts left in that shape have typically ended up being discarded," says Brendan. In an academic lab, developers rotate often—grad students finish degrees, postdocs move on, interns leave at the end of summer. In the past, any work-in-progress would have remained forever shelved.

Three years ago, Brendan stopped adding features to Skyline's nightly test management module after losing the developer who maintained it. The module was coded in Java as part of the LabKey Server scientific data web portal. Recently, after having a skilled LabKey developer create setup documentation using Claude Code, Brendan spent less than a day adding features he'd wanted for years and updating the page layout with CSS he had only ever employed designers to produce in the past.

New infrastructure followed.

Screenshot reproduction for Skyline's 2,000+ tutorial images is now fully automated and nearly 100% reproducible, extended with Claude Code to add diff-only views and pixel change amplification, and an MCP server written in C# by Claude so that it can “see” these diffs. Claude Code generates a daily summary each morning, showing test failures, exceptions, and open support threads pulled from Skyline's nightly test infrastructure that lands in Brendan's inbox before he sits down to work.

Claude also wrote the MCP server in Python to make this capability possible, drawing from three separate relational data streams on a LabKey Server, team email, and code with release tags on GitHub.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef9d6a1af11e710950d66f_29befb00.png)

*A daily summary email generated automatically by Claude Code, pulling from Skyline's nightly test infrastructure. Image courtesy of MacCoss lab.*

Brendan's developers are now barely writing code themselves, largely instructing Claude Code instead, and use the tool to autonomously generate  automation scripts and MCP implementations. For instance, a developer in the lab who had been skeptical of agentic coding tools built and shipped a new plotting extension—a mobilogram pane for visualizing ion mobility data—and credited Claude Code.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef9d6a1af11e710950d66c_0712da57.png)

*The mobilogram pane was built with Claude Code, visualizing ion mobility data alongside mass spectrometry results. Image courtesy of MacCoss lab.*

"I am seeing almost everyone taking on fun new features that they might have felt too buried in other work to attempt," says Brendan.

## Advice for developers working on legacy codebases

Based on 17 years of onboarding developers and more than a year of applying the same methodology to Claude Code, here's what Brendan would tell developers working on legacy codebases.

**Context is your best friend**

The to-do lists and plans Claude generates don't persist across sessions. [Context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) is what persists, and it has to be maintained deliberately. This is the part most developers skip, and it's why most developer success plateaus.

"Understand that Claude can't learn without you recording ‘context.’ Don't expect magic,” says Brendan. “Invest in building and maintaining your context layer. And treat it like any other project artifact: version it, grow it, maintain it.”

Brendan keeps the AI context in a separate repository because it grows at a different speed than the code and applies to all branches and time points—keeping it inside the code repository was becoming limiting. Keeping context in the same repo is a valid alternative; what matters is that it's versioned, maintained, and available when needed.

**Invest in building your skill library**

Use [skills](https://claude.ai/skills) to encode domain knowledge any Claude instance can load. Brendan's skills follow a "reference do not embed" principle: each skill points into a central documentation knowledgebase rather than duplicating content, keeping them lightweight and easy to maintain.

His most-used include: a`skyline-development`skill that orients Claude to the project and its documentation; a `version-control`skill that encodes project-specific commit and PR conventions; and a`debugging`skill designed to pull Claude out of "guess and test" mode, pushing it toward root cause analysis before attempting any fix.

**Use MCP integrations when data access is key**  
Build [MCP integrations](https://anthropic.com/engineering/mcp) where Claude needs access to real data: test results, exception reports, support threads.

For open source projects, building and maintaining a context layer carries particular weight. There's no onboarding budget, no institutional memory beyond what gets written down, no guarantee that any contributor will still be around next year. Context, once built, is available to every contributor and persists across the project's lifetime in a way that human institutional knowledge never does. The `pwiz-ai` repository is itself an open source artifact—context that belongs to the project, not any one contributor, and outlasts everyone who built it.

## Seventeen years of onboarding, one conclusion

You wouldn't hand a new hire a 700,000-line codebase and expect results on day one. You'd find them a contained project, walk them through it, and expand their scope as their understanding grew.

As Brendan learned, the context you build with Claude works the same way.

Once knowledgeable enough about a codebase, engineers can work across branches and time points. Claude, given sufficient context and direction, can do the same.

*\*Dario Amodei, co-founder of Anthropic, was previously a member of the MacCoss Lab.*

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

Get Claude Code

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code

Health care and life sciences

Coding
