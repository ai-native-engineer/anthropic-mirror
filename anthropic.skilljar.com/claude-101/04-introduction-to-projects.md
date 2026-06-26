<!-- https://anthropic.skilljar.com/claude-101/383393 -->

**Estimated time:** 20 minutes

### Learning objectives

By the end of this lesson, you will be able to:

* Explain what projects are and when to use them
* Create a new project with a name, description, and visibility settings
* Add documents and files to your project's knowledge base
* Write effective project instructions to guide Claude's behavior
* Share projects with teammates (for Claude for Work (Team and Enterprise plan) users)

---

### Video

[Video: Introduction to Projects - Getting started with projects in Claude.ai]

#### Key takeaways

* **Projects are self-contained workspaces** with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.
* **Project knowledge enhances Claude's understanding** by letting you upload relevant documents that Claude references across all chats within that project. No more re-uploading the same files each time.
* **Project instructions guide Claude's behavior**—you can specify tone, expertise level, response style, and more. These instructions apply to every conversation within the project.
* **Projects scale automatically.** When your knowledge base approaches context limits, Claude seamlessly enables Retrieval Augmented Generation (RAG) mode to expand capacity by up to 10x while maintaining response quality.
* **For Claude for Work users, projects enable collaboration.** Share projects with teammates so everyone benefits from the same context, instructions, and accumulated knowledge.

### What are Projects?

Projects are ideal for storing knowledge Claude should reference, organizing related chats around a specific topic or work area, and collaborating with team members who need access to the same shared context.

#### When to use Projects

Projects are particularly valuable when you're working on something ongoing—not just a one-off question. Consider creating a project when you have a workflow with:

* **Reference materials you'll use repeatedly** (meeting notes, survey results, reports, historical data, etc.)
* **Consistent requirements** for how Claude should respond (always use formal language, always cite sources, always follow our template)
* **Team collaboration needs** where multiple people should work from the same foundation

### Creating your first project

Setting up a project takes just a few minutes. Here's how to get started:

#### Step 1: Set up your project

1. Hover over the left sidebar and click "Projects," or navigate directly to claude.ai/projects 2. Click "+ New Project" in the upper right corner 3. Give your project a descriptive name (e.g., "Q4 Marketing Campaign" or "Product Documentation") 4. Add a brief description of what you're working on. While Claude doesn't see this description directly, it helps you and your teammates understand the project's purpose. 5. Choose your visibility settings: keep it private or share with your organization (for Claude for Work users)

#### Step 2: Add project instructions

Project instructions tell Claude how to behave across all conversations in this project. Click on "Instructions" to open the instructions panel.

Good project instructions typically include:

* **Context about what you're working on:** "This project is for creating marketing content for our B2B software product."
* **Process instructions:** "First consider a blog structure that will entice this audience, then write the draft."
* **Tone and style preferences:** "Use a professional but conversational tone. Avoid jargon when possible."
* **Specific requirements:** "Always include a call-to-action at the end of marketing copy."

Once you've written your instructions, click "Save instructions." These will apply to every chat in this project and work alongside any user preferences and styles you've set.

You can also use project instructions to automate workflows — for example, "When I upload a meeting transcript, create a structured summary using this template." Think of instructions as programming Claude's behavior for this project.

#### Step 3: Build your knowledge base

Your project's knowledge base is where you upload documents that Claude should reference. You'll find the files menu on the right side of your project's main page.

Click the "+" button to add content. You can upload various file types including PDF, DOCX, CSV, TXT, HTML, and more. You can also connect to Google Drive to link documents directly.

**What to upload:**

* Reference documents (brand guidelines, style guides, templates)
* Background materials (research reports, meeting notes, requirements docs)
* Examples of work you want Claude to emulate
* Technical documentation or specifications

**Pro tip:** Name your files descriptively. Claude uses file names to understand and retrieve the right information, so "Q4-2024-Brand-Guidelines.pdf" is more helpful than "document1.pdf."

#### How projects handle large knowledge bases

You might wonder what happens when you upload a lot of content. Projects automatically scale to handle large amounts through a process called Retrieval Augmented Generation (RAG). At a high level, this means that Claude can automatically find and use the most relevant parts of your uploaded documents when answering, without you needing to tell it which file to look at.

When your project knowledge approaches the context window limit, Claude seamlessly enables RAG mode. Instead of loading all project content into memory at once, Claude intelligently searches and retrieves only the most relevant information needed to answer your questions. This expands your project's capacity by up to 10x while maintaining response quality.

You'll see a visual indicator when your project is RAG-enabled, but the experience should feel the same—you can still upload documents, chat with Claude, and get context-aware responses.

### Working within your project

Once your project is set up, you can start chatting with Claude. Each conversation within the project automatically has access to your knowledge base and follows your project instructions.

### Collaboration features

For users on Claude for Work (Team and Enterprise) plans, projects become even more powerful through collaboration features.

#### Permission levels

When sharing a project, you can choose from three permission levels:

1. **Can view:** Members can see project contents, access knowledge, and chat—but can't make changes. Think of this as read-only access with discussion rights. 2. **Can edit:** Members have full collaboration power. They can modify instructions, update knowledge, manage other members, and actively contribute to the project. 3. **Owner:** Project creators control everything, including who sees the project. They can share with specific people or make projects visible to the entire organization.

#### Sharing your project

To share a project:

* Open the project you want to share
* Click the "Share project" button to the right of the project name
* Add individual members using their name or email, or copy and paste a list of email addresses for bulk sharing (in this case, the project will show up in their "Shared with you" section)
* Or, share with "Everyone at [your organization]" to make your project discoverable within the Team tab

Team members will receive email notifications when you share a project with them, and they can find shared projects in their "Shared with me" tab.

### Example projects to inspire you

Not sure where to start? Here are some common project types across different functions:

* **Q4 product launch:** Upload your product specs, competitive analysis, and messaging brainstorming notes. Claude will have this context top of mind for any inquiry or document draft.
* **Research support:** Centralize your competitive review, user research data, and customer feedback. Claude can help you synthesize sources, draft reports, and maintain consistency across recommendations.
* **Client account hub:** Keep your client's brand guidelines, past deliverables, and communication history in one place. Set instructions so Claude matches their tone and references their specific context when creating proposals or reports.
* **Event planning workspace:** Upload venue contracts, speaker bios, and attendee data. Claude can help generate run-of-show documents, attendee communications, and post-event reports that stay consistent with your event's theme.
* **Job description generator:** Gather past job descriptions, team charters, and internal headcount request docs. Work with Claude to draft job descriptions that reflect your team's actual work and culture.

### Best practices for projects

To get the most out of projects:

* **Start focused, then expand.** Begin with a specific use case rather than trying to create one project for everything. You can always add more content as you go.
* **Keep your knowledge base current.** Outdated documents can lead to outdated responses. Review and update your project knowledge periodically.
* **Write clear instructions.** Be specific about what you want. Vague instructions lead to inconsistent results.
* **Name your documents descriptively.** (e.g., 'Q4-2025-Sales-Report.pdf' not 'report.pdf') and group related files together. Claude uses filenames and proximity to understand relationships between documents.
* **Reference documents by name.** When asking questions, you can mention specific documents to help Claude focus its search: "Based on our Q3 report, what were the top customer concerns?"

### Lesson reflection

Before moving on, consider:

* What ongoing work could benefit from having a dedicated project with persistent context?
* What documents do you expect you'll be re-uploading or re-explaining to Claude on a regular basis?
* If you're on a team, are there projects that would benefit from shared knowledge and instructions?

### What's next

In the next lesson, we'll learn how to create mini-apps with Artifacts — actual outputs that Claude build and you can share right away.

For more information on getting started with projects, visit the [Anthropic Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects).

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback [here](https://forms.gle/sY9ou5fqZBd3TjHF8).

#### Acknowledgments and license

*Copyright 2025 Anthropic. All rights reserved.*

<!-- youtube: GJ5jTgcbRHA -->

## 자막 (영상 전사)

What are projects and how do they improve working with Claude? With projects, Claude users can create self-contained environments with their own chat histories, specific knowledge bases, and customized settings. We are going to provide an overview of projects, what they are used for, how to create them, and some [music] advanced features. Let's talk about a few of the key features of projects. Project knowledge enhances Claude's understanding by allowing you to upload relevant documents within each project. Every time you chat with Claude inside of a project, this knowledge is automatically [music] considered alongside your prompt. This contextual information enables Claude to deliver more informed project specific responses that align with your team's goals, terminology, and background. Projects can handle much more content without running into limits. Projects with lots of information are automatically processed [music] using retrieval augmented generation, enabling Claude to use more context to help you. When setting up a project, you can define project instructions for each project to further tailor Claude's responses. [music] Like context, these are considered every time you chat with Claude. It's a good space to guide the way Claude responds. For example, you can ask Claude to use a more formal tone or answer questions from a specific perspective targeting a specific industry. If you're on a Claude for work plan, you can share projects with other members of your organization, enabling powerful collaboration and knowledge sharing capabilities. For example, a brand team can create a project with voice and tone guidelines that helps anyone at their company write like a marketer. Okay, let's get started by creating your first project in three simple steps. Click new project and give it a name. Next, describe your project and what you are hoping to achieve like I would [music] like to make brand guidelines to write a series of case study blogs for my flower business. Click create project. To the right of the project title, you see a few menu items. You can star this project for quicker access and edit project details and archive or delete the project. Provide Claude with relevant instructions and information for the chats within the project. This will work alongside user preferences and the selected style. Choose visibility for your project. You can choose private for personal use or public for team collaboration. From here, provide project instructions and information for the chats within the project. This will work alongside the user preferences and the selected style. Click on instructions to define how Claude should respond. Within this space, you can specify tone, expertise level, response style, and desired [music] outcomes or simply give more context on what you're trying to achieve with this project. For instance, when providing the brand guidelines, explain the thought process and highlight tone and brand application. Once done providing instructions, click save instructions. This will apply to every chat in the project. You'll find the files menu on the right side of your project's main page. Anything you upload to this space will be used across all of your chats within this project. Click on the plus button to add content to the project. You can upload PDFs, documents, CSVs, text files, or connect to Google Drive. Now Claude can instantly reference this content in any conversation. Claude will process this information and use it as context in your chats within the project. For example, if you are working on creating new brand guidelines for a specific client, you can upload their existing branded materials and Claude will reference that file in its response. Note that context is not shared across disparate chats within a project unless the information is added into [music] the project knowledge base. Sometimes your project knowledge will approach the context window limit. Claude will automatically enable rag mode to expand your project's capacity. Once your project is set up, you can initiate chats with Claude within the project. You can learn more about best practices for chatting and Claude by reviewing one of our other videos. You can make chats public [music] so teammates can view and build onto your work. There are three permission levels that control who can do what in your projects. Can view members can view project contents, access knowledge, and chat, but can't make changes. Think readonly access with discussion rights. Canedit members have full collaboration power. They can modify instructions, update knowledge, manage members, [music] and actively contribute to the project. Project creators control everything. Plus, they decide who sees the project. They can share with specific people or make private projects visible to the entire organization. The right permissions keep your projects secure while enabling smooth collaboration. So, pick the options that work best for your team. Here are some of Claude's collaboration features. Check out the shared with me tab to easily find projects that others have shared with you. You will receive email notifications when someone shares a project with you. And project creators can modify permissions or remove access as needed. Multiple members can contribute documents, create chats, and work together within the same project environment, making projects ideal for team collaboration. Sometimes you need to use content without adding it to your project's knowledge base. [music] No problem. Simply upload it during the conversation, and it stays separate from your project [music] knowledge. It's a perfect way to share context or examples without cluttering the knowledge base. Here are some examples of projects you can create. You can create a new product for market like managing the development process of a new product from ideiation to launch like an eco-friendly water bottle. Useful for keeping all product related information in one place using Claude for creative ideation and tracking the evolution of the product design. Claude can streamline the content creation process by generating content ideas, providing writing assistance and maintaining consistency across platforms. You can design and develop an educational course like Anthropics AI Fluency coursework. In projects, you can organize course materials, use Claude to [music] help explain complex concepts, and iteratively improve the course content. You can create a project to track, analyze, and plan personal finances for your personal financial goals and budget. Keeping all financial information in one secure place, Claude can analyze spending patterns and help with financial calculations and planning. Or you can plan and manage a home renovation like updating a kitchen space, centralize all project information, use Claude to help with a design idea and budget calculations, and keep track of all decisions and communications. These examples demonstrate the flexibility of what can be done with projects in Claude. Whether you're working on professional tasks, personal goals, or collaborative efforts, projects can help you organize information, generate ideas, and streamline your work process. Remember, you can customize each project to fit your specific needs and workflow. For more information on getting started with projects, check out our help center article.
