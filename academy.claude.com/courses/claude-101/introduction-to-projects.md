<!-- source: https://academy.claude.com/courses/claude-101/introduction-to-projects -->

Lesson 5 of 13 · Claude 101Introduction to projects

3. /[Claude 101](https://academy.claude.com/courses/claude-101)

[Claude 101](https://academy.claude.com/courses/claude-101)

# Introduction to projects

Lesson 515 min

In this lessonBy the end, you’ll be able to

* Explain what projects are and when to use them
* Create a new project with a name, description, and visibility settings
* Add documents and files to your project's knowledge base
* Write effective project instructions to guide Claude's behavior
* Share projects with teammates (for Claude for Work (Team and Enterprise plan) users)

## Video

## Key takeaways

* **Projects are self-contained workspaces** with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.
* **Project knowledge enhances Claude's understanding** by letting you upload relevant documents that Claude references across all chats within that project. No more re-uploading the same files each time.
* **Project instructions guide Claude's behavior**—you can specify tone, expertise level, response style, and more. These instructions apply to every conversation within the project.
* **Projects scale automatically.** When your knowledge base approaches context limits, Claude switches to searching your project knowledge and pulling in only what's relevant, expanding capacity by up to 10x while maintaining response quality.
* **For Claude for Work users, projects enable collaboration.** Share projects with teammates so everyone benefits from the same context, instructions, and accumulated knowledge.

## What are Projects?

Projects are ideal for storing knowledge Claude should reference, organizing related chats around a specific topic or work area, and collaborating with team members who need access to the same shared context.

### When to use Projects

Projects are particularly valuable when you're working on something ongoing—not just a one-off question. Consider creating a project when you have a workflow with:

* **Reference materials you'll use repeatedly** (meeting notes, survey results, reports, historical data, etc.)
* **Consistent requirements** for how Claude should respond (always use formal language, always cite sources, always follow our template)
* **Team collaboration needs** where multiple people should work from the same foundation

## Creating your first project

Setting up a project takes just a few minutes. Here's how to get started:

### Step 1: Set up your project

1. Hover over the left sidebar and click "Projects," or navigate directly to claude.ai/projects
2. Click "+ New Project" in the upper right corner
3. Give your project a descriptive name (e.g., "Q4 Marketing Campaign" or "Product Documentation")
4. Add a brief description of what you're working on. While Claude doesn't see this description directly, it helps you and your teammates understand the project's purpose.
5. Choose your visibility settings: keep it private or share with your organization (for Claude for Work users)

### Step 2: Add project instructions

Project instructions tell Claude how to behave across all conversations in this project. Click on "Instructions" to open the instructions panel.

Good project instructions typically include:

* **Context about what you're working on:** "This project is for creating marketing content for our B2B software product."
* **Process instructions:** "First consider a blog structure that will entice this audience, then write the draft."
* **Tone and style preferences:** "Use a professional but conversational tone. Avoid jargon when possible."
* **Specific requirements:** "Always include a call-to-action at the end of marketing copy."

Once you've written your instructions, click "Save instructions." These will apply to every chat in this project and work alongside any user preferences and styles you've set.

You can also use project instructions to automate workflows — for example, "When I upload a meeting transcript, create a structured summary using this template." Think of instructions as programming Claude's behavior for this project.

### Step 3: Build your knowledge base

Your project's knowledge base is where you upload documents that Claude should reference. You'll find the files menu on the right side of your project's main page.

Click the "+" button to add content. You can upload various file types including PDF, DOCX, CSV, TXT, HTML, and more. You can also connect to Google Drive to link documents directly.

**What to upload:**

* Reference documents (brand guidelines, style guides, templates)
* Background materials (research reports, meeting notes, requirements docs)
* Examples of work you want Claude to emulate
* Technical documentation or specifications

Pro tip

Name your files descriptively. Claude uses file names to understand and
retrieve the right information, so "Q4-2024-Brand-Guidelines.pdf" is more
helpful than "document1.pdf."

### How projects handle large knowledge bases

You might wonder what happens when you upload a lot of content. Projects automatically scale to handle large amounts through a process called Retrieval Augmented Generation (RAG). At a high level, this means that Claude can automatically find and use the most relevant parts of your uploaded documents when answering, without you needing to tell it which file to look at.

When your project knowledge approaches the context window limit, Claude stops loading everything at once and instead searches your project's files, retrieving only what's relevant to your question. This expands your project's capacity by up to 10x while maintaining response quality.

You'll see a visual indicator when your project is RAG-enabled, but the experience should feel the same—you can still upload documents, chat with Claude, and get context-aware responses.

## Working within your project

Once your project is set up, you can start chatting with Claude. Each conversation within the project automatically has access to your knowledge base and follows your project instructions.

## Collaboration features

For users on Claude for Work (Team and Enterprise) plans, projects become even more powerful through collaboration features.

### Permission levels

When sharing a project, you can choose from three permission levels:

1. **Can view:** Members can see project contents, access knowledge, and chat—but can't make changes. Think of this as read-only access with discussion rights.
2. **Can edit:** Members have full collaboration power. They can modify instructions, update knowledge, manage other members, and actively contribute to the project.
3. **Owner:** Project creators control everything, including who sees the project. They can share with specific people or make projects visible to the entire organization.

### Sharing your project

To share a project:

* Open the project you want to share
* Click the "Share project" button to the right of the project name
* Add individual members using their name or email, or copy and paste a list of email addresses for bulk sharing (in this case, the project will show up in their "Shared with you" section)
* Or, share with "Everyone at [your organization]" to make your project discoverable within the Team tab

Team members will receive email notifications when you share a project with them, and they can find shared projects in their "Shared with me" tab.

## Example projects to inspire you

Not sure where to start? Here are some common project types across different functions:

* **Q4 product launch:** Upload your product specs, competitive analysis, and messaging brainstorming notes. Claude will have this context top of mind for any inquiry or document draft.
* **Research support:** Centralize your competitive review, user research data, and customer feedback. Claude can help you synthesize sources, draft reports, and maintain consistency across recommendations.
* **Client account hub:** Keep your client's brand guidelines, past deliverables, and communication history in one place. Set instructions so Claude matches their tone and references their specific context when creating proposals or reports.
* **Event planning workspace:** Upload venue contracts, speaker bios, and attendee data. Claude can help generate run-of-show documents, attendee communications, and post-event reports that stay consistent with your event's theme.
* **Job description generator:** Gather past job descriptions, team charters, and internal headcount request docs. Work with Claude to draft job descriptions that reflect your team's actual work and culture.

## Best practices for projects

To get the most out of projects:

* **Start focused, then expand.** Begin with a specific use case rather than trying to create one project for everything. You can always add more content as you go.
* **Keep your knowledge base current.** Outdated documents can lead to outdated responses. Review and update your project knowledge periodically.
* **Write clear instructions.** Be specific about what you want. Vague instructions lead to inconsistent results.
* **Name your documents descriptively.** (e.g., 'Q4-2025-Sales-Report.pdf' not 'report.pdf') and group related files together. Claude uses filenames and proximity to understand relationships between documents.
* **Reference documents by name.** When asking questions, you can mention specific documents to help Claude focus its search: "Based on our Q3 report, what were the top customer concerns?"

## Lesson reflection

Before moving on, consider:

* What ongoing work could benefit from having a dedicated project with persistent context?
* What documents do you expect you'll be re-uploading or re-explaining to Claude on a regular basis?
* If you're on a team, are there projects that would benefit from shared knowledge and instructions?

## What's next

In the next lesson, we'll learn how to create mini-apps with Artifacts — actual outputs that Claude build and you can share right away.

For more information on getting started with projects, visit the [Anthropic Help Center(opens in new tab)](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

[Previous lessonHow you'll work with Claude on your desktop](https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code)[Next lessonCreating with artifacts](https://academy.claude.com/courses/claude-101/creating-with-artifacts)

Lesson 5 of 13 · Claude 101Introduction to projects

Meet Claude

* [What is Claude?](https://academy.claude.com/courses/claude-101/what-is-claude)
* [Your first conversation with Claude](https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude)
* [Getting better results](https://academy.claude.com/courses/claude-101/getting-better-results)
* [How you'll work with Claude on your desktop](https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code)

Organizing your work and knowledge

* [Introduction to projects](https://academy.claude.com/courses/claude-101/introduction-to-projects)
* [Creating with artifacts](https://academy.claude.com/courses/claude-101/creating-with-artifacts)
* [Working with skills](https://academy.claude.com/courses/claude-101/working-with-skills)

Expanding Claude's reach

* [Connecting your tools](https://academy.claude.com/courses/claude-101/connecting-your-tools)
* [Enterprise search](https://academy.claude.com/courses/claude-101/enterprise-search)
* [Research for deep dives](https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives)

Putting it all together

* [Claude in action: use-cases by role](https://academy.claude.com/courses/claude-101/claude-in-action-use-cases-by-role)
* [Other ways to work with Claude](https://academy.claude.com/courses/claude-101/other-ways-to-work-with-claude)

Conclusion & badge

* [What's next?](https://academy.claude.com/courses/claude-101/what-s-next)
* [Course quizQuiz](https://academy.claude.com/courses/claude-101/certificate-of-completion)

* [Completion badge](https://academy.claude.com/courses/claude-101/badge)

* [Video](#video)
* [Key takeaways](#key-takeaways)
* [What are Projects?](#what-are-projects)
* [Creating your first project](#creating-your-first-project)
* [Working within your project](#working-within-your-project)
* [Collaboration features](#collaboration-features)
* [Example projects to inspire you](#example-projects-to-inspire-you)
* [Best practices for projects](#best-practices-for-projects)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
