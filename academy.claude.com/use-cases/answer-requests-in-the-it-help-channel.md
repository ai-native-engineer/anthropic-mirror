<!-- source: https://academy.claude.com/use-cases/answer-requests-in-the-it-help-channel -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Answer requests in the IT help channel

Give Claude Tag a standing responsibility in the IT help channel: it answers each request first from your policies, asks for missing details, and files one ticket for the owner when a request needs them.

10 minOperationsClaude Tag

![](https://academy.claude.com/assets/v1/thumbnail.light-g2rf84ww.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ncxwpfp1.png)

Most requests in an internal help channel first need either an answer from the team's policies or a question back to the requester about a detail they left out. With Claude Tag in an IT help channel, Claude can give every request that first response from the knowledge base. When a request needs the owner's decision, Claude files one complete ticket for them.

Connect the IT knowledge base and the ticket queue to the channel and give Claude Tag the job as a **[standing responsibility(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity#set-up-standing-work)**. With **[proactive replies(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off)** on, Claude replies to each new request in its thread without being tagged. When something needs the owner, it **[files the ticket(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts)** with the context and assigns it to them. The owner still makes the decision.

## Set up[](#set-up)

**Make sure Claude is in the channel:** `/invite @Claude`.

**Check what tools are connected:** `@Claude what can you access from this channel?`

For help, ask your admin or visit our [troubleshooting docs(opens in new tab)](https://claude.com/docs/claude-tag/users/troubleshooting).

## What to ask Claude, and what it does[](#what-to-ask-claude-and-what-it-does)

Send this once in your IT help channel. From then on, Claude answers each new request in its thread, asks for anything missing and passes what it cannot resolve to the owner. If the channel's history does not show who the owner is or where the policies are kept, add both to your message.

Ravi posted the question below a week later, without tagging Claude:

Claude answered from the policy and filed nothing until Ravi replied.

For the first weeks, the owner reads some of Claude's answers and opens the linked article to check each one against the policy. Where an answer does not match, the owner corrects Claude in the thread.

## Follow ups[](#follow-ups)

### File the request for the owner to approve[](#file-the-request-for-the-owner-to-approve)

Anyone in the thread can answer Claude without tagging it again. If the ticketing tool is connected to this channel with write access, Claude files the request under its own name and assigns it to the owner ([turn threads into tickets(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts)).

### Tell Claude who handles which kind of request[](#tell-claude-who-handles-which-kind-of-request)

Claude keeps instructions for the channel in [channel memory(opens in new tab)](https://claude.com/docs/claude-tag/users/memory), which anyone in the channel can read and correct. When the same kind of request keeps coming in, the owner can add who handles it and how to treat duplicates. Claude then applies it to every later request in the channel.

### Get a weekly summary of requests[](#get-a-weekly-summary-of-requests)

Claude can post a summary of the week's requests as a [routine(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity#scheduled-jobs), including posts that did not tag it. Add your time zone to the time.

### Make Claude mention-only in a channel[](#make-claude-mention-only-in-a-channel)

The channel's Respond automatically setting decides whether Claude answers messages that do not tag it, and anyone in the channel can turn it off by asking ([quiet the whole channel(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#quiet-the-whole-channel)). Requesters then include @Claude in their posts.

## Tips[](#tips)

### Correct Claude in the thread and ask it to remember[](#correct-claude-in-the-thread-and-ask-it-to-remember)

When Claude answers a request that should have gone to the owner, or sends the owner one it could have answered, the owner says so in that thread and asks Claude to update its memory for the channel. Claude applies the correction to later requests.

## Related resources[](#related-resources)

* Learn more in the [Introduction to Claude Tag(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag) course.
* [Get started with Claude Tag(opens in new tab)](https://claude.com/docs/claude-tag/users/getting-started): add @Claude to a channel and see what it can read there.
* [Triage requests(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/triage-requests): the Claude Tag docs on triaging a request channel.

* [Set up](#set-up)
* [What to ask Claude, and what it does](#what-to-ask-claude-and-what-it-does)
* [Follow ups](#follow-ups)
* [Tips](#tips)
* [Related resources](#related-resources)
