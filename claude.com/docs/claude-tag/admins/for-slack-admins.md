<!-- source: https://claude.com/docs/claude-tag/admins/for-slack-admins -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

You’re approving the Claude app install for someone who’s setting up Claude Tag. This page covers what the app can do in your Slack workspace. The rest of setup happens on their side, in the Claude console; you don’t need a Claude account.

##  Where Claude reads and posts

Claude reads and posts only in channels a workspace member has added it to, and in direct messages with users who link their own Claude account. Installing the app does not add it to any channel.
A member can add Claude with `/invite @Claude`, or Claude can join a public channel itself when a member asks it to (the `channels:join` scope). Either way, a person in your workspace initiates it; Claude does not join channels on its own.
Reading a channel’s full history requires being added there. Workspace search can surface public-channel content, the same as any app with the search scope.
Slack Connect channels (shared with another company) are always excluded, regardless of configuration.

##  Requested scopes

The app requests bot scopes for reading and posting in channels it’s a member of, reactions, files, canvases, user lookup, and public-channel search. Slack’s install consent screen shows the full current list; treat that as the canonical reference, since the set can change between releases.
Two scopes a Slack admin commonly asks about:

* `channels:join` lets Claude add itself to a public channel when a workspace member directs it there. It cannot join private channels this way.
* `users:read.email` lets Claude match a Slack member to their Claude account by email, so a person who DMs Claude is recognized without a separate linking step.

##  What installing does not grant

Credentials for GitHub, Google Drive, a data warehouse, or anything else are provisioned separately by a Claude organization Owner and live on Anthropic’s side rather than in Slack.
It responds when @-mentioned, and may respond to other messages it judges warrant a reply.

##  After you install

Post `@Claude connect` as a new top-level message in any channel (with no other text) or in a direct message with `@Claude`, and send the code it returns to whoever asked you to install. Posted as a reply inside a thread, the command is treated as a normal request and no code is issued. That code is what pairs your workspace to their Claude organization; it expires after 15 minutes.

##  Related resources

* [Security and data handling](https://claude.com/docs/claude-tag/concepts/security-and-data): where credentials are stored and what leaves your workspace
* [Pair your Slack workspace](https://claude.com/docs/claude-tag/admins/pair-workspace): what the Claude Owner does with the code you send
