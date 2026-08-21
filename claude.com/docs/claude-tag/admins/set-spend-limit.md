<!-- source: https://claude.com/docs/claude-tag/admins/set-spend-limit -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

[1 · Pair workspace](https://claude.com/docs/docs/claude-tag/admins/pair-workspace)[2 · Give access](https://claude.com/docs/docs/claude-tag/admins/add-connections)[3 · Spend limit](https://claude.com/docs/docs/claude-tag/admins/set-spend-limit)[4 · See it work](https://claude.com/docs/docs/claude-tag/admins/test-it)

Work Claude does in channels bills to your **organization’s usage balance**, not to individual seats. The **spend limit** is a cap you set on how much of that balance Claude Tag can use each billing period.

| Work | Bills to | Capped by |
| --- | --- | --- |
| Channel work | Your organization’s usage balance | The spend limit, plus any [per-channel limits](https://claude.com/docs/claude-tag/admins/restrict-access#set-spend-limits) |
| Reading a channel, [deciding whether to reply](https://claude.com/docs/claude-tag/users/when-claude-responds#what-claude-does-with-a-channel-message), and short replies from what Claude already knows | Nothing | Not counted toward any limit. A working session Claude starts from the channel is channel work, above |
| A DM with Claude | The sender’s own seat | The seat’s usual limits, not the spend limit |

##  Whether this step is required depends on your plan

| Your plan | What you need to do here |
| --- | --- |
| **Team** | **Required, before anything runs.** A Team plan has no usage balance until it’s funded, and Claude won’t respond in channels until it is. A [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) counts as a funded balance, so check for one before buying credits. Then set a spend limit. |
| **Enterprise (invoiced)** | **Recommended.** Usage bills to your invoice with no upper bound until you set a spend limit. Set one to cap exposure during the pilot. |

##  Set the spend limit

If your organization bills through a reseller, this page is not available and these steps don’t apply; your organization’s usage is funded through the reseller instead.

1

Open the usage page

Go to [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag).

2

Enter an amount

Enter an amount in your organization’s billing currency. The spend limit resets at the start of each billing period and applies across every paired workspace. You can change it any time.

There’s no published per-task cost guidance. For a pilot, set a spend limit you’re comfortable with for the first billing period, then watch the per-channel usage breakdown on the same page and adjust.

##  What happens when the spend limit is reached

When usage reaches the spend limit, Claude stops and tells the requester in the thread that it couldn’t finish. The requester can ask an admin to raise the limit.
The spend limit counts usage at list price. If your organization has a negotiated discount, that discount applies at invoice time, not to the cap.

###  Rate limits versus the spend limit

The spend limit caps how much your organization is charged. It doesn’t change how fast Claude can work. Claude Tag also applies its own throughput limits on how quickly threads can be started and messages delivered, and an organization with many busy channels can hit one while the spend limit still has plenty of room.
When that happens, Claude tells the requester in the thread that it hit a rate limit and names a short wait, usually a few seconds. Re-send the message after the wait. Raising the spend limit doesn’t clear a rate limit, and a rate-limited request doesn’t spend anything.

| Claude says | Limit reached | What to do |
| --- | --- | --- |
| The spend limit is reached | Spend limit | Raise it on the usage page above |
| It hit the session rate limit, or is rate limited delivering a message | Throughput limit | Wait the few seconds the reply names, then re-send. If your organization hits this often, contact your account team. |

##  Per-channel limits

Per-channel limits and the per-channel spend breakdown are on the same usage page. See [Set spend limits](https://claude.com/docs/claude-tag/admins/restrict-access#set-spend-limits) for the full set of controls.

##  Attribute costs by channel

Channel work can’t be attributed to individual users. It bills to your organization’s usage balance, not to any user’s seat, and often has no single requesting user (several people contribute to one thread, and scheduled jobs run without anyone asking). The channel is the unit you can attribute.
The usage page at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag) shows spend broken down by channel.
To attribute spend to teams or departments for showback or chargeback reporting, structure channels so each maps to one team or department, and give those channels [their own scopes](https://claude.com/docs/claude-tag/admins/attach-to-scope). The per-channel breakdown then reads as your per-team report, and per-channel spend limits act as team-level budgets.
DMs are separate. A DM bills to the sender’s own seat, not to the organization’s usage balance.

##  Related resources

* [See it work](https://claude.com/docs/claude-tag/admins/test-it): run a first task in the pilot channel
* [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access#set-spend-limits): per-channel limits and the usage page in full
