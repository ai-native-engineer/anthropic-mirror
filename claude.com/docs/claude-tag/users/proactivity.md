<!-- source: https://claude.com/docs/claude-tag/users/proactivity -->

You can give Claude standing work from any channel it’s in. This standing work is called a routine: a job that runs on a schedule, such as watching a channel, following a pull request, or posting status updates. You set a routine up in the channel where it should run, and it uses that channel’s connections with the same permissions as a typed request.

##  Set up standing work

###  Scheduled jobs

Describe the schedule you want and the work Claude should do in one message:

@Claude every weekday at 9am, read the open threads in this channel, check the tickets and pull requests linked in them, and post a one-line status per item. Skip anything with a ✅ reaction.

Name the output format in the job so recurring posts stay scannable.

###  Watch channels

Ask Claude to watch named channels and post here when something matches a topic:

@Claude watch #product-announce, #eng-announce, and #design-announce. Once a day, post here if anything is relevant to user education. Skip days with nothing.

Naming both the channels and the topic is what keeps a watch useful. The watch can cover this channel too (“keep an eye on this channel and post a morning summary”).

###  Follow a pull request

Claude can subscribe to a single pull request and react when it updates.

@Claude subscribe to PR #482 in acme/data-pipeline. When CI finishes or a review lands, post here, and tag me if anything failed.

##  Manage standing work

Anyone in the channel can list, edit, or disable its standing work:

* **List.** Ask “what routines do you have set up in this channel?”
* **Edit.** Describe the change and it updates the job
* **Disable.** Name the job to stop, as in “disable the Friday rollup”

Standing work is visible to the channel: jobs post into the channel they belong to. Routines keep running if their creator leaves the organization, but stop firing if the creator is removed from the channel.
A few boundaries apply:

* A job runs with the channel’s connections, the same as an interactive request.
* Schedules default to UTC. When you say “every weekday at 9am,” include the timezone (for example “9am Pacific”) so Claude converts correctly; without one it may guess. Ask “what triggers do you have set up?” to confirm the time it actually scheduled.
* A scheduled job that touches a github.com repository uses the same GitHub connection your admin set up for interactive work. See [Configure GitHub access](/docs/claude-tag/admins/configure-github#scheduled-work-uses-the-same-connection).

* [Use case library](/docs/claude-tag/users/use-cases): every entry has a proactive form to copy
* [Good habits](/docs/claude-tag/users/good-habits): write schedules that keep working

[Good habits](/docs/claude-tag/users/good-habits)[What Claude Tag remembers](/docs/claude-tag/users/memory)
