<!-- source: https://claude.com/docs/government/tenant-admin/credits -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators who allocate usage credits to the organizations in their deployment.

Use this page to move credit from your billing accounts onto the balances of the organizations they fund.

The **Billing** tab appears in the navigation only when credits apply to your tenant, which means at least one organization can use credits or there is a credit balance on any billing account or organization in your tenant. If neither is true, the tab is hidden and **Seats** appears on its own in the navigation, but this page is still reachable from a direct link and shows a short message explaining that billing does not apply. In that case there is nothing to set up here, and the tab appears automatically once Anthropic configures billing for your tenant.

##  How credits work

A **billing account** is a funding container that Anthropic sets up for your tenant. It holds a dollar balance of credit. Each organization is linked to exactly one billing account, and several organizations may share the same one.
When you **allocate** credit, you move a dollar amount from a billing account onto a specific organization’s own balance. Usage in that organization then draws down the organization’s balance, not the billing account’s. Because each organization holds its own balance, one organization running out of credit never affects another, even if they share a billing account.

##  What the page shows

Billing account cards only appear once Anthropic has set up at least one billing account for your tenant. Until then, the page shows a message asking you to contact Anthropic.

Each billing account appears as its own card, and each card shows the following:

* The **available balance** is the credit remaining in the account that hasn’t yet been allocated to any organization.
* A count of how many organizations this account funds. Open an organization’s own admin view to see its remaining balance.

##  Allocating credit

In a billing account’s card, pick an organization (if the account funds more than one), enter a dollar amount up to the available balance, and click **Allocate**. The amount is moved from the account to that organization’s balance immediately. The minimum allocation is one dollar, and you can use cents.

Allocating is one-way. Credit that has been moved to an organization can’t be returned to the billing account from this page.

##  When you can’t allocate

You’ll see a note instead of the form in a few situations:

* If the account’s available balance is **zero**, there’s nothing left to allocate. Contact Anthropic to add credits.
* If the account is **deactivated**, its organizations can’t receive new credit. Contact Anthropic to move them to an active account.
* If the account is **managed by one organization’s administrators** rather than by tenant administrators, you won’t be able to allocate from it here; the owning organization controls its own allocations.

##  Things to know

* If an organization is deactivated, any unspent credit on its balance is returned to its billing account automatically as part of deactivation.
* The available balance is enforced at the moment you submit. If another administrator allocates from the same account between when the page loaded and when you click Allocate, your request may be rejected for exceeding the balance; refresh and try again with a smaller amount.
* Credit is added to billing accounts by Anthropic, typically as part of your agency’s procurement. New organizations with a new dedicated billing account start with a zero balance until Anthropic funds the account.
