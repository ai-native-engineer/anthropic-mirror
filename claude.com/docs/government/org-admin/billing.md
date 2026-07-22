<!-- source: https://claude.com/docs/government/org-admin/billing -->

> **Who this is for:** Organization owners who can manage the billing account that funds their organization.

Use this page to check your account’s credit balance and seat pool, distribute credits to your organization, and adjust how many seats your organization holds.
What you see here depends on how your organization’s billing account is set up. When your organization shares a billing account that the tenant manages, this page is read-only: you can see the balance and the seat pool, but changes are made from the tenant portal. When your organization has its own dedicated billing account, an allocate form appears in each section and you can move credits and seats yourself as described below.
A **billing account** is the funding source that pays for one or more organizations in your tenant. It holds two things: a pool of **credits** (a prepaid dollar balance that self-managed seat tiers draw down as people use Claude) and a pool of **seats** for Anthropic-managed tiers. The **Billing** page shows the account that funds your organization and lets you adjust your organization’s share of both pools.

The **Billing** tab appears in the navigation only when you have permission to manage this billing account, the account is active, and your own organization is active on it. If any of those conditions is not met, the tab is hidden but the page is still reachable from a direct link and opens in read-only form. In that case funding is managed centrally by your tenant administrators, so contact them to request changes to credits or seat counts.

##  Who can make changes here

The permission to manage a billing account is attached to your actual user account. It does not carry over when a tenant administrator is acting as your organization, so a tenant administrator who needs to distribute credits or seats should do so from the tenant portal instead of from here.

##  Billing account

At the top you see how much credit has been allocated to your organization and how much of that allocation remains.

###  Distributing credits

Use the allocation form to move credits from the account’s available balance into your organization. Enter a positive dollar amount and submit. Once allocated, those credits become part of your organization’s balance and are consumed by your users’ activity on self-managed seat tiers. You can see your organization’s current balance, burn rate, and projected runway on the [Analytics](/docs/government/org-admin/analytics) page.
Credits move in one direction on this page: from the billing account into an organization. If you need to return unused credits to the account or move them to a different organization, contact a tenant administrator.
When your organization’s balance reaches 70 percent, 90 percent, and 100 percent consumed, a spend-alert banner appears on every page of the organization admin portal and an email is sent to your organization’s owners. The banner stays in place until more credits are added to your organization and cannot be dismissed; it escalates in color and wording as each higher threshold is crossed.

##  Seats

The **Seats** section shows the pool of Anthropic-managed seats funded by this account. For each tier the table shows the **Pool** total, which is the number of seats granted to the account, the **Distributed** count, which is how many of those seats have been handed out to organizations, and the **Remaining** count, which is the number still available to distribute.

The seat allocation editor below only appears when the account has at least one seat tier in its pool.

An editor below the table lets you set how many seats of each tier your organization holds. Enter the number you want for each tier and click **Save**. The change takes effect immediately.

###  Rules for changing seat allocations

The editor enforces the following rules and will refuse a save that violates any of them.

* You cannot request more seats for a tier than the billing account has remaining in its pool after accounting for other organizations.
* You cannot reduce a tier’s seat count below the number of users currently seated on it in your organization. Move users off the tier on the [Users](/docs/government/org-admin/users) page first, then lower the count.
* You can set a tier to zero seats, which removes the tier from your organization entirely, but only if no one is seated on it.
* Each tier’s seat count can be at most 100,000.

Saving a seat allocation also triggers a directory provisioning sync. If users were previously left unassigned because a tier was full, the sync will now seat them automatically up to the new limit.

[Compliance API](/docs/government/org-admin/compliance-api)[Config](/docs/government/org-admin/configuration)
