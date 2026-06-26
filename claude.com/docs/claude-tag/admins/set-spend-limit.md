<!-- source: https://claude.com/docs/claude-tag/admins/set-spend-limit -->

[1 · Pair workspace](/docs/claude-tag/admins/pair-workspace)[2 · Give access](/docs/claude-tag/admins/add-connections)[3 · Spend limit](/docs/claude-tag/admins/set-spend-limit)[4 · Test it](/docs/claude-tag/admins/test-it)

Work Claude does in channels bills to your **organization’s usage balance**, not to individual seats. The **spend limit** is a cap you set on how much of that balance Claude in Slack can use each billing period. (DMs are separate: a DM bills to the user’s own seat, not to this balance.)

##  Whether this step is required depends on your plan

| Your plan | What you need to do here |
| **Team** | **Required, before anything runs.** A Team plan has no usage balance until it’s funded, and Claude won’t respond in channels until it is. A [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) counts as a funded balance, so check for one before buying credits. Then set a spend limit. |
| **Enterprise (invoiced)** | **Recommended.** Usage bills to your invoice with no upper bound until you set a spend limit. Set one to cap exposure during the pilot. |

##  Set the spend limit

1

Open the usage page

Go to [`claude.ai/admin-settings/usage/claude-in-slack`](https://claude.ai/admin-settings/usage/claude-in-slack).

2

Enter an amount

Enter an amount in your organization’s billing currency. The spend limit resets at the start of each billing period and applies across every paired workspace. You can change it any time.

There’s no published per-task cost guidance. For a pilot, set a spend limit you’re comfortable with for the first billing period, then watch the per-channel usage breakdown on the same page and adjust.

##  What happens when the spend limit is reached

When usage reaches the spend limit, Claude stops and tells the requester in the thread that it couldn’t finish. The requester can ask an admin to raise the limit.
The spend limit counts usage at list price. If your organization has a negotiated discount, that discount applies at invoice time, not to the cap.

##  Per-channel limits

Per-channel limits and the per-channel spend breakdown are on the same usage page. See [Set spend limits](/docs/claude-tag/admins/restrict-access#set-spend-limits) for the full set of controls.

* [Test your setup](/docs/claude-tag/admins/test-it): run a task in the pilot channel
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access#set-spend-limits): per-channel limits and the usage page in full

[2. Give Claude access](/docs/claude-tag/admins/add-connections)[4. Test your setup](/docs/claude-tag/admins/test-it)
