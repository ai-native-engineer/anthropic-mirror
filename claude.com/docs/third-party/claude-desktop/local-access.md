<!-- source: https://claude.com/docs/third-party/claude-desktop/local-access -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Like [Cowork](https://claude.com/docs/cowork/overview) in standard Claude Desktop, Claude Desktop on third-party (3P) works directly with files on the user’s computer. Users attach one or more **workspace folders** to a session; the agent can then read, create, and modify files anywhere inside those folders, and run code against them inside the sandbox VM.
In Claude Desktop on 3P, administrators can constrain which folders users are allowed to attach.

##  Workspace folder allowlist

The `allowedWorkspaceFolders` configuration key restricts which paths users may attach as workspace folders.

| Value | Behavior |
| --- | --- |
| Unset | Unrestricted. Users can attach any folder they have OS-level access to, matching standard Claude Desktop. |
| `["~/Documents/Claude", "/Volumes/Shared/Projects"]` | Users may attach only folders **inside** one of the listed roots. |
| `[]` | No folders may be attached. The agent can still create files in its own sandbox scratch space, but cannot read or write the user’s filesystem. |

A leading `~` expands to the user’s home directory, so a single profile can express per-user roots like `~/Documents/Claude` across the fleet.
The check is enforced against the **resolved** path, so symlinks and `..` traversal can’t be used to escape an allowed root.

The allowlist controls what users can **attach**. Within an attached folder, the agent has full read/write access to every file the user’s OS account can reach. To isolate sensitive data, keep it outside the allowed roots.

##  Network drives on Windows

Users can attach a mapped network drive (for example, `Z:\`) as a workspace folder through the folder picker. Raw UNC paths (`\\server\share`) are not supported; map the share to a drive letter first.
What the agent can do on the network drive depends on whether the drive was mapped and reachable when the sandbox started:

* **Mapped and reachable at sandbox start:** the sandbox mounts the attached folder alongside local folders. File tools and shell commands both work.
* **Mapped later, or unreachable at sandbox start:** file tools still work, but shell commands cannot reach the drive. Copy the relevant files to a local folder before running a script or build against them.

The sandbox can stay running between sessions. A drive the user maps while the sandbox is already up falls into the second case until the sandbox next restarts.
The agent cannot attach a network-drive path on its own; only the user can, through the folder picker. This is a security boundary.
On macOS, network mounts under `/Volumes/` are currently treated as local folders.

##  WSL

You do not need Windows Subsystem for Linux (WSL) to run Claude Desktop or Cowork. On Windows, Cowork’s sandbox runs on the operating system’s built-in virtualization, which the [readiness check](https://claude.com/docs/third-party/claude-desktop/installation#check-device-readiness) verifies. Install the macOS or Windows package (see [System requirements](https://claude.com/docs/third-party/claude-desktop/installation#system-requirements)); there is no installation path inside WSL. Run the Windows app and work with WSL files from there.
Windows exposes a WSL distribution’s filesystem as a UNC path (`\\wsl$\<distro>` or `\\wsl.localhost\<distro>`). Like any other raw UNC path, these cannot be attached as workspace folders directly. To attach files that live inside WSL as a workspace folder, map the share to a drive letter and attach the mapped drive, or copy the files to a local Windows folder. [Network drives on Windows](#network-drives-on-windows) describes what the agent can do on a mapped drive.
