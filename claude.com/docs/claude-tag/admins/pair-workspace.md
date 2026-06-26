<!-- source: https://claude.com/docs/claude-tag/admins/pair-workspace -->

[1 · Pair workspace](/docs/claude-tag/admins/pair-workspace)[2 · Give access](/docs/claude-tag/admins/add-connections)[3 · Spend limit](/docs/claude-tag/admins/set-spend-limit)[4 · Test it](/docs/claude-tag/admins/test-it)

Role you needOwner in your Claude organization, plus a Slack workspace admin to install the app and generate the pairing code. These can be the same person or two people.

Before this stepThe [prerequisites](/docs/claude-tag/admins/setup-overview#before-you-start): confirm your role and decide where you’ll pilot

Do I need this?RequiredNothing else in setup works until a workspace is paired.

##  Install and pair

Pairing has three parts: install the app in Slack, get a code from Slack, and paste it in the Claude console.

1

Install the Claude app in Slack

Open [claude.com/claude-for-slack](https://claude.com/claude-for-slack), click **Add to Slack**, and approve the permissions Slack shows. Skip if the app is already installed.

2

Run @Claude connect in Slack

Send `@Claude connect` in any channel or in a DM with `@Claude`. Claude replies with a pairing code. Only a Slack workspace admin (or Grid org admin) can run this command; if that’s not you, [send them the install request](#send-the-install-request-to-your-slack-admin) and have them return the code.If your install is missing a permission, the reply names it (and may still issue a code with a warning); see [the section below](#if-claude-connect-says-the-installation-is-out-of-date).

3

In the console: run the setup wizard

At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), select **Set up** (or **+ Connect** next to **Where Claude Tag works** if a workspace is already paired) to open the **Set up Claude Tag for your workspace** wizard. Paste the code, choose whether to enable Claude for the whole workspace or specific channels, and click **Next**.

The wizard moves straight on to giving Claude access, so there’s nothing to check at this point; continue with [Give Claude access](/docs/claude-tag/admins/add-connections). After the wizard finishes, the Slack row under **Where Claude Tag works** shows your workspace as connected, and a [scope](/docs/claude-tag/concepts/glossary#scope) for it (the entry where you’ll bind tool access) appears on the **Slack** tab under **Claude Tag’s access**.

##  Send the install request to your Slack admin

Steps 1–2 above need a Slack workspace admin; step 3 needs an Owner in your Claude organization. If those are two people, send the Slack admin this and have them return the code:

Please install the Claude app (https://claude.com/claude-for-slack) in [workspace], then run "@Claude connect" in any channel and send me the code it returns. What it can access: https://claude.com/docs/claude-tag/admins/for-slack-admins

###  If `@Claude` doesn’t respond at all

On Enterprise Grid, an earlier install can lose its connection and stop responding in every workspace. Don’t uninstall the app. Have a Slack Org Owner or Org Admin, while signed in to one of the workspaces (not the org-level admin page), open [claude.com/claude-for-slack](https://claude.com/claude-for-slack), select **Add to Slack**, and choose **Install to entire organization**. This refreshes the connection in place. Then run `@Claude connect` again.

###  If `@Claude connect` says the installation is out of date

Your Slack install predates a permission the app now requests. The reply names the missing scope and includes a **reinstalls the Claude app** link. A Slack workspace admin clicks that link (or opens [claude.com/claude-for-slack](https://claude.com/claude-for-slack) and clicks **Add to Slack** again), approves the consent screen Slack shows, then runs `@Claude connect` again. This installs over the existing app; do not uninstall first.
Slack’s **Manage apps** page lists the scopes the app requests, not the scopes your workspace has granted, so seeing a permission listed there does not mean it is approved. The grant happens on the consent screen.

###  If the console says “already connected to a different organization”

A Slack workspace can pair with only one Claude organization at a time, and this one is already paired elsewhere. An Owner in the Claude organization that currently holds the pairing must [disconnect it](/docs/claude-tag/admins/workspaces#revoke-a-pairing) from their **Connected workspaces** list before your code can be redeemed here. If your company has more than one Claude organization, check the others; the existing pairing is often in a test or trial org.

###  If the console says “claim code is invalid, expired, or already used”

Pairing codes are single-use and expire after a short window. Ask the Slack admin to send `@Claude connect` again and paste the fresh code; reinstalling the app is not required. On Enterprise Grid, a Grid org admin’s reply includes a Grid-wide code alongside the workspace code.

##  After pairing: where Claude is enabled

Once a workspace is paired, where Claude responds depends on what you chose in the wizard (whole workspace or specific channels), the **Turn on Claude Tag** toggle, and your [Members](/docs/claude-tag/admins/restrict-access#members) setting.

* **What Claude can reach** in each channel depends on which Access bundles you bind; see [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope).
* **Nothing runs until usage is funded** on Team plans; see [Set a spend limit](/docs/claude-tag/admins/set-spend-limit).
* **DMs work separately** from channels and run on each user’s own claude.ai account; pairing isn’t what enables DMs.

* [Give Claude access](/docs/claude-tag/admins/add-connections): create an Access bundle and add connections
* [What the Claude Slack app can access](/docs/claude-tag/admins/for-slack-admins): the page to send a Slack admin who’s approving the install

[Set up Claude Tag](/docs/claude-tag/admins/setup-overview)[2. Give Claude access](/docs/claude-tag/admins/add-connections)
