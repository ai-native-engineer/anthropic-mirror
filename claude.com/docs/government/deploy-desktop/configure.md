<!-- source: https://claude.com/docs/government/deploy-desktop/configure -->

> **Who this is for:** IT administrators who install Claude Desktop on agency devices and connect it to their agency’s Claude for Government deployment.

A fresh install of Claude Desktop connects to claude.ai. To connect it to Claude for Government instead, each device needs one managed setting that tells the app where your deployment lives. Once that setting is in place, everything else that governs the app (enabled products and tabs, model access, [connectors](/docs/government/connectors/overview), usage limits, the desktop banner) is controlled through the [tenant](/docs/government/tenant-admin/configuration) and [organization](/docs/government/org-admin/configuration) configuration pages in this portal and delivered to each user when they sign in.
You can apply the setting by hand on a single machine, which is useful for confirming your deployment address before a wider rollout, or deploy it to your fleet through your device management system. The single-machine path can export profiles for the fleet path, so it is usually worth doing first.

##  Before you begin

* **User accounts exist.** Claude Desktop signs users in to the same accounts as this portal. For each user, including your own test account, check with your tenant administrators that the user can sign in (a [routing rule](/docs/government/tenant-admin/identity-and-access) covers them) and has a [seat tier](/docs/government/org-admin/seat-tiers) with at least one model enabled.
* **Devices can reach your deployment.** Claude Desktop on every device must reach your deployment address over HTTPS on port 443. That one address carries the app’s configuration and chat traffic.
* **Browsers can reach sign-in.** Sign-in happens in the user’s default web browser, not in the app. Browsers on each device must reach your deployment address, your deployment’s sign-in service (a separate address that your Anthropic representative provides), and your agency’s identity provider.
* **The app is current.** This configuration mechanism requires Claude Desktop 1.10628.0 or later. The [general deployment guides](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos) cover where to download the installer and how to distribute it.

##  The setting you deploy

The setting is called `bootstrapUrl`, and its value is your deployment address followed by the fixed path `/gateway-api/user/bootstrap`.

```
https://<your-deployment-host>/gateway-api/user/bootstrap
```

Your deployment address is the same host as this portal. If you are unsure of it, ask your Anthropic representative. The app uses the address exactly as entered; it fetches each user’s configuration from it and derives the location of the sign-in service from it, so include the full path.

##  Configure a single machine

Claude Desktop has a built-in configuration window that is hidden until you enable developer mode. These steps use it to set the address on one machine without any management tooling.

1

Launch the app without signing in

Install Claude Desktop on the test machine and open it. The claude.ai sign-in screen appears; this is expected before the app is configured. Stay on this screen.

2

Enable developer mode

From the **Help** menu, choose **Troubleshooting**, then **Enable Developer Mode**, and confirm the prompt. On Windows the **Help** menu is under the application menu (☰) on the sign-in screen. The app relaunches with a **Developer** menu added.

3

Open the configuration window

From the **Developer** menu, choose **Configure Third-Party Inference**. This is the correct option for Claude for Government despite the name. The window opens on its **Connection** section.

4

Enter the bootstrap address

In the window’s left sidebar, click **Source**. On an unconfigured machine it appears last in the list and is dimmed, but is still clickable. Enter the full address from the section above in the **Bootstrap config URL** field. Leave every other field alone; your deployment supplies the provider, credentials, and model list after sign-in.

5

Apply and sign in

Click **Apply Changes** and let the app relaunch. The sign-in screen now offers **Sign in with your organization** alongside the claude.ai option. Choose it. The app shows a pairing code and opens the sign-in page in your browser. Sign in with your agency credentials, confirm that the code in the browser matches the one in the app, and approve. The app picks up the session and opens to Claude.

6

Run the verification checklist

Work through [Confirm it worked](#confirm-it-worked) below.

After the test, the same configuration window has an **Export** menu that produces files ready for your management system: a `.mobileconfig` profile for macOS, a `.reg` file for Windows, an ADMX template for Intune or Group Policy, and a Profile Manifest for Jamf. Before exporting, turn on **Disable Claude.ai sign-in** in the window’s **Workspace restrictions** section so the exported profile hides the claude.ai option on managed devices.

##  Deploy to your fleet

The recommended profile contains two keys. In the macOS and Windows profiles below, write every value as a string exactly as shown, including booleans as the strings `"true"` or `"false"`; the Linux file uses native JSON types, as shown.

| Key | Value | Purpose |
| --- | --- | --- |
| `bootstrapUrl` | `https://<your-deployment-host>/gateway-api/user/bootstrap` | Required. Points the app at your deployment. |
| `disableDeploymentModeChooser` | `"true"` | Recommended. Hides the claude.ai sign-in option so users can only sign in to your deployment. |

No other keys are needed; your deployment supplies everything else per user after sign-in. The profile contains no secrets, only an address. Keys documented for other Claude plans, such as `forceLoginOrgUUID` or `loginSsoOrgDomain`, apply only to claude.ai workspaces and are ignored by your deployment.

###  macOS

Claude Desktop reads managed preferences in the `com.anthropic.claudefordesktop` domain. Deploy a configuration profile that sets the two keys in that domain as strings.

```
<key>bootstrapUrl</key>
<!-- substitute your deployment's address -->
<string>https://<your-deployment-host>/gateway-api/user/bootstrap</string>
<key>disableDeploymentModeChooser</key>
<string>true</string>
```

Most device management consoles, including Jamf and Intune, build the profile around these keys for you. For a complete `.mobileconfig` ready to upload, use the Export menu described in the single-machine path.

###  Windows

Claude Desktop reads string (`REG_SZ`) values by name under `HKLM\SOFTWARE\Policies\Claude`. Deliver them with Intune, Group Policy, or any tool that writes machine policy. The ADMX template from the Export menu makes both keys available in the policy editor. As a `.reg` file:

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude]
; substitute your deployment's address
"bootstrapUrl"="https://<your-deployment-host>/gateway-api/user/bootstrap"
"disableDeploymentModeChooser"="true"
```

The `.reg` file from the Export menu targets `HKEY_CURRENT_USER`, which is correct for single-machine testing. For fleet deployment, deliver the values under `HKEY_LOCAL_MACHINE` as shown here.

###  Linux

Place a JSON file at `/etc/claude-desktop/managed-settings.json` containing the same keys at the top level.

```
{
  "bootstrapUrl": "https://<your-deployment-host>/gateway-api/user/bootstrap",
  "disableDeploymentModeChooser": true
}
```

The file must be a regular file (not a symlink), and the file and its directory must be owned by root and must not be group- or world-writable. If the permissions are wrong, the app rejects the file, logs the reason to `main.log`, and treats the device as managed but unreadable, so local settings are also disabled until the permissions are corrected and the app is relaunched.

###  Order of deployment

Deploy the configuration before the app wherever you can. A user whose device already has the profile opens Claude Desktop for the first time and lands directly on your deployment’s sign-in screen, with no opportunity to sign in to claude.ai by mistake.

Once `bootstrapUrl` or any other connection key is present in the profile, the device is managed. The in-app configuration window becomes read-only, and locally authored settings, including a single-machine test configuration, are ignored in favor of the profile. Removing the profile returns the device to local control.

The app reads managed configuration at launch. After you change the profile on a device where the app is already running, have the user fully quit and reopen it.

##  Confirm it worked

Run through these checks on a configured machine from either path.

1

Check the sign-in screen

Launch the app. The sign-in screen offers **Sign in with your organization**. On a managed device with `disableDeploymentModeChooser` set, it is the only option. If only the claude.ai sign-in appears, the configuration did not reach the app.

2

Check that the device is managed

On a device that received the profile through your management system, open the configuration window (the first three steps of the single-machine path). It should be read-only with a banner noting that your organization manages the configuration. If it is still editable, no recognized key reached the app, even if your management console reports the profile as delivered. The diagnostic report’s Configuration section (next step) shows exactly what the app read.

3

Generate a diagnostic report

From **Help**, choose **Troubleshooting**, then **Generate Diagnostic Report**. The report’s Configuration section lists which keys the app read, where each came from, and any values that failed to parse. Secret values are redacted, so the report is safe to attach to a help-desk ticket.

4

Sign in and send a message

Sign in as a provisioned test user. Chat works and the model picker lists the models you expect for that user’s seat tier.

5

Confirm per-user settings arrived

After sign-in, the tabs that are enabled for the user and any organization-managed connectors appear in the app. One end-to-end test is to set a short message in the **Desktop banner** setting on the tenant [Config](/docs/government/tenant-admin/configuration) page during rollout; if the message appears across the top of the app after sign-in, per-user delivery is working. If sign-in succeeds but none of these settings arrive, re-check the configured address.

##  Troubleshooting

| What you see | Likely cause | What to do |
| --- | --- | --- |
| Only the claude.ai sign-in screen; no organization option | The configuration never reached the app: the profile was not delivered, a key name is misspelled, the value is in the wrong location or registry type, or the app was not relaunched after the change | Verify delivery in your management console, generate a diagnostic report and check its Configuration section, then fully quit and reopen the app |
| Sign-in times out, or the browser says the code expired | The app stops waiting after about five minutes | Cancel and start sign-in again; a fresh code is issued |
| The diagnostic report or `main.log` shows “Managed configuration is invalid; local settings are disabled until it is fixed” | The app detected a managed profile but could not read any of its values | Correct the profile and redeploy; the report’s Configuration section names each key that failed |
| Signed in, but the model picker is empty | The user has no seat tier, or none of the tier’s models is available in your deployment | Have an organization owner check the user’s seat on the [Users](/docs/government/org-admin/users) page and the tier’s models on the [Seat tiers](/docs/government/org-admin/seat-tiers) page |

For anything else, the app writes its log to `~/Library/Logs/Claude-3p/main.log` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\main.log` on Windows, and `~/.config/Claude-3p/logs/main.log` on Linux. The log records which configuration keys were read or dropped and why. The diagnostic report from the verification checklist produces a bundle, without conversation content, that you can send to your Anthropic representative.

* Configuration changes made in this portal do not need to be pushed to devices. The app re-checks your deployment for changes about every 30 minutes and at each launch, and prompts users to relaunch when something changed.
* New and retired models appear in the model picker without any profile change or app update; model access is controlled through [seat tiers](/docs/government/org-admin/seat-tiers).
* Claude Desktop keeps itself updated by default. If your agency distributes software through its own pipeline, add `disableAutoUpdates` with the value `"true"` to the same profile and redistribute installers yourself.
* The sign-in flow and what a user sees on the [Sessions](/docs/government/account/sessions) page after pairing a device are covered on that page.

[Microsoft 365 connector](/docs/government/connectors/microsoft-365)[Overview](/docs/government/account/overview)
