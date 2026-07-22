<!-- source: https://claude.com/docs/government/org-admin/readiness -->

> **Who this is for:** Organization owners who are setting up an organization for the first time, or who need to find out why their users are unable to use Claude.

Use this page to see everything that is stopping people in your organization from using Claude, and where each blocker is resolved.
Your organization is ready when a member can sign in, hold a seat on a tier that reaches a working model, and send a message that the organization can pay for. This page runs that check and lists each step that is complete, blocked, or waiting on someone else. You would normally work through it once when the organization is first set up and then return whenever the **Settings** menu shows a notification dot, which appears whenever anything on this page needs attention.

##  How the checklist is presented

Each step sits on a vertical track with a status marker.

* A **green check** means the step is complete. The label is struck through and you can ignore it.
* A **filled circle** marks the step you should act on next. It expands to explain why it is blocked and offers an **Open** button that takes you to the page where the fix is made.
* A **clock** means the step is blocked but you are not the person who can clear it. A line underneath tells you whether it is waiting on Anthropic, on your tenant administrator, or on the owner of a shared billing account.
* A **hollow circle** is a step still to come. It stays collapsed until the steps ahead of it are cleared.

Use **Refresh** at the top right after you make a change elsewhere to see the updated state without leaving the page.

##  What each check means

* **Activate the tenant** appears on its own if your agency’s tenant is still being provisioned by Anthropic or has been deactivated. Nobody in any organization can sign in until this clears. Only Anthropic can resolve it, so contact your Anthropic representative.
* **Activate the organization** appears on its own if this organization has been deactivated. While it is inactive its members cannot sign in and none of the other checks can be cleared. Reactivation is handled by Anthropic. If the organization’s billing account has also been retired, the page explains that it must be assigned a new account before it can be brought back.
* **Add credits** checks that the organization’s credit balance is enough to cover at least one request on the cheapest model available to it. Until it is, every message from a user on a self-managed tier is refused. If you can manage this organization’s billing account directly, **Open Billing** takes you to the [Billing](/docs/government/org-admin/billing) page to allocate credits. Otherwise the step shows who to ask: your tenant administrator, or the owner of the organization that manages the shared billing account.
* **Allocate seats** checks that the organization has been allocated at least one seat of any tier. This is advisory. Without an allocation you can still assign tiers to people individually, but anyone who signs in before you do lands without a seat and cannot send messages. **Open Seats** or **Open Billing** takes you to the page where allocations are set, depending on how your billing account is managed. If the shared seat pool is already fully distributed, the step instead explains that the pool needs to be raised and shows who can do that.
* **Assign a model to your seat tier** checks that at least one seat tier in this organization can actually reach a working model, meaning a model that is enabled, priced, and allowed by a tier whose usage limits are high enough to cover a single request. If no tier qualifies, nobody can send a message regardless of credits or seats. **Open Tiers** takes you to the [Seat tiers](/docs/government/org-admin/seat-tiers) page to add a model or raise a tier’s limits. If every tier available to you is Anthropic-managed, only Anthropic can change its model list, so the step shows a waiting state.
* **Enable a product** checks that at least one Claude product, such as the desktop app, Claude Code, or Claude for Microsoft 365, is enabled for this organization. This is advisory. With nothing enabled, direct API access still works, but no client application can start. Enable a product on the [Config](/docs/government/org-admin/configuration) page.

* Every **Open** button goes to the page where the fix belongs. You make the change there and return here to see it reflected.
* If a step you expect to clear yourself is shown as waiting on your tenant administrator, it usually means the resource it checks is managed at the tenant level. Your tenant administrator can clear it from the [tenant Readiness page](/docs/government/tenant-admin/readiness), which shows every organization’s checklist in one place.
* Hover the help icon next to any step’s label for a one-line explanation of what the check looks for.

[Setup wizard](/docs/government/org-admin/setup-wizard)[Users](/docs/government/org-admin/users)
