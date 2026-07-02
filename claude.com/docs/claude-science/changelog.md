<!-- source: https://claude.com/docs/claude-science/changelog -->

0.1.15

July 1, 2026

* Corporate networks: environment builds now work behind TLS-inspecting proxies (such as Zscaler or Netskope). On macOS, corporate root CAs in your keychain are picked up automatically for conda/pip package downloads; on macOS or Linux you can also point at a CA-bundle file under Settings > Network > Package mirror. The mirror card’s Check button now verifies TLS trust with the same bundle the builds use. (In-session `pip`/`curl` and the Desktop app’s guest-VM builds are not covered)
* Package mirrors: point conda and pip at your organization’s internal mirror (Artifactory/Nexus) via Settings > Network > Package mirror. Setting a mirror also drops the public package hosts from the sandbox network allowlist
* OpenAlex now requires a free API key for full-text access. Claude Science resolves access automatically or asks you in the session when a key is needed; you can also add and validate a key anytime under Customize > Credentials
* New Context usage view: see how full a session’s context window is and where tokens go, from the + menu in the composer
* Lots of other miscellaneous improvements and fixes

0.1.14

June 30, 2026

* Public launch of Claude Science

[Command line settings](/docs/claude-science/command-line-settings)[Legal and compliance](/docs/claude-science/legal-and-compliance)
