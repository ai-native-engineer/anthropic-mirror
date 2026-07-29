<!-- source: https://claude.com/docs/claude-tag/admins/test-it -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

[1 · Pair workspace](https://claude.com/docs/claude-tag/admins/pair-workspace)[2 · Give access](https://claude.com/docs/claude-tag/admins/add-connections)[3 · Spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit)[4 · See it work](https://claude.com/docs/claude-tag/admins/test-it)

Role you needAnyone in the pilot channel can run the prompts; you’ll want Owner access handy to fix anything they surface

Before this stepWorkspace paired and a [spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit) set

Do I need this?RequiredThe only way to know the setup holds together before rolling out to more channels.

Claude starts taking work the moment the workspace is paired, with or without connections. This step has two parts: tasks that run on the channel’s own content, then a check for each connection you added.

##  Run tasks that need no connections

Add Claude to the pilot channel:

```
/invite @Claude
```

Then paste the recap task. It uses only the channel’s history, so it confirms the app install, the scope, and the session machinery before any connection is in play.

```
@Claude summarize what this channel decided this week and list any open questions
```

**Passed when:** an “is thinking…” line appears under the message, Claude posts its work in the thread, and delivers a summary.
The recap proves the setup; the prompts below preview the work your channels can hand Claude before anything is connected. Each links to a use case page with the full setup.
Roll up the channel’s open requests, the one-off version of [Triage requests](https://claude.com/docs/claude-tag/users/use-cases/triage-requests):

```
@Claude post a summary of this week's requests in this channel: how many, top themes, and anything still unrouted
```

Turn a settled discussion into a document, from [Turn threads into docs and tickets](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts):

```
@Claude turn this thread into a one-page decision doc: what we decided, the options we rejected, and why.
```

Ask for a personalized menu of next tasks, from the [prompt library](https://claude.com/docs/claude-tag/users/prompt-library):

```
@Claude learn what you can about my role from this workspace, then tell me three tasks you could take off my plate this week.
```

##  Test the connections you added

If you skipped connections during setup, you’re done; come back to this section after you [add a connection](https://claude.com/docs/claude-tag/admins/add-connections). For each connection, run a task in a new thread.

1

Ask what the channel can reach

```
@Claude what can you access from this channel?
```

Claude replies with the systems available there.

2

Ask for data from the connection

Pick one connection and ask for something a read-only credential can do, like the latest items from an issue tracker or a single row count from a warehouse.

```
@Claude pull the five most recent items from our issue tracker and post them here
```

For a GitHub repository grant, ask about pull request state:

```
@Claude list the open pull requests in your-org/your-repo and who each one is waiting on
```

3

Check the service's own audit log

Confirm the action appears in that service’s audit log under the service account you provisioned. That entry proves the credential chain end to end and is the trail your security team reads later.

**Passed when:** the connection responds, and the action shows in that service’s audit log under your service account.

##  If a test fails

Most first-task failures trace to one of three causes, in order of likelihood:

* **No response at all**: the channel isn’t covered by any scope you’ve configured. Check the workspace appears under **Claude Tag’s access** on the **Slack** tab in admin settings.
* **Claude responds but can’t reach a service you connected**: Claude isn’t told about a connection added after the thread started. Ask it to use the service by name, or start a fresh thread, before investigating anything else.
* **An error message**: the message text names what’s missing (a connection, [a host on the allowlist](https://claude.com/docs/claude-tag/admins/add-connections#add-a-domain), or a permission). Fix that piece and try again.

##  Related resources

* [Getting started for users](https://claude.com/docs/claude-tag/users/getting-started): what to send the first people in
* [Use case library](https://claude.com/docs/claude-tag/users/use-cases): tasks to hand the pilot channel, with the prompts to paste
* [Prompt library](https://claude.com/docs/claude-tag/users/prompt-library): every prompt on one page, each with why it works
