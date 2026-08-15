<!-- source: https://claude.com/docs/government/tenant-admin/configuration -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators who set and enforce product settings across every organization in their tenant.

Use this page to set tenant-wide defaults for product behavior, lock settings so organizations can’t change them, and preview how a change would affect each organization.
The Config page works the same way at the tenant and organization levels, with the same list of settings. See [How Config works](https://claude.com/docs/government/config/overview) for the levels model, locks, groups, comparing across levels, and looking up one person’s settings, and [Available settings](https://claude.com/docs/government/config/settings) for what each setting does. This page covers only what is specific to the tenant level.

##  What is specific to the tenant level

**Previewing impact across organizations.** After you change a setting here, a **Preview impact** button appears next to **Save changes**. It shows every organization with its current effective value and what it would become after your change. See [Previewing impact](https://claude.com/docs/government/config/overview#previewing-impact). This button does not appear at the organization level.
**Two settings that only tenant administrators can change.** [Let organizations manage their own seat tiers](https://claude.com/docs/government/config/settings#let-organizations-manage-their-own-seat-tiers) and [Compliance API](https://claude.com/docs/government/config/settings#compliance-api) are always read-only for organization owners, regardless of whether they are locked.
**Group priority order.** You set the priority order between directory groups on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access) page by dragging the groups into the order you want. Organization owners see this order for reference but cannot change it. See [When someone belongs to more than one group](https://claude.com/docs/government/config/overview#when-someone-belongs-to-more-than-one-group).
**Managing any organization’s config.** As a tenant administrator you can open any organization’s Config page and act on that organization’s behalf, using the scope bar above the settings list. Organization owners see only their own organization.
**Resetting a tenant setting** removes only the tenant’s value. Organization values are unaffected and remain in effect once your value is gone.
