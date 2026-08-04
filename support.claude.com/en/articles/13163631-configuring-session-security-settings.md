<!-- source: https://support.claude.com/en/articles/13163631-configuring-session-security-settings -->

# Configuring session security settings

May 7, 2026

This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

## Enabling session length settings

### For Enterprise Admins

1. Log in to your Enterprise organization as an Admin or above.
2. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 7 days, 14 days, or 28 days.
5. Confirm your selection by clicking “Enable.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1785803400&signature=c7ae570098b7f8fa1572016e15aa318da11fda3bf08edf3b46b11a93193c2d3d&req=dSgvHs14lIVcX%2FMW1HO4zQNx6%2BcvQ1lUg%2F6XaftFnjxMPEAMo43FYC7ocJFs%0ABoEFu97Cv4D98VPFc0s%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1785803400&signature=c7ae570098b7f8fa1572016e15aa318da11fda3bf08edf3b46b11a93193c2d3d&req=dSgvHs14lIVcX%2FMW1HO4zQNx6%2BcvQ1lUg%2F6XaftFnjxMPEAMo43FYC7ocJFs%0ABoEFu97Cv4D98VPFc0s%3D%0A)

### For Console Admins

1. Log in to your Console account as an Admin.
2. Navigate to **[Settings > Organization and access](http://platform.claude.com/settings/organization)**.
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.
5. Confirm your selection by clicking “Enable.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1785803400&signature=921f37c58d7f08ce0cabc4c4ff992d1965963b80b97bd646b6fb2a768b5cdd1b&req=dSgvHs14lIVcXPMW1HO4zWzx2Lw%2BJ3wlXZ5D7eVpMteisD7P%2F2P5MKOIAFgt%0AT6bQixucClGZd8lZejs%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1785803400&signature=921f37c58d7f08ce0cabc4c4ff992d1965963b80b97bd646b6fb2a768b5cdd1b&req=dSgvHs14lIVcXPMW1HO4zWzx2Lw%2BJ3wlXZ5D7eVpMteisD7P%2F2P5MKOIAFgt%0AT6bQixucClGZd8lZejs%3D%0A)

### What happens after enabling shortened session length?

* Existing sessions older than the selected duration will expire immediately.
* Other active sessions will expire no later than the selected duration.
* Users whose sessions expire will be directed to sign in again.

## Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

* Sessions older than the new duration will expire immediately.
* Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1785803400&signature=06f813acaa04204462ee6a94132c0874c3c2513afdde0fc927f7f8f1b33e6ad5&req=dSgvHs14lIVcXvMW1HO4zZ7mWs2T5zqnA00cbyPOLDWDhN%2F%2FgEBF%2FSdH%2BeSv%0AKEkj5q1wziqEYbATtX8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1785803400&signature=06f813acaa04204462ee6a94132c0874c3c2513afdde0fc927f7f8f1b33e6ad5&req=dSgvHs14lIVcXvMW1HO4zZ7mWs2T5zqnA00cbyPOLDWDhN%2F%2FgEBF%2FSdH%2BeSv%0AKEkj5q1wziqEYbATtX8%3D%0A)

## Disabling session length settings

To disable session duration, select "Disable" next to **Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

## Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.

* [Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
* [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
* [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
* [Claude Code on Console to Enterprise migration](https://support.claude.com/en/articles/14128775-claude-code-on-console-to-enterprise-migration)
* [Claude Enterprise activation promo for Claude Code and Cowork](https://support.claude.com/en/articles/15282265-claude-enterprise-activation-promo-for-claude-code-and-cowork)
