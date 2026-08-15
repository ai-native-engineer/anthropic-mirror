<!-- source: https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

# Claude Tag now reads even more of the room

Claude has more context to decide when to proactively collaborate in Slack (and when not to)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Tag](https://claude.com/product/tag)
* Date

  August 13, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

Claude Tag lets you add Claude to a Slack channel, where it works alongside your team. Claude responds when you @-mention it, or proactively when it thinks it can be helpful.

Before, Claude only saw **one message at a time**, so it made decisions to act proactively based on what was in front of it, but not the wider context of what was around it.

Now, Claude uses **context** **from across the channel**, as well as its memory and the standing instructions you have given it, to determine when to contribute to the conversation.

As a result, Claude is now roughly 30% better at determining when, and when not, to proactively respond.

This update comes at no additional cost today. While holding more context does increase Claude Tag’s usage, the additional context Claude Tag holds does not count toward usage or spend limits on any plan.

## From passive responder to active participant

Previously a lightweight classifier decided when Claude should act. It looked at each new message on its own and made one yes-or-no call.

For example, here are two engineers chasing the same bug from opposite ends. Neither has a free hour to run it down, and neither message asks for anything.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fea6_9120db7b.png)

Priya has a theory. Devon has the evidence. Neither message is for Claude, and neither asks for anything.

Read one at a time, neither message is for Claude, so the classifier correctly does nothing, twice. Read together, there's an obvious piece of work sitting there. One engineer has a theory, the other has the evidence for it, and nobody has time to check.

With the classifier removed, Claude uses context across the channel to make one of four moves:

* **Reply inline**, when the answer is short, verifiable, and something the channel doesn't already know.
* **Start deeper work in a thread**, when a message deserves real time.
* **Route the message to work it has in flight**, when it adds to a workstream Claude already has open.
* **Say nothing**, when nothing is called for.

Here's the same conversation with Claude Tag using additional context. Claude picks the second move, even without being @-mentioned. It sees Priya's hypothesis and Devon's evidence, opens a thread with the investigation already running, and pulls both engineers in. It acts within the boundaries of the permissions, tools, and scope you have configured.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fead_96b287d1.png)

Same thread, two minutes later. Claude reads the two messages together and starts the work. No @-mention.

The conversations aren't walled off from each other. So when Devon posts an update, it lands in the right workstream. When two investigations turn out to be the same bug, that connection gets made.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fea9_dcb183e0.png)

Claude now looks at all messages to understand the full context of the channel, to more accurately determine if it should participate in a conversation unprompted.

## How Claude decides when not to speak

An annoying agent is worse than an unhelpful one. We built Claude Tag to speak up only when it's useful, and in most channels, on most messages, that means saying nothing.

We do this by grading Claude’s channel-by-channel choices against a rubric based on principles like how useful the comment is, how confident Claude is in the response, and whether there is a person better suited to respond.

Claude also knows when to stop paying attention, similar to how people navigate Slack. It follows a few channels closely while paying less attention to others until someone tags it in. In a channel where, message after message, Claude keeps concluding it has nothing to add, it goes to sleep. A @-mention wakes it instantly.

You can also steer its response behavior in plain language: "Never respond here unless someone tags you," or "Feel free to jump in on anything about the deploy pipeline."

 And if you'd rather Claude only spoke in a channel when someone tags it, [any member can switch ‘**Respond automatically’** off](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off).

## The first reply is faster

The additional context also allows Claude to respond more quickly. It acknowledges you in seconds instead of operating silently while it starts up. The work itself takes as long as it always did; what's gone is the silent first minute when you couldn't tell whether it heard you.

## Live today

This update is now available across Claude Tag, available for Claude Teams and Enterprise customers. You can get started [here](https://claude.ai/admin-settings/claude-tag). Claude now acts as a more effective collaborator, one that can follow the conversation, decide for itself when to act, and when to stay out of the way.

Add Claude to one channel and watch what it adds to your conversations. Learn more about [Claude Tag](https://claude.com/product/tag).

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Nov 20, 2025

### What’s new in Claude: Turning Claude into your thinking partner

Product announcements

[What’s new in Claude: Turning Claude into your thinking partner](#)What’s new in Claude: Turning Claude into your thinking partner

[What’s new in Claude: Turning Claude into your thinking partner](https://claude.com/blog/your-thinking-partner)What’s new in Claude: Turning Claude into your thinking partner

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

Aug 12, 2026

### The Claude in Chrome side panel is now Claude Cowork

Product announcements

[The Claude in Chrome side panel is now Claude Cowork](#)The Claude in Chrome side panel is now Claude Cowork

[The Claude in Chrome side panel is now Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel)The Claude in Chrome side panel is now Claude Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 11, 2026

### Compliance API coverage extends to Claude Cowork and Claude Code

Enterprise AI

[Compliance API coverage extends to Claude Cowork and Claude Code](#)Compliance API coverage extends to Claude Cowork and Claude Code

[Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)Compliance API coverage extends to Claude Cowork and Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

Aug 5, 2026

### Inference hooks: inline data loss prevention for Claude Enterprise

Enterprise AI

[Inference hooks: inline data loss prevention for Claude Enterprise](#)Inference hooks: inline data loss prevention for Claude Enterprise

[Inference hooks: inline data loss prevention for Claude Enterprise](https://claude.com/blog/claude-enterprise-inference-hooks)Inference hooks: inline data loss prevention for Claude Enterprise

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Tag
