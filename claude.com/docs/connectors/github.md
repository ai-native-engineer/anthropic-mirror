<!-- source: https://claude.com/docs/connectors/github -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

The GitHub integration lets you add files and folders from your GitHub repositories to a conversation or a project, so Claude can read your code and answer development questions with that context. It’s available on every plan, including Free, and works with public repositories and with private repositories you grant access to.
By the end of this page you have added repository content to a chat or a project and asked Claude about it. Claude reads file names and contents only: it doesn’t see commit history, pull requests, or issues.

If you want Claude to edit code, run commands, and open pull requests in your repository, see [Claude Code](https://code.claude.com/docs).

##  Add repository content

You can add repository content to a single conversation, or to a [project](https://support.claude.com/en/articles/9517075-what-are-projects), a workspace in Claude where a set of chats share the same background documents. Choose the tab below for where you want the content available. If you haven’t signed in to GitHub from Claude yet, Claude sends you to GitHub to sign in before you continue.

* In a chat
* In a project

1

Open the add menu

In the conversation, select **+** at the lower left of the message box.

2

Choose GitHub

Select **Add from GitHub**.

3

Select files and folders

Use the file browser to select the files and folders you want Claude to read.

4

Send your message

Write your question and send it. Claude reads and processes the selected content when you send the message.

You can add repository content only to a private project, one you haven’t shared with other people. In a shared project, the **GitHub** option is dimmed and shows **Only accessible from private projects**.

1

Open project knowledge

Open the project and, in its project knowledge section, select **+**.

2

Choose GitHub

Select **GitHub**.

3

Pick a repository

Search the repositories you have access to, or paste a repository URL.

4

Select files and folders

Use the file browser to select the files and folders you want Claude to read.

The selected content is added to the project’s knowledge.

##  Connect a private repository

If a warning appears after you enter a valid repository URL, the repository is most likely private and Claude doesn’t have access to it yet. Follow the link in the warning to the Claude GitHub App, where you have two options:

* **Grant access yourself**: allow Claude access to all of your repositories or only to specific ones
* **Request access**: your GitHub organization’s administrators receive an email notification. Once they approve, you can sync and add the repository

##  Try the connector

After you add repository content, ask Claude something that depends on the code you selected. For example, ask Claude:

* Explain how request authentication works in these files
* Where is the retry logic, and what happens when it gives up?

Claude answers from the names and contents of the files you selected on the branch you chose. It doesn’t see commit history, pull requests, issues, or repository metadata; [Review what Claude retrieves from GitHub](#review-what-claude-retrieves-from-github) has the full list.

##  Keep repository content current

After you add a repository, use these controls in your project knowledge to keep its content current and scoped to what you need:

* **Sync**: select **Sync now** on the repository in your project knowledge to fetch the latest changes, especially before a new analysis or after major changes to the repository
* **Change the selection**: select **Configure files** to change which files and folders Claude reads
* **Multiple repositories**: you can add several repositories for broader context, as long as the selected content fits within Claude’s context window
* **Lost access**: if you lose access to a repository, you can no longer view its contents in projects where it was added. The repository preview is removed, but your conversation history remains

##  Review what Claude retrieves from GitHub

The table lists what the integration reads from a repository and what it leaves out.

| Retrieved | Not retrieved |
| --- | --- |
| File names | Commit history |
| File contents | Pull requests |
| Branch content | Issues |
|  | Repository metadata |

##  Best practices

These habits help Claude give useful answers about a codebase:

* **Start small**: begin with a small subset of the codebase to see how Claude interprets your code
* **Select files thoughtfully**: include the files central to your task while staying within token limits
* **Iterate and refine**: ask follow-up questions when an initial response needs clarification
* **Combine with human expertise**: treat Claude’s analysis as a starting point for team discussion
* **Sync regularly**: refresh the GitHub sync periodically, especially before a new analysis or after major repository changes

##  Next steps

* [Get started with connectors](https://claude.com/docs/connectors/getting-started): set up another connector and use it in conversations
* [Connectors directory](https://claude.com/docs/connectors/directory): browse verified and community integrations
