<!-- https://anthropic.skilljar.com/claude-101/383396 -->

**Estimated time:** 15 minutes

### Learning objectives

By the end of this lesson, you will be able to:

* Explain what Skills are and how Claude uses them
* Identify Anthropic's built-in Skills for document creation
* Enable and manage Skills in your settings

---

> **Plan availability:** Skills are currently a feature preview for Pro, Max, Team, and Enterprise plans. If you're on the Free plan, you can read along to understand the concept and skip the hands-on steps.

### What are Skills?

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Think of them as expertise packages—they teach Claude how to complete specific tasks in a repeatable way.

You've already seen Skills at work if you've used Claude to create Excel spreadsheets, PowerPoint presentations, Word documents, or PDFs. Those file creation capabilities are powered by Skills running behind the scenes. But Skills go far beyond document creation. Custom Skills can codify entire repeatable workflows — a quarterly variance analysis methodology, a brand voice review process, or a compliance checklist — so Claude follows the same rigorous steps every time.

### Types of Skills

There are two categories of Skills you'll encounter:

* **Anthropic Skills** are created and maintained by Anthropic. These include enhanced document creation capabilities for Excel, Word, PowerPoint, and PDF files. Anthropic Skills are available to all paid users and Claude invokes them automatically when relevant—you don't need to do anything special to use them.
* **Custom Skills** are ones you or your organization create for specialized workflows and domain-specific tasks. For example, you might create a skill that applies your company's brand guidelines to presentations, structures meeting notes in a specific format, or executes your organization's data analysis workflows.

### Enabling Skills

Skills are currently available as a feature preview for users on Pro, Max, Team, and Enterprise plans. To use Skills, you'll need to have Code execution and file creation enabled, since Skills require Claude's secure sandboxed computing environment to function.

Here's how to enable Skills:

1. Navigate to **Settings > Capabilities**
2. Ensure that **Code execution and file creation** is toggled on
3. Scroll to the **Skills** section
4. Toggle individual skills on or off as needed

For **Enterprise plans**, organization Owners must first enable both Code execution and Skills in Admin settings before individual members can access them.

For **Team plans**, this feature preview is enabled by default at the organization level.

Once enabled, you'll see available Skills listed in your settings, including Anthropic's built-in Skills and any custom Skills you've uploaded.

### Using Skills in practice

The beauty of Skills is that you typically don't need to think about them—Claude handles skill selection automatically based on your request. Here are some examples of prompts that would invoke Skills:

* "Create an Excel spreadsheet tracking monthly expenses with formulas for totals"
* "Turn this meeting notes document into a PowerPoint presentation"
* "Generate a PDF report summarizing this data"
* "Build a financial model in Excel with scenario analysis"

When Claude uses a Skill, you'll see it mentioned in Claude's chain of thought as it works. The output will be a downloadable file you can save to your computer or directly to Google Drive.

### File execution

**Claude works with you on slides, spreadsheets, and contract redlines**

This same capability means that Claude can work with **your actual files** (within a contained environment) to create updated versions of your files (note: in Chat, Claude creates a new version of the document rather than editing the original in place). Upload slides, spreadsheets, contracts, (or any .xlsx, .pptx, .docx, or .pdf files) and watch as Claude creates slides, performs analyses, and adds suggested edits. When Claude is done, you can download these files or open them in Drive.

Note: To use these capabilities you'll need to give Claude access to external data sources. Simply toggle Allow limited network access on when prompted:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789944703/e9af099affd9b52e18cf9decd373/8ecc03cc-e50b-43b0-8694-c500638cb781?expires=1765910700&signature=09ecdf26fa5bf37cc61b9b9d921a5dc240d882f68a5cb008c2b306d67be06f3f&req=dScvH8B6mYZfWvMW1HO4zYwjyHsgM4gXNv1GpC923dkWEbTC23XmsD7tF%2FZ%2B%0AoqVGyu8SDXplXHIQX7g%3D%0A)

#### Security considerations

Because Skills can include executable code, it's important to use them thoughtfully:

* Only install custom Skills from trusted sources
* Anthropic's built-in Skills are tested and maintained by Anthropic
* Custom Skills you upload are private to your individual account
* If you're installing a custom Skill from an external source, review its contents before use to understand what it does.

### Creating custom skills

While Anthropic's built-in Skills cover common document creation tasks, the real power of Skills comes from creating your own. Custom Skills let you teach Claude your specific workflows, brand guidelines, and ways of working—so Claude can apply that knowledge automatically whenever it's relevant.

The easiest way to create a custom Skill is through conversation with Claude itself. You don't need to write code or manually create files—Claude handles the technical structure for you.

Here's how to create a Skill through conversation:

1. **Start a new chat** and tell Claude what you want to create. For example: "I want to create a skill for writing quarterly business reviews" or "I need a skill that applies our brand guidelines to presentations."
2. **Answer Claude's questions.** Claude will interview you about your workflow, asking things like: What should this skill do? What makes good output for this type of work? Can you give examples of when you'd use this skill?
3. **Upload reference materials** if you have them. Templates, style guides, brand assets, or examples of work you're proud of all help Claude understand exactly what you're looking for.
4. **Save your skill.** When finished, Claude generates a file containing your properly structured skill. All you have to do is save it and the skill will be ready for Claude to use.

**See your skills.** Find the Customize tab in the left sidebar. There you can see all of the skills that are available to you and even edit the skills you use manually or by chatting with Claude.

Your custom Skill will appear in your Skills list alongside Anthropic's built-in Skills. From that point forward, Claude will automatically invoke it whenever you work on relevant tasks—no manual triggering needed. You can improve your skills with iteration — ask Claude to edit a skill and it will update the files for you.

### Skills vs. Projects

You might be wondering—if both skills and projects can be used to give more context to Claude, when should I use each? Think of it this way: **projects store knowledge, skills perform tasks**.

**Projects** are knowledge hubs. They hold the reference materials Claude needs to understand your work—project specs, meeting notes, research documents. When you upload files to a project, Claude draws on that information across every conversation within that project.

**Skills** are procedural machines. They encode *how* Claude should execute a task—the specific steps, order of operations, and methodology you want followed every time. Skills shine when you have repeatable workflows you want Claude to run consistently.

The two features complement each other. A skill can reference knowledge stored in a project—your "customer call prep" skill might pull from customer profiles uploaded to a project's knowledge base. The project provides the *what* (information), the skill provides the *how* (process).

|  | Projects | Skills |
| --- | --- | --- |
| **Purpose** | Store knowledge Claude references | Define processes Claude executes |
| **Best for** | Long-term context, reference materials, team collaboration | Repeatable workflows, multi-step tasks, consistent methodology |
| **Example** | Customer hub, research buddy, feedback generator | Process guidelines (like brand or legal), Blog drafting, PDF creation |
| **Persistence** | Knowledge available across all chats in the project | Instructions applied when the skill is invoked |

### Lesson reflection

Before moving on, consider:

* What types of documents do you create regularly that could benefit from Claude's built-in Skills?
* Are there repetitive workflows in your work that might be good candidates for custom Skills?
* How might Skills change the way you think about document creation and data analysis?

### What's next

In the next set of lessons, you'll start to expand Claude's reach with connectors. These powerful tools make information gathering seamless, and can give Claude the ability to perform actions right inside the tools where your work is happening.

For more information on Skills, including how to create your own custom Skills, visit the [Anthropic Help Center](https://support.claude.com/en/articles/12512176-what-are-skills).

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback [here](https://forms.gle/sY9ou5fqZBd3TjHF8).

#### Acknowledgments and license

*Copyright 2025 Anthropic. All rights reserved.*
