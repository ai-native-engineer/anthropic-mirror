<!-- source: https://claude.com/docs/government/tenant-admin/seats -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators who distribute purchased seats to the organizations in their deployment.

Use this page to divide each billing account’s seat pool among the organizations that account funds.

##  How seats are organized

A **seat** is what entitles one person to use Claude. Every seat belongs to a **seat tier**, which is a named level of access that determines how much a person in that seat may use (for example, different usage limits per tier).
Seats live in **billing accounts**, which are the credit and seat pools Anthropic sets up with your agency. Anthropic grants each billing account a pool of seats, broken down by tier. Every organization is linked to exactly one billing account, and on this page you divide each account’s pool among the organizations it funds. For each tier, the totals you hand out across those organizations can’t exceed what’s in the pool.
Seat distribution is a two-step process. On this page you give each organization a number of seats per tier. Organization owners then assign those seats to individual people in the organization admin portal.

##  What the page shows

Billing account cards only appear once Anthropic has set up at least one billing account for your tenant. Until then, the page shows a message asking you to contact Anthropic.

Each billing account appears as its own card, and each card contains the following:

* The **seat pool** table shows each seat tier with the pool size, how many seats have been distributed across organizations, and how many remain. A negative **Remaining** number (shown in red) means the pool was reduced after seats were distributed; contact Anthropic to adjust the pool, or reduce some organizations’ allocations.
* The **organizations** section lists every organization funded by this account, and each one has a number field per tier showing its current allocation.

##  Changing an organization’s seats

Edit the number fields next to an organization’s name and click **Save**. Saving replaces that organization’s allocation across all tiers at once. Changes take effect immediately: newly added seats are available for the organization’s owners to assign right away.
The save will be rejected in a few cases:

* If the totals you entered across all of an account’s organizations would exceed the pool for any tier, you’ll see an error explaining which tier is over.
* If you try to reduce a tier below the number of people (and service accounts) already seated on it in that organization, you’ll see an error. Ask the organization’s owners to unassign people from that tier first, then reduce the allocation.
* Similarly, you cannot remove a tier from an organization entirely (by setting it to zero) while anyone is still seated on it there.

##  How seats affect new users

When a new person is placed in an organization (by a routing rule on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access) page), they’re automatically given a seat if one is free. Tiers are filled in a fixed order, so the first tier is filled before the next is started. If every tier the organization has is completely full, the new person is placed in the organization without a seat. They can sign in and see the portal, but cannot send messages to Claude until an owner assigns them a seat or you distribute more seats here.
An organization that has no seat allocation at all is treated as uncapped. New users can join and use Claude, but this is unusual; normally every active organization has at least one tier allocated.

##  When you can’t edit

You’ll see a note instead of the editor in a few situations:

* If the billing account is **deactivated**, its seats can’t be redistributed. Contact Anthropic to move its organizations to an active account.
* If the account is **managed by one organization’s administrators** rather than by tenant administrators, you won’t be able to edit it here; the owning organization controls its own distribution.
* If the account has **no seat pool yet**, contact Anthropic to set one up.

##  Things to know

* Reducing an organization’s allocation never unassigns anyone automatically. The reduction is refused until enough people have been moved off the tier.
* You can freely move seats between organizations on the same billing account by lowering one and raising another, as long as neither change violates the rules above. You may need to save the reduction first to free the pool, then save the increase.
* Seat pools are set by Anthropic. If you need more seats in a tier, or a new tier added, contact Anthropic.
