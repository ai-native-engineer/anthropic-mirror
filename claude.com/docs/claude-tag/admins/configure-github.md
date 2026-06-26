<!-- source: https://claude.com/docs/claude-tag/admins/configure-github -->

Claude Tag gives Claude its own GitHub identity, the Claude GitHub App, so pull requests it opens from a channel are authored by Claude rather than by a person. You only need GitHub access if a team will hand Claude code work: branches, pull requests, review, or CI follow-up.
You link GitHub once for your Claude organization, then grant repositories per Access bundle.

##  Link your GitHub organization

The person who completes the link must be both an **owner of the GitHub organization** and an **Admin in your Claude organization**. If you aren’t a GitHub organization owner, use **Copy message** under **Not a GitHub organization owner?** on the GitHub settings page to send the link to someone who is.

1

Open the GitHub settings page

Open [`claude.ai/admin-settings/claude-code/github`](https://claude.ai/admin-settings/claude-code/github). This page is shared with Claude Code; one connection serves both products.

2

Connect GitHub

Click **Connect GitHub** and complete the GitHub authorization. After authorizing, the page shows two sections: **Installations** lists organizations already linked, and **Unlinked accounts** lists organizations where the Claude GitHub App is installed but not yet linked.

3

Link or install

If your organization is under **Unlinked accounts**, click **Link** next to it. If it isn’t listed at all, click **Install on another organization** and complete the install on github.com; you’re returned to this page with the organization under **Installations** as **Active**.

* A disabled **Link** button means you aren’t an owner of that GitHub organization
* A **Needs permissions** status means the installation has a pending request; **Review permissions** takes you to github.com to approve it

##  Grant repository access

The remaining steps are in the Claude Tag admin page, not GitHub’s settings. Repository grants live on the Access bundle; editing a bundle’s Repositories tab requires the **Owner** role in your Claude organization.

1

Open the bundle's Repositories tab

Open an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle) and go to its **Repositories** tab. Before any GitHub organization is linked, this tab shows a **Get started with GitHub** button that opens [`claude.ai/admin-settings/claude-code/github`](https://claude.ai/admin-settings/claude-code/github).

2

Select repositories

Choose the repositories Claude can read from and open pull requests against. Access is per listed repository, or choose **Connect all repos** for the organization.

##  Verify GitHub access

* The GitHub organization shows as **Active** under **Installations** at [`claude.ai/admin-settings/claude-code/github`](https://claude.ai/admin-settings/claude-code/github).
* The granted repositories are listed in the bundle’s **Repositories** tab.
* For the end-to-end check, open a draft PR from a test channel; see [Verify the bundle is live](/docs/claude-tag/admins/attach-to-scope#verify-the-bundle-is-live).

##  How granted repositories reach a session

Granting a repository in a bundle makes it *available* to Claude in any channel under that bundle’s scope. It doesn’t clone the code into a session on its own. A session starts with no repositories checked out; Claude clones one when the request names it, or when someone in the thread tells it which repository to add. Tell your team to name the repository in the first message of a code task.

###  What loads from a repository

When Claude clones a granted repository into a session, its `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` files load on the next turn after the clone completes, so project context arrives without further prompting. A repository’s `.mcp.json` is never loaded; connections come only from the Access bundle.

##  Scheduled work uses the same connection

Scheduled jobs use the same GitHub connection as interactive work, with nothing extra to configure. A recurring job that can’t reach its repository skips that run and retries on its next schedule; after three consecutive failed runs spanning at least an hour, it disables itself. A one-time job that can’t reach its repository is disabled on the first failure; the routine’s page shows why.

##  GitHub Enterprise

###  GitHub Enterprise Cloud with data residency

Organizations on `*.ghe.com` (Enterprise Cloud with Data Residency) are registered the same way as a GitHub Enterprise Server host below.

###  GitHub Enterprise Server

GitHub Enterprise Server instances are supported when reachable from the public internet. A GHES host on a private network without a public address can’t be connected.
On GHES, you create the GitHub App on your own instance instead of installing Anthropic’s. The setup is shared with Claude Code; follow the [Claude Code GitHub Enterprise Server guide](https://code.claude.com/docs/en/github-enterprise-server) to create and register the app. After registering the GHE host, a host picker appears on the bundle’s **Repositories** tab; select your host there to grant its repositories.
Registering a GHE host with your Claude organization isn’t fully self-serve. Raise it with your account team if the guide doesn’t get you all the way through.

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): bind the bundle to the workspaces and channels that need it
* [Set up routines](/docs/claude-tag/users/proactivity): the scheduled jobs that use this connection

[Per-channel access](/docs/claude-tag/admins/attach-to-scope)[Connection guides](/docs/claude-tag/admins/connections/overview)
