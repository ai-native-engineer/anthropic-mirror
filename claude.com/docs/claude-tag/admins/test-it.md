<!-- source: https://claude.com/docs/claude-tag/admins/test-it -->

[1 · Pair workspace](/docs/claude-tag/admins/pair-workspace)[2 · Give access](/docs/claude-tag/admins/add-connections)[3 · Spend limit](/docs/claude-tag/admins/set-spend-limit)[4 · Test it](/docs/claude-tag/admins/test-it)

Role you needAnyone in the pilot channel can run the test; you’ll want Owner access handy to fix anything it surfaces

Before this stepWorkspace paired and a [spend limit](/docs/claude-tag/admins/set-spend-limit) set

Do I need this?RequiredThe only way to know the setup holds together before rolling out to more channels.

The test has two parts: a first task that uses only the channel itself, then a task for each connection you added.

##  Run the first task

Add Claude to the pilot channel, then hand it a task:

/invite @Claude

@Claude summarize what this channel decided this week and list any open questions

This task uses only the channel’s history, so it confirms the app install, the scope, and the session machinery before any connection is in play.
**Passed when:** an “is thinking…” line appears under the message, Claude posts its work in the thread, and delivers a summary.

##  Test each connection

For each connection you added in [step 2](/docs/claude-tag/admins/add-connections), run a second task in a new thread.

1

Ask what the channel can reach

Send `@Claude what can you access from this channel?` Claude replies with the systems available there.

2

Ask for data from the connection

Pick one connection and ask for something a read-only credential can do, like the latest items from an issue tracker or a single row count from a warehouse.

3

Check the service's own audit log

Confirm the action appears in that service’s audit log under the service account you provisioned. That entry proves the credential chain end to end and is the trail your security team reads later.

**Passed when:** the connection responds, and the action shows in that service’s audit log under your service account.

##  If a test fails

Most first-task failures trace to one of three causes, in order of likelihood:

* **No response at all**: the channel isn’t covered by any scope you’ve configured. Check the workspace appears under **Claude Tag’s access** on the **Slack** tab in admin settings.
* **Claude responds but can’t reach a service you connected**: connections apply to new threads only. Start a fresh thread before investigating anything else.
* **An error message**: the message text names what’s missing (a connection, a host on the allowlist, or a permission). Fix that piece and try again in a new thread.

* [Customize Claude Tag](/docs/claude-tag/admins/customize): standing instructions, plugins, and what channel members can change
* [Roll out, scope by scope](/docs/claude-tag/admins/setup-overview#after-setup): the two rollout patterns and where elevated credentials go
* [Getting started for users](/docs/claude-tag/users/getting-started): what to send the first people in
* [Use case library](/docs/claude-tag/users/use-cases): tasks to hand the pilot channel, with the prompts to paste

[3. Set a spend limit](/docs/claude-tag/admins/set-spend-limit)[For Slack admins](/docs/claude-tag/admins/for-slack-admins)
