<!-- source: https://academy.claude.com/use-cases/meeting-notes-and-filed-tasks-from-a-call-transcript -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Create meeting notes and tasks from a call transcript

With proactive replies on in the project channel, Claude Tag reads each transcript the call recorder posts, replies with the decisions and action items, files the tickets and publishes the notes as a page.

10 minOperationsClaude Tag

![](https://academy.claude.com/assets/v1/thumbnail.light-hd84bxm1.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-fxufp05i.png)

After a project or customer call, someone usually writes up the decisions and action items and copies them into the tracker.

With Claude Tag, connect the tracker to the project channel where your call recorder posts transcripts. Then give Claude Tag the job as a **[standing responsibility(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity#set-up-standing-work)**. With **[proactive replies(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off)** on for the channel, Claude picks up each transcript post that tags it, so no one on the team has to tag it, and posts the decisions and action items in its thread. It files the tickets and publishes **[the notes as a page(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts#ask-for-a-hosted-page)** there. From there, anyone in the thread can follow up to adjust Claude's output, like to correct an owner or date.

## Set up[](#set-up)

**Make sure Claude is in the channel:** `/invite @Claude`.

**Check what tools are connected:** `@Claude what can you access from this channel?`

For help, ask your admin or visit our [troubleshooting docs(opens in new tab)](https://claude.com/docs/claude-tag/users/troubleshooting).

## What to ask Claude, and what it does[](#what-to-ask-claude-and-what-it-does)

Send this once in your project channel. From then on, each time the recorder posts a transcript, Claude reads it and replies in that post's thread. Ask Claude to file tickets only if its tracker connection in this channel can create them, and name the board if there is more than one.

The recorder posted the transcript below the following Wednesday, and nobody tagged Claude:

The recorder includes @Claude in each transcript post. With Respond automatically on, Claude replied without a person tagging it. The tickets are under Claude's name, and nothing was sent to the customer.

Before anyone starts on a ticket, read the action items against the transcript, and correct an owner or a date in the thread.

## Follow ups[](#follow-ups)

### Correct an owner in the thread[](#correct-an-owner-in-the-thread)

Anyone in the thread can correct Claude with a plain reply, and Claude updates the ticket and the page to match ([reply in the thread to steer(opens in new tab)](https://claude.com/docs/claude-tag/concepts/how-it-works#reply-in-the-thread-to-steer)). Sam, who was on the call, replies under the notes:

### Ask for a decision doc instead[](#ask-for-a-decision-doc-instead)

Claude writes whichever document you name from the same thread, so when a call settled one question, ask for a decision doc instead of notes ([turn threads into docs(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts)).

### File one more ticket from the thread[](#file-one-more-ticket-from-the-thread)

When someone in the thread raises a new task and names an owner, ask Claude to file it. Claude posts the ticket link in the thread.

### Have Claude reply only when tagged[](#have-claude-reply-only-when-tagged)

With Respond automatically off, Claude replies only when a person tags it, and posts from the recorder are ignored until someone in the channel turns it back on ([quiet the whole channel(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#quiet-the-whole-channel)).

## Related resources[](#related-resources)

* Learn more in the [Introduction to Claude Tag(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag) course.
* [Get started with Claude Tag(opens in new tab)](https://claude.com/docs/claude-tag/users/getting-started): add @Claude to a channel and see what it can read there.
* [Turn threads into docs and tickets(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts): the Claude Tag docs on documents, tickets and hosted pages from a thread.

* [Set up](#set-up)
* [What to ask Claude, and what it does](#what-to-ask-claude-and-what-it-does)
* [Follow ups](#follow-ups)
* [Related resources](#related-resources)
