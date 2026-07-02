<!-- source: https://claude.com/docs/third-party/claude-desktop/mdm -->

On the MDM delivery model, the profile you deploy carries your organization’s full configuration, and every device the profile targets gets the same settings. This page covers the workflow end to end: build the configuration in the app, export it, open the firewall, and deploy the profile and installer to your fleet.
Before you start, install Claude Desktop on an admin workstation; see [Installation and setup](/docs/third-party/claude-desktop/installation). If you deliver configuration from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap) instead, follow that page; your profile then carries only the bootstrap keys, but it is exported and deployed the same way described here.

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

##  1. Build a configuration in the app

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
| --- | --- |
| **Connection** | * Inference provider (Gateway, Anthropic API, Vertex AI, Bedrock, or Foundry) and its credentials * Model list * Organization UUID * Optional credential-helper script |
| **Workspace restrictions** | * Which tabs (Cowork, Code) are enabled * Allowed egress hosts for the sandbox * Disabled built-in tools * Allowed workspace folders |
| **Connectors & extensions** | * Managed MCP servers pushed to all users * Whether users can add their own local MCP servers * Whether desktop extensions (`.mcpb`) are allowed * Whether the extension directory is shown * Whether unsigned extensions are rejected |
| **Telemetry & updates** | * OpenTelemetry collector endpoint * Whether auto-updates are blocked, and the enforcement window if not * The three Anthropic-bound telemetry toggles (essential, nonessential, nonessential services) |
| **Usage limits** | * Per-device token cap and its window length |
| **Appearance** | * Persistent banner shown across the app window |
| **Plugins & skills** | * Shows the org-plugins folder path for your platform * Plugins are distributed by mounting bundles to that folder via your MDM, not through this window |
| **Egress Requirements** | * A read-only firewall allowlist derived from everything you’ve entered above, grouped by feature * **Copy hostnames**, **Download .txt**, and **Test connectivity** actions |
| **Source** | * The bootstrap keys, if you are using the [bootstrap server](/docs/third-party/claude-desktop/bootstrap) delivery model instead of a full MDM profile * Bootstrap-delivered configuration takes priority over MDM-delivered values: it replaces them wholesale rather than merging key by key |

The configuration picker in the top-right shows which saved configuration you’re editing and whether it’s the one currently applied. On a managed device it indicates the configuration is organization-managed, and every section shows a banner directing users to their IT administrator.
The configuration window is the recommended way to author configurations. It validates field formats, knows which keys each provider requires, and stays current as new keys are added.

When a managed (MDM-delivered) configuration is already present on the device, the configuration window opens read-only. It shows what the admin deployed but won’t let the user change or override it. To author a new configuration, use a device without a managed profile, or temporarily remove the profile. (Profiles that set only the two update keys are an exception; see [how the update keys are treated](#update-keys-and-managed-precedence).)

##  2. Export the profile

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

###  Creating profiles for multiple user groups

Many organizations deploy distinct configurations to different populations: for example, a permissive profile for an engineering pilot group and a restricted profile for the broader rollout, or per-region profiles that point at different inference endpoints.
The configuration window can hold multiple named configurations. Use the picker in the top-right of the window:

* **New configuration** creates an empty configuration.
* **Duplicate** copies the current configuration as a starting point for a variant.
* **Rename** and **Delete** manage the list.
* **Reveal in Finder** opens the on-disk location where saved configurations are stored.

Selecting a configuration in the picker loads it for editing; the **applied** badge marks the one currently active on your machine. **Apply locally** and **Export** each act on whichever configuration is selected, so you can test each one locally and export them independently.
In your MDM, scope each exported profile to the corresponding device or user group. Targeting is handled by your MDM’s assignment rules; the configuration name is for your authoring workflow and is not part of the deployed profile.

##  3. Allow required network egress

The hosts the app needs to reach depend on the configuration you built: your inference provider’s endpoint is always required, and each telemetry, update, and service setting you leave enabled adds its own hosts. The configuration window shows the exact allowlist for your settings and can export it as a text file for your network team.

`downloads.claude.ai` is required to run the app regardless of your configuration: it serves the VM workspace bundle and the latest Claude Code binary, fetched at session start. Without it, Cowork sessions cannot start. The only exception is the [offline installer](/docs/third-party/claude-desktop/installation#air-gapped-deployment), which builds both components into the installer package.

Open these hosts on your perimeter firewall before rolling out to devices. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths) for the full list of hosts grouped by the setting that controls each one, and for the distinction between the perimeter firewall and the in-app sandbox allowlist.

##  4. Deploy the configuration

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

When a managed source sets any key other than the two update keys, the managed configuration owns the device: it takes effect, the in-app configuration window becomes read-only, and locally authored values in `configLibrary/` are ignored.

###  Update keys and managed precedence

The update keys `disableAutoUpdates` and `autoUpdaterEnforcementHours` are treated specially, so you can set an update policy from MDM without managing the whole configuration. When a managed source sets only these keys (one or both), the device keeps its locally authored configuration and the configuration window stays editable. The update keys themselves are still enforced as a pair: both are resolved from the managed source alone, so a locally set value for either key is ignored even if the profile only sets the other one.
If the managed profile sets any other recognized key, the normal rule above applies and the whole configuration is managed.

##  5. Distribute the app

Deploy the Claude Desktop installer to enrolled devices using your standard software-distribution mechanism. On launch, the app reads the managed configuration, detects the configured inference provider and credentials, and the sign-in screen offers users the option to start in Claude Desktop on 3P.

##  6. Deploy organization plugins (optional)

If you’re distributing [organization plugins](/docs/third-party/claude-desktop/extensions#organization-plugins-admin), push the plugin bundles to the org-plugins directory on each device alongside the configuration profile. Plugins are picked up at the next app launch.

##  Next steps

After deployment, confirm devices picked up the configuration with the checks in [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment).

[Installation and setup](/docs/third-party/claude-desktop/installation)[Deploy with bootstrap](/docs/third-party/claude-desktop/bootstrap)
