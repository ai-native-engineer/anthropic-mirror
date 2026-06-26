<!-- source: https://claude.com/docs/claude-tag/admins/skills-repo -->

A **skill** is a set of instructions that teaches Claude how to use a specific tool or follow a specific process (for example, which Datadog endpoints answer which questions, or your org’s incident-response runbook). Claude Tag uses the same [skills format as Claude Code](https://code.claude.com/docs/en/skills). A **plugin** bundles one or more skills together.
You can upload skills one at a time in the console, but putting them in a git repository means Claude can open pull requests to improve them from what it learns working in your channels. You review the PR; once merged, every channel picks up the update.

##  Set up the skills repository

1

Create the repository

A new GitHub repository in your organization, with one folder per plugin. Each plugin bundles one or more skills.

2

Register the repository as a plugin marketplace

In claude.ai admin settings, add the repository as an organization plugin source and leave **Sync automatically** on (the default).

3

Grant Claude write access to the repository

Open an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle), go to its **Repositories** tab, and add the repository. The Claude GitHub App must already be linked to your GitHub organization; see [Configure GitHub access](/docs/claude-tag/admins/configure-github).

4

Attach the plugins to a scope

In the same bundle’s **Plugins** section, select **+** and add your new marketplace. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

**You’ll see:** the repository appears in the bundle’s Repositories list, and the marketplace appears in the bundle’s Plugins section.

##  How updates propagate

Once the repository is set up, Claude can propose changes and they reach channels automatically after you merge:

| Stage | What happens |
| Claude works in a channel | Using the skills currently attached to that scope |
| Claude proposes an update | Opens a pull request against the skills repository, under the Claude GitHub App identity, linked back to the thread that prompted it |
| You review and merge | The PR is yours to approve, edit, or close, like any contributor’s |
| The marketplace syncs | On push to the default branch, the updated plugin syncs to your organization automatically |
| New threads pick it up | The next thread in any covered channel uses the updated skill. Threads already running keep what they started with. |

Every skill change reaches channels only after a human approves the merge; Claude opens the PR, you merge it.

##  Prompt Claude to propose updates

Claude won’t open skill PRs unprompted. Ask in the channel when something it learned should stick:

@Claude that worked. Open a PR to the skills repo so the Datadog skill includes that query pattern.

Or set a routine that sweeps a channel’s corrections into proposed updates:

@Claude every Friday, review what you got wrong in this channel this week and open one PR to the skills repo with the fixes.

##  Why a repository instead of uploading skills

You can also upload individual skills in the console without a repository. The repository pattern is worth the setup because Claude can propose changes to it, every change goes through version control and code review, and you can attach the same skills to multiple bundles without uploading them again.

##  What belongs in the repository

| Put in the skills repo | Put in channel memory instead |
| How to call a specific API correctly | This channel’s preferred output format |
| A runbook that any team would reuse | A one-off decision this channel made |
| Tool-specific gotchas (auth headers, pagination, rate limits) | Who owns what in this team |

Skills in the repository reach every channel under the scope.

* [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins): how plugins and skills load into a scope
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): granting Claude write access to a repository
* [What Claude Tag remembers](/docs/claude-tag/users/memory): when channel memory is the right place instead

[Customize Claude Tag](/docs/claude-tag/admins/customize)[Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access)
