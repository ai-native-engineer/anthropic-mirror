<!-- source: https://claude.com/docs/third-party/claude-desktop/installation -->

Claude Desktop on third-party (3P) is the standard Claude Desktop application plus a managed configuration that activates third-party inference mode. You distribute the regular Claude Desktop installer and apply the configuration through your existing device-management tooling.

##  Recommended rollout

For most organizations, we recommend the following rollout:

1

Evaluate on a single machine

An admin installs Claude Desktop on their own device and uses the in-app configuration window to build and test a working configuration against your inference provider.

2

Allow required network egress

Open the hostnames your configuration requires on your perimeter firewall. The configuration window lists them for the exact settings you’ve chosen.

3

Export and deploy via MDM

From the configuration window, export the validated configuration as a `.mobileconfig` (macOS) or `.reg` (Windows) file and distribute it through Jamf, Intune, Group Policy, or your MDM of choice.

4

Distribute the app

Push the Claude Desktop installer to enrolled devices. When the app launches and finds a managed configuration, it enters 3P mode automatically with no user sign-in or setup required.

Deploying the configuration before the app means end users open Claude for the first time and land directly in the third-party deployment, with no opportunity to sign in to claude.ai by mistake.

##  Check device readiness

Before installing Claude Desktop, you can confirm that a device supports Cowork by running the readiness check: a small standalone program that requires no installation or sign-in.

| Platform | Download |
| macOS | [Cowork readiness check for macOS](https://claude.ai/api/desktop/darwin/universal/cowork-readiness-check/latest/redirect) |
| Windows (Arm) | [Cowork readiness check for Windows arm64](https://claude.ai/api/desktop/win32/arm64/cowork-readiness-check/latest/redirect) |
| Windows (x64) | [Cowork readiness check for Windows x64](https://claude.ai/api/desktop/win32/x64/cowork-readiness-check/latest/redirect) |

Open the downloaded program to run the check. If it reports **This computer is ready for Cowork**, the device can run Cowork.
For fleet deployments, run the check on a representative device of each hardware model in your fleet before the broad rollout, so unsupported models are identified before users hit them.

##  Admin installation

###  1. Install Claude Desktop

Download the installer for your platform from [claude.com/download](https://claude.com/download). If you’re not sure the machine supports Cowork, run the [readiness check](#check-device-readiness) first.

| Platform | Installer | Notes |
| --- | --- | --- |
| macOS | `.dmg` | Drag **Claude.app** to Applications |
| Windows | `.msix` | Supports per-machine provisioning for enterprise deployment |

###  2. Build a configuration in the app

Launch Claude Desktop. **Do not sign in or create an Anthropic account** — stay on the login screen.

* macOS
* Windows

From the macOS menu bar at the top of the screen:

1. Go to **Help → Troubleshooting → Enable Developer Mode** to reveal the Developer menu.
2. Then go to **Developer → Configure third-party inference** to open the configuration window.

Open the application menu (☰) in the top-left of the Claude login screen:

1. Go to **Help → Troubleshooting → Enable Developer Mode** to reveal the Developer menu.
2. Then go to **Developer → Configure third-party inference** to open the configuration window.

The window is organized into sections in the left sidebar. Work through them in order; each maps to a group of [configuration keys](/docs/third-party/claude-desktop/configuration), and the window validates values as you enter them.

| Section | What you set |
| **Connection** | * Inference provider (Gateway, Anthropic API, Vertex AI, Bedrock, or Foundry) and its credentials * Model list * Organization UUID * Optional credential-helper script |
| **Workspace restrictions** | * Which tabs (Cowork, Code) are enabled * Allowed egress hosts for the sandbox * Disabled built-in tools * Allowed workspace folders |
| **Connectors & extensions** | * Managed MCP servers pushed to all users * Whether users can add their own local MCP servers * Whether desktop extensions (`.mcpb`) are allowed * Whether the extension directory is shown * Whether unsigned extensions are rejected |
| **Telemetry & updates** | * OpenTelemetry collector endpoint * Whether auto-updates are blocked, and the enforcement window if not * The three Anthropic-bound telemetry toggles (essential, nonessential, nonessential services) |
| **Usage limits** | * Per-device token cap and its window length |
| **Appearance** | * Persistent banner shown across the app window |
| **Plugins & skills** | * Shows the org-plugins folder path for your platform * Plugins are distributed by mounting bundles to that folder via your MDM, not through this window |
| **Egress Requirements** | * A read-only firewall allowlist derived from everything you’ve entered above, grouped by feature * **Copy hostnames**, **Download .txt**, and **Test connectivity** actions |
| **Source** | * Optional bootstrap URL to fetch this configuration remotely * Bootstrap-delivered configuration takes priority over MDM-delivered values: it replaces them wholesale rather than merging key by key |

The configuration picker in the top-right shows which saved configuration you’re editing and whether it’s the one currently applied. On a managed device it indicates the configuration is organization-managed, and every section shows a banner directing users to their IT administrator.
The configuration window is the recommended way to author configurations. It validates field formats, knows which keys each provider requires, and stays current as new keys are added.

When a managed (MDM-delivered) configuration is already present on the device, the configuration window opens read-only. It shows what the admin deployed but won’t let the user change or override it. To author a new configuration, use a device without a managed profile, or temporarily remove the profile.

###  3. Export for MDM

Once your configuration tests successfully, click **Export** and choose a format:

| Format | Platform | Deploy with |
| --- | --- | --- |
| `.mobileconfig` | macOS | Jamf, Kandji, Mosyle, Workspace ONE, or any Apple MDM |
| `.reg` | Windows | Group Policy (import into a GPO), Intune (via custom ADMX or script), or any MDM that can write registry policy |
| `.zip` (ADMX template) | Windows | Schema-only template for Intune or Group Policy; you enter values in the management console |
| `.plist` (Profile Manifest) | macOS | Schema-only template for Jamf, ProfileCreator, or similar macOS tools |

The two actions in the configuration window do different things:

* **Apply locally** writes the selected configuration to your own machine’s Claude settings and relaunches the app, so you can test it end to end before deploying it.
* **Export** writes a `.mobileconfig` or `.reg` file and leaves your local settings untouched.

####  Creating profiles for multiple user groups

Many organizations deploy distinct configurations to different populations: for example, a permissive profile for an engineering pilot group and a restricted profile for the broader rollout, or per-region profiles that point at different inference endpoints.
The configuration window can hold multiple named configurations. Use the picker in the top-right of the window:

* **New configuration** creates an empty configuration.
* **Duplicate** copies the current configuration as a starting point for a variant.
* **Rename** and **Delete** manage the list.
* **Reveal in Finder** opens the on-disk location where saved configurations are stored.

Selecting a configuration in the picker loads it for editing; the **applied** badge marks the one currently active on your machine. **Apply locally** and **Export** each act on whichever configuration is selected, so you can test each one locally and export them independently.
In your MDM, scope each exported profile to the corresponding device or user group. Targeting is handled by your MDM’s assignment rules; the configuration name is for your authoring workflow and is not part of the deployed profile.

###  4. Allow required network egress

The hosts the app needs to reach depend on the configuration you built: your inference provider’s endpoint is always required, and each telemetry, update, and service setting you leave enabled adds its own hosts. The configuration window shows the exact allowlist for your settings and can export it as a text file for your network team.
Open these hosts on your perimeter firewall before rolling out to devices. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths) for the full list of hosts grouped by the setting that controls each one, and for the distinction between the perimeter firewall and the in-app sandbox allowlist.

###  5. Deploy the configuration

Push the exported configuration through your MDM. The app reads from these locations:

* macOS
* Windows

| Source | Path | Precedence |
| --- | --- | --- |
| Managed (per-user) | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` | Highest |
| Managed (machine) | `/Library/Managed Preferences/com.anthropic.claudefordesktop.plist` |  |
| Local (user) | `~/Library/Application Support/Claude-3p/configLibrary/` | Lowest |

A `.mobileconfig` profile delivered by MDM lands in the Managed Preferences locations automatically. Both managed paths are read; where a key appears in both, the per-user value wins.

| Source | Path | Precedence |
| --- | --- | --- |
| Machine policy | `HKLM\SOFTWARE\Policies\Claude` | Highest |
| User policy | `HKCU\SOFTWARE\Policies\Claude` |  |
| Local (user) | `%LOCALAPPDATA%\Claude-3p\configLibrary\` | Lowest |

A Group Policy Object or Intune configuration profile writes to the registry policy paths. Both hives are read; where a key appears in both, the machine (`HKLM`) value wins.

When **any** managed source is present, it takes effect and the in-app configuration window becomes read-only. Locally authored values in `configLibrary/` are ignored.

###  6. Distribute the app

Deploy the Claude Desktop installer to enrolled devices using your standard software-distribution mechanism. On launch, the app reads the managed configuration, detects the configured inference provider and credentials, and the sign-in screen offers users the option to start in Claude Desktop on 3P.

###  7. Deploy organization plugins (optional)

If you’re distributing [organization plugins](/docs/third-party/claude-desktop/extensions#organization-plugins-admin), push the plugin bundles to the org-plugins directory on each device alongside the configuration profile. Plugins are picked up at the next app launch.

##  End-user installation

For pilots, evaluations, or organizations that don’t use MDM, individual users can configure 3P mode themselves.

1. Install Claude Desktop from [claude.com/download](https://claude.com/download). If you’re not sure your computer supports Cowork, run the [readiness check](#check-device-readiness) first.
2. Launch the app. **Do not sign in or create an Anthropic account.** From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the login screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure third-party inference**.
3. Enter the provider, endpoint, and credential values supplied by your administrator.
4. Click **Apply locally**. The app relaunches and the sign-in screen now offers the option to start in Claude Desktop on 3P using the configuration you entered.

The configuration is written to the application’s local config file and applies only to that device and user account. It can be edited from the same window at any time. To return to standard Claude Desktop, choose the Anthropic sign-in option on the sign-in screen instead.

##  Verifying the deployment

On any configured device, open Claude Desktop and go to **Help → Troubleshooting → Copy Managed Configuration Report**. This copies a summary showing which keys were detected, where they were read from (managed profile vs. user store), and whether the inference credentials validated successfully. Secret values are redacted.
If the app shows the standard claude.ai sign-in screen instead of Cowork, the configuration was not read. Common causes:

* `inferenceProvider` is missing, misspelled, or set to an unrecognized value
* The configuration was applied while the app was running (fully quit and relaunch)
* The configuration was written to the local config file but you’re checking the managed location (or vice versa)
* A required key for the chosen provider is missing; check **Help → Troubleshooting** or the application log at `~/Library/Logs/Claude-3p/main.log` (macOS) / `%LOCALAPPDATA%\Claude-3p\Logs\main.log` (Windows)

##  Troubleshooting

If you’re experiencing technical issues with installation or setup, generate a diagnostic report and share it with Anthropic.
On the affected machine, go to **Help → Troubleshooting → Generate Diagnostic Report** in the menu bar, choose a save location, and send the resulting folder to your Anthropic representative.
Please generate the diagnostic before requesting support. The report contains the configuration state, application logs, and environment details needed to investigate, and does not include any user data or conversation content.

##  Endpoint security software

If your organization runs binary-authorization or EDR software (such as [Santa](https://santa.dev), CrowdStrike Falcon, or Microsoft Defender ASR) with path-based deny rules, the Cowork agent helper may be blocked from launching. The symptom is that Claude Desktop opens normally and reads the managed configuration, but Cowork sessions fail to start.
The agent helper is a signed binary that Claude Desktop installs under its user-data directory. **Allowlist by signing identity rather than path** so the rule survives version updates.
**macOS**

~/Library/Application Support/Claude-3p/claude-code/<version>/claude.app/Contents/MacOS/claude

The helper is Developer ID signed and notarized:

* Team ID: `Q6L2SF6YDW` (Anthropic PBC)
* Signing ID: `com.anthropic.claude-code`

For Santa, a `TEAMID` allow rule for `Q6L2SF6YDW` covers the helper across version updates. Standard (non-3P) installs use `~/Library/Application Support/Claude/` with the same subpath.
**Windows**

%LOCALAPPDATA%\Claude-3p\claude-code\<version>\claude.exe

The helper is Authenticode-signed with publisher `Anthropic, PBC`. For Defender ASR or AppLocker, allowlist by publisher rather than path. Standard installs use `%APPDATA%\Claude\` with the same subpath.

##  Updates

By default, Claude Desktop checks Anthropic’s update server and applies updates automatically. In 3P deployments you can:

* **Leave auto-update enabled** (recommended) so fixes reach users without IT intervention. Use `autoUpdaterEnforcementHours` to bound how long users can defer a pending update.
* **Disable auto-update** (`disableAutoUpdates`) and redistribute new builds through your MDM on your own cadence. This is required for air-gapped environments but means your IT team owns the update pipeline.

See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for the network paths the updater uses.

[Features](/docs/third-party/claude-desktop/feature-matrix)[Configuration reference](/docs/third-party/claude-desktop/configuration)
