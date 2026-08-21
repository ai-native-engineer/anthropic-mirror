<!-- source: https://claude.com/docs/claude-tag/admins/configure-github -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Using GitLab instead of GitHub? See [Configure GitLab access](https://claude.com/docs/claude-tag/admins/configure-gitlab). GitLab uses a service-account token rather than an installed app.

Claude Tag gives Claude its own GitHub identity, the Claude GitHub App, so pull requests it opens from a channel are authored by Claude rather than by a person. You only need GitHub access if a team will hand Claude code work: branches, pull requests, review, or CI follow-up.
You link GitHub once for your Claude organization, then grant repositories per Access bundle.

If you link your GitHub organization before running [setup](https://claude.com/docs/claude-tag/admins/setup-overview), setup includes a step for granting repository access inline, so you don’t need to return to the Repositories tab afterward.

##  Link your GitHub organization

The person who completes the link must be both an **owner of the GitHub organization** and an **Admin in your Claude organization**. If you aren’t a GitHub organization owner, use **Copy message** under **Not a GitHub account owner?** on the GitHub settings page to send the link to someone who is.

1

Open the GitHub settings page

Open [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github). This page is shared with Claude Code; one connection serves both products.

2

Connect Claude to GitHub

Click **Connect Claude to GitHub** and complete the GitHub authorization. After authorizing, the page shows two sections: **Connected GitHub accounts** lists organizations already linked, and **Unlinked accounts** lists organizations where the Claude GitHub App is installed but not yet linked.

3

Link or install

If your organization is under **Unlinked accounts**, click **Link** next to it. If it isn’t listed at all, click **Install on another organization** and complete the install on github.com; you’re returned to this page with the organization under **Connected GitHub accounts** as **Connected**.

* A disabled **Link** button means you aren’t an owner of that GitHub organization
* A **Needs permissions** status means the installation has a pending request; **Review permissions** takes you to github.com to approve it

##  Grant repository access

The remaining steps are in the Claude Tag admin page, not GitHub’s settings. Repository grants live on the Access bundle; editing a bundle’s Repositories tab requires the **Owner** role in your Claude organization. A [channel manager](https://claude.com/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can also add repositories to their own channel, limited to repositories their GitHub account can write to.

1

Open the bundle's Repositories tab

Open an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle) and go to its **Repositories** tab. Before any GitHub organization is linked, this tab shows a **Get started with GitHub** button that opens [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github).

2

Select repositories

Choose the repositories Claude can read from and open pull requests against. Access is per listed repository, or choose **Connect all** for the organization.

##  Verify GitHub access

* The GitHub organization shows as **Connected** under **Connected GitHub accounts** at [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github).
* The granted repositories are listed in the bundle’s **Repositories** tab.
* For the end-to-end check, open a draft PR from a test channel; see [Verify the bundle is live](https://claude.com/docs/claude-tag/admins/attach-to-scope#verify-the-bundle-is-live).

###  If Claude can’t reach a repository

When Claude replies “That environment or repo isn’t configured for Claude Code”, or reports that GitHub returned a 403, check the two levels in order.

| Check | Where |
| --- | --- |
| The GitHub organization that owns the repository shows **Connected** under **Connected GitHub accounts** | [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github). An installation still waiting on a GitHub organization owner shows **Needs permissions**; **Review permissions** opens the approval on github.com. |
| The repository is listed on the bundle’s **Repositories** tab, and that bundle is attached to the channel’s scope | [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Access bundles** → the bundle → **Repositories**. A repository granted in one bundle isn’t reachable from a channel under a different bundle. |

Repository grants apply to new threads. After changing the **Repositories** tab, start a fresh thread in the channel and name the repository in the first message.
The message “GitHub Actions writes are not permitted for this session type.” is a different `403`. It says nothing about repository access; see [What Claude can do with GitHub Actions](#what-claude-can-do-with-github-actions).

##  How granted repositories reach a session

Granting a repository in a bundle makes it *available* to Claude in any channel under that bundle’s scope. It doesn’t clone the code into a session on its own. A session starts with no repositories checked out; Claude clones one when the request names it, or when someone in the thread tells it which repository to add. Tell your team to name the repository in the first message of a code task.

###  What loads from a repository

When Claude clones a granted repository into a session, its Claude Code configuration loads on the next turn after the clone completes, so project context arrives without further prompting:

* `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` load as project context
* Skills in `.claude/skills/` load, so Claude can use them in the session
* The project settings in `.claude/settings.json` load, so hooks defined there run in the session as they do under Claude Code

A repository’s `.mcp.json` is never loaded, and connections come only from the Access bundle.
Repository skills apply only in sessions that have the repository. To give a skill to every channel under a scope, add it through a [skills repository](https://claude.com/docs/claude-tag/admins/skills-repo).

###  Install project dependencies

Every session runs in an isolated sandbox with a standard set of preinstalled tools. The sandbox is the same for every repository; there is no setup script or custom image to configure. If a project needs something the standard set doesn’t include, such as a specific language runtime or a database client, add the install commands to the repository’s `CLAUDE.md`.
Claude follows `CLAUDE.md` as guidance when it starts work that needs it, not as an unconditional setup step. Write each install as a precondition of the work it supports, for example “install the SDK before building or running tests”, so Claude runs it when a task touches that code. The sandbox is fresh for every session, so the installs repeat each time Claude works in the repository.
Prefer the standard package manager and its default registry over a vendor install script or a third-party package source. Package managers such as `apt`, `pip`, `npm`, and `dotnet` reach their default registries from the sandbox; downloads from other hosts can be blocked at the sandbox’s [egress boundary](https://claude.com/docs/claude-tag/concepts/security-and-data#network-egress). An Owner can allow an additional host on the bundle’s Domains tab; see [Allow a host without a credential](https://claude.com/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential).

##  What Claude can do with GitHub Actions

In a channel, Claude acts on GitHub as the Claude GitHub App, and that identity carries a fixed set of GitHub Actions permissions. No admin setting changes it, and adding `api.github.com` as a [custom connection](https://claude.com/docs/claude-tag/admins/connections/custom) with your own token doesn’t change it either; Claude’s GitHub requests always act as the Claude GitHub App.
Claude can:

* Read workflow runs, jobs, logs, and artifacts, so it follows a pull request’s CI and reports the result
* Re-run a workflow run or its failed jobs, and cancel a run in progress
* Trigger `push` and `pull_request` workflows by pushing a branch or opening a pull request, the same way any other author does. To let Claude start automation on demand, put the workflow behind one of these triggers instead of `workflow_dispatch`
* Edit files under `.github/workflows/` and open a pull request with the change, like any other file

Claude can’t:

* Dispatch a workflow (`workflow_dispatch` or `repository_dispatch`)
* Approve a workflow run that’s waiting on approval, or its pending deployments
* Delete runs, logs, or artifacts
* Enable or disable a workflow

A request for any of those is refused with a `403`. A `repository_dispatch` request returns “repository\_dispatch is not permitted for this session type.” The others return “GitHub Actions writes are not permitted for this session type.” Dispatching a workflow or approving a held run starts new code running with the repository’s Actions secrets, so it needs a person; do it from the repository’s **Actions** tab on github.com.

##  Scheduled work uses the same connection

Scheduled jobs use the same GitHub connection as interactive work, with nothing extra to configure. A recurring job that can’t reach its repository skips that run and retries on its next schedule; after three consecutive failed runs spanning at least an hour, it disables itself. A one-time job that can’t reach its repository is disabled on the first failure; the routine’s page shows why.

##  GitHub Enterprise

###  GitHub Enterprise Cloud with data residency

Organizations on `*.ghe.com` (Enterprise Cloud with Data Residency) are registered the same way as a GitHub Enterprise Server host below.

###  GitHub Enterprise Server

GitHub Enterprise Server instances are supported when reachable from the public internet. A GHES host on a private network without a public address can’t be connected.
On GHES, you create the GitHub App on your own instance instead of installing Anthropic’s. The setup is shared with Claude Code; follow the [Claude Code GitHub Enterprise Server guide](https://code.claude.com/docs/en/github-enterprise-server) to create and register the app. After registering the GHE host, a host picker appears on the bundle’s **Repositories** tab; select your host there to grant its repositories.
Registering a GHE host with your Claude organization isn’t fully self-serve. Raise it with your account team if the guide doesn’t get you all the way through.

##  Related resources

* [Configure per-channel access](https://claude.com/docs/claude-tag/admins/attach-to-scope): bind the bundle to the workspaces and channels that need it
* [Set up routines](https://claude.com/docs/claude-tag/users/proactivity): the scheduled jobs that use this connection
