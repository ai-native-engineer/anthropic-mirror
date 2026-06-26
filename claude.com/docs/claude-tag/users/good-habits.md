<!-- source: https://claude.com/docs/claude-tag/users/good-habits -->

Tasks should have a verifiable end state. Claude runs each one in its own thread, and a thread closes when someone can confirm the work is done. A task without that end state produces an open-ended report, and the thread stays open while you decide what to do with it.
The habits here are for anyone who tags Claude in from Slack.

##  Work in the open

Claude is most useful when the work is somewhere the team can see, steer, and build on. A few mindsets make that the default rather than something you remember to do.

* **Work in public.** Assume everyone in the channel can read the thread, including its checklist and results. Anything your team writes down, like decisions, conventions, and postmortems, is context Claude can use. Knowledge that lives in DMs or was only said aloud is invisible to it. Put anything personal in a DM instead.
* **Share control.** Replying in a thread someone else started is how work moves. Redirect the approach, add what the requester didn’t know, or pick up the result and run with it.
* **Grant broad access.** A channel with more connections (the tools an admin linked for this channel, like GitHub or Drive) produces more useful results, because Claude can join more sources together. The connections are scoped to the agent’s identity, so granting them to a channel does not expose anyone’s personal data.
* **Give Claude the destination, not the route.** State the outcome you want and let Claude work out the steps; the [definition of done](#give-every-task-a-definition-of-done) below makes that concrete.
* **Tolerate the mess.** A first draft posted in the thread is more useful than a polished one in a DM. The thread is the workspace, not the deliverable.

##  Write tasks that close

The phrasing of a task determines whether it has a verifiable end state, what form the result takes, and how Claude responds while working on it.

###  Name the outcome, not the activity

A task like “post the project status and tag me when it’s up” has an end state Claude can verify; “look at this” does not, and invites an open-ended report. Put the verifiable outcome in the first sentence of the task.

###  Give every task a definition of done

Starting a thread costs one sentence. Closing it costs your attention, because you read the output, decide whether it’s right, and reply.
Without a stated end condition, Claude can’t declare the thread finished and you can’t stop checking it. The end condition you write determines who can close the thread, and the table matches each kind of condition to who closes it.

| End condition | Who closes it | Example |
| --- | --- | --- |
| An objective check passes | Claude, on its own | ”Done when CI is green” |
| You approve a prepared result | You, one click | ”Draft the status memo and post it here for approval” |
| You choose between options | You, one word | ”Research approaches A and B and recommend one” |
| No verifiable condition exists | No one | Reframe it as a question instead of a task |

Two refinements make the table work in practice:

* **The condition must be observable by Claude.** “Done when CI is green” requires access to CI. If the proof lives in a system the channel isn’t connected to, change the condition to one you close yourself.
* **Spell out everything the condition includes.** “Babysit this PR until it merges” can produce a merge the moment approvals arrive, before open review comments are addressed. If the full condition is approvals present, comments resolved, and your final go-ahead, write all three into the task.

For tasks Claude closes itself, ask it to attach proof, such as the source link, the chart, the test output, or the diff. You read the proof, not the transcript.
For long-running work, make getting the deliverable somewhere durable part of the definition. Post the file to the thread, push the branch, or open the draft pull request as it goes. See [what survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).
Calibrate over time. Check everything it produces in a new channel at first, and widen what it closes on its own as its output holds up under review.

###  Specify the output format for anything recurring

A monitor or digest that posts on a schedule posts to the channel repeatedly, so spell out the shape you want each post to take. Say how long each item should be, give it the status legend to use, and tell it what to leave out, so the channel can read every post at a glance.

@Claude every 6 hours, check #alerts and post one line per item: 🔴 needs a person, 🟡 watch, 🟢 fine. Skip 🟢 unless something changed.

Once a post matches the format you want, you can also point at it directly: “use the format from your 9am post going forward.”

###  Steer Claude Tag explicitly

Claude adapts to instructions, but it won’t guess that you want it to. Tell it how to behave in this channel and ask it to remember. That works in both directions, whether you want more structure or less noise:

@Claude remember for this channel: always format reports as a table, and ask before posting anything longer than a screen.

@Claude remember for this channel: keep replies to three sentences unless someone asks for detail.

Verify what stuck by asking what it remembers about the channel. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

##  Work in the right place

Where you start a thread determines what Claude can reach, who else can pick the work up, and which standing conventions apply.

###  Pick the right surface

Channel access belongs to the channel, and DM access belongs to you. The table matches each kind of work to the surface it belongs on.

| Use a channel when | Use a DM when |
| The work is shared, or someone else might pick it up | The work is personal |
| The task needs the channel’s connections, like the issue tracker, the warehouse, or CI | The task needs your own connections |
| The result should be visible to the team | You’re handling data that shouldn’t run through a shared channel connection |
|  | You want a private answer about a public channel |

For that last case, name the channel in the DM: `summarize the last week of #product-feedback`. Claude’s Slack search covers public channels in this workspace from either surface; the DM advantage is privacy of the answer, not broader reach. Reading a channel’s full history directly needs Claude to be a member of it. It can’t reach channels in a different workspace or Slack Connect channels. If it says it can’t read a channel, `/invite @Claude` from inside that channel adds it.
When either would work, prefer the channel. Work that happens there compounds, because Claude can draw on it in later threads and teammates can find it, redirect it, or build on it.
If Claude says it can’t reach something in a channel, the channel likely wasn’t granted that access. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).

###  Teach Claude something that sticks

When Claude gets something wrong, or learns something worth keeping, where you put the fix decides who else benefits and whether you can do it yourself.

| You want Claude to know | Put it in | Who can write it | Reaches |
| --- | --- | --- | --- |
| How this channel should behave: format, tone, when to respond | [**Channel memory**](/docs/claude-tag/users/memory) (say it and ask Claude to remember) | Anyone in the channel | This channel (or workspace, from a public channel) |
| Conventions for one repository: file layout, PR labels, review rules | **`CLAUDE.md`** at the repo root ([loaded when the repo is](/docs/claude-tag/admins/configure-github#what-loads-from-a-repository)) | Anyone with repo write | Any session that works in that repo, from any channel |
| How to use a tool correctly, or follow a specific process, org-wide | [**A skill**](/docs/claude-tag/admins/skills-repo) in your org’s plugin marketplace | An organization Owner adds it; anyone can ask Claude to open a PR proposing the change | Every channel under the scope it’s attached to |
| Standing rules for a channel that outrank memory | [**Custom instructions**](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) on the scope | An organization Owner, in the console | Every session in that scope |

The first two are yours to write. For skills and custom instructions, an Owner attaches them, but you can still ask Claude to draft a skill change as a pull request for an admin to review:

@Claude that worked. Open a PR to the skills repo so this query pattern is part of the Datadog skill.

See [the admin guide to a skills repository](/docs/claude-tag/admins/skills-repo) for what that setup gives you.
A `CLAUDE.md` is guidance; a required status check is a gate. If a pull request must carry a label or pass a check, make that a repository rule rather than a memory note or a skill.

##  Keep thread count and review rate matched

Claude runs as many threads as you start. Your capacity to review them doesn’t scale the same way, because every thread that needs your judgment routes through you serially. Three conventions keep the queue manageable:

* **One channel per project.** Threads and the project’s working context stay in one place, and a glance at the channel shows the project’s state.
* **Batch your reviews.** Several threads in one sitting costs less than the same number spread across the day, because each return is a context reload.
* **Mark closed threads.** React ✅ to anything you consider done, and tell your digest routine to skip them.

* [Use case library](/docs/claude-tag/users/use-cases): the full setups these habits make reliable
* [What Claude Tag remembers](/docs/claude-tag/users/memory): make corrections stick

[Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds)[Set up routines](/docs/claude-tag/users/proactivity)
