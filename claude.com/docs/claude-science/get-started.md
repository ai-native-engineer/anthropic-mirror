<!-- source: https://claude.com/docs/claude-science/get-started -->

##  Install

macOS: Download the installer from claude.com/product/claude-science and double-click to install. On first launch, the app sets up its runtime and starter Python and R environments, which takes a few minutes, then opens a new tab in your default browser. If no browser tab appears, choose Open from the menu bar icon.

Although Claude Science opens in a browser tab, it’s a local application, not a website. You can only open it from the application itself (the menu bar icon on macOS, or the `claude-science` command on Linux); you can’t reach it by typing a URL.

Linux: Download and run the binary.

```
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

```
claude-science serve
```

First launch prints progress to the terminal and ends with a local URL. On a remote server, start with `--no-browser`, forward the port over SSH, and open the URL from your laptop.

##  Sign in and complete setup

When the app opens in your browser, sign in with your Claude account. If the OAuth redirect can’t return to the app (for example, through an SSH tunnel), use the Paste a code option on the sign-in screen instead. No API key is required.
After sign-in, a setup wizard walks you through enabling connectors and skills and setting which websites Claude can access. You can change these at any time in Settings.

Everything Claude Science installs lives in a single folder (`~/.claude-science`) in your home directory. It doesn’t modify your existing conda installation, R libraries, or shell configuration.

Deleting that folder removes all projects, artifacts, and conversation history. Deleting the folder and the application removes Claude Science entirely.

##  Run your first analysis

* Open the Example project, or create a new one.
* Start a conversation. Reference a folder on your computer by typing its path or using the @ picker in the composer.
* Review the folder-access card when it appears and choose whether to allow it.
* Review the code-execution card when Claude proposes running code and choose whether to allow it.
* Results appear as artifacts in the Files panel.

##  Troubleshooting first launch

* No browser tab appeared: on macOS, choose Open from the menu bar icon. On Linux, copy the printed URL into a browser on the same machine, or run `claude-science url` to print a fresh one.
* Linux refuses to start: install bubblewrap 0.8.0+ and confirm unprivileged user namespaces are enabled (check with `bwrap --version`).
* Sign-in stops at claude.ai: your account is on the Free plan (upgrade required), or the redirect couldn’t return (use Paste a code).

[Claude Science](/docs/claude-science/overview)[Run on Windows (WSL)](/docs/claude-science/run-on-windows-wsl)
