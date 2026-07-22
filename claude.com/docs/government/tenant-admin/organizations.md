<!-- source: https://claude.com/docs/government/tenant-admin/organizations -->

> **Who this is for:** Tenant administrators who create and oversee the organizations within their agency’s deployment.

Use this page to see every organization in your tenant, open any organization’s admin view, and create new organizations.

##  How organizations work

An **organization** is a workspace that holds a set of users, a set of seats, its own credit balance, and its own product settings. Users always belong to exactly one organization, and each organization is linked to exactly one **billing account** (the credit and seat pool that funds it).
Organizations share the tenant’s sign-in and provisioning setup. You configure single sign-on once on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page and every organization uses the same connection. What differs between organizations is who belongs to each one, and that is decided by the routing rules on that same page rather than here.

##  The organization list

Each organization appears with its name and ID. Clicking an organization’s name opens its organization admin view. When you do this you are acting as an administrator of that organization, and you can manage its users, seats, and settings exactly as one of its own owners would.

Which organization a user joins isn’t controlled on this page. That’s set by the routing rules on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page.

##  Adding an organization

Expand the **Add organization** section to create a new organization. You’ll provide the following:

* **Name** is what the organization will be called. Leading and trailing spaces are trimmed, and the name can be up to 256 characters. There is no uniqueness requirement, so you can create two organizations with the same name, but you generally shouldn’t.
* **Primary owner email** is the email address of the person who will be the new organization’s first administrator. This person becomes the Primary Owner and can immediately manage the organization’s users and settings. They do **not** become a tenant administrator; tenant-level access is granted separately on the [Admins](/docs/government/tenant-admin/admins) page.
* **Billing account** determines where the organization’s credits and seats come from. Choose an existing billing account from the list; the new organization draws from that account’s credit balance and seat pool alongside any other organizations already on it. Only billing accounts that are active and tenant-managed appear in the list.

If the list is empty, your tenant has no active tenant-managed billing accounts yet. Contact Anthropic to have one set up.

###  After you add an organization

The new organization appears in the list immediately and you can click through to its organization admin view. A few follow-up steps are usually needed before people can use it:

* Add a routing rule on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page so that the right people are placed in the new organization when they sign in or are provisioned. Until a rule targets the new organization, nobody will land there automatically.
* Give it seats on the [Seats](/docs/government/tenant-admin/seats) page. A newly created organization starts with no seats distributed to it.
* Allocate credit to it on the [Billing](/docs/government/tenant-admin/credits) page once its billing account has a balance.

> **For organization owners:** Being named the primary owner of a new organization does **not** make you a tenant administrator. Tenant admin access is granted separately on the [Admins](/docs/government/tenant-admin/admins) page.

* You cannot delete an organization from this page. If an organization is no longer needed, contact Anthropic to have it deactivated. Routing rules that target a deactivated organization stop matching, and users in a deactivated organization cannot sign in until it is reactivated or they are moved.
* Organization names can be changed later from the organization’s own admin view.
* There is no fixed limit on the number of organizations you can create, but each one adds a row to your seat distribution and configuration surfaces, so create only as many as you need to keep administration manageable.

[Readiness](/docs/government/tenant-admin/readiness)[Identity and access](/docs/government/tenant-admin/identity-and-access)
