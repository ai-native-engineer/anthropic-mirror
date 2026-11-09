<!-- source: https://support.claude.com/en/articles/15811196-what-to-expect-with-claude-cowork-in-the-cloud -->

# What to expect with Claude Cowork in the cloud

Updated over a week ago

Table of contents

Claude Cowork can now run your tasks in the cloud, on Anthropic's servers instead of your computer. It lets Claude keep working when your computer is closed and brings Cowork to web and mobile. This article covers what changes when a session runs in the cloud and what stays the same.

## Availability

Claude Cowork is available on desktop on all paid plans (Pro, Max, Ultra, Team, and Enterprise). On web and mobile, it's available on Pro, Max, Ultra, and Team plans (in beta on Team), and on Enterprise plans when an owner enables it. This article is for existing Cowork users on the desktop app.

The new Claude experience, which combines chat and Cowork, is rolling out to Pro, Max, and Ultra plans. On Team plans (in beta) and Enterprise plans, it's available where **Chat and Cowork unified** is turned on. If your message box no longer shows "Chat" and "Cowork" options, you have the new experience, and some steps in this article may look different. Learn more in **[Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823)**.

## What stays the same

Your connectors stay linked across sessions and devices, and files Claude delivers to you are saved. Sessions work the way you're used to: describe the task, review Claude's approach, and steer when it matters.

## What's different when using Cowork in the cloud

These differences apply to any cloud session, including on desktop:

* **Save what you want to keep.** Files Claude delivers are saved. Working files it doesn't hand back aren't kept or referenced after the session ends.
* **You can't switch modes mid-session.** Once a session starts, it stays in the cloud or local. To change modes, start a new session.
* **Search is title-only.** You can find past cloud sessions by title, but you can't search their full text yet.
* **Attach folders manually.** Reaching files or tools on your computer requires the Claude Desktop app to be open and connected.
* **Very large files may be slower.** The same goes for a large number of files.
* **Scheduled tasks created in the cloud can't use local folders or local connectors.** Scheduled tasks that run in the cloud use the built-in schedule options. Existing local tasks that rely on a local folder or local connector keep running locally.

## What still needs the desktop app

Some capabilities reach things on your computer, so they require the Claude Desktop app to be open and connected, even when your session runs in the cloud:

* Local files and folders
* Local MCP servers, including plugins that bundle them
* Browser use, through Claude in Chrome
* Computer use

If the desktop app is closed, sessions in the cloud keep running but can't reach your computer.

## Switch between cloud and local execution

You can switch modes when starting a new session by clicking the “Beta” button in the upper right corner, or by navigating to **[Settings > Cowork](https://claude.ai/settings/cowork)** and toggling **Run new tasks in the cloud** on or off.

**Note:** If you have the new Claude experience, tasks run in the cloud, and there's no option to run them locally.

---

## Chat and Cowork now live in one place

Chat and Cowork share one home on every surface. In the message box, select “Cowork” to hand off a task, or “Chat” for a regular conversation. Some things are shared between them, and a few still differ while we finish bringing them together. If you have the new Claude experience, there's no "Chat" or "Cowork" option. Describe what you need in any conversation. Learn more in **[Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823)**.

**What's shared now:**

* **Projects.** From a project, you can start a chat or a Cowork session, and Claude uses the project's knowledge as context. If a project is tied to a local folder, it supports Cowork sessions only. Cowork uses one project at a time and won't change a project's contents, so add anything you want to keep to the project yourself.
* **Artifacts.** Artifacts Claude creates in chat or Cowork show up in one artifacts view and are saved there. Artifacts created on or after August 19, 2026 are available on the desktop app and web. Live artifacts created before that date are available on the desktop app only.
* **Recent history and search.** Both carry across chat and Cowork.
* **Memory.** What Claude remembers from your chats is available in Cowork tasks that run in the cloud, and what comes up in a task carries back to chat. Sessions that run locally on your computer don't use memory. Learn more about **[Claude's memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#h_82126ebcc9)**.

---

## Troubleshoot local sessions on Windows

### I'm seeing “VM service not running” when I start a local session

This means the Claude VM Service (CoworkVMService) isn't available. It can happen if you installed Cowork with the older .exe installer instead of MSIX, or if the Windows service is stopped. To fix it, reinstall from our download page, or start “Claude VM Service” in services.msc or with sc start CoworkVMService (CoworkVMServiceStore for Microsoft Store installs).

### I'm seeing “EXDEV: cross-device link not permitted”

This happens when the VM image download crosses a drive boundary, most often when Settings > System > Storage > “Where new content is saved” points at D:\ instead of C:\. It can also happen when AppData is redirected to a network share through a roaming profile. To fix it, set storage back to C:\, uninstall and reinstall Cowork, and update to the latest desktop version.

---

## Learn more

For where to find Cowork on each surface and what's available on each, see **[Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349)**. For safety guidance, see **[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)**.

---

Related Articles

* [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
* [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
* [Claude Cowork architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview)
* [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
* [Run your endpoint detection and response (EDR) sensor in Claude Cowork on Claude Desktop](https://support.claude.com/en/articles/17828685-run-your-endpoint-detection-and-response-edr-sensor-in-claude-cowork-on-claude-desktop)

Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents
