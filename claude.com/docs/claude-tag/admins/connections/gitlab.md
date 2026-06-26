<!-- source: https://claude.com/docs/claude-tag/admins/connections/gitlab -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting GitLab lets Claude clone repositories, read and search projects, comment on issues and merge requests, and check pipeline status, all through the GitLab REST API. The connection is a single access token added to a bundle.
Pair this connection with the GitLab plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

##  Add the connection

1

Create the token in GitLab

A project access token or group access token, so activity is attributed to a bot identity rather than a person. Grant the `api` scope for read and write; `read_api` for read-only. The token starts with `glpat-`.

2

Add the credential to a bundle

On the bundle’s **Credentials** tab, click **Connect** next to **GitLab** and paste the token. For self-managed GitLab, switch to the form’s **Advanced** tab and add your instance’s hostname under **Allowed websites**.

**You’ll see:** GitLab listed in the bundle’s connections, and `@Claude what can you access from this channel?` returns it in a new thread under the bundle’s scope.

| Field | Value |
| Claude’s personal access token | The token from GitLab, starting with `glpat-`. Project and group access tokens work here too; the label is the field name, not a token-type constraint. |
| Allowed websites | `gitlab.com` (preset). For self-managed GitLab, open the **Advanced** tab and add your instance’s hostname here. |

GitLab’s own guide for creating tokens is at [docs.gitlab.com](https://docs.gitlab.com/api/rest/authentication/).

##  How GitLab differs from GitHub

|  | GitLab | GitHub |
| --- | --- | --- |
| Auth | One org-level access token | The Claude GitHub App, [installed separately](/docs/claude-tag/admins/configure-github) |
| Attaching a repo in a thread | Give Claude the full repository URL; it clones it | Typing `owner/repo` in the message auto-attaches it |
| Self-managed | Your hostname under **Advanced → Allowed websites** | [GitHub Enterprise setup](/docs/claude-tag/admins/configure-github#github-enterprise) |

The token is auto-injected on every request to your GitLab host and used as the credential when cloning repositories into a session. The model and the sandbox are not given the key; see [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

* [What this connection adds](/docs/claude-tag/users/use-cases/fix-bugs): the code use cases
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): the GitHub App path, which is different
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Datadog](/docs/claude-tag/admins/connections/datadog)[Gong](/docs/claude-tag/admins/connections/gong)
