<!-- source: https://claude.com/docs/claude-tag/admins/connections/gitlab -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Connections are added inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting GitLab lets Claude read and search projects, manage issues, comment on merge requests, and check pipeline status, all through the GitLab REST API. The connection is a single access token added to a bundle.

This page is the credential field reference. The full setup walkthrough, including creating a dedicated GitLab service account for Claude and scoping its group access, is at [Configure GitLab access](https://claude.com/docs/claude-tag/admins/configure-gitlab).

If your plugin marketplace includes a GitLab plugin, pair it with this connection so Claude knows how to call the API. See [Attach plugins](https://claude.com/docs/claude-tag/admins/add-connections#attach-plugins). The connection works without it.

##  Add the connection

1

Create the token in GitLab

A personal access token from a [dedicated service account](https://claude.com/docs/claude-tag/admins/configure-gitlab#create-a-dedicated-gitlab-account-for-claude) is recommended, so one identity covers every group you add it to. Project and group access tokens also work if you only need a single project or group. Grant the `api` scope for read and write, or `read_api` for read-only. The token starts with `glpat-`.

2

Add the credential to a bundle

On the bundle’s **Credentials** tab, click **Connect** next to **GitLab** and paste the token. For self-managed GitLab, switch to the form’s **Advanced** tab and add your instance’s hostname under **Allowed websites**.

**You’ll see:** GitLab listed in the bundle’s connections, and `@Claude what can you access from this channel?` returns it in a new thread under the bundle’s scope. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

| Field | Value |
| --- | --- |
| Personal access token | The token from GitLab, starting with `glpat-`. Project and group access tokens work here too; the label is the field name, not a token-type constraint. |
| Allowed websites | `gitlab.com` (preset). For self-managed GitLab, open the **Advanced** tab and add your instance’s hostname here. |

GitLab’s own guide for creating tokens is at [docs.gitlab.com](https://docs.gitlab.com/api/rest/authentication/).

##  How GitLab differs from GitHub

|  | GitLab | GitHub |
| --- | --- | --- |
| Auth | A service account’s personal access token | The Claude GitHub App, [installed separately](https://claude.com/docs/claude-tag/admins/configure-github) |
| Referencing a project in a thread | Give Claude the full project URL; it reads it through the API | Typing `owner/repo` in the message auto-attaches it |
| Self-managed | Your hostname under **Advanced → Allowed websites** | [GitHub Enterprise setup](https://claude.com/docs/claude-tag/admins/configure-github#github-enterprise) |
| Handing back changes | Manages issues and comments on merge requests through the API | [Draft pull requests](https://claude.com/docs/claude-tag/users/use-cases/work-with-github) authored by the Claude GitHub App |

The token is auto-injected on every API request to your GitLab host. The model and the sandbox are not given the key; see [how Agent Proxy works](https://claude.com/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Related resources

* [Configure GitHub access](https://claude.com/docs/claude-tag/admins/configure-github): the GitHub App path, which is different
* [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
